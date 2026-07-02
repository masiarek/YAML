# Runoff 04 — the reversal holds at scale (67/33)

*Generated from [`Runoff_04_reversal_at_scale_bfjqmg.yaml`](../Runoff_04_reversal_at_scale_bfjqmg.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Olive

## Scenario

A REAL BetterVoting election (BV id bfjqmg), captured 2026-06-28. The atom
(Runoff_02) blown up to a real crowd: three voters love Maple (5s) and push
Maple's total to the top of the Scoring Round (39), but six voters prefer Olive,
so Olive wins the Automatic Runoff 6-3 — a clean 2-to-1 majority (67/33). Proof
a reversal isn't a small-numbers fluke. Maple leads on HOW MUCH; Olive wins on
HOW MANY. Winner = the Condorcet winner. Level 101. Full two-view lesson:
Runoff_04_reversal_at_scale_bfjqmg.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Maple, Olive, Pine
4, 5, 0
4, 5, 0
4, 5, 0
5, 1, 2
5, 1, 2
4, 5, 0
5, 1, 2
4, 5, 0
4, 5, 0
```

## What the engine says

Full report from the [`_tabulated` mirror](../runoff_overturns_leader_tabulated/Runoff_04_reversal_at_scale_bfjqmg_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Maple   | * Olive   |    Pine   |
-----------------------------------------------------
     * Maple > |    ---     |3 - 0 - 6  |9 - 0 - 0  |
     * Olive > | 6 - 0 - 3  |   ---     |6 - 0 - 3  |
        Pine > | 0 - 0 - 9  |3 - 0 - 6  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Olive — matches the STAR winner

[Divergence from STAR]
  STAR     = Olive
  Approval = Maple   (differs from STAR)

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Maple)
 - Runoff Round Winner   = (Olive)
  Candidate Maple earned the highest total score,
  but Candidate Olive won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 9 ballots.
Count × Maple,Olive,Pine
    6 ×     4,    5,   0
    3 ×     5,    1,   2

[Score Distribution] (number of ballots giving each score)
       5  4  3  2  1  0  | Total   Avg
Maple  3  6  0  0  0  0  |    39   4.3
Olive  6  0  0  0  3  0  |    33   3.7
Pine   0  0  0  3  0  6  |     6   0.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Maple         -- 39 -- First place
   Olive         -- 33 -- Second place
   Pine          --  6
 Maple and Olive advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Olive         -- 6 -- First place
   Maple         -- 3
   Equal Support -- 0
 Olive wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Olive 6 (67%)  ·  Maple 3 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Olive
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/Runoff_04_reversal_at_scale_bfjqmg.yaml
```

## See also

- [This set's lesson (README)](../README_runoff_overturns_leader.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/Runoff_04_reversal_at_scale_bfjqmg.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Runoff reversal (worked set)](../README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c3_b3_more-stars-fewer-voters](01a_c3_b3_more-stars-fewer-voters.md) · [01b_c3_b9_overturn-holds-at-scale](01b_c3_b9_overturn-holds-at-scale.md) · [02_c5_b5_leader-overturned](02_c5_b5_leader-overturned.md) · [03_c7_b3_ice-cream-live](03_c7_b3_ice-cream-live.md) · [04_c4_b3_runoff-confirms-leader](04_c4_b3_runoff-confirms-leader.md) · [05_c3_b5_low-scores-bv1265](05_c3_b5_low-scores-bv1265.md) · [Runoff_01_confirms_leader_r2pvc9](Runoff_01_confirms_leader_r2pvc9.md) · [Runoff_02_atom_reversal_yx9447](Runoff_02_atom_reversal_yx9447.md) · [Runoff_03_enthusiasts_vs_majority_rkgtpk](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) · [Runoff_05_reversal_with_equal_support_xgkw3w](Runoff_05_reversal_with_equal_support_xgkw3w.md) · [Runoff_06_confirms_at_scale_d664xw](Runoff_06_confirms_at_scale_d664xw.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md)
