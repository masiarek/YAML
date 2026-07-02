# Five candidates — the score leader is overturned in the runoff

*Generated from [`02_c5_b5_leader-overturned.yaml`](../02_c5_b5_leader-overturned.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Boston

## Scenario

Five candidates, five voters. Austin is the high-ceiling favorite — its two fans
rate it 5 and the rest still give a respectful 4 — so Austin leads the scoring
round with 22 stars. But Boston is the broad compromise and the real majority pick:
three of the five prefer Boston to Austin, so Boston takes the automatic runoff 3-2.
Chicago, Denver and Erie are genuine options that simply don't reach the final two.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Austin, Boston, Chicago, Denver, Erie
     5,      0,       1,      0,    2
     5,      0,       0,      1,    0
     4,      5,       1,      0,    0
     4,      5,       0,      2,    0
     4,      5,       0,      0,    1
```

## What the engine says

Full report from the [`_tabulated` mirror](../runoff_overturns_leader_tabulated/02_c5_b5_leader-overturned_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |  * Austin   | * Boston   |   Chicago  |   Denver   |    Erie    |
-----------------------------------------------------------------------------------
     * Austin > |     ---     | 2 - 0 - 3  | 5 - 0 - 0  | 5 - 0 - 0  | 5 - 0 - 0  |
     * Boston > |  3 - 0 - 2  |    ---     | 3 - 1 - 1  | 3 - 1 - 1  | 3 - 1 - 1  |
      Chicago > |  0 - 0 - 5  | 1 - 1 - 3  |    ---     | 2 - 1 - 2  | 1 - 2 - 2  |
       Denver > |  0 - 0 - 5  | 1 - 1 - 3  | 2 - 1 - 2  |    ---     | 2 - 1 - 2  |
         Erie > |  0 - 0 - 5  | 1 - 1 - 3  | 2 - 2 - 1  | 2 - 1 - 2  |    ---     |

[Condorcet Winner]
  Condorcet Winner: Boston — matches the STAR winner

[Divergence from STAR]
  STAR     = Boston
  Approval = Austin   (differs from STAR)

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Austin)
 - Runoff Round Winner   = (Boston)
  Candidate Austin earned the highest total score,
  but Candidate Boston won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 5 ballots.
Austin,Boston,Chicago,Denver,Erie
     5,     0,      1,     0,   2
     5,     0,      0,     1,   0
     4,     5,      1,     0,   0
     4,     5,      0,     2,   0
     4,     5,      0,     0,   1

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Austin   2  3  0  0  0  0  |    22   4.4
Boston   3  0  0  0  0  2  |    15   3.0
Chicago  0  0  0  0  2  3  |     2   0.4
Denver   0  0  0  1  1  3  |     3   0.6
Erie     0  0  0  1  1  3  |     3   0.6

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Austin        -- 22 -- First place
   Boston        -- 15 -- Second place
   Denver        --  3
   Erie          --  3
   Chicago       --  2
 Austin and Boston advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Boston        -- 3 -- First place
   Austin        -- 2
   Equal Support -- 0
 Boston wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Boston 3 (60%)  ·  Austin 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Boston
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/02_c5_b5_leader-overturned.yaml
```

## See also

- [This set's lesson (README)](../README_runoff_overturns_leader.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/02_c5_b5_leader-overturned.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c3_b3_more-stars-fewer-voters](01a_c3_b3_more-stars-fewer-voters.md) · [01b_c3_b9_overturn-holds-at-scale](01b_c3_b9_overturn-holds-at-scale.md) · [03_c7_b3_ice-cream-live](03_c7_b3_ice-cream-live.md) · [04_c4_b3_runoff-confirms-leader](04_c4_b3_runoff-confirms-leader.md) · [05_c3_b5_low-scores-bv1265](05_c3_b5_low-scores-bv1265.md) · [Runoff_01_confirms_leader_r2pvc9](Runoff_01_confirms_leader_r2pvc9.md) · [Runoff_02_atom_reversal_yx9447](Runoff_02_atom_reversal_yx9447.md) · [Runoff_03_enthusiasts_vs_majority_rkgtpk](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) · [Runoff_04_reversal_at_scale_bfjqmg](Runoff_04_reversal_at_scale_bfjqmg.md) · [Runoff_05_reversal_with_equal_support_xgkw3w](Runoff_05_reversal_with_equal_support_xgkw3w.md) · [Runoff_06_confirms_at_scale_d664xw](Runoff_06_confirms_at_scale_d664xw.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md)
