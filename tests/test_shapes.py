"""Small CPU dummy-tensor cases adapted from the source shape script."""

import torch

from ssvp_rc.models.hsvs import ATFBlock, HSVS
from ssvp_rc.models.vcpg import VCPG
from ssvp_rc.models.vtam import VTAM
from ssvp_rc.models.losses import SSVPLoss
from ssvp_rc.paths import default_config_path
from ssvp_rc.utils import load_config


def test_trainable_module_shapes_and_gradients():
    torch.manual_seed(7)
    batch, tokens, clip_dim, dino_dim, proj = 1, 9, 16, 16, 12
    clip = torch.randn(batch, tokens, clip_dim)
    dino = torch.randn(batch, tokens, dino_dim)
    atf = ATFBlock(clip_dim, dino_dim, d_head=4, num_heads=3, d_proj=proj)
    assert atf(clip, dino).shape == (batch, tokens, proj)

    hsvs = HSVS(clip_dim, dino_dim, proj, d_head=4, num_heads=3, num_layers=2)
    global_syn, local_syn = hsvs(clip[:, 0], [clip, clip], dino[:, 0], [dino, dino])
    assert global_syn.shape == (batch, proj)
    assert [tuple(x.shape) for x in local_syn] == [(batch, tokens, proj)] * 2

    cfg = load_config(default_config_path())
    cfg["hsvs"]["d_proj"] = proj
    cfg["vcpg"].update(d_text=proj, d_latent=8, n_normal_prompts=2, n_abnormal_prompts=2)
    vcpg = VCPG(cfg)
    t_normal, t_abnormal, t_init_normal, t_init_abnormal, vae = vcpg(global_syn)
    n_agg, a_agg = vcpg.get_aggregated_prompt_features(t_normal, t_abnormal)
    assert n_agg.shape == a_agg.shape == (batch, proj)

    vtam = VTAM(d_proj=proj, num_layers=2)
    anomaly_map, anomaly_score = vtam(local_syn, global_syn, n_agg, a_agg)
    assert anomaly_map.shape == (batch, 1, 3, 3)
    assert anomaly_score.shape == (batch,)

    outputs = {
        "anomaly_map": anomaly_map,
        "anomaly_score": anomaly_score,
        "mu": vae["mu"], "logvar": vae["logvar"],
        "v_syn_global": global_syn, "v_recon": vae["v_recon"],
        "t_final_normal": t_normal, "t_final_abnormal": t_abnormal,
        "t_init_normal": t_init_normal, "t_init_abnormal": t_init_abnormal,
    }
    targets = {"mask": torch.randint(0, 2, (batch, 1, 3, 3)).float(), "label": torch.ones(batch)}
    loss, parts = SSVPLoss(cfg)(outputs, targets)
    assert loss.ndim == 0
    assert {"total", "seg", "class", "vae", "reg"} <= parts.keys()
    loss.backward()
    assert any(param.grad is not None for param in hsvs.parameters())
