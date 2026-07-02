"""
test_pref_voting_crosscheck.py
==============================
Cross-checks the LH engine against Eric Pacuit's `pref_voting` library — an
independent, peer-reviewed social-choice package — on the ranked-ballot methods
both compute: **Condorcet, RCV-IRV, Plurality**.

For every cross-checkable single-winner election in the repo we assert the LH
engine and pref_voting agree:
  - **Condorcet** winner always (tie-aware on both sides);
  - **IRV / Plurality** when the result is unambiguous; when pref_voting reports a
    *tie* (a set of co-winners), we only require LH's pick to be *among* them,
    since cross-engine tie-breaking legitimately differs.

pref_voting has no STAR, so STAR's runoff itself isn't checked here — that's the
job of the STAR positive tests. This validates the surrounding ranked machinery.

Skipped entirely if `pref_voting` isn't installed (it's an optional dev dep:
`pip install pref_voting`).
"""
import sys
from pathlib import Path

import pytest

pytest.importorskip("pref_voting",
                    reason="pref_voting not installed (optional dev dep)")

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(REPO_ROOT / "pref_voting_tabulation_engine"))

from pref_voting_tabulation import crosscheck, discover  # noqa: E402

CROSS_DIRS = [
    str(REPO_ROOT / "01_STAR" / "_main"),
    str(REPO_ROOT / "01_STAR" / "runoff_overturns_leader"),
    str(REPO_ROOT / "01_STAR" / "Flat_scores_ties"),
    str(REPO_ROOT / "method_comparisons" / "paradoxes_and_whoops"),
    str(REPO_ROOT / "method_comparisons" / "summability_demo"),
    str(REPO_ROOT / "method_comparisons" / "BV_Library"),
    str(REPO_ROOT / "method_comparisons" / "center_squeeze"),
    str(REPO_ROOT / "method_comparisons" / "monotonicity"),
    str(REPO_ROOT / "method_comparisons" / "split_voting" / "_main"),
    str(REPO_ROOT / "YAML_library" / "1_positive"),
]

FILES = discover(CROSS_DIRS)
IDS = [str(Path(f).relative_to(REPO_ROOT)) for f in FILES]


def test_at_least_some_files_discovered():
    assert len(FILES) >= 20, f"expected many cross-checkable files, got {len(FILES)}"


@pytest.mark.parametrize("path", FILES, ids=IDS)
def test_lh_matches_pref_voting(path):
    result = crosscheck(path)
    bad = {m: (lh, pv) for m, (lh, pv, st) in result.items() if st == "mismatch"}
    assert not bad, (
        f"LH vs pref_voting disagree in {Path(path).name}: "
        + "; ".join(f"{m}: LH={lh} pref_voting={pv}" for m, (lh, pv) in bad.items())
    )
