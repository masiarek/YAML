"""
test_yaml_pages_current.py
==========================
The generated Markdown pages (`<folder>/<folder>_pages/<stem>.md`) must match
what `scripts/build_yaml_pages.py` would produce from the current YAMLs and
`_tabulated` mirrors — same pattern as the YAML-index staleness test, so the
pages can never silently drift from their sources.

If this fails, regenerate:

    python scripts/build_yaml_pages.py
"""
import importlib.util
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
SCRIPT = REPO_ROOT / "scripts" / "build_yaml_pages.py"


def _load():
    spec = importlib.util.spec_from_file_location("build_yaml_pages", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["build_yaml_pages"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_pages_exist_and_are_current():
    mod = _load()
    stale, orphans = mod.check()
    msg = []
    if stale:
        msg.append(f"{len(stale)} stale/missing page(s):")
        msg += [f"  {Path(p).relative_to(REPO_ROOT)}" for p in stale[:10]]
    if orphans:
        msg.append(f"{len(orphans)} orphan page(s) (source YAML gone):")
        msg += [f"  {Path(p).relative_to(REPO_ROOT)}" for p in orphans[:10]]
    assert not stale and not orphans, (
        "\n".join(msg) + "\nRegenerate with: python scripts/build_yaml_pages.py"
    )


def test_discovery_not_vacuous():
    mod = _load()
    assert len(mod.expected_pages()) >= 50, "page discovery collapsed"
