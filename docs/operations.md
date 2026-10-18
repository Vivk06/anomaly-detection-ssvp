# Operations

Run commands from the repository root in Bash. The repository includes code and curated results; you supply MVTec AD images and a compatible checkpoint for inference. `data/mvtec/` and `outputs/` are created at runtime and are gitignored.

## Environment

```bash
python3 -m venv .venv
.venv/bin/pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
.venv/bin/pip install -e ".[captions,dev]"
CUDA_VISIBLE_DEVICES="" HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 .venv/bin/pytest -q
```

The dependency list lives in [pyproject.toml](../pyproject.toml). The smoke suite uses dummy CPU tensors and never loads a dataset or checkpoint. It excludes the upstream third-party example test from default pytest discovery.

## Prepare a cable split

Supply a MVTec AD root with a `cable/` category. The resplit script writes train, validation, and test folders using the 70/20/10 protocol.

```bash
.venv/bin/python scripts/data/make_resplit.py --source "<mvtec_root>" --output_root data/mvtec/cable_resplit --categories cable
```

The destination above is created at runtime. See [data/README.md](../data/README.md) for the committed example images.

## Training and evaluation

The training entrypoint is [train.py](../scripts/pipelines/train.py). Running it trains a model and writes weights under the output directory; it is user-owned work.

```bash
.venv/bin/python scripts/pipelines/train.py --config configs/default.yaml --data_root data/mvtec/cable_resplit --categories cable --output_dir "<output_dir>"
.venv/bin/python scripts/eval/eval_clean.py --config configs/default.yaml --data_root data/mvtec/cable_resplit --categories cable --checkpoint "<checkpoint.pth>" --output_dir "<output_dir>"
.venv/bin/python scripts/eval/eval_noisy.py --config configs/default.yaml --data_root data/mvtec/cable_resplit --categories cable --checkpoint "<checkpoint.pth>" --output_dir "<output_dir>"
```

The noisy evaluator can receive `--clean_results` and `--calibration_file` from a prior user run. [full_pipeline.py](../scripts/pipelines/full_pipeline.py) joins training, clean and noisy evaluation, visualization, and captions. [ablation_matrix.py](../scripts/pipelines/ablation_matrix.py) runs the configured variant matrix. Both can take substantial compute time.

```bash
.venv/bin/python scripts/pipelines/full_pipeline.py --config configs/default.yaml --data_root data/mvtec/cable_resplit --output_dir "<output_dir>"
.venv/bin/python scripts/pipelines/ablation_matrix.py --config configs/default.yaml --data_root data/mvtec/cable_resplit --output_root "<output_dir>"
```

## Caption evaluation and demo

Caption evaluation can generate text from a model or use deterministic spatial synthesis. The comparison wrapper labels its simple rephrasing control `rephrase_control`.

```bash
.venv/bin/python scripts/eval/eval_captions.py --config configs/default.yaml --data_root data/mvtec/cable_resplit --checkpoint "<checkpoint.pth>" --output_dir "<output_dir>" --categories cable
.venv/bin/python scripts/eval/compare_captions.py --config configs/default.yaml --data_root data/mvtec/cable_resplit --checkpoint "<checkpoint.pth>" --output_dir "<output_dir>" --categories cable
.venv/bin/python scripts/demo/demo_folder.py --config configs/default.yaml --checkpoint "<checkpoint.pth>" --input_folder data/samples/combined --output_dir "<output_dir>"
```

The demo exposes image and pixel thresholds through `--help`. Caption text transformer INT8 conversion is enabled unless you pass `--no_caption_text_int8`. Caption generation may need model weights supplied through the relevant library cache.

## Baselines and reports

The WinCLIP wrapper accepts a dataset root and writes per-image scores into a runtime output directory. Its source is vendored under [third_party](../third_party/); check [THIRD_PARTY.md](../THIRD_PARTY.md) for upstream dependency notes. The simulated AnomalyCLIP wrapper was removed. The committed AnomalyCLIP results came from the source experiment summary; the vendored source remains under [third_party](../third_party/).

```bash
CUDA_VISIBLE_DEVICES="" HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 .venv/bin/python -m scripts.baselines.winclip_eval --mvtec-root "<mvtec_root>" --out-root "<output_dir>"
.venv/bin/python scripts/reporting/render_tables.py
```

The renderer reads [metrics.csv](../results/metrics.csv) and [captions.csv](../results/captions.csv), rewrites [tables](../results/tables/), and replaces the marked results block in [README.md](../README.md). It performs no evaluation. [generate_reports.py](../scripts/reporting/generate_reports.py) summarizes user-created run outputs. [aggregate_run22_results.py](../scripts/reporting/aggregate_run22_results.py) has no CLI and is compile-checked only. The historical scripts in [archive](../scripts/archive/) are unsupported.
