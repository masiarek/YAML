"""
test_negative_validation.py
===========================
Negative tests: malformed single-winner files must FAIL with a clear, specific
error message (exit code 1) — not a traceback, and not a silent wrong answer.

Fixtures live in `tests/negative_cases/`. Each is a current-schema (flat YAML)
STAR file with one deliberate defect, plus one file that bundles several defects
to confirm they're reported together.

Covers:
  * wrong number of columns (too few / too many)
  * invalid characters / out-of-range scores
  * ranked ballots under a score method
  * single-winner method asked for multiple seats
  * MULTIPLE errors in a single file (all reported before exit)
"""

import subprocess
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"
NEG_DIR = Path(__file__).resolve().parent / "negative_cases"
LIB_NEG_DIR = REPO_ROOT / "YAML_library" / "2_negative"


def _run_cli(path):
    return subprocess.run(
        [sys.executable, str(WRAPPER), str(path)],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )


# fixture filename -> substrings that MUST appear in the error output
SINGLE_ERROR_CASES = {
    "neg_wrong_columns.yaml":  ["Error: STAR ballots use scores 0..5",
                                "has 2 value(s), expected 3"],
    "neg_extra_columns.yaml":  ["has 4 value(s), expected 3"],
    "neg_bad_characters.yaml": ["invalid: Bob=x"],
    "neg_out_of_range.yaml":   ["invalid: Bob=7"],
    "neg_ranked_in_star.yaml": ["is a score-ballot method, but the ballots are ranked"],
    "neg_seats_mismatch.yaml": ["elects a single winner", "seats=3"],
}


@pytest.mark.parametrize(
    "fname,needles", list(SINGLE_ERROR_CASES.items()), ids=list(SINGLE_ERROR_CASES)
)
def test_negative_reports_expected_message(fname, needles):
    proc = _run_cli(NEG_DIR / fname)
    assert proc.returncode == 1, (
        f"{fname}: expected exit 1, got {proc.returncode}\n{proc.stdout}\n{proc.stderr}"
    )
    out = proc.stdout + proc.stderr
    assert "Traceback" not in out, f"{fname}: leaked a traceback:\n{out}"
    for needle in needles:
        assert needle in out, f"{fname}: expected {needle!r} in:\n{out}"


def test_multiple_errors_in_one_file_are_all_reported():
    proc = _run_cli(NEG_DIR / "neg_multiple_errors.yaml")
    assert proc.returncode == 1
    out = proc.stdout + proc.stderr
    assert "Traceback" not in out
    # all three distinct defects appear together (wrong columns + 2 invalids)
    assert "has 2 value(s), expected 3" in out
    assert "invalid: Bob=x" in out
    assert "invalid: Bob=7" in out
    # at least three per-ballot offending lines listed before the single exit
    offending = [l for l in out.splitlines() if l.strip().startswith("ballot ")]
    assert len(offending) >= 3, f"expected >=3 offending-ballot lines:\n{out}"


def test_old_nested_schema_gives_friendly_error_not_traceback():
    """A file in the OLD nested schema (or with no flat 'ballots:') must produce a
    friendly message, not a Python KeyError traceback."""
    proc = _run_cli(NEG_DIR / "neg_old_nested_schema.yaml")
    assert proc.returncode == 1
    out = proc.stdout + proc.stderr
    assert "Traceback" not in out, f"leaked a traceback:\n{out}"
    assert "no 'ballots:' block found" in out
    assert "Minimal example (copy & paste):" in out   # the key-components template


# --- The migrated legacy YAML_library/2_negative fixtures ---------------------
# Each was converted from the old nested schema to the current flat schema while
# preserving (or, where a feature no longer exists, repurposing) its defect.
LIB_CASES = {
    "bv10_neg1.yaml": ["has 3 value(s), expected 2"],
    "bv10_neg2.yaml": ["elects a single winner", "seats=2"],
    "bv15_neg1.yaml": ["Approval ballots may only use scores {0, 1}", "invalid: Blake=5"],
    "bv15_neg2.yaml": ["invalid: Blake=x"],
    "bv20_neg1.yaml": ["has 2 value(s), expected 3"],
    "bv20_neg2.yaml": ["STAR ballots use scores 0..5", "invalid: Blake=a"],
}


@pytest.mark.parametrize("fname,needles", list(LIB_CASES.items()), ids=list(LIB_CASES))
def test_yaml_library_negative(fname, needles):
    proc = _run_cli(LIB_NEG_DIR / fname)
    assert proc.returncode == 1, (
        f"{fname}: expected exit 1, got {proc.returncode}\n{proc.stdout}\n{proc.stderr}"
    )
    out = proc.stdout + proc.stderr
    assert "Traceback" not in out, f"{fname}: leaked a traceback:\n{out}"
    for needle in needles:
        assert needle in out, f"{fname}: expected {needle!r} in:\n{out}"


def test_every_yaml_library_negative_fails_cleanly():
    """Inventory guard: EVERY file under YAML_library/2_negative must exit non-zero
    with a clear error and no traceback (no silent pass, no crash)."""
    files = sorted(LIB_NEG_DIR.glob("*.yaml"))
    assert files, "no YAML_library/2_negative fixtures found"
    for p in files:
        proc = _run_cli(p)
        out = proc.stdout + proc.stderr
        assert proc.returncode != 0, f"{p.name}: expected non-zero exit\n{out}"
        assert "Traceback" not in out, f"{p.name}: leaked a traceback:\n{out}"
        assert "Error" in out, f"{p.name}: no 'Error' message:\n{out}"
