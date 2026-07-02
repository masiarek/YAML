"""
test_approval_mirror.py
=======================
Guards the Approval-path '_tabulated' mirror (house rule: EVERY tabulated YAML
gets a full-context mirror). An Approval election must:

  - exit 0 and elect the most-approved candidate,
  - write '<folder>_tabulated/<stem>_tabulated.txt' nested beside the source,
  - use the same composed format as the STAR path: provenance header, the
    ORIGINAL file copied as-is, then the TABULATION RESULTS.

Also re-guards the STAR mirror's composed format, since both paths now share
write_composed_tabulated().
"""
import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

APPROVAL_YAML = (
    "voting_method: Approval\n"
    "num_winners: 1\n"
    "ballots: |-\n"
    "  Ann,Bob,Cal\n"
    "  0,1,1\n"
    "  0,1,1\n"
    "  0,1,1\n"
    "  1,1,0\n"
    "  1,1,0\n"
    "expected_winners:\n"
    "  - Bob\n"
)

STAR_YAML = (
    "voting_method: STAR\n"
    "num_winners: 1\n"
    "ballots: |-\n"
    "  Ann,Bob,Cal\n"
    "  5,4,0\n"
    "  3,5,2\n"
    "  0,3,5\n"
    "expected_winners:\n"
    "  - Bob\n"
)


def _run(path):
    return subprocess.run([sys.executable, str(WRAPPER), str(path)],
                          capture_output=True, text=True, cwd=str(ENGINE_DIR))


def _mirror_of(src):
    return src.parent / (src.parent.name + "_tabulated") / (src.stem + "_tabulated.txt")


def _assert_composed(mirror_text, src_name, must_contain):
    assert "SOURCE FILE:     " + src_name in mirror_text
    assert "TABULATION RESULTS" in mirror_text
    assert "ballots: |-" in mirror_text          # the original file is embedded
    for needle in must_contain:
        assert needle in mirror_text, f"mirror missing: {needle!r}"


def test_approval_writes_composed_mirror(tmp_path):
    src = tmp_path / "approval_case.yaml"
    src.write_text(APPROVAL_YAML, encoding="utf-8")
    r = _run(src)
    assert r.returncode == 0, r.stderr
    assert "Winner — Approval Voting (single winner)" in r.stdout
    assert "Bob" in r.stdout
    mirror = _mirror_of(src)
    assert mirror.exists(), "Approval run wrote no _tabulated mirror"
    _assert_composed(mirror.read_text(encoding="utf-8"), src.name,
                     ["--- Approval Voting (single winner) ---",
                      "Winner — Approval Voting (single winner)"])


def test_star_mirror_still_composed(tmp_path):
    """The shared helper must not change the STAR mirror's format."""
    src = tmp_path / "star_case.yaml"
    src.write_text(STAR_YAML, encoding="utf-8")
    r = _run(src)
    assert r.returncode == 0, r.stderr
    mirror = _mirror_of(src)
    assert mirror.exists(), "STAR run wrote no _tabulated mirror"
    _assert_composed(mirror.read_text(encoding="utf-8"), src.name,
                     ["Automatic Runoff Round", "Winner — STAR Voting Method"])


def test_approval_error_text_not_swallowed(tmp_path):
    """A 0-5 score ballot under voting_method: Approval must still print the
    plain-language error (exit 1), not vanish into the capture buffer."""
    src = tmp_path / "bad_approval.yaml"
    src.write_text(
        "voting_method: Approval\nnum_winners: 1\nballots: |-\n"
        "  Ann,Bob\n  5,4\n", encoding="utf-8")
    r = _run(src)
    assert r.returncode == 1
    combined = r.stdout + r.stderr
    assert "Approval ballots may only use scores" in combined
    assert not _mirror_of(src).exists(), "no mirror should be written on error"
