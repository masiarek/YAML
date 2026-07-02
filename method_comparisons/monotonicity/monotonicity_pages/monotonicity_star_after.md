# Monotonicity — STAR counterpart (AFTER — X still wins)

*Generated from [`monotonicity_star_after.yaml`](../monotonicity_star_after.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** X

## Scenario

The ONLY change from _before: 4 voters raise X to the top (their ballot goes from
Y>Z to X>Y, i.e. scores 0,5,3 → 5,3,0). X gained support.

STAR still elects X — raising the winner did not hurt them. Compare the RCV-IRV
twin (01_Single_winner/monotonicity_irv_after.yaml), where the same change makes
X LOSE to Z. The [Divergence from STAR] block below shows RCV-IRV electing Z on
these very ballots: STAR is monotone, RCV-IRV is not.
See 00_start_here/monotonicity.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:X,Y,Z
16:5,3,0   # X>Y  (12 + the 4 who raised X)
8:0,5,3    # Y>Z
10:3,0,5   # Z>X
```

## What the engine says

Full report from the [`_tabulated` mirror](../monotonicity_tabulated/monotonicity_star_after_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * X      |    * Y      |      Z      |
-------------------------------------------------------------
           * X > |     ---      |26 -  0 -  8 |16 -  0 - 18 |
           * Y > |  8 -  0 - 26 |    ---      |24 -  0 - 10 |
             Z > | 18 -  0 - 16 |10 -  0 - 24 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: X > Y > Z > X)

[Divergence from STAR]
  STAR    = X
  RCV-IRV = Z   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: monotonicity_tabulated/monotonicity_star_after_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 34 ballots.
Count × X,Y,Z
   16 × 5,3,0
   10 × 3,0,5
    8 × 0,5,3

[Score Distribution] (number of ballots giving each score)
    5   4   3   2   1   0  | Total   Avg
X  16   0  10   0   0   8  |   110   3.2
Y   8   0  16   0   0  10  |    88   2.6
Z  10   0   8   0   0  16  |    74   2.2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   X             -- 110 -- First place
   Y             --  88 -- Second place
   Z             --  74
 X and Y advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   X             -- 26 -- First place
   Y             --  8
   Equal Support --  0
 X wins.
   Runoff math:
     34  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     34  voters with a preference  (majority = 18)
           X 26 (76%)  ·  Y 8 (24%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 X
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/monotonicity_star_after.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/monotonicity_star_after.md) — its entry in the divergence review ledger
- [Monotonicity (topic hub)](../../../00_start_here/topics/monotonicity/README_monotonicity.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [monotonicity_irv_after](monotonicity_irv_after.md) · [monotonicity_irv_before](monotonicity_irv_before.md) · [monotonicity_star_before](monotonicity_star_before.md)
