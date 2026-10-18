from pathlib import Path

import pytest

from ssvp_rc import paths


def test_paths_resolve_from_nested_location():
    assert paths.find_repo_root(Path(__file__)) == paths.REPO_ROOT
    assert Path(paths.default_config_path()).is_file()
    assert paths.DATASETS_DIR == paths.REPO_ROOT / "data" / "mvtec"
    assert paths.OUTPUTS_DIR == paths.REPO_ROOT / "outputs"


def test_root_lookup_rejects_unrelated_directory(tmp_path):
    with pytest.raises(FileNotFoundError):
        paths.find_repo_root(tmp_path)
