"""
test_ranked_robin.py
====================
Guards the first-class Ranked Robin (RCV-RR / Copeland) path in the LH engine.

A file with `voting_method: RankedRobin` (alias RCV_RR / Copeland / Consensus)
and ranked ballots must dispatch to `run_ranked_robin` — printing the round-robin
(ballots + pairwise table + win-loss record), NOT the RCV-IRV elimination rounds —
exit 0, elect the round-robin winner, and write its `_tabulated` sibling.

Also checks the cycle path: a Rock/Paper/Scissors profile must be reported as a
Condorcet cycle (3-way tie on wins), not silently resolved without a flag.
"""
import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"
CANON = REPO_ROOT / "05_Ranked_Robin" / "_main" / "ranked_robin_consensus_center.yaml"


def _run(path):
    return subprocess.run([sys.executable, str(WRAPPER), str(path)],
                          capture_output=True, text=True, cwd=str(ENGINE_DIR))


def test_canonical_ranked_robin_file():
    """The repo's worked RR example dispatches to the round-robin and elects Ben."""
    r = _run(CANON)
    assert r.returncode == 0, r.stderr
    out = r.stdout
    assert "Ranked Robin (RCV-RR / Copeland) Method" in out
    assert "Instant-Runoff" not in out and "Elimination" not in out
    assert "Round-Robin — every pair" in out          # the pairwise table
    assert "Ballots:" in out                            # ballots are shown
    assert "Winner — Ranked Robin (RCV-RR): Ben" in out
    # This file sets options: { show_matrix: true }, so the echo opts INTO the
    # full pairwise matrix. The _tabulated mirror always has it regardless.
    assert "Pairwise (Round-Robin) Matrix" in out
    tab = (REPO_ROOT / "05_Ranked_Robin" / "_main" / "_main_tabulated"
           / "ranked_robin_consensus_center_tabulated.txt")
    assert tab.exists()
    mirror = tab.read_text()
    assert "Pairwise (Round-Robin) Matrix" in mirror
    assert "Legend: For - Equal Support - Against" in mirror


def test_echo_matrix_is_opt_in(tmp_path):
    """Default echo is compact (no matrix); show_matrix opts it in. The mirror
    always has the matrix either way."""
    base = ("voting_method: RankedRobin\nnum_winners: 1\nballots: |-\n"
            "  3:Ada>Ben>Cara\n  2:Ben>Cara>Ada\n  2:Cara>Ben>Ada\n")
    # default (no options) → compact echo, no matrix
    f1 = tmp_path / "compact.yaml"
    f1.write_text(base)
    r1 = _run(f1)
    assert r1.returncode == 0, r1.stderr
    assert "Pairwise (Round-Robin) Matrix" not in r1.stdout
    hits = list(tmp_path.parent.rglob("compact_tabulated.txt"))
    assert hits, "no _tabulated mirror was written"
    assert "Pairwise (Round-Robin) Matrix" in hits[0].read_text()
    # options: { show_matrix: true } → echo includes the matrix
    f2 = tmp_path / "full.yaml"
    f2.write_text(base + "options:\n  show_matrix: true\n")
    r2 = _run(f2)
    assert r2.returncode == 0, r2.stderr
    assert "Pairwise (Round-Robin) Matrix" in r2.stdout


def test_collapse_and_separator_options(tmp_path):
    """collapse_ballots and count_separator are honored by the RR echo."""
    base = ("voting_method: RankedRobin\nnum_winners: 1\nballots: |-\n"
            "  3:Ada>Ben>Cara\n  2:Ben>Cara>Ada\n  2:Cara>Ben>Ada\n")
    # custom separator
    fs = tmp_path / "sep.yaml"
    fs.write_text(base + 'options:\n  count_separator: ":"\n')
    rs = _run(fs)
    assert rs.returncode == 0, rs.stderr
    assert "3 : Ada > Ben > Cara" in rs.stdout
    assert "×" not in rs.stdout
    # collapse off → one row per voter (7 ballot rows, no count prefix)
    fc = tmp_path / "nocollapse.yaml"
    fc.write_text(base + "options:\n  collapse_ballots: false\n")
    rc = _run(fc)
    assert rc.returncode == 0, rc.stderr
    assert rc.stdout.count("Ada > Ben > Cara") == 3
    assert "3 ×" not in rc.stdout


def test_ranked_robin_aliases_and_cycle(tmp_path):
    """rcv_rr alias works, and a Condorcet cycle is flagged (not hidden)."""
    f = tmp_path / "rps.yaml"
    f.write_text(
        "voting_method: rcv_rr\nnum_winners: 1\nballots: |-\n"
        "  1:Rock>Scissors>Paper\n"
        "  1:Paper>Rock>Scissors\n"
        "  1:Scissors>Paper>Rock\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    assert "Ranked Robin (RCV-RR / Copeland) Method" in r.stdout
    assert "Condorcet cycle" in r.stdout
