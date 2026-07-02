# Runoff 01 — Runoff confirms the leader (control)

*Generated from [`Runoff_01_confirms_leader_r2pvc9.yaml`](../Runoff_01_confirms_leader_r2pvc9.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Aspen

## Scenario

A REAL BetterVoting election (BV id r2pvc9), captured 2026-06-28. The control
case for the Runoff Reversal set: the Scoring-Round leader (Aspen) is ALSO the
candidate more voters prefer head-to-head, so the runoff CONFIRMS the leader —
proof the runoff isn't rigged against whoever has the most stars. Winner = the
Condorcet winner. Level 101. Full two-view lesson: Runoff_01_confirms_leader_r2pvc9.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Aspen, Birch, Cedar
5, 2, 1
2, 5, 0
5, 3, 0
```

## What the engine says

Full report from the [`_tabulated` mirror](../runoff_overturns_leader_tabulated/Runoff_01_confirms_leader_r2pvc9_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Aspen   | * Birch   |   Cedar   |
-----------------------------------------------------
     * Aspen > |    ---     |2 - 0 - 1  |3 - 0 - 0  |
     * Birch > | 1 - 0 - 2  |   ---     |3 - 0 - 0  |
       Cedar > | 0 - 0 - 3  |0 - 0 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Aspen — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots.
Aspen,Birch,Cedar
    5,    2,    1
    2,    5,    0
    5,    3,    0

[Score Distribution] (number of ballots giving each score)
       5  4  3  2  1  0  | Total   Avg
Aspen  2  0  0  1  0  0  |    12   4.0
Birch  1  0  1  1  0  0  |    10   3.3
Cedar  0  0  0  0  1  2  |     1   0.3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Aspen         -- 12 -- First place
   Birch         -- 10 -- Second place
   Cedar         --  1
 Aspen and Birch advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Aspen         -- 2 -- First place
   Birch         -- 1
   Equal Support -- 0
 Aspen wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Aspen 2 (67%)  ·  Birch 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Aspen
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/Runoff_01_confirms_leader_r2pvc9.yaml
```

## See also

- [This set's lesson (README)](../README_runoff_overturns_leader.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Runoff reversal (worked set)](../README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c3_b3_more-stars-fewer-voters](01a_c3_b3_more-stars-fewer-voters.md) · [01b_c3_b9_overturn-holds-at-scale](01b_c3_b9_overturn-holds-at-scale.md) · [02_c5_b5_leader-overturned](02_c5_b5_leader-overturned.md) · [03_c7_b3_ice-cream-live](03_c7_b3_ice-cream-live.md) · [04_c4_b3_runoff-confirms-leader](04_c4_b3_runoff-confirms-leader.md) · [05_c3_b5_low-scores-bv1265](05_c3_b5_low-scores-bv1265.md) · [Runoff_02_atom_reversal_yx9447](Runoff_02_atom_reversal_yx9447.md) · [Runoff_03_enthusiasts_vs_majority_rkgtpk](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) · [Runoff_04_reversal_at_scale_bfjqmg](Runoff_04_reversal_at_scale_bfjqmg.md) · [Runoff_05_reversal_with_equal_support_xgkw3w](Runoff_05_reversal_with_equal_support_xgkw3w.md) · [Runoff_06_confirms_at_scale_d664xw](Runoff_06_confirms_at_scale_d664xw.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md)
