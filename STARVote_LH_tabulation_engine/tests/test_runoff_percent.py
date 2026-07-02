"""
test_runoff_percent.py
======================
Locks the optional runoff percentage summary, in BOTH of its two forms:

  * ON SCREEN — one *self-reconciling* line. It uses the DECIDED-VOTERS
    denominator (voters who expressed a preference between the two finalists,
    so Equal Support is EXCLUDED) AND states that count against the total
    ballots with the Equal Support gap named inline — "N of TOTAL (E Equal
    Support)" — so the denominator never has to be inferred by subtraction.
  * IN THE `_tabulated` COPY — a "Runoff math" funnel that makes the same
    arithmetic explicit (TOTAL − Equal Support = decided), then the finalists'
    shares of the decided voters.

Behaviour locked here:
  * the on-screen line is OFF by default (house "less is more");
  * it is ON when `options: { show_runoff_percent: true }`;
  * the always-full `_tabulated` copy carries the funnel regardless of the
    file option;
  * the funnel does NOT appear on screen (echo stays a single line).

Fixture election (scores 0-5):

    A,B,C
    5,4,0      A>B
    5,4,0      A>B
    2,5,0      B>A
    3,3,0      A==B  -> Equal Support
    4,0,5      A>B

  Scores: A=19, B=16, C=5  -> finalists A,B.
  Runoff A-vs-B: A=3, B=1, Equal Support=1  -> decided=4 (NOT 5), total=5.
  Expected (two lines):  "Voters with a preference: 4 of 5 (1 Equal Support)."
                         "A 3 (75%) vs B 1 (25%); majority = 3."
"""

import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

# On-screen summary — now two lines (self-reconciling: "4 of 5 (1 Equal Support)").
EXPECTED = (
    "Voters with a preference: 4 of 5 (1 Equal Support).\n"
    "   A 3 (75%) vs B 1 (25%); majority = 3."
)

# Distinctive fragments of the `_tabulated` "Runoff math" funnel.
FUNNEL_HEADER = "Runoff math:"
FUNNEL_TOTAL = "5  ballots cast"
FUNNEL_EQUAL = "Equal Support (no preference between the two finalists)"
FUNNEL_DECIDED = "4  voters with a preference  (majority = 3)"
FUNNEL_SHARES = "A 3 (75%)  ·  B 1 (25%)"

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
    # tabulated_output_path: out_dir = p.parent / (p.parent.name + "_tabulated")
    hits = list(yaml_path.parent.glob("*_tabulated/case_tabulated.txt"))
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


# --- positive: the on-screen line ------------------------------------------

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


def test_line_self_reconciles(tmp_path):
    # The whole point of the new wording: decided, total, and the Equal Support
    # gap all appear so the reader can see 5 − 1 = 4 without hunting.
    proc = _run_cli(_write(tmp_path, with_option=True))
    assert "4 of 5 (1 Equal Support)" in proc.stdout, proc.stdout


def test_equal_support_excluded_from_denominator(tmp_path):
    # The percentage denominator is 4 (decided), not 5 (all ballots): the Equal
    # Support ballot is named in the reconciliation but kept OUT of the share.
    proc = _run_cli(_write(tmp_path, with_option=True))
    assert "preference: 4 of 5" in proc.stdout, proc.stdout
    assert "75%" in proc.stdout and "25%" in proc.stdout, proc.stdout
    # 3/5 would be 60%, not 75% — guards against an all-ballots denominator.
    assert "60%" not in proc.stdout, proc.stdout


# --- positive: the _tabulated funnel ---------------------------------------

def test_tabulated_copy_has_funnel(tmp_path):
    # Even with the option OFF on screen, the full _tabulated copy forces the
    # funnel on, and it visibly adds up (5 − 1 = 4).
    yaml_path = _write(tmp_path, with_option=False)
    proc = _run_cli(yaml_path)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    txt = _tabulated_text(yaml_path)
    for frag in (FUNNEL_HEADER, FUNNEL_TOTAL, FUNNEL_EQUAL, FUNNEL_DECIDED, FUNNEL_SHARES):
        assert frag in txt, f"missing {frag!r} in:\n{txt}"


# --- negative: each form stays out of the other render ----------------------

def test_line_absent_on_screen_by_default(tmp_path):
    proc = _run_cli(_write(tmp_path, with_option=False))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "Voters with a preference" not in proc.stdout, proc.stdout
    assert FUNNEL_HEADER not in proc.stdout, proc.stdout


def test_funnel_does_not_appear_on_screen(tmp_path):
    # On screen it is ALWAYS the one-liner, never the multi-line funnel — even
    # when the option is on.
    proc = _run_cli(_write(tmp_path, with_option=True))
    assert EXPECTED in proc.stdout, proc.stdout
    assert FUNNEL_HEADER not in proc.stdout, proc.stdout


def test_one_liner_not_in_tabulated(tmp_path):
    # And the reverse: the _tabulated copy uses the funnel INSTEAD of the
    # one-liner, so the compact "N of TOTAL (...)" phrasing is not duplicated there.
    yaml_path = _write(tmp_path, with_option=True)
    _run_cli(yaml_path)
    txt = _tabulated_text(yaml_path)
    assert "Voters with a preference:" not in txt, txt
