# Runoff 03 — two enthusiasts vs the majority

*Generated from [`Runoff_03_enthusiasts_vs_majority_rkgtpk.yaml`](../Runoff_03_enthusiasts_vs_majority_rkgtpk.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Eden

## Scenario

A REAL BetterVoting election (BV id rkgtpk), captured 2026-06-28. A reversal in a
five-candidate field, the "narrow-but-deep" pattern: two voters are Dakota
enthusiasts (Dakota 5), and their intensity pushes Dakota to the top of the
Scoring Round (22). But the other three voters score Eden 5 over Dakota 4 — they
like Dakota, prefer Eden — so 3 of 5 pick Eden in the runoff. Dakota leads on HOW
MUCH (intensity); Eden wins on HOW MANY (majority). Winner = the Condorcet winner
(calm case). Level 201. Full two-view lesson: Runoff_03_enthusiasts_vs_majority_rkgtpk.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Dakota, Eden, Flynn, Gale, Hazel
5, 0, 1, 0, 0
5, 0, 0, 1, 0
4, 5, 0, 0, 1
4, 5, 1, 0, 0
4, 5, 0, 1, 0
```

## What the engine says

Full report from the [`_tabulated` mirror](../runoff_overturns_leader_tabulated/Runoff_03_enthusiasts_vs_majority_rkgtpk_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Dakota  |  * Eden   |   Flynn   |    Gale   |   Hazel   |
-----------------------------------------------------------------------------
    * Dakota > |    ---     |2 - 0 - 3  |5 - 0 - 0  |5 - 0 - 0  |5 - 0 - 0  |
      * Eden > | 3 - 0 - 2  |   ---     |3 - 1 - 1  |3 - 1 - 1  |3 - 2 - 0  |
       Flynn > | 0 - 0 - 5  |1 - 1 - 3  |   ---     |2 - 1 - 2  |2 - 2 - 1  |
        Gale > | 0 - 0 - 5  |1 - 1 - 3  |2 - 1 - 2  |   ---     |2 - 2 - 1  |
       Hazel > | 0 - 0 - 5  |0 - 2 - 3  |1 - 2 - 2  |1 - 2 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Eden — matches the STAR winner

[Divergence from STAR]
  STAR     = Eden
  Approval = Dakota   (differs from STAR)

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Dakota)
 - Runoff Round Winner   = (Eden)
  Candidate Dakota earned the highest total score,
  but Candidate Eden won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 5 ballots.
Dakota,Eden,Flynn,Gale,Hazel
     5,   0,    1,   0,    0
     5,   0,    0,   1,    0
     4,   5,    0,   0,    1
     4,   5,    1,   0,    0
     4,   5,    0,   1,    0

[Score Distribution] (number of ballots giving each score)
        5  4  3  2  1  0  | Total   Avg
Dakota  2  3  0  0  0  0  |    22   4.4
Eden    3  0  0  0  0  2  |    15   3.0
Flynn   0  0  0  0  2  3  |     2   0.4
Gale    0  0  0  0  2  3  |     2   0.4
Hazel   0  0  0  0  1  4  |     1   0.2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dakota        -- 22 -- First place
   Eden          -- 15 -- Second place
   Flynn         --  2
   Gale          --  2
   Hazel         --  1
 Dakota and Eden advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Eden          -- 3 -- First place
   Dakota        -- 2
   Equal Support -- 0
 Eden wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Eden 3 (60%)  ·  Dakota 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Eden
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/Runoff_03_enthusiasts_vs_majority_rkgtpk.yaml
```

## See also

- [This set's lesson (README)](../README_runoff_overturns_leader.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/Runoff_03_enthusiasts_vs_majority_rkgtpk.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Runoff reversal (worked set)](../README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c3_b3_more-stars-fewer-voters](01a_c3_b3_more-stars-fewer-voters.md) · [01b_c3_b9_overturn-holds-at-scale](01b_c3_b9_overturn-holds-at-scale.md) · [02_c5_b5_leader-overturned](02_c5_b5_leader-overturned.md) · [03_c7_b3_ice-cream-live](03_c7_b3_ice-cream-live.md) · [04_c4_b3_runoff-confirms-leader](04_c4_b3_runoff-confirms-leader.md) · [05_c3_b5_low-scores-bv1265](05_c3_b5_low-scores-bv1265.md) · [Runoff_01_confirms_leader_r2pvc9](Runoff_01_confirms_leader_r2pvc9.md) · [Runoff_02_atom_reversal_yx9447](Runoff_02_atom_reversal_yx9447.md) · [Runoff_04_reversal_at_scale_bfjqmg](Runoff_04_reversal_at_scale_bfjqmg.md) · [Runoff_05_reversal_with_equal_support_xgkw3w](Runoff_05_reversal_with_equal_support_xgkw3w.md) · [Runoff_06_confirms_at_scale_d664xw](Runoff_06_confirms_at_scale_d664xw.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md)
