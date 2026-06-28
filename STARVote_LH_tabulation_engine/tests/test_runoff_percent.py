"""
test_runoff_percent.py
======================
Locks the optional runoff percentage summary line:

  * the line uses the DECIDED-VOTERS denominator — voters who expressed a
    preference between the two finalists — so Equal Support is EXCLUDED;
  * it is OFF on screen by default (house "less is more");
  * it is ON when `options: { show_runoff_percent: true }`;
  * the always-full `_tabulated` copy carries it regardless of the file option.

Fixture election (scores 0-5):

    A,B,C
    5,4,0      A>B
    5,4,0      A>B
    2,5,0      B>A
    3,3,0      A==B  -> Equal Support
    4,0,5      A>B

  Scores: A=19, B=16, C=5  -> finalists A,B.
  Runoff A-vs-B: A=3, B=1, Equal Support=1  -> decided=4 (NOT 5).
  Expected line: "Voters with a preference: 4. A 3 (75%) vs B 1 (25%); majority = 3."
"""

import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

EXPECTED = "Voters with a preference: 4. A 3 (75%) vs B 1 (25%); majority = 3."

BALLOTS = "  A,B,C\n  5,4,0\n  5,4,0\n  2,5,0\n  3,3,0\n  4,0,5\n"


def _run_cli(path):
    return subprocess.run(
        [sys.executable, str(WRAPPER), str(path)],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )


def _write(tmp_path, with_option):
    d = tmp_path / "d"
    d.mkdir()
    p = d / "case.yaml"
    opt = "options:\n  show_runoff_percent: true\n" if with_option else ""
    p.write_text(f"voting_method: STAR\nnum_winners: 1\n{opt}ballots: |-\n{BALLOTS}")
    return p


def _tabulated_text(yaml_path):
    # tabulated_output_path: out_dir = p.parent.parent / (p.parent.name + "_tabulated")
    hits = list(yaml_path.parent.parent.glob("*_tabulated/case_tabulated.txt"))
    assert hits, "no _tabulated copy was written"
    return hits[0].read_text()


def _write_nested(tmp_path):
    # BetterVoting-style nested schema: options live under `election.options`,
    # which the loader previously ignored entirely (regression guard).
    d = tmp_path / "n"
    d.mkdir()
    p = d / "case.yaml"
    p.write_text(
        "election:\n"
        "  options:\n"
        "    show_runoff_percent: true\n"
        "  races:\n"
        "  - num_winners: 1\n"
        "    voting_method: STAR\n"
        "    ballots: |-\n"
        + "".join("      " + ln + "\n" for ln in BALLOTS.strip("\n").split("\n"))
    )
    return p


def test_line_on_screen_when_option_set(tmp_path):
    proc = _run_cli(_write(tmp_path, with_option=True))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert EXPECTED in proc.stdout, proc.stdout


def test_nested_election_options_are_honored(tmp_path):
    # `election.options.show_runoff_percent: true` must reach the render — the bug
    # was that the whole nested options block was dropped, so nothing applied.
    proc = _run_cli(_write_nested(tmp_path))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert EXPECTED in proc.stdout, proc.stdout


def test_line_absent_on_screen_by_default(tmp_path):
    proc = _run_cli(_write(tmp_path, with_option=False))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "Voters with a preference" not in proc.stdout, proc.stdout


def test_tabulated_copy_always_has_line(tmp_path):
    # Even with the option OFF on screen, the full _tabulated copy forces it on.
    yaml_path = _write(tmp_path, with_option=False)
    proc = _run_cli(yaml_path)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert EXPECTED in _tabulated_text(yaml_path)


def test_equal_support_excluded_from_denominator(tmp_path):
    # The denominator is 4 (decided), not 5 (all ballots): the Equal Support
    # ballot must not be counted in the runoff percentage.
    proc = _run_cli(_write(tmp_path, with_option=True))
    assert "preference: 4." in proc.stdout and "preference: 5." not in proc.stdout, proc.stdout
