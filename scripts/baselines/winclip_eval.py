import os
import sys
import argparse
import logging
import csv
import numpy as np
import torch
from ssvp_rc.paths import DATASETS_DIR, OUTPUTS_DIR



def ensure_category_has_defects(mvtec_dir, category):
    test_dir = os.path.join(mvtec_dir, category, 'test')
    if not os.path.isdir(test_dir):
        raise FileNotFoundError(f"Test directory not found: {test_dir}")
    subdirs = [d for d in os.listdir(test_dir) if os.path.isdir(os.path.join(test_dir, d))]
    defect_subdirs = [d for d in subdirs if d != 'good']
    if len(defect_subdirs) == 0:
        raise RuntimeError(f"No defect images found for category '{category}' in {test_dir}")


def ground_truth_exists(mvtec_dir, category):
    gt_dir = os.path.join(mvtec_dir, category, 'ground_truth')
    return os.path.isdir(gt_dir) and len(os.listdir(gt_dir)) > 0


def add_gaussian_noise(batch, noise_std, noise_p):
    if noise_std <= 0.0 or noise_p <= 0.0:
        return batch
    noisy = batch.clone()
    b = noisy.shape[0]
    apply_mask = torch.rand((b, 1, 1, 1), device=noisy.device) < noise_p
    noise = torch.randn_like(noisy) * noise_std
    noisy = torch.where(apply_mask, noisy + noise, noisy)
    return torch.clamp(noisy, 0.0, 1.0)


def run_category(category, mvtec_dir, out_root, device, batch_size=32, noise_std=0.0, noise_p=0.0):
    # configure dataset path used by WinCLIP
    from third_party.winclip.datasets import get_dataloader_from_args, denormalization
    from third_party.winclip.utils.eval_utils import specify_resolution
    from third_party.winclip.utils.metrics import metric_cal
    from third_party.winclip.WinCLIP.model import WinClipAD
    from third_party.winclip.utils.training_utils import setup_seed
    import third_party.winclip.datasets.mvtec as mvtec_mod

    # handle cases where dataset layout is either <mvtec-root>/<category>/(test|train)
    # or <mvtec-root>/<category>/<category>/(test|train)
    category_path = os.path.join(mvtec_dir, category)
    if os.path.isdir(os.path.join(category_path, 'test')):
        mvtec_mod.MVTEC2D_DIR = mvtec_dir
    elif os.path.isdir(os.path.join(category_path, category, 'test')):
        # nested layout, point MVTEC2D_DIR to the category folder so load_mvtec finds category/<test>
        mvtec_mod.MVTEC2D_DIR = category_path
    else:
        # leave as provided; ensure check will catch missing dirs
        mvtec_mod.MVTEC2D_DIR = mvtec_dir

    ensure_category_has_defects(mvtec_mod.MVTEC2D_DIR, category)

    kwargs = {
        'dataset': 'mvtec',
        'class_name': category,
        'img_resize': 240,
        'img_cropsize': 240,
        'resolution': 224,
        'batch_size': batch_size,
        'k_shot': 0,
        'experiment_indx': 0,
        'scales': (2, 3),
    }

    setup_seed(42)

    device_str = device if device is not None else ('cuda:0' if torch.cuda.is_available() else 'cpu')

    # dataloader
    test_dataloader, _ = get_dataloader_from_args(phase='test', **kwargs)

    # model
    scales_val = kwargs.pop('scales', (2, 3))
    model = WinClipAD(out_size_h=kwargs['resolution'], out_size_w=kwargs['resolution'], device=device_str,
                      backbone='ViT-B-16-plus-240', pretrained_dataset='laion400m_e32', scales=scales_val, **kwargs)
    model = model.to(device_str)
    model.eval_mode()
    model.build_text_feature_gallery(category)

    scores = []
    test_imgs = []
    gt_list = []
    gt_mask_list = []
    names = []

    # output dirs
    score_dir = os.path.join(out_root, 'scores', category)
    os.makedirs(score_dir, exist_ok=True)
    tag = 'noisy' if (noise_std > 0.0 and noise_p > 0.0) else 'clean'
    csv_path = os.path.join(out_root, f'{category}_{tag}_scores.csv')

    from PIL import Image

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['image_path', 'gt_label', 'anomaly_score'])

        for (data, mask, label, name, img_type) in test_dataloader:
            data = [model.transform(Image.fromarray(f.numpy())) for f in data]
            data = torch.stack(data, dim=0)

            for d, n, l, m in zip(data, name, label, mask):
                test_imgs += [denormalization(d.cpu().numpy())]
                l = l.numpy()
                m = m.numpy()
                m[m > 0] = 1

                names += [n]
                gt_list += [l]
                gt_mask_list += [m]

            data = data.to(device_str)
            data = add_gaussian_noise(data, noise_std=noise_std, noise_p=noise_p)
            batch_scores = model(data)  # list of numpy arrays (H,W)

            # save per-image score maps and write csv rows
            for s_map, nm, lb in zip(batch_scores, name, label):
                # s_map is (H,W)
                base = os.path.splitext(os.path.basename(nm))[0]
                npy_path = os.path.join(score_dir, base + '.npy')
                np.save(npy_path, s_map)
                img_score = float(np.max(s_map))
                writer.writerow([nm, int(lb.item()), img_score])

            scores += batch_scores

    # resize/align
    test_imgs, scores, gt_mask_list = specify_resolution(test_imgs, scores, gt_mask_list, resolution=(kwargs['resolution'], kwargs['resolution']))

    # compute metrics
    metrics = metric_cal(np.array(scores), gt_list, gt_mask_list, cal_pro=ground_truth_exists(mvtec_dir, category))

    return metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mvtec-root', type=str, default=str(DATASETS_DIR))
    parser.add_argument('--out-root', type=str, default=str(OUTPUTS_DIR / 'winclip'))
    parser.add_argument('--device', type=str, default=None)
    parser.add_argument('--categories', nargs='+', default=['cable', 'transistor', 'capsule'])
    parser.add_argument('--noise-std', type=float, default=0.0)
    parser.add_argument('--noise-p', type=float, default=0.0)
    args = parser.parse_args()

    os.makedirs(args.out_root, exist_ok=True)

    summary = {}
    for cat in args.categories:
        logging.info(f'Running WinCLIP on category: {cat}')
        try:
            metrics = run_category(cat, args.mvtec_root, args.out_root, args.device,
                                   noise_std=args.noise_std, noise_p=args.noise_p)
        except Exception as e:
            logging.error(f'Error processing {cat}: {e}')
            raise
        summary[cat] = metrics
        logging.info(f'{cat} metrics: {metrics}')

    # print consolidated table
    mode_name = 'noisy' if (args.noise_std > 0.0 and args.noise_p > 0.0) else 'clean'
    print(f'\nModel: WinCLIP ({mode_name})')
    print('Category     I-AUROC   I-F1    I-AP    P-AUROC   P-PRO   P-AP')
    i_auros = []
    for cat in args.categories:
        m = summary[cat]
        print(f"{cat:<12}{m['i_roc']:8.2f}{m['i_f1']:9.2f}{m.get('i_ap',0):9.2f}{m['p_roc']:10.2f}{m['p_pro']:9.2f}{m.get('p_ap',0):9.2f}")
        i_auros.append(m['i_roc'])

    mean_i = float(np.mean(i_auros))
    print(f"mean         {mean_i:8.2f}")


if __name__ == '__main__':
    main()
