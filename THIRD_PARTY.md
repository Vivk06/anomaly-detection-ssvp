# Third-party code

`third_party/winclip/` combines the top-level WinCLIP copy with the nested resize and dataset layout fixes. The top-level `utils/metrics.py` retains AP metrics and cable seeds. The upstream license is at `third_party/winclip/LICENSE`.

`third_party/anomalyclip/` carries the source implementation and its upstream `LICENSE`. We dropped upstream README images under `assets/` and log-only `checkpoints/` and `results/` directories. We also dropped the WinCLIP teaser image and its old installation script. The active baseline wrappers live under `scripts/baselines/`.

Vendored code may need dependencies beyond the package's core development environment when you run a baseline. The repository does not ship pretrained weights or datasets.
