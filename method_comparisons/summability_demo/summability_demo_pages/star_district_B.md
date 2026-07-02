# Summability demo — STAR district B (Oak wins — a runoff reversal)

*Generated from [`star_district_B.yaml`](../star_district_B.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Oak

**Official tie-break (lot) order:** Maple > Oak > Pine — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

District B of the STAR summability trio — the other half of the
star_combined electorate. Publish its per-candidate score sums and pairwise
matrix, add them to district A's, and you have the combined election's
entire count: that's summability, and it's what makes STAR precinct-friendly
and cheap to audit. Contrast the irv_* files, whose district tallies cannot
be combined.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Maple, Oak, Pine
1,5,4
0,5,3
4,0,5
```

## What the engine says

Full report from the [`_tabulated` mirror](../summability_demo_tabulated/star_district_B_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    Maple   |  * Oak    |  * Pine   |
-----------------------------------------------------
       Maple > |    ---     |1 - 0 - 2  |0 - 0 - 3  |
       * Oak > | 2 - 0 - 1  |   ---     |2 - 0 - 1  |
      * Pine > | 3 - 0 - 0  |1 - 0 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Oak — matches the STAR winner

[Divergence from STAR]
  STAR     = Oak
  Approval = Pine   (differs from STAR)

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Pine)
 - Runoff Round Winner   = (Oak)
  Candidate Pine earned the highest total score,
  but Candidate Oak won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots.
Maple,Oak,Pine
    1,  5,   4
    0,  5,   3
    4,  0,   5

[Score Distribution] (number of ballots giving each score)
       5  4  3  2  1  0  | Total   Avg
Maple  0  1  0  0  1  1  |     5   1.7
Oak    2  0  0  0  0  1  |    10   3.3
Pine   1  1  1  0  0  0  |    12   4.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Pine          -- 12 -- First place
   Oak           -- 10 -- Second place
   Maple         --  5
 Pine and Oak advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Oak           -- 2 -- First place
   Pine          -- 1
   Equal Support -- 0
 Oak wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Oak 2 (67%)  ·  Pine 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Oak
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/summability_demo/star_district_B.yaml
```

## See also

- [This set's lesson (README)](../README_summability_demo.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/star_district_B.md) — its entry in the divergence review ledger
- [Summability (topic hub)](../../../00_start_here/topics/summability/README_summability.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [irv_combined](irv_combined.md) · [irv_district_A](irv_district_A.md) · [irv_district_B](irv_district_B.md) · [star_combined](star_combined.md) · [star_district_A](star_district_A.md)
