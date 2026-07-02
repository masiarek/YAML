# Monotonicity — STAR counterpart (BEFORE — X wins)

*Generated from [`monotonicity_star_before.yaml`](../monotonicity_star_before.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** X

## Scenario

The SAME 34-voter profile as the RCV-IRV monotonicity demo
(01_Single_winner/monotonicity_irv_before.yaml), translated to 0–5 scores
(1st → 5, 2nd → 3, unranked → 0). STAR elects X.

In the _after file, 4 voters RAISE X to the top. RCV-IRV flips X from winner to
loser (the non-monotonicity paradox); STAR still elects X. See
00_start_here/monotonicity.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:X,Y,Z
12:5,3,0   # X>Y
12:0,5,3   # Y>Z
10:3,0,5   # Z>X
```

## What the engine says

Full report from the [`_tabulated` mirror](../monotonicity_tabulated/monotonicity_star_before_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * X      |    * Y      |      Z      |
-------------------------------------------------------------
           * X > |     ---      |22 -  0 - 12 |12 -  0 - 22 |
           * Y > | 12 -  0 - 22 |    ---      |24 -  0 - 10 |
             Z > | 22 -  0 - 12 |10 -  0 - 24 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: X > Y > Z > X)

[Divergence from STAR]
  STAR     = X
  Approval = Y   (differs from STAR)
  RCV-RR   = Y   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: monotonicity_tabulated/monotonicity_star_before_RCV-RR_tabulated.txt

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Y)
 - Runoff Round Winner   = (X)
  Candidate Y earned the highest total score,
  but Candidate X won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 34 ballots.
Count × X,Y,Z
   12 × 5,3,0
   12 × 0,5,3
   10 × 3,0,5

[Score Distribution] (number of ballots giving each score)
    5   4   3   2   1   0  | Total   Avg
X  12   0  10   0   0  12  |    90   2.6
Y  12   0  12   0   0  10  |    96   2.8
Z  10   0  12   0   0  12  |    86   2.5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Y             -- 96 -- First place
   X             -- 90 -- Second place
   Z             -- 86
 Y and X advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   X             -- 22 -- First place
   Y             -- 12
   Equal Support --  0
 X wins.
   Runoff math:
     34  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     34  voters with a preference  (majority = 18)
           X 22 (65%)  ·  Y 12 (35%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 X
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/monotonicity_star_before.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/monotonicity_star_before.md) — its entry in the divergence review ledger
- [Monotonicity (topic hub)](../../../00_start_here/topics/monotonicity/README_monotonicity.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [monotonicity_irv_after](monotonicity_irv_after.md) · [monotonicity_irv_before](monotonicity_irv_before.md) · [monotonicity_star_after](monotonicity_star_after.md)
