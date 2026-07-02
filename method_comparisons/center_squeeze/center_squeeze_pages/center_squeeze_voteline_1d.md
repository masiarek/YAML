# Center squeeze — the voteline 1D spectrum (Red / Green / Yellow)

*Generated from [`center_squeeze_voteline_1d.yaml`](../center_squeeze_voteline_1d.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Green

## Scenario

The classic 1-D spectrum demo (zesty.ca/voting/voteline): Red on the left,
Green in the center, Yellow on the right, with voters spread across the line.
Green is the CONDORCET winner (beats Red AND Yellow head-to-head) but has the
FEWEST first choices (31.3%), so RCV-IRV eliminates Green first and YELLOW wins
(52.9%) — the center squeeze. STAR advances Green on strength of support and wins
the runoff 65-35. Plurality also picks Yellow. Approval / Borda / Condorcet /
Ranked Robin all pick Green. Scores are a reasonable 1-D spatial model (own side
5, adjacent center 3, far side 0-1). Weights are percentages x10. Level 201/301.
Lesson: 00_start_here/RCV_IRV/RCV_IRV_center_squeeze.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Red, Green, Yellow
332 × 5, 3, 0      # red > green > yellow  (left bloc)
138 × 3, 5, 1      # green > red > yellow  (center-left)
175 × 1, 5, 3      # green > yellow > red  (center-right)
353 × 0, 3, 5      # yellow > green > red  (right bloc)
```

## What the engine says

Full report from the [`_tabulated` mirror](../center_squeeze_tabulated/center_squeeze_voteline_1d_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |        Red      |    * Green     |   * Yellow     |
-------------------------------------------------------------------------
              Red > |       ---       |332 -   0 - 666 |470 -   0 - 528 |
          * Green > | 666 -   0 - 332 |      ---       |645 -   0 - 353 |
         * Yellow > | 528 -   0 - 470 |353 -   0 - 645 |      ---       |

[Condorcet Winner]
  Condorcet Winner: Green — matches the STAR winner

[Divergence from STAR]
  STAR                   = Green
  Choose-One (Plurality) = Yellow   (differs from STAR)
  RCV-IRV                = Yellow   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: center_squeeze_tabulated/center_squeeze_voteline_1d_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 998 ballots.
Count × Red,Green,Yellow
  353 ×   0,    3,     5
  332 ×   5,    3,     0
  175 ×   1,    5,     3
  138 ×   3,    5,     1

[Score Distribution] (number of ballots giving each score)
          5    4    3    2    1    0  | Total   Avg
Red     332    0  138    0  175  353  |  2249   2.3
Green   313    0  685    0    0    0  |  3620   3.6
Yellow  353    0  175    0  138  332  |  2428   2.4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Green         -- 3620 -- First place
   Yellow        -- 2428 -- Second place
   Red           -- 2249
 Green and Yellow advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Green         -- 645 -- First place
   Yellow        -- 353
   Equal Support --   0
 Green wins.
   Runoff math:
     998  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     998  voters with a preference  (majority = 500)
           Green 645 (65%)  ·  Yellow 353 (35%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Green
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/center_squeeze/center_squeeze_voteline_1d.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/center_squeeze_voteline_1d.md) — its entry in the divergence review ledger
- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README_center_squeeze.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [center_squeeze_irv](center_squeeze_irv.md) · [center_squeeze_star](center_squeeze_star.md)
