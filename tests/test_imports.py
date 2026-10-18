import importlib
import pkgutil

import ssvp_rc


def test_all_package_modules_import():
    modules = [name for _, name, _ in pkgutil.walk_packages(ssvp_rc.__path__, prefix="ssvp_rc.")]
    assert len(modules) >= 15
    for name in modules:
        importlib.import_module(name)
