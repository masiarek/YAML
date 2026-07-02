"""
test_md_links.py
================
Every relative link in a tracked Markdown file must resolve to a real file or
folder. Folder reorganizations silently break these (a 2026-07 reorg left 85+
dangling links); this test makes that class of breakage impossible to commit.

The scan itself lives in scripts/check_repo_hygiene.py (`check_links`) so the
warn-only pre-commit report and this blocking test can never disagree.

Deliberate placeholders — link a screenshot you haven't captured yet as
`img/REPLACE_<what>.png` — are skipped by convention.
"""
import importlib.util
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
HYGIENE = REPO_ROOT / "scripts" / "check_repo_hygiene.py"


def _load_hygiene():
    spec = importlib.util.spec_from_file_location("check_repo_hygiene", HYGIENE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_repo_hygiene"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_all_relative_md_links_resolve():
    mod = _load_hygiene()
    broken = mod.check_links()
    assert not broken, (
        f"{len(broken)} broken relative Markdown link(s):\n" +
        "\n".join(f"  {f}  ->  ({raw})" for f, raw in broken) +
        "\n(Fix the path, or use the img/REPLACE_*.png placeholder convention "
        "for screenshots not yet captured.)"
    )
