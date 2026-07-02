# Runoff 06 — the runoff confirms the leader at scale (control)

*Generated from [`Runoff_06_confirms_at_scale_d664xw.yaml`](../Runoff_06_confirms_at_scale_d664xw.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Wren

## Scenario

A REAL BetterVoting election (BV id d664xw), captured 2026-06-28. The closing
control: the Scoring-Round leader (Wren) is ALSO the candidate most voters prefer
head-to-head, so the Automatic Runoff confirms the leader, 4-1. After four
reversals, this is the reassurance — *how much* and *how many* point at the same
candidate, so the runoff just agrees with the score round. Winner = the Condorcet
winner. The bookend to Runoff_01. Level 101. Full two-view lesson:
Runoff_06_confirms_at_scale_d664xw.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Wren, Yarrow, Zinnia
5, 2, 0
5, 3, 1
5, 2, 0
4, 5, 0
2, 1, 5
```

## What the engine says

Full report from the [`_tabulated` mirror](../runoff_overturns_leader_tabulated/Runoff_06_confirms_at_scale_d664xw_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Wren   | * Yarrow  |   Zinnia  |
-----------------------------------------------------
      * Wren > |    ---     |4 - 0 - 1  |4 - 0 - 1  |
    * Yarrow > | 1 - 0 - 4  |   ---     |4 - 0 - 1  |
      Zinnia > | 1 - 0 - 4  |1 - 0 - 4  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Wren — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 5 ballots.
Count × Wren,Yarrow,Zinnia
    2 ×    5,     2,     0
    1 ×    5,     3,     1
    1 ×    4,     5,     0
    1 ×    2,     1,     5

[Score Distribution] (number of ballots giving each score)
        5  4  3  2  1  0  | Total   Avg
Wren    3  1  0  1  0  0  |    21   4.2
Yarrow  1  0  1  2  1  0  |    13   2.6
Zinnia  1  0  0  0  1  3  |     6   1.2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Wren          -- 21 -- First place
   Yarrow        -- 13 -- Second place
   Zinnia        --  6
 Wren and Yarrow advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Wren          -- 4 -- First place
   Yarrow        -- 1
   Equal Support -- 0
 Wren wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Wren 4 (80%)  ·  Yarrow 1 (20%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Wren
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/Runoff_06_confirms_at_scale_d664xw.yaml
```

## See also

- [This set's lesson (README)](../README_runoff_overturns_leader.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Runoff reversal (worked set)](../README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c3_b3_more-stars-fewer-voters](01a_c3_b3_more-stars-fewer-voters.md) · [01b_c3_b9_overturn-holds-at-scale](01b_c3_b9_overturn-holds-at-scale.md) · [02_c5_b5_leader-overturned](02_c5_b5_leader-overturned.md) · [03_c7_b3_ice-cream-live](03_c7_b3_ice-cream-live.md) · [04_c4_b3_runoff-confirms-leader](04_c4_b3_runoff-confirms-leader.md) · [05_c3_b5_low-scores-bv1265](05_c3_b5_low-scores-bv1265.md) · [Runoff_01_confirms_leader_r2pvc9](Runoff_01_confirms_leader_r2pvc9.md) · [Runoff_02_atom_reversal_yx9447](Runoff_02_atom_reversal_yx9447.md) · [Runoff_03_enthusiasts_vs_majority_rkgtpk](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) · [Runoff_04_reversal_at_scale_bfjqmg](Runoff_04_reversal_at_scale_bfjqmg.md) · [Runoff_05_reversal_with_equal_support_xgkw3w](Runoff_05_reversal_with_equal_support_xgkw3w.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md)
