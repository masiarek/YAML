# pref_voting Tabulation Engine (independent cross-check)

A third tabulation engine for the repo — but with a job the other two don't have:
it's the **independent referee.** It wraps Eric Pacuit's
[`pref_voting`](https://github.com/voting-tools/pref_voting) library (a peer-reviewed
Python social-choice package) and runs it on the *same* YAML elections as the LH and
RCV-IRV engines, then **compares the results** so we know our winners are right, not just
self-consistent.

Unlike the [RCV-IRV engine](../RCV_IRV_tabulation_engine/), `pref_voting` is **not
vendored** — it's a large, actively-maintained PyPI package, so it's an optional
dependency:

```bash
pip install pref_voting        # or: pip install -e STARVote_LH_tabulation_engine[crosscheck]
```

## Usage

```bash
# one election — shows each method's winner from BOTH engines, side by side
python pref_voting_tabulation.py example_tennessee.yaml

# cross-check every single-winner election in the repo
python pref_voting_tabulation.py --all
```

Any STAR-style (score) **or** ranked (`A>B>C`) YAML works — score ballots are converted to
rankings the same way the engines do (higher score = higher preference, 0 = unranked).

## What it checks

| Method | Role |
|--------|------|
| **Condorcet** | cross-checked vs LH (tie-aware) — always |
| **RCV-IRV** | cross-checked vs LH (truncation preserved; unranked = exhausted) |
| **Plurality** | cross-checked vs LH |
| **Copeland (= Ranked Robin)** | bonus — `pref_voting` computes it, the LH engine doesn't |
| **Borda** | bonus |
| **STAR** | *not available* — `pref_voting` has no STAR; the runoff is covered by the STAR positive tests |

When `pref_voting` reports a **tie** (a set of co-winners), the cross-check only requires
the LH engine's pick to be *among* them — cross-engine tie-breaking legitimately differs
(e.g. a 1–1 IRV final round, or bullet/truncated ballots).

## Status

Run across the repo's single-winner elections: **0 mismatches** — the LH engine's
Condorcet / IRV / Plurality machinery is independently confirmed. Wired into
[`tests/test_pref_voting_crosscheck.py`](../STARVote_LH_tabulation_engine/tests/test_pref_voting_crosscheck.py)
(skips cleanly if `pref_voting` isn't installed). Full write-up:
[`cross_checking_with_pref_voting.md`](../00_start_here/concepts/tabulation_engines/cross_checking_with_pref_voting.md).

## Files

- `pref_voting_tabulation.py` — the cross-check wrapper (parser + both engines + compare).
- `example_tennessee.yaml` — a demo election (the classic 3-methods-3-winners case).
