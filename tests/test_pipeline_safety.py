import json
import runpy
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_script(path):
    return runpy.run_path(str(ROOT / path))


def test_full_pipeline_forwards_categories_without_running_models(monkeypatch, tmp_path):
    script = load_script("scripts/pipelines/full_pipeline.py")
    main = script["main"]
    commands = []
    samples = []
    output = tmp_path / "output"

    def fake_run(command):
        commands.append(command)
        if command[1].endswith("train.py"):
            (output / "best_model.pth").touch()

    main.__globals__["run_subprocess"] = fake_run
    main.__globals__["sample_and_save_visuals"] = lambda *args, **kwargs: samples.append((args, kwargs))
    monkeypatch.setattr(sys, "argv", [
        "full_pipeline.py", "--data_root", str(tmp_path),
        "--categories", "cable", "transistor", "--output_dir", str(output),
    ])

    main()

    assert len(commands) == 3
    for command in commands:
        assert command[command.index("--categories") + 1:] == ["cable", "transistor"]
        assert command[command.index("--data_root") + 1] == str(tmp_path)
    assert samples[0][1]["categories"] == ["cable", "transistor"]


@pytest.mark.parametrize("inside_category", [False, True])
def test_resplit_rejects_overlapping_output_before_deletion(monkeypatch, tmp_path, inside_category):
    script = load_script("scripts/data/make_resplit.py")
    source = tmp_path / "source"
    category = source / "cable"
    (category / "train" / "good").mkdir(parents=True)
    sentinel = category / "train" / "good" / "keep.png"
    sentinel.write_bytes(b"source image")
    output = category / "nested" if inside_category else source
    monkeypatch.setattr(sys, "argv", [
        "make_resplit.py", "--source", str(source), "--output_root", str(output),
        "--categories", "cable",
    ])

    with pytest.raises(ValueError, match="overlaps input category"):
        script["main"]()

    assert sentinel.read_bytes() == b"source image"
    if inside_category:
        assert not output.exists()


def test_gate_requires_noisy_report_and_fields(tmp_path):
    script = load_script("scripts/eval/gate_vs_baseline.py")
    run = tmp_path / "run"
    clean = run / "eval_results"
    noisy = run / "noise_eval"
    clean.mkdir(parents=True)
    noisy.mkdir()
    levels = {"image_level": {"auroc": 1, "f1_max": 2, "ap": 3},
              "pixel_level": {"auroc": 4, "pro": 5, "ap": 6}}
    (clean / "results.json").write_text(json.dumps({"overall": levels}))

    with pytest.raises(FileNotFoundError, match="robustness_report.json"):
        script["_build_metric_set"](str(run))

    (noisy / "robustness_report.json").write_text(json.dumps({"noisy": levels}))
    metrics = script["_build_metric_set"](str(run))
    assert len(metrics) == 12
    with pytest.raises(ValueError, match="missing=.*noisy.pixel_ap"):
        script["_compare_metrics"](metrics, {k: v for k, v in metrics.items() if k != "noisy.pixel_ap"}, 7.5)

    del levels["pixel_level"]["pro"]
    (noisy / "robustness_report.json").write_text(json.dumps({"noisy": levels}))
    with pytest.raises(KeyError, match="pro"):
        script["_build_metric_set"](str(run))
