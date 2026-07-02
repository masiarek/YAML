# Summability demo — STAR district A (Maple wins outright)

*Generated from [`star_district_A.yaml`](../star_district_A.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Maple

**Official tie-break (lot) order:** Maple > Oak > Pine — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

District A of the STAR summability trio: 3 ballots, Maple wins. The point of
the trio: STAR's precinct subtotals — per-candidate score sums and the
pairwise matrix — can be published as-is and simply ADDED. See
star_combined.yaml, where this district's tallies and district B's sum,
cell by cell, to the combined result with no ballot-level recount.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Maple, Oak, Pine
5,4,0
5,3,1
0,2,5
```

## What the engine says

Full report from the [`_tabulated` mirror](../summability_demo_tabulated/star_district_A_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Maple   |  * Oak    |    Pine   |
-----------------------------------------------------
     * Maple > |    ---     |2 - 0 - 1  |2 - 0 - 1  |
       * Oak > | 1 - 0 - 2  |   ---     |2 - 0 - 1  |
        Pine > | 1 - 0 - 2  |1 - 0 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Maple — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots.
Maple,Oak,Pine
    5,  4,   0
    5,  3,   1
    0,  2,   5

[Score Distribution] (number of ballots giving each score)
       5  4  3  2  1  0  | Total   Avg
Maple  2  0  0  0  0  1  |    10   3.3
Oak    0  1  1  1  0  0  |     9   3.0
Pine   1  0  0  0  1  1  |     6   2.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Maple         -- 10 -- First place
   Oak           --  9 -- Second place
   Pine          --  6
 Maple and Oak advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Maple         -- 2 -- First place
   Oak           -- 1
   Equal Support -- 0
 Maple wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Maple 2 (67%)  ·  Oak 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Maple
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/summability_demo/star_district_A.yaml
```

## See also

- [This set's lesson (README)](../README_summability_demo.md) — the hand-written teaching context for every case in this folder
- [Summability (topic hub)](../../../00_start_here/topics/summability/README_summability.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [irv_combined](irv_combined.md) · [irv_district_A](irv_district_A.md) · [irv_district_B](irv_district_B.md) · [star_combined](star_combined.md) · [star_district_B](star_district_B.md)
