# More stars, fewer voters — the runoff overturns the score leader

*Generated from [`01a_c3_b3_more-stars-fewer-voters.yaml`](../01a_c3_b3_more-stars-fewer-voters.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Brownie

## Scenario

The whole lesson in three voters. Almond is the star-magnet: one fan rates it 5,
so Almond tops the scoring round with 13 stars. But STAR doesn't crown the biggest
star pile — it asks the finalists' question: of the top two, Almond and Brownie,
which one do MORE voters prefer? Two of the three rank Brownie above Almond, so
Brownie wins the automatic runoff 2-1.

More stars from fewer people loses to fewer stars from more people. (Cocoa is only
here so the runoff is picking finalists out of a real field, not a forced pair.)

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Almond, Brownie, Cocoa
     5,       1,     2
     4,       5,     0
     4,       5,     0
```

## What the engine says

Full report from the [`_tabulated` mirror](../runoff_overturns_leader_tabulated/01a_c3_b3_more-stars-fewer-voters_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |  * Almond   | * Brownie  |    Cocoa   |
---------------------------------------------------------
     * Almond > |     ---     | 1 - 0 - 2  | 3 - 0 - 0  |
    * Brownie > |  2 - 0 - 1  |    ---     | 2 - 0 - 1  |
        Cocoa > |  0 - 0 - 3  | 1 - 0 - 2  |    ---     |

[Condorcet Winner]
  Condorcet Winner: Brownie — matches the STAR winner

[Divergence from STAR]
  STAR     = Brownie
  Approval = Almond   (differs from STAR)

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Almond)
 - Runoff Round Winner   = (Brownie)
  Candidate Almond earned the highest total score,
  but Candidate Brownie won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots.
Count × Almond,Brownie,Cocoa
    2 ×      4,      5,    0
    1 ×      5,      1,    2

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Almond   1  2  0  0  0  0  |    13   4.3
Brownie  2  0  0  0  1  0  |    11   3.7
Cocoa    0  0  0  1  0  2  |     2   0.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Almond        -- 13 -- First place
   Brownie       -- 11 -- Second place
   Cocoa         --  2
 Almond and Brownie advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Brownie       -- 2 -- First place
   Almond        -- 1
   Equal Support -- 0
 Brownie wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Brownie 2 (67%)  ·  Almond 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Brownie
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/01a_c3_b3_more-stars-fewer-voters.yaml
```

## See also

- [This set's lesson (README)](../README_runoff_overturns_leader.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/01a_c3_b3_more-stars-fewer-voters.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01b_c3_b9_overturn-holds-at-scale](01b_c3_b9_overturn-holds-at-scale.md) · [02_c5_b5_leader-overturned](02_c5_b5_leader-overturned.md) · [03_c7_b3_ice-cream-live](03_c7_b3_ice-cream-live.md) · [04_c4_b3_runoff-confirms-leader](04_c4_b3_runoff-confirms-leader.md) · [05_c3_b5_low-scores-bv1265](05_c3_b5_low-scores-bv1265.md) · [Runoff_01_confirms_leader_r2pvc9](Runoff_01_confirms_leader_r2pvc9.md) · [Runoff_02_atom_reversal_yx9447](Runoff_02_atom_reversal_yx9447.md) · [Runoff_03_enthusiasts_vs_majority_rkgtpk](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) · [Runoff_04_reversal_at_scale_bfjqmg](Runoff_04_reversal_at_scale_bfjqmg.md) · [Runoff_05_reversal_with_equal_support_xgkw3w](Runoff_05_reversal_with_equal_support_xgkw3w.md) · [Runoff_06_confirms_at_scale_d664xw](Runoff_06_confirms_at_scale_d664xw.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md)
