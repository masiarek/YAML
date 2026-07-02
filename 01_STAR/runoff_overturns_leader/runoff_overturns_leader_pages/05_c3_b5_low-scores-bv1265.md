# Low scores, switched winner — the popover example (BetterVoting BV1265)

*Generated from [`05_c3_b5_low-scores-bv1265.yaml`](../05_c3_b5_low-scores-bv1265.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

A real BetterVoting election (the one whose result pops up the "Why is the top
scoring candidate different from the winner?" note). It's a Runoff Reversal where
every score is LOW — proof the effect isn't about big enthusiasm gaps.

Five voters, three candidates. C tops the Scoring Round with just 7 stars (A 6,
B 4). The Finalists are C and A. In the Automatic Runoff, 3 of 5 voters prefer A
to C, so A wins 60% to 40% — the score leader C is overturned.

See the plain-language explainer (and the fix for BetterVoting's popover wording)
in explaining_to_voters.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A, B, C
0, 0, 4
2, 0, 0
0, 2, 3
2, 0, 0
2, 2, 0
```

## What the engine says

Full report from the [`_tabulated` mirror](../runoff_overturns_leader_tabulated/05_c3_b5_low-scores-bv1265_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |     B     |   * C     |
-----------------------------------------------------
         * A > |    ---     |2 - 2 - 1  |3 - 0 - 2  |
           B > | 1 - 2 - 2  |   ---     |1 - 2 - 2  |
         * C > | 2 - 0 - 3  |2 - 2 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: A — matches the STAR winner

[Divergence from STAR]
  STAR     = A
  Approval = C   (differs from STAR)

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (C)
 - Runoff Round Winner   = (A)
  Candidate C earned the highest total score,
  but Candidate A won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 5 ballots.
Count × A,B,C
    2 × 2,0,0
    1 × 0,0,4
    1 × 0,2,3
    1 × 2,2,0

[Score Distribution] (number of ballots giving each score)
   5  4  3  2  1  0  | Total   Avg
A  0  0  0  3  0  2  |     6   1.2
B  0  0  0  2  0  3  |     4   0.8
C  0  1  1  0  0  3  |     7   1.4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 7 -- First place
   A             -- 6 -- Second place
   B             -- 4
 C and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 3 -- First place
   C             -- 2
   Equal Support -- 0
 A wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           A 3 (60%)  ·  C 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/05_c3_b5_low-scores-bv1265.yaml
```

## See also

- [This set's lesson (README)](../README_runoff_overturns_leader.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/05_c3_b5_low-scores-bv1265.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c3_b3_more-stars-fewer-voters](01a_c3_b3_more-stars-fewer-voters.md) · [01b_c3_b9_overturn-holds-at-scale](01b_c3_b9_overturn-holds-at-scale.md) · [02_c5_b5_leader-overturned](02_c5_b5_leader-overturned.md) · [03_c7_b3_ice-cream-live](03_c7_b3_ice-cream-live.md) · [04_c4_b3_runoff-confirms-leader](04_c4_b3_runoff-confirms-leader.md) · [Runoff_01_confirms_leader_r2pvc9](Runoff_01_confirms_leader_r2pvc9.md) · [Runoff_02_atom_reversal_yx9447](Runoff_02_atom_reversal_yx9447.md) · [Runoff_03_enthusiasts_vs_majority_rkgtpk](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) · [Runoff_04_reversal_at_scale_bfjqmg](Runoff_04_reversal_at_scale_bfjqmg.md) · [Runoff_05_reversal_with_equal_support_xgkw3w](Runoff_05_reversal_with_equal_support_xgkw3w.md) · [Runoff_06_confirms_at_scale_d664xw](Runoff_06_confirms_at_scale_d664xw.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md)
