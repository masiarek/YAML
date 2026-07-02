# Ice Cream — Flavor of the Year (the real recorded race)

*Generated from [`03_c7_b3_ice-cream-live.yaml`](../03_c7_b3_ice-cream-live.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** ChocoAlm

## Scenario

The actual recorded election (BetterVoting id 4c7kp9). ChocoDrk wins the scoring
round with 9 stars — one voter adores it (5). But the automatic runoff is between
the two finalists, ChocoDrk and ChocoAlm, and two of the three voters prefer
ChocoAlm, so ChocoAlm wins 2-1 (67% to 33%).

This is exactly the "why isn't the top-scoring candidate the winner?" moment STAR
is built to answer: the scoring round finds the two finalists; the runoff lets each
voter's full vote back the finalist they actually prefer.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
ChocoDrk, ChocoAlm, ChocoHzn, VanillaClssc, VanillaFrnch, Mango, Peach
       4,        5,        3,            0,            1,     2,     0
       0,        3,        0,            0,            0,     0,     0
       5,        0,        0,            0,            0,     0,     0
```

## What the engine says

Full report from the [`_tabulated` mirror](../runoff_overturns_leader_tabulated/03_c7_b3_ice-cream-live_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                     |    * ChocoDrk    |   * ChocoAlm    |     ChocoHzn    |   VanillaClssc  |   VanillaFrnch  |      Mango      |      Peach      |
-----------------------------------------------------------------------------------------------------------------------------------------------------
        * ChocoDrk > |       ---        |   1 - 0 - 2     |   2 - 1 - 0     |   2 - 1 - 0     |   2 - 1 - 0     |   2 - 1 - 0     |   2 - 1 - 0     |
        * ChocoAlm > |    2 - 0 - 1     |      ---        |   2 - 1 - 0     |   2 - 1 - 0     |   2 - 1 - 0     |   2 - 1 - 0     |   2 - 1 - 0     |
          ChocoHzn > |    0 - 1 - 2     |   0 - 1 - 2     |      ---        |   1 - 2 - 0     |   1 - 2 - 0     |   1 - 2 - 0     |   1 - 2 - 0     |
      VanillaClssc > |    0 - 1 - 2     |   0 - 1 - 2     |   0 - 2 - 1     |      ---        |   0 - 2 - 1     |   0 - 2 - 1     |   0 - 3 - 0     |
      VanillaFrnch > |    0 - 1 - 2     |   0 - 1 - 2     |   0 - 2 - 1     |   1 - 2 - 0     |      ---        |   0 - 2 - 1     |   1 - 2 - 0     |
             Mango > |    0 - 1 - 2     |   0 - 1 - 2     |   0 - 2 - 1     |   1 - 2 - 0     |   1 - 2 - 0     |      ---        |   1 - 2 - 0     |
             Peach > |    0 - 1 - 2     |   0 - 1 - 2     |   0 - 2 - 1     |   0 - 3 - 0     |   0 - 2 - 1     |   0 - 2 - 1     |      ---        |

[Condorcet Winner]
  Condorcet Winner: ChocoAlm — matches the STAR winner

[Divergence from STAR]
  STAR     = ChocoAlm
  Approval = ChocoDrk   (differs from STAR)

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (ChocoDrk)
 - Runoff Round Winner   = (ChocoAlm)
  Candidate ChocoDrk earned the highest total score,
  but Candidate ChocoAlm won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots.
ChocoDrk,ChocoAlm,ChocoHzn,VanillaClssc,VanillaFrnch,Mango,Peach
       4,       5,       3,           0,           1,    2,    0
       0,       3,       0,           0,           0,    0,    0
       5,       0,       0,           0,           0,    0,    0

[Score Distribution] (number of ballots giving each score)
              5  4  3  2  1  0  | Total   Avg
ChocoDrk      1  1  0  0  0  1  |     9   3.0
ChocoAlm      1  0  1  0  0  1  |     8   2.7
ChocoHzn      0  0  1  0  0  2  |     3   1.0
VanillaClssc  0  0  0  0  0  3  |     0   0.0
VanillaFrnch  0  0  0  0  1  2  |     1   0.3
Mango         0  0  0  1  0  2  |     2   0.7
Peach         0  0  0  0  0  3  |     0   0.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   ChocoDrk      -- 9 -- First place
   ChocoAlm      -- 8 -- Second place
   ChocoHzn      -- 3
   Mango         -- 2
   VanillaFrnch  -- 1
   Peach         -- 0
   VanillaClssc  -- 0
 ChocoDrk and ChocoAlm advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   ChocoAlm      -- 2 -- First place
   ChocoDrk      -- 1
   Equal Support -- 0
 ChocoAlm wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           ChocoAlm 2 (67%)  ·  ChocoDrk 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 ChocoAlm
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/03_c7_b3_ice-cream-live.yaml
```

## See also

- [This set's lesson (README)](../README_runoff_overturns_leader.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/03_c7_b3_ice-cream-live.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c3_b3_more-stars-fewer-voters](01a_c3_b3_more-stars-fewer-voters.md) · [01b_c3_b9_overturn-holds-at-scale](01b_c3_b9_overturn-holds-at-scale.md) · [02_c5_b5_leader-overturned](02_c5_b5_leader-overturned.md) · [04_c4_b3_runoff-confirms-leader](04_c4_b3_runoff-confirms-leader.md) · [05_c3_b5_low-scores-bv1265](05_c3_b5_low-scores-bv1265.md) · [Runoff_01_confirms_leader_r2pvc9](Runoff_01_confirms_leader_r2pvc9.md) · [Runoff_02_atom_reversal_yx9447](Runoff_02_atom_reversal_yx9447.md) · [Runoff_03_enthusiasts_vs_majority_rkgtpk](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) · [Runoff_04_reversal_at_scale_bfjqmg](Runoff_04_reversal_at_scale_bfjqmg.md) · [Runoff_05_reversal_with_equal_support_xgkw3w](Runoff_05_reversal_with_equal_support_xgkw3w.md) · [Runoff_06_confirms_at_scale_d664xw](Runoff_06_confirms_at_scale_d664xw.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md)
