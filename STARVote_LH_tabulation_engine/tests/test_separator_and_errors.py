"""
test_separator_and_errors.py
============================
Locks the input-robustness behavior added for copy-paste friendliness:

  * a SPACE-aligned ballots grid (the common slide/paste mistake) is auto-
    normalized to commas and tabulates correctly;
  * comma/tab input is left untouched;
  * an AMBIGUOUS block (multi-word names, a mixed separator, or an unsupported
    delimiter like '|') is NOT silently mis-parsed;
  * every error path exits NON-ZERO (regression guard for a bug where the
    "No valid ballots" path returned exit code 0 on an error);
  * a broken-YAML (block-scalar indentation) error prints a copy-paste template.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"


def _load_engine():
    spec = importlib.util.spec_from_file_location("slh_engine_for_tests", WRAPPER)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["slh_engine_for_tests"] = mod
    spec.loader.exec_module(mod)
    return mod


engine = _load_engine()
norm = engine._normalize_ballot_separators


def _run_cli(path):
    return subprocess.run(
        [sys.executable, str(WRAPPER), str(path)],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )


def _write(tmp_path, ballots_block):
    p = tmp_path / "case.yaml"
    p.write_text("voting_method: STAR\nnum_winners: 1\nballots: |-\n" + ballots_block)
    return p


# --- unit: the separator normalizer -----------------------------------------
def test_spaces_become_commas():
    assert norm("A B C\n5 4 0\n1 5 2") == "A, B, C\n5, 4, 0\n1, 5, 2"


def test_extra_spacing_collapses():
    assert norm("Apple  Banana  Cherry\n5   4   0") == "Apple, Banana, Cherry\n5, 4, 0"


def test_comma_input_untouched():
    src = "A, B, C\n5, 4, 0"
    assert norm(src) == src


def test_tab_input_untouched():
    src = "A\tB\tC\n5\t4\t0"
    assert norm(src) == src


def test_ragged_multiword_names_untouched():
    # header -> 4 tokens, rows -> 2 tokens: ambiguous, must NOT be guessed
    src = "Plain Choco Almond Choco\n5 4\n3 5"
    assert norm(src) == src


def test_mixed_comma_and_space_untouched():
    # a comma is present anywhere -> treat as comma-delimited, leave it alone
    src = "A B C\n5, 4 0"
    assert norm(src) == src


# --- CLI: a space-aligned grid tabulates correctly --------------------------
def test_space_aligned_ballot_tabulates(tmp_path):
    p = _write(tmp_path, "  Apple  Banana  Cherry\n  5  4  0\n  5  0  2\n  1  5  3\n")
    proc = _run_cli(p)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "Apple wins" in proc.stdout, proc.stdout


# --- CLI: every error path exits non-zero (the bug we fixed) ----------------
@pytest.mark.parametrize("ballots", [
    "  A|B|C\n  5|4|0\n  1|5|2\n",          # unsupported delimiter (pipe)
    "  A B C\n  5, 4 0\n  1 5 2\n",          # mixed comma + space
    "  Plain Choco Almond Choco\n  5 4\n  3 5\n",  # ambiguous multi-word names
])
def test_bad_ballots_exit_nonzero_cleanly(tmp_path, ballots):
    proc = _run_cli(_write(tmp_path, ballots))
    out = proc.stdout + proc.stderr
    assert proc.returncode == 1, f"expected exit 1, got {proc.returncode}\n{out}"
    assert "Traceback" not in out, f"leaked a traceback:\n{out}"


# --- CLI: a broken-YAML error prints a copy-paste template ------------------
def test_bad_indentation_prints_template(tmp_path):
    # header indented far more than the rows -> block ends early -> YAML error
    p = _write(tmp_path, "            A  B  C\n  5  4  0\n  1  5  2\n")
    proc = _run_cli(p)
    out = proc.stdout + proc.stderr
    assert proc.returncode == 1
    assert "Minimal example" in out and "ballots: |-" in out, out
