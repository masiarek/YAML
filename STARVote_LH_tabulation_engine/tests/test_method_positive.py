"""
test_method_positive.py
=======================
Discovery test for the NON-(single-winner-STAR) teaching cases — the coverage
gap left by test_single_winner_positive.py (which asserts only single-winner
STAR files in its fixed folder list).

Every *.yaml under the teaching roots (01_STAR through 05_Ranked_Robin,
method_comparisons, other_methods — recursively, skipping *_tabulated
mirrors) that declares a
top-level `expected_winners:` list is run through the real CLI. The run must
exit 0 and elect exactly the declared winners — RCV-IRV, Ranked Robin,
Approval, STV, and the multi-winner STAR family (bloc / sss / rrv / allocated)
included.

Winner extraction is text-light but format-aware:
  - Ranked Robin prints  "Winner — Ranked Robin (RCV-RR): <name>"
  - every other method prints a "Winner(s) — …" / "Winners — …" header line
    followed by one indented winner name per line.

Single-winner STAR files in the folders test_single_winner_positive.py already
covers are skipped here so each case runs once per suite.
"""
import re
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

TEACHING_ROOTS = [
    REPO_ROOT / "01_STAR",
    REPO_ROOT / "02_STAR_Bloc",
    REPO_ROOT / "03_STAR_PR",
    REPO_ROOT / "04_Approval",
    REPO_ROOT / "05_Ranked_Robin",
    REPO_ROOT / "method_comparisons",
    REPO_ROOT / "other_methods",
]

# Folders whose single-winner STAR files test_single_winner_positive.py already
# runs (keep in sync with SINGLE_WINNER_DIRS there).
STAR_COVERED = {
    REPO_ROOT / "01_STAR" / "_main",
    REPO_ROOT / "01_STAR" / "runoff_overturns_leader",
    REPO_ROOT / "method_comparisons" / "summability_demo",
    REPO_ROOT / "method_comparisons" / "BV_Library",
    REPO_ROOT / "method_comparisons" / "split_voting" / "_main",
    REPO_ROOT / "YAML_library" / "1_positive",
}

ANSI = re.compile(r"\x1b\[[0-9;]*m")


def _find_method(node):
    """Recursively find the first voting_method in a (possibly nested) file."""
    if isinstance(node, dict):
        if "voting_method" in node:
            return str(node["voting_method"])
        for v in node.values():
            m = _find_method(v)
            if m is not None:
                return m
    elif isinstance(node, list):
        for v in node:
            m = _find_method(v)
            if m is not None:
                return m
    return None


def _cases():
    cases = []
    for root in TEACHING_ROOTS:
        if not root.is_dir():
            continue
        for p in sorted(root.rglob("*.yaml")):
            if any(part.endswith("_tabulated") for part in p.parts):
                continue
            try:
                data = yaml.safe_load(p.read_text(encoding="utf-8"))
            except Exception:
                continue
            if not isinstance(data, dict):
                continue
            expected = data.get("expected_winners")
            if not isinstance(expected, list) or not expected:
                continue
            method = (_find_method(data) or "STAR").strip().lower()
            seats = data.get("num_winners", 1)
            # Leave plain single-winner STAR files in the covered folders to
            # test_single_winner_positive.py.
            if method == "star" and seats in (1, None) and p.parent in STAR_COVERED:
                continue
            cases.append((p, [str(w) for w in expected]))
    return cases


CASES = _cases()
IDS = [str(p.relative_to(REPO_ROOT)) for p, _ in CASES]


def test_discovery_not_vacuous():
    """The scan must find a healthy number of non-STAR cases (RCV-IRV, Ranked
    Robin, multi-winner…). If this drops to a trickle, discovery is broken."""
    assert len(CASES) >= 10, f"only {len(CASES)} cases discovered: {IDS}"


def _elected(stdout):
    """Extract the elected names from a CLI run's output."""
    out = ANSI.sub("", stdout)
    m = None
    for m in re.finditer(r"Winner — Ranked Robin \(RCV-RR\): (.+)", out):
        pass
    if m:
        return [m.group(1).strip()]
    lines = out.splitlines()
    hdr = None
    for i, ln in enumerate(lines):
        if re.match(r"\s*Winner(\(s\))?s? —", ln):
            hdr = i
    assert hdr is not None, f"no Winner header found in output:\n{out[-800:]}"
    names = []
    for ln in lines[hdr + 1:]:
        if not ln.strip():
            break
        if not ln.startswith((" ", "\t")):
            break
        names.append(ln.strip())
    return names


@pytest.mark.parametrize("path,expected", CASES, ids=IDS)
def test_method_case_elects_expected(path, expected):
    r = subprocess.run([sys.executable, str(WRAPPER), str(path)],
                       capture_output=True, text=True, cwd=str(ENGINE_DIR))
    assert r.returncode == 0, f"{path.name} exited {r.returncode}:\n{r.stderr or r.stdout}"
    elected = _elected(r.stdout)
    assert sorted(elected) == sorted(expected), (
        f"{path.name}: elected {elected}, expected {expected}")
