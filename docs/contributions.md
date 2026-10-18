# Contributions and prior work

The project reproduces the SSVP semantic and visual prompting pipeline, then trains and evaluates a cable detector on a 70/20/10 MVTec AD resplit. The base method's zero-shot framing belongs to [SSVP, arXiv 2601.09147](https://arxiv.org/abs/2601.09147). The project adds a caption branch, a caption-side INT8 option, clean and heavy-noise evaluation, and a gate for compression candidates.

The [model package](../src/ssvp_rc/models/) contains CLIP and DINO feature extraction, fusion, prompt generation, and anomaly mapping. [Caption evaluation](../scripts/eval/eval_captions.py) measures text and detection outputs. [Results](../results/tables/metrics.md) record the reported detector comparisons, including unsuccessful variants, without rerunning them.

The source claim notes describe the consistency-free and pruning candidates as unsuccessful and the prompt-tuning variant as slower. We preserve those outcomes in the curated tables and avoid treating exploratory runs as deployment defaults.

The source prior-work notes identify WinCLIP and AnomalyCLIP as baseline comparisons. They also cite work on fine-grained CLIP alignment, anomaly-aware prompts, prompt banks, feature rectification, and vision-language adaptation as design context. [THIRD_PARTY.md](../THIRD_PARTY.md) identifies the code actually vendored here. This document makes no new priority or novelty claim about those papers.
