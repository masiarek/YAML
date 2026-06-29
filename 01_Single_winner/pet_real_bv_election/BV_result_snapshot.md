# BetterVoting result — frozen snapshot (pet race)

**Why this file exists:** BetterVoting (<https://bettervoting.com/pet/results>) is a
**live** result that can change if the election is recounted, re-opened, or the
platform's tabulation is updated. Our lessons cite specific numbers, so we freeze
BetterVoting's reported result **as captured on the date below**. If the live page
ever differs from this snapshot, *this file is the version our lessons describe* —
update the lessons and this snapshot together, deliberately.

- **Captured:** 2026-06-28
- **BetterVoting election id:** `pet` ("What Makes the Best Pet?")
- **Live result (may change):** <https://bettervoting.com/pet/results>
- **Frozen raw export (this folder):** [`best_pet_c7_b461_bv_export.json`](best_pet_c7_b461_bv_export.json)
  — the full BetterVoting JSON (461 ballots + BetterVoting's own `Results`).
- **Converted election (tabulated by the LH engine):** [`best_pet_c7_b461.yaml`](best_pet_c7_b461.yaml)

## BetterVoting's reported result (frozen)

From the export's `Results[0].summaryData`:

```json
{ "nAbstentions": 6, "nTallyVotes": 455, "nOutOfBoundsVotes": 0 }
```

- Winner: **Dog**
- Automatic Runoff: **Dog 190**, Cat 173, Equal Support 92
- Per-candidate score totals (from the lesson's BV screenshots): Dog **1798**, Cat 1741, Bird 969, Rabbit 954, Fish 854, Rat 580, Python 440

## The 6 ballots BetterVoting counts as "abstentions"

All six are **flat** ballots (every candidate scored the same). Extracted from the
frozen JSON (candidate order: Bird, Cat, Python, Dog, Fish, Rabbit, Rat):

```
[0,0,0,0,0,0,0]  ×3   all-zero  (cast: rates everyone zero)
[ blank       ]  ×1   blank     (the ONE true abstention)
[5,5,5,5,5,5,5]  ×1   all-FIVES (a maximally engaged voter)
[4,4,4,4,4,4,4]  ×1   all-FOURS
```

## Reconciliation with a full count (LH engine, all 461 ballots)

| | BetterVoting (frozen) | LH engine (all 461) |
|---|---:|---:|
| Ballots tallied | 455 | 461 |
| "Abstentions" | 6 (all flat ballots) | 1 (the blank only) |
| Equal Support in runoff | 92 | 98 |
| Per-candidate score totals | 9 lower (Dog 1798) | Dog 1807 |
| Runoff Dog / Cat | 190 / 173 | 190 / 173 |
| Voters with a preference | 363 | 363 |
| **Winner** | **Dog** | **Dog** |

The whole gap is one classification choice: BetterVoting files **flat / Equal
Support** ballots under *abstention* and drops their stars. `92 + 6 = 98`; the
all-5s + all-4s ballots add `5 + 4 = 9` to every candidate — exactly the score-total
gap. The winner and runoff margin are identical.

## See also

- The correctness/reconciliation write-up: [`LH_BV_reconciliation_issue.md`](LH_BV_reconciliation_issue.md) → filed as [Equal-Vote/bettervoting#1407](https://github.com/Equal-Vote/bettervoting/issues/1407)
- **Canonical small case (a lesson in itself): [`small_case_abstention_lesson.md`](small_case_abstention_lesson.md)** — real BV election `dq2dmm`, 3 candidates / 8 ballots, where BV files 3 flat ballots (incl. an engaged `3,3,3`) as abstentions
- Even-simpler 2-candidate capture (BV calls a `5,5` an abstention): [`small_abstention_c2_b5_lesson.md`](small_abstention_c2_b5_lesson.md)
- Minimal synthetic illustration (LH-correct behavior): [`abstention_reconciliation_min_c2_b6.yaml`](abstention_reconciliation_min_c2_b6.yaml)
- How that small case was reproduced on BetterVoting: [`SMALL_CASE_reproduce_on_BV.md`](SMALL_CASE_reproduce_on_BV.md)
- Worked lesson: [`README.md`](README.md)
- Concept: [BetterVoting and the LH engine](../../00_start_here/tabulation_engines/bettervoting_and_the_engine.md) · [Runoff percentages](../../00_start_here/STAR_Voting/runoff_percentages.md)
