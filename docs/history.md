# Repository history

This tree was built from SSVP_Extension@b14a5e4. The source already contained an SSVPREFAC merge that brought caption evaluation and run22 scripts into the nested project; this cleanup flattened those paths, curated results, and kept historical run IDs as labels. The source repository remained read-only.

| Old script name | Target script |
| --- | --- |
| prepare_cable_split.py | `scripts/data/make_resplit.py` |
| train.py | `scripts/pipelines/train.py` |
| inference.py | `scripts/eval/eval_clean.py` |
| evaluate_noise_robustness.py | `scripts/eval/eval_noisy.py` |
| evaluate_captions.py | `scripts/eval/eval_captions.py` |
| caption_compare.py | `scripts/eval/compare_captions.py` |
| compare_against_baseline.py | `scripts/eval/gate_vs_baseline.py` |
| run_full_pipeline.py | `scripts/pipelines/full_pipeline.py` |
| run_ablation_matrix.py | `scripts/pipelines/ablation_matrix.py` |
| train_run22.py | `scripts/pipelines/run22_caption_compare.py` |
| live_demo_noisy_folder.py | `scripts/demo/demo_folder.py` |
| winclip_eval.py | `scripts/baselines/winclip_eval.py` |
| run_anomalyclip_baseline.py | Removed: the wrapper emitted simulated metrics. |
| generate_reports.py | `scripts/reporting/generate_reports.py` |
| aggregate_run22_results.py | `scripts/reporting/aggregate_run22_results.py` |

The five historical entrypoints now live under `scripts/archive/`, with their unsupported status in [archive README](../scripts/archive/README.md).
