# Runoff 05 — reversal with Equal Support

*Generated from [`Runoff_05_reversal_with_equal_support_xgkw3w.yaml`](../Runoff_05_reversal_with_equal_support_xgkw3w.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Sage

## Scenario

A REAL BetterVoting election (BV id xgkw3w), captured 2026-06-28. The first
reversal where some voters have NO PREFERENCE between the two finalists. Rosa
leads the Scoring Round (21), but two voters scored Rosa and Sage equally (3,3
and 5,5) — Equal Support — so they sit out the runoff. Of the three voters who DID
pick between the finalists, two prefer Sage, so Sage wins. The runoff line reads
"3 of 5 (2 Equal Support)" — the bridge to the two-denominator idea. Both
equal-support voters rated Tulip (a 1 and a 2), so they are CAST votes, not
abstentions — BetterVoting and LH agree (nAbstentions = 0). Winner = the Condorcet
winner. Level 201. Full two-view lesson: Runoff_05_reversal_with_equal_support_xgkw3w.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Rosa, Sage, Tulip
5, 1, 0
4, 5, 0
4, 5, 0
3, 3, 1
5, 5, 2
```

## What the engine says

Full report from the [`_tabulated` mirror](../runoff_overturns_leader_tabulated/Runoff_05_reversal_with_equal_support_xgkw3w_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Rosa   |  * Sage   |   Tulip   |
-----------------------------------------------------
      * Rosa > |    ---     |1 - 2 - 2  |5 - 0 - 0  |
      * Sage > | 2 - 2 - 1  |   ---     |5 - 0 - 0  |
       Tulip > | 0 - 0 - 5  |0 - 0 - 5  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Sage — matches the STAR winner

[Divergence from STAR]
  STAR     = Sage
  Approval = Rosa   (differs from STAR)

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Rosa)
 - Runoff Round Winner   = (Sage)
  Candidate Rosa earned the highest total score,
  but Candidate Sage won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 5 ballots.
Count × Rosa,Sage,Tulip
    2 ×    4,   5,    0
    1 ×    5,   1,    0
    1 ×    3,   3,    1
    1 ×    5,   5,    2

[Score Distribution] (number of ballots giving each score)
       5  4  3  2  1  0  | Total   Avg
Rosa   2  2  1  0  0  0  |    21   4.2
Sage   3  0  1  0  1  0  |    19   3.8
Tulip  0  0  0  1  1  3  |     3   0.6

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Rosa          -- 21 -- First place
   Sage          -- 19 -- Second place
   Tulip         --  3
 Rosa and Sage advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Sage          -- 2 -- First place
   Rosa          -- 1
   Equal Support -- 2
 Sage wins.
   Runoff math:
     5  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Sage 2 (67%)  ·  Rosa 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Sage
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/Runoff_05_reversal_with_equal_support_xgkw3w.yaml
```

## See also

- [This set's lesson (README)](../README_runoff_overturns_leader.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/Runoff_05_reversal_with_equal_support_xgkw3w.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Runoff reversal (worked set)](../README_runoff_overturns_leader.md)
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c3_b3_more-stars-fewer-voters](01a_c3_b3_more-stars-fewer-voters.md) · [01b_c3_b9_overturn-holds-at-scale](01b_c3_b9_overturn-holds-at-scale.md) · [02_c5_b5_leader-overturned](02_c5_b5_leader-overturned.md) · [03_c7_b3_ice-cream-live](03_c7_b3_ice-cream-live.md) · [04_c4_b3_runoff-confirms-leader](04_c4_b3_runoff-confirms-leader.md) · [05_c3_b5_low-scores-bv1265](05_c3_b5_low-scores-bv1265.md) · [Runoff_01_confirms_leader_r2pvc9](Runoff_01_confirms_leader_r2pvc9.md) · [Runoff_02_atom_reversal_yx9447](Runoff_02_atom_reversal_yx9447.md) · [Runoff_03_enthusiasts_vs_majority_rkgtpk](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) · [Runoff_04_reversal_at_scale_bfjqmg](Runoff_04_reversal_at_scale_bfjqmg.md) · [Runoff_06_confirms_at_scale_d664xw](Runoff_06_confirms_at_scale_d664xw.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md)
