"""
test_single_winner_positive.py
==============================
Positive regression tests for the single-winner STAR example/test cases.

For every single-winner STAR file that declares `expected_winners`, we:
  1. run the engine through its CLI (a subprocess) — this is the real path that
     also (re)writes the `*_tabulated/<name>_tabulated.txt` sibling, so the test
     doubles as a check that tabulation succeeds and the _tabulated file is
     produced;
  2. assert the process exits 0;
  3. assert the elected winner equals `expected_winners` (computed with the
     shared, no-print `scenario_eval` helper so we don't parse report text);
  4. assert the `_tabulated` sibling now exists.

Scope: single-winner *score* methods only (voting_method STAR / default).
Ranked (RCV/STV) and Approval files are skipped — they have their own paths.
"""

import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

# tools_adam holds the shared no-print evaluator used by the engine + tests.
sys.path.insert(0, str(ENGINE_DIR / "tools_adam"))
from scenario_eval import scenario_winners  # noqa: E402

# Folders that hold single-winner example/test cases.
SINGLE_WINNER_DIRS = [
    REPO_ROOT / "01_Single_winner",
    REPO_ROOT / "split_voting",
    REPO_ROOT / "YAML_library" / "1_positive",
]


def _load(path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _single_winner_positive_files():
    files = []
    for d in SINGLE_WINNER_DIRS:
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.yaml")):
            data = _load(p)
            if not isinstance(data, dict) or "ballots" not in data:
                continue
            method = str(data.get("voting_method", "star")).strip().lower()
            if method != "star":          # single-winner STAR only
                continue
            if data.get("num_winners", 1) not in (1, None):
                continue
            if ">" in str(data.get("ballots", "")):   # ranked -> not STAR
                continue
            ew = data.get("expected_winners")
            if not (isinstance(ew, list) and len(ew) == 1):
                continue
            files.append(p)
    return files


POSITIVE = _single_winner_positive_files()
POSITIVE_IDS = [str(p.relative_to(REPO_ROOT)) for p in POSITIVE]


def _run_cli(path):
    return subprocess.run(
        [sys.executable, str(WRAPPER), str(path)],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )


def _tabulated_sibling(path):
    return path.parent.parent / (path.parent.name + "_tabulated") / (
        path.stem + "_tabulated.txt"
    )


def test_at_least_one_case_discovered():
    assert POSITIVE, "no single-winner positive cases were discovered"


@pytest.mark.parametrize("path", POSITIVE, ids=POSITIVE_IDS)
def test_single_winner_tabulates_and_elects_expected(path):
    expected = _load(path)["expected_winners"]

    # 1-2. Full CLI run: must succeed (this also (re)writes the _tabulated copy).
    proc = _run_cli(path)
    assert proc.returncode == 0, (
        f"{path.name} exited {proc.returncode}\n--- stdout ---\n{proc.stdout}\n"
        f"--- stderr ---\n{proc.stderr}"
    )

    # 3. Winner matches expectation (structured, not text-parsed).
    winners, seats = scenario_winners(path)
    assert seats == 1, f"{path.name}: num_winners should be 1, got {seats}"
    assert sorted(winners) == sorted(str(w) for w in expected), (
        f"{path.name}: elected {winners}, expected {expected}"
    )

    # 4. The _tabulated sibling was produced.
    tab = _tabulated_sibling(path)
    assert tab.exists(), f"{path.name}: expected _tabulated file at {tab}"
