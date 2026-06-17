"""
test_scenarios.py
=================
Outcome tests for the example elections in `elections_illustrations/`.

These are OUR tests (separate from the upstream engine tests in test_all.py).
Each scenario file may carry an `expected_winners:` list; this suite tabulates
the file and asserts the engine still elects exactly those winners, and that the
winner count matches `num_winners`.

We assert on structured data (winner set + count) only — never on verbatim
report text — so the tests stay robust to display/formatting changes.

Regenerate / add expectations with:
    python tools_adam/add_expected_winners.py          # fill where missing
    python tools_adam/add_expected_winners.py --force   # rewrite all
"""

import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_DIR))
sys.path.insert(0, str(ENGINE_DIR / "tools_adam"))

import yaml  # noqa: E402

from scenario_eval import scenario_winners  # noqa: E402

SCENARIO_ROOT = ENGINE_DIR / "elections_illustrations"


def _scenario_files():
    files = []
    for p in sorted(SCENARIO_ROOT.rglob("*")):
        if p.is_file() and p.suffix.lower() in (".yaml", ".yml"):
            if not any(part.endswith("_tabulated") for part in p.relative_to(SCENARIO_ROOT).parts):
                files.append(p)
    return files


def _expected_winners(path):
    """Return the file's declared expected_winners list, or None if absent."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        ew = data.get("expected_winners")
        if isinstance(ew, list):
            return [str(w) for w in ew]
    return None


SCENARIOS = _scenario_files()
# Pretty ids like "Multi_winner/proportional_sss.yaml"
SCENARIO_IDS = [str(p.relative_to(SCENARIO_ROOT)) for p in SCENARIOS]


@pytest.mark.parametrize("path", SCENARIOS, ids=SCENARIO_IDS)
def test_scenario_winners(path):
    expected = _expected_winners(path)
    if expected is None:
        pytest.skip("no expected_winners declared in this file")

    winners, seats = scenario_winners(path)

    # Winner SET must match (order of election is not asserted).
    assert sorted(winners) == sorted(expected), (
        f"{path.name}: elected {winners}, expected {expected}"
    )
    # Number of winners must equal the number of seats.
    assert len(winners) == seats, (
        f"{path.name}: elected {len(winners)} winner(s) but num_winners={seats}"
    )


def test_every_scenario_has_expectations():
    """Soft inventory: list any scenario files lacking expected_winners."""
    missing = [p.name for p in SCENARIOS if _expected_winners(p) is None]
    # Not a hard failure target yet — surface them so they can be filled in.
    if missing:
        pytest.skip(f"{len(missing)} scenario(s) missing expected_winners: {missing}")
