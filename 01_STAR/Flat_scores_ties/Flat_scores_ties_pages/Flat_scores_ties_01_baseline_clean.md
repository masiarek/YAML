# Flat scores 01 — clean top two (works-fine baseline)

*Generated from [`Flat_scores_ties_01_baseline_clean.yaml`](../Flat_scores_ties_01_baseline_clean.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Apple

## Scenario

The control. Distinct totals leave an unambiguous top two and a decisive runoff, so
NO tie-break fires anywhere; BV and LH agree trivially. Fruits cast. Level 101.
Lesson: Flat_scores_ties_01_baseline_clean.md  (BV id pending).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Apple, Banana, Cherry
5, 3, 1
5, 3, 1
```

## What the engine says

Full report from the [`_tabulated` mirror](../Flat_scores_ties_tabulated/Flat_scores_ties_01_baseline_clean_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Apple   | * Banana  |   Cherry  |
-----------------------------------------------------
     * Apple > |    ---     |2 - 0 - 0  |2 - 0 - 0  |
    * Banana > | 0 - 0 - 2  |   ---     |2 - 0 - 0  |
      Cherry > | 0 - 0 - 2  |0 - 0 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Apple — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Count × Apple,Banana,Cherry
    2 ×     5,     3,     1

[Score Distribution] (number of ballots giving each score)
        5  4  3  2  1  0  | Total   Avg
Apple   2  0  0  0  0  0  |    10   5.0
Banana  0  0  2  0  0  0  |     6   3.0
Cherry  0  0  0  0  2  0  |     2   1.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Apple         -- 10 -- First place
   Banana        --  6 -- Second place
   Cherry        --  2
 Apple and Banana advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Apple         -- 2 -- First place
   Banana        -- 0
   Equal Support -- 0
 Apple wins.
   Runoff math:
     2  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           Apple 2 (100%)  ·  Banana 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Apple
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/Flat_scores_ties/Flat_scores_ties_01_baseline_clean.yaml
```

## See also

- [This set's lesson (README)](../README_Flat_scores_ties.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Flat_scores_ties_02_runoff_tie_2cand](Flat_scores_ties_02_runoff_tie_2cand.md) · [Flat_scores_ties_03_runoff_tie_split](Flat_scores_ties_03_runoff_tie_split.md) · [Flat_scores_ties_04_scoring_tie_2way](Flat_scores_ties_04_scoring_tie_2way.md) · [Flat_scores_ties_05_scoring_tie_3way_xmyf7k](Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md) · [Flat_scores_ties_06_scoring_tie_4way](Flat_scores_ties_06_scoring_tie_4way.md) · [Flat_scores_ties_07_fully_flat](Flat_scores_ties_07_fully_flat.md) · [Flat_scores_ties_08_all_flat_zero_count](Flat_scores_ties_08_all_flat_zero_count.md)
