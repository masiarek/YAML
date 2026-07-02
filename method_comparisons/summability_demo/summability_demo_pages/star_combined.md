# Summability demo — STAR combined A+B (Oak; precinct subtotals add up)

*Generated from [`star_combined.yaml`](../star_combined.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Oak

**Official tie-break (lot) order:** Maple > Oak > Pine — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Districts A + B merged (all six ballots): Oak wins the combined STAR count.
Check it against the two district files — every score total and every
pairwise-matrix cell here is exactly the SUM of the districts' published
subtotals. No central ballot pile, no recount: precincts report, totals add.
That is summability; the irv_* trio shows RCV-IRV failing exactly this
test.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Maple, Oak, Pine
5,4,0
5,3,1
0,2,5
1,5,4
0,5,3
4,0,5
```

## What the engine says

Full report from the [`_tabulated` mirror](../summability_demo_tabulated/star_combined_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    Maple   |  * Oak    |  * Pine   |
-----------------------------------------------------
       Maple > |    ---     |3 - 0 - 3  |2 - 0 - 4  |
       * Oak > | 3 - 0 - 3  |   ---     |4 - 0 - 2  |
      * Pine > | 4 - 0 - 2  |2 - 0 - 4  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: Oak — matches the STAR winner

[Divergence from STAR]
  STAR                   = Oak
  Choose-One (Plurality) = Maple   (differs from STAR)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 6 ballots.
Maple,Oak,Pine
    5,  4,   0
    5,  3,   1
    0,  2,   5
    1,  5,   4
    0,  5,   3
    4,  0,   5

[Score Distribution] (number of ballots giving each score)
       5  4  3  2  1  0  | Total   Avg
Maple  2  1  0  0  1  2  |    15   2.5
Oak    2  1  1  1  0  1  |    19   3.2
Pine   2  1  1  0  1  1  |    18   3.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Oak           -- 19 -- First place
   Pine          -- 18 -- Second place
   Maple         -- 15
 Oak and Pine advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Oak           -- 4 -- First place
   Pine          -- 2
   Equal Support -- 0
 Oak wins.
   Runoff math:
     6  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     6  voters with a preference  (majority = 4)
           Oak 4 (67%)  ·  Pine 2 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Oak
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/summability_demo/star_combined.yaml
```

## See also

- [This set's lesson (README)](../README_summability_demo.md) — the hand-written teaching context for every case in this folder
- [Summability (topic hub)](../../../00_start_here/topics/summability/README_summability.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [irv_combined](irv_combined.md) · [irv_district_A](irv_district_A.md) · [irv_district_B](irv_district_B.md) · [star_district_A](star_district_A.md) · [star_district_B](star_district_B.md)
