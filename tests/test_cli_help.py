import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_every_active_argparse_script_answers_help():
    env = os.environ.copy()
    env.update(CUDA_VISIBLE_DEVICES="", HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1")
    scripts = [path for path in sorted((ROOT / "scripts").rglob("*.py"))
               if "archive" not in path.parts and "argparse.ArgumentParser" in path.read_text()]
    assert len(scripts) >= 13
    for path in scripts:
        result = subprocess.run([sys.executable, str(path), "--help"], cwd=ROOT, env=env,
                                capture_output=True, text=True, timeout=60)
        assert result.returncode == 0, f"{path}: {result.stderr[-1500:]}"
        assert "usage:" in result.stdout.lower(), path
