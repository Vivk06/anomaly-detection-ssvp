# Anomaly Detection SSVP

Noise-robust anomaly segmentation and defect captioning on MVTec AD cable, extending SSVP

This repository contains a cable anomaly detector trained on the MVTec AD cable 70/20/10 resplit, caption evaluation, curated results, and the source needed to reproduce the reported workflow. The base SSVP method is described in [arXiv 2601.09147](https://arxiv.org/abs/2601.09147) as zero-shot; the experiments here train on cable images.

## What is here

- [Architecture](docs/architecture.md) explains CLIP and DINO features, visual fusion, prompts, maps, losses, and captions.
- [Operations](docs/operations.md) gives Bash commands for setup, split preparation, evaluation, and reporting.
- [Experiments](docs/experiments.md) explains run selection, baselines, and caption comparisons.
- [Results](results/README.md) documents the curated CSVs and known interpretation issues.
- [Contributions](docs/contributions.md), [history](docs/history.md), and [third-party code](THIRD_PARTY.md) record provenance and scope.

## Quick start

```bash
python3 -m venv .venv
.venv/bin/pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
.venv/bin/pip install -e ".[captions,dev]"
CUDA_VISIBLE_DEVICES="" HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 .venv/bin/pytest -q
```

The smoke suite runs with CPU dummy tensors. Supply your own MVTec AD root and compatible checkpoint for actual evaluation. `data/mvtec/` and `outputs/` are created at runtime and ignored by Git. [Sample images](data/README.md) and [report](report/final_report.pdf) are included.

<!-- results:start -->
## Selected results

| Model | Title | Eval | Image AUROC | Pixel AUROC | Pixel PRO |
| --- | --- | --- | --- | --- | --- |
| ssvp | Cable 70/20/10 resplit, 15 epochs | clean | 97.42 | 95.34 | 29.54 |
| ssvp | Cable 70/20/10 resplit, 15 epochs | noisy | 87.00 | 91.82 | 58.27 |
| anomalyclip | AnomalyCLIP cable | clean | 61.3 | 86.1 | 64.7 |
| winclip | WinCLIP summary cable | clean | 44.64 | 49.43 | 29.41 |
<!-- results:end -->

The table is generated from [metrics.csv](results/metrics.csv) and [captions.csv](results/captions.csv) by [render_tables.py](scripts/reporting/render_tables.py). It transcribes source results; it does not rerun experiments. Full tables are in [results/tables](results/tables/).
