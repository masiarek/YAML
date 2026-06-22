"""
test_harness_selfcheck.py
=========================
Meta-test ("who tests the tests"): prove that the positive suite's winner check
would actually CATCH a wrong `expected_winners`.

`harness_cases/expected_winner_mismatch.yaml` is a valid election (Chocolate wins)
whose answer key deliberately says Vanilla. If this meta-test passes, we know the
positive `assert sorted(winners) == sorted(expected)` is meaningful — it isn't
silently passing regardless of the declared winner.
"""

import sys
from pathlib import Path

import yaml

ENGINE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_DIR / "tools_adam"))
from scenario_eval import scenario_winners  # noqa: E402

CASES = Path(__file__).resolve().parent / "harness_cases"


def test_positive_oracle_detects_wrong_expected_winner():
    """Single-winner: a deliberately-wrong answer key must differ from the real winner."""
    fixture = CASES / "expected_winner_mismatch.yaml"
    declared = [str(w) for w in yaml.safe_load(fixture.read_text(encoding="utf-8"))["expected_winners"]]
    winners, seats = scenario_winners(fixture)

    # The engine elects the REAL winner...
    assert winners == ["Chocolate"], f"unexpected real winner: {winners}"
    # ...which must NOT equal the deliberately-wrong answer key. So the very
    # assertion the positive suite uses would FAIL on this file — confirming the
    # winner check is real, not vacuous.
    assert sorted(winners) != sorted(declared), (
        "self-test broken: the declared winner should differ from the real one"
    )


def test_positive_oracle_detects_wrong_multiwinner_set():
    """Multi-winner: the SET assertion must catch a wrong key (order alone never
    counts as wrong — we compare sets)."""
    fixture = CASES / "wrong_winner_set_multiwinner.yaml"
    declared = [str(w) for w in yaml.safe_load(fixture.read_text(encoding="utf-8"))["expected_winners"]]
    winners, seats = scenario_winners(fixture)

    assert seats == 2 and len(winners) == 2, f"expected 2 winners, got {winners}"
    assert sorted(winners) == ["Almond", "Vanilla"], f"unexpected real winners: {winners}"
    # The declared set {Choco, Almond} differs from the real set {Almond, Vanilla},
    # so the positive suite's sorted-set assertion would FAIL here — as intended.
    assert sorted(winners) != sorted(declared), (
        "self-test broken: declared multi-winner set should differ from the real one"
    )
