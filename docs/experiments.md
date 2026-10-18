# Experiments

This repository reports experiments trained on the MVTec AD cable 70/20/10 resplit. The original SSVP method is described as zero-shot; the cable experiments here trained a detector. [All metric rows](../results/tables/metrics.md) and [caption rows](../results/tables/captions.md) hold the reported numbers. This narrative does not maintain a second copy of those values.

## Detector selection

The source results ledger recommends `run21_resplit_15es` for the cable detector. Its clean and heavy-noise rows appear in the metric table. Ablations that remove consistency regularization, add LoRA without it, or prune heads did not replace that recommendation. The table preserves both accepted and rejected runs as labels with their source values.

The heavy-noise evaluator applies Gaussian noise, blur, salt-and-pepper corruption, and JPEG degradation. WinCLIP uses a separate Gaussian protocol on normalized tensors. See [Known issues](../results/README.md) before comparing noisy rows across models.

## Baselines and transfer

The full metric table includes WinCLIP category rows at the reported resolutions, [the separate WinCLIP source summary](../results/tables/winclip_summary.md), AnomalyCLIP category rows, and a cable-trained SSVP cross-category test on transistor. The README selected comparison excludes the separate WinCLIP summary. The transfer result shows that the cable-trained checkpoint did not carry the same image-level quality to transistor. The dated source summary reported later AnomalyCLIP pixel metrics and WinCLIP resolution updates; those values are represented as rows rather than copied into this prose.

WinCLIP's cable image AUROC and pixel PRO deserve care. The summary files and the dated resolution runs disagree in some fields. We preserved each source as a distinct row, and [results/README.md](../results/README.md) records the provenance issue. No baseline was rerun for this repository cleanup.

## Captions and compression

The caption table records baseline BLIP, fine-tuned BLIP, and deterministic spatial synthesis comparisons. A perfect deterministic text score reflects references that use the same spatial phrasing. BLIP fine-tuning improves the reported text match without using that exact-match shortcut. The caption-side INT8 option changes the text transformer's representation and leaves detector weights intact.

The source ledger rejects the tested pruning paths under its gate and treats prompt fine-tuning as a runtime trade-off. [Contributions](contributions.md) states the project claims; [architecture](architecture.md) and [operations](operations.md) describe the corresponding code and commands.
