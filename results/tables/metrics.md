# All reported metrics

| Run ID | Title | Model | Status | Eval | Categories | Resolution | Noise | I-AUROC | I-F1 | I-AP | P-AUROC | P-PRO | P-AP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ablation_m1_tiny/lora_no_consistency | ablation m1 tiny / lora no consistency | ssvp | rejected | clean | cable |  | none | 57.64 | 42.86 | 35.00 | 66.07 | 27.72 | 1.89 |
| ablation_m1_tiny/lora_no_consistency | ablation m1 tiny / lora no consistency | ssvp | rejected | noisy | cable |  | heavy_v1 | 49.70 | 42.62 | 28.96 | 58.69 | 22.91 | 1.27 |
| ablation_m1_tiny/no_consistency | ablation m1 tiny / no consistency | ssvp | rejected | clean | cable |  | none | 78.67 | 61.54 | 57.06 | 78.57 | 41.14 | 4.04 |
| ablation_m1_tiny/no_consistency | ablation m1 tiny / no consistency | ssvp | rejected | noisy | cable |  | heavy_v1 | 42.76 | 40.00 | 22.87 | 71.67 | 39.64 | 2.12 |
| apples_to_apples_run21_3ep/depth_pruning | apples to apples run21 3ep / depth pruning | ssvp | rejected | clean | cable |  | none | 53.97 | 44.44 | 31.72 | 80.67 | 35.06 | 2.75 |
| apples_to_apples_run21_3ep/depth_pruning | apples to apples run21 3ep / depth pruning | ssvp | rejected | noisy | cable |  | heavy_v1 | 57.94 | 47.83 | 36.53 | 81.23 | 43.37 | 2.75 |
| apples_to_apples_run21_3ep/differentiated_pruning | apples to apples run21 3ep / differentiated pruning | ssvp | rejected | clean | cable |  | none | 44.54 | 39.13 | 33.62 | 82.44 | 37.79 | 2.84 |
| apples_to_apples_run21_3ep/differentiated_pruning | apples to apples run21 3ep / differentiated pruning | ssvp | rejected | noisy | cable |  | heavy_v1 | 45.24 | 39.13 | 24.98 | 85.12 | 44.68 | 3.42 |
| compression_gate/depth_pruning_heads/prelim_3ep | compression gate / depth pruning heads / prelim 3ep | ssvp | rejected | clean | cable |  | none | 53.97 | 44.44 | 31.72 | 80.67 | 35.06 | 2.75 |
| compression_gate/depth_pruning_heads/prelim_3ep | compression gate / depth pruning heads / prelim 3ep | ssvp | rejected | noisy | cable |  | heavy_v1 | 57.94 | 47.83 | 36.53 | 81.23 | 43.37 | 2.75 |
| compression_gate/differentiated_pruning_heads/prelim_3ep | compression gate / differentiated pruning heads / prelim 3ep | ssvp | rejected | clean | cable |  | none | 44.54 | 39.13 | 33.62 | 82.44 | 37.79 | 2.84 |
| compression_gate/differentiated_pruning_heads/prelim_3ep | compression gate / differentiated pruning heads / prelim 3ep | ssvp | rejected | noisy | cable |  | heavy_v1 | 45.24 | 39.13 | 24.98 | 85.12 | 44.68 | 3.42 |
| noise_ap_pro_prelim_3ep/v1_consistency_mild | noise ap pro prelim 3ep / v1 consistency mild | ssvp | exploratory | clean | cable |  | none | 52.38 | 42.86 | 28.86 | 84.99 | 48.06 | 3.33 |
| noise_ap_pro_prelim_3ep/v1_consistency_mild | noise ap pro prelim 3ep / v1 consistency mild | ssvp | exploratory | noisy | cable |  | heavy_v1 | 52.08 | 40.74 | 29.73 | 84.64 | 51.98 | 3.21 |
| noise_ap_pro_prelim_3ep/v2_consistency_prolite | noise ap pro prelim 3ep / v2 consistency prolite | ssvp | exploratory | clean | cable |  | none | 46.63 | 39.13 | 26.39 | 83.21 | 53.94 | 3.01 |
| noise_ap_pro_prelim_3ep/v2_consistency_prolite | noise ap pro prelim 3ep / v2 consistency prolite | ssvp | exploratory | noisy | cable |  | heavy_v1 | 49.21 | 39.56 | 27.26 | 80.95 | 52.08 | 2.67 |
| noise_ap_pro_prelim_3ep/v3_consistency_prolite_entropy | noise ap pro prelim 3ep / v3 consistency prolite entropy | ssvp | exploratory | clean | cable |  | none | 48.81 | 40.00 | 27.71 | 84.11 | 48.93 | 3.28 |
| noise_ap_pro_prelim_3ep/v3_consistency_prolite_entropy | noise ap pro prelim 3ep / v3 consistency prolite entropy | ssvp | exploratory | noisy | cable |  | heavy_v1 | 50.69 | 39.56 | 27.87 | 79.91 | 44.88 | 2.62 |
| noisy_dae_3ep/dae_noisy_train_rerun | noisy dae 3ep / dae noisy train rerun | ssvp | rejected | clean | cable |  | none | 52.88 | 40.91 | 32.05 | 79.88 | 39.00 | 2.50 |
| noisy_dae_3ep/dae_noisy_train_rerun | noisy dae 3ep / dae noisy train rerun | ssvp | rejected | noisy | cable |  | heavy_v1 | 58.83 | 43.24 | 41.72 | 85.05 | 45.72 | 3.42 |
| run15 | run15 | ssvp | exploratory | clean | cable |  | none | 89.66 | 86.41 | 93.58 | 69.81 | 25.63 | 5.25 |
| run16_seg | run16 seg | ssvp | exploratory | clean | cable |  | none | 100.00 | 100.00 | 100.00 | 92.87 | 83.41 | 73.62 |
| run21_resplit_15es | Cable 70/20/10 resplit, 15 epochs | ssvp | recommended | clean | cable |  | none | 97.42 | 84.85 | 93.62 | 95.34 | 29.54 | 50.89 |
| run21_resplit_15es | Cable 70/20/10 resplit, 15 epochs | ssvp | recommended | noisy | cable |  | heavy_v1 | 87.00 | 75.86 | 81.33 | 91.82 | 58.27 | 34.91 |
| run22_promptdice_3ep | PromptDice, 3 epochs | ssvp | exploratory | clean | cable |  | none | 67.96 | 48.65 | 45.37 | 83.07 | 42.33 | 11.29 |
| run22_promptdice_3ep | PromptDice, 3 epochs | ssvp | exploratory | noisy | cable |  | heavy_v1 | 61.81 | 45.83 | 41.17 | 74.37 | 42.34 | 3.00 |
| run23_robustpatch_15ep | run23 robustpatch 15ep | ssvp | exploratory | clean | cable |  | none | 72.92 | 54.17 | 46.90 | 76.99 | 40.71 | 3.87 |
| run23_robustpatch_15ep | run23 robustpatch 15ep | ssvp | exploratory | noisy | cable |  | heavy_v1 | 46.63 | 39.56 | 25.83 | 68.17 | 34.96 | 1.83 |
| run28_lora_segfix_10ep | run28 lora segfix 10ep | ssvp | exploratory | clean | cable |  | none | 72.42 | 54.55 | 40.97 | 80.24 | 27.10 | 3.50 |
| run28_lora_segfix_10ep | run28 lora segfix 10ep | ssvp | exploratory | noisy | cable |  | heavy_v1 | 74.31 | 53.85 | 47.00 | 76.56 | 28.55 | 2.95 |
| run29_entropy_pro_noisycal_5ep | run29 entropy pro noisycal 5ep | ssvp | exploratory | clean | cable |  | none | 66.67 | 48.28 | 51.02 | 64.21 | 34.45 | 3.55 |
| run29_entropy_pro_noisycal_5ep | run29 entropy pro noisycal 5ep | ssvp | exploratory | noisy | cable |  | heavy_v1 | 54.37 | 40.51 | 36.48 | 69.59 | 35.25 | 2.98 |
| run30_entropy_pro_noisycal_15es | run30 entropy pro noisycal 15es | ssvp | exploratory | clean | cable |  | none | 66.07 | 47.76 | 38.12 | 79.91 | 52.72 | 2.89 |
| run30_entropy_pro_noisycal_15es | run30 entropy pro noisycal 15es | ssvp | exploratory | noisy | cable |  | heavy_v1 | 45.34 | 44.16 | 21.84 | 82.09 | 43.49 | 2.58 |
| run21_on_transistor | Cable-trained run21 on transistor | ssvp | exploratory | cross_category | transistor |  | none | 43.125 |  | 42.909 | 70.238 | 27.563 |  |
| winclip_d1_cable_res240 | WinCLIP cable at 240 | winclip | exploratory | clean | cable | 240 | none | 44.51 |  |  | 49.41 | 0.00 |  |
| winclip_d1_transistor_res240 | WinCLIP transistor at 240 | winclip | exploratory | clean | transistor | 240 | none | 71.71 |  |  | 71.03 | 0.00 |  |
| winclip_d1_capsule_res240 | WinCLIP capsule at 240 | winclip | exploratory | clean | capsule | 240 | none | 54.57 |  |  | 84.36 | 0.00 |  |
| winclip_d1_cable_res336 | WinCLIP cable at 336 | winclip | exploratory | clean | cable | 336 | none | 51.46 |  |  | 48.51 | 0.00 |  |
| winclip_d1_transistor_res336 | WinCLIP transistor at 336 | winclip | exploratory | clean | transistor | 336 | none | 71.96 |  |  | 63.54 | 0.00 |  |
| winclip_d1_capsule_res336 | WinCLIP capsule at 336 | winclip | exploratory | clean | capsule | 336 | none | 57.72 |  |  | 82.83 | 0.00 |  |
| winclip_d1_cable_res518 | WinCLIP cable at 518 | winclip | exploratory | clean | cable | 518 | none | 55.55 |  |  | 52.63 | 0.00 |  |
| winclip_d1_transistor_res518 | WinCLIP transistor at 518 | winclip | exploratory | clean | transistor | 518 | none | 57.21 |  |  | 63.00 | 0.00 |  |
| winclip_d1_capsule_res518 | WinCLIP capsule at 518 | winclip | exploratory | clean | capsule | 518 | none | 56.16 |  |  | 78.64 | 0.00 |  |
| anomalyclip_d2_cable | AnomalyCLIP cable | anomalyclip | accepted | clean | cable |  | none | 61.3 |  | 45.1 | 86.1 | 64.7 |  |
| anomalyclip_d2_transistor | AnomalyCLIP transistor | anomalyclip | accepted | clean | transistor |  | none | 88.2 |  | 71.7 | 70.7 | 63.4 |  |
| anomalyclip_d2_capsule | AnomalyCLIP capsule | anomalyclip | accepted | clean | capsule |  | none | 86.4 |  | 79.3 | 98.9 | 94.0 |  |
| anomalyclip_d2_mean | AnomalyCLIP three-category mean | anomalyclip | accepted | clean | cable;transistor;capsule |  | none | 78.6 |  |  | 85.2 | 74.0 |  |
| winclip_summary_cable | WinCLIP separate source summary cable | winclip | exploratory | clean | cable |  | none | 44.64 | 76.35 | 56.97 | 49.43 | 29.41 | 3.02 |
| winclip_summary_transistor | WinCLIP separate source summary transistor | winclip | exploratory | clean | transistor |  | none | 71.71 | 67.39 | 56.0 | 71.0 | 0.0 | 12.47 |
| winclip_summary_capsule | WinCLIP separate source summary capsule | winclip | exploratory | clean | capsule |  | none | 54.33 | 90.46 | 85.42 | 84.39 | 0.0 | 5.76 |
| winclip_summary_mean | WinCLIP separate source summary mean | winclip | exploratory | clean | cable;transistor;capsule |  | none | 56.89 | 78.07 | 66.13 | 68.27 | 9.8 | 7.08 |
| winclip_summary_cable | WinCLIP separate source summary cable | winclip | exploratory | noisy | cable |  | winclip_gauss020 | 46.42 | 76.03 | 63.84 | 45.82 | 28.18 | 2.88 |
| winclip_summary_transistor | WinCLIP separate source summary transistor | winclip | exploratory | noisy | transistor |  | winclip_gauss020 | 42.42 | 57.55 | 41.46 | 62.48 | 0.0 | 10.94 |
| winclip_summary_capsule | WinCLIP separate source summary capsule | winclip | exploratory | noisy | capsule |  | winclip_gauss020 | 56.48 | 90.83 | 87.64 | 76.13 | 0.0 | 5.31 |
| winclip_summary_mean | WinCLIP separate source summary mean | winclip | exploratory | noisy | cable;transistor;capsule |  | winclip_gauss020 | 48.44 | 74.8 | 64.31 | 61.48 | 9.39 | 6.38 |
| run22_caption_compare_cable | Run22 caption comparison cable | ssvp | exploratory | clean | cable |  | none | 77.57936507936508 | 61.53846104142012 | 53.780314855937384 | 94.73455385869288 | 81.42378184136139 | 42.90750283463433 |
| run22_caption_compare_transistor | Run22 caption comparison transistor | ssvp | exploratory | clean | transistor |  | none | 73.14814814814814 | 66.66666622222223 | 60.11705685618729 | 91.49088375411755 | 79.90403674974738 | 46.910849986749994 |
| run22_caption_compare_capsule | Run22 caption comparison capsule | ssvp | exploratory | clean | capsule |  | none | 95.66666666666667 | 86.95652124007563 | 93.88528138528139 | 97.88630522301285 | 86.65451514659857 | 40.34364081527094 |
