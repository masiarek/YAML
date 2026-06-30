"""
test_yaml_index_current.py
==========================
Anti-staleness guard for the by-voting-method YAML index.

Regenerates the index in memory (scripts/build_yaml_index.py) and asserts the
committed file 00_start_here/YAML_test_case_index/README_YAML_test_case_index.md matches. If you add,
move, or remove a YAML election file and forget to refresh the index, this fails
with a clear instruction.
"""
import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
GEN = REPO_ROOT / "scripts" / "build_yaml_index.py"
INDEX = REPO_ROOT / "00_start_here" / "YAML_test_case_index" / "README_YAML_test_case_index.md"


def _load_generator():
    spec = importlib.util.spec_from_file_location("build_yaml_index", GEN)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["build_yaml_index"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_yaml_index_is_current():
    if not GEN.exists():
        pytest.skip("build_yaml_index.py not present")
    mod = _load_generator()
    expected = mod.render(mod.collect())
    actual = INDEX.read_text() if INDEX.exists() else ""
    assert actual == expected, (
        "YAML index is stale. Regenerate it with:\n"
        "    python scripts/build_yaml_index.py\n"
        "(a YAML election file was added/moved/removed since it was last built)."
    )
