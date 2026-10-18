"""Repository paths for scripts and vendored baselines."""

from pathlib import Path


def find_repo_root(start=None):
    current = Path(start or __file__).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "pyproject.toml").is_file():
            return candidate
    raise FileNotFoundError("pyproject.toml was not found above " + str(current))


REPO_ROOT = find_repo_root()
CONFIG_DIR = REPO_ROOT / "configs"
DATASETS_DIR = REPO_ROOT / "data" / "mvtec"
SAMPLE_INPUTS_DIR = REPO_ROOT / "data" / "samples"
SCRIPTS_DIR = REPO_ROOT / "scripts"
OUTPUTS_DIR = REPO_ROOT / "outputs"
LOGS_DIR = OUTPUTS_DIR
ABLATIONS_DIR = OUTPUTS_DIR / "ablations"
ABLATION_JSON_DIR = OUTPUTS_DIR / "ablation_json_results"


def default_config_path(config_name="default.yaml"):
    return str(CONFIG_DIR / config_name)
