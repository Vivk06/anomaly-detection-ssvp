import csv
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
METRIC_COLUMNS = ["run_id", "title", "model", "status", "eval", "categories", "resolution",
                  "noise_protocol", "image_auroc", "image_f1_max", "image_ap", "pixel_auroc", "pixel_pro", "pixel_ap"]
CAPTION_COLUMNS = ["eval_id", "title", "variant", "split", "n_images", "bertscore_f1", "notes"]


def test_curated_schemas_and_source_values():
    with (ROOT / "results/metrics.csv").open(newline="") as file:
        reader = csv.DictReader(file)
        assert reader.fieldnames == METRIC_COLUMNS
        rows = list(reader)
    assert len(rows) == 59
    assert {r["model"] for r in rows} == {"ssvp", "winclip", "anomalyclip"}
    assert {r["status"] for r in rows} <= {"recommended", "accepted", "rejected", "exploratory"}
    assert {r["eval"] for r in rows} <= {"clean", "noisy", "cross_category"}
    assert {r["noise_protocol"] for r in rows} <= {"none", "heavy_v1", "winclip_gauss020"}
    selected = next(r for r in rows if r["run_id"] == "run21_resplit_15es" and r["eval"] == "clean")
    assert selected["image_auroc"] == "97.42"
    assert selected["pixel_pro"] == "29.54"
    for row in rows:
        for column in METRIC_COLUMNS[8:]:
            if row[column]:
                assert 0 <= float(row[column]) <= 100, (row["run_id"], column)
    with (ROOT / "results/captions.csv").open(newline="") as file:
        reader = csv.DictReader(file)
        assert reader.fieldnames == CAPTION_COLUMNS
        captions = list(reader)
    assert len(captions) == 21
    assert all(0 <= float(row["bertscore_f1"]) <= 1 for row in captions)
    assert len(list((ROOT / "results/raw/captions/run22").glob("*/caption_before_after_report.json"))) == 10
    assert not list((ROOT / "results").rglob("*.npy"))


def test_table_renderer_is_idempotent_without_touching_repo(tmp_path):
    for relative in ("README.md", "results/metrics.csv", "results/captions.csv", "scripts/reporting/render_tables.py"):
        dest = tmp_path / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, dest)
    command = [sys.executable, str(tmp_path / "scripts/reporting/render_tables.py")]
    subprocess.run(command, check=True)
    first = {path.relative_to(tmp_path): path.read_bytes() for path in (tmp_path / "results/tables").glob("*.md")}
    first[Path("README.md")] = (tmp_path / "README.md").read_bytes()
    subprocess.run(command, check=True)
    assert first == {path: (tmp_path / path).read_bytes() for path in first}
    readme = (tmp_path / "README.md").read_text()
    assert (tmp_path / "results/tables/summary.md").read_text() in readme
