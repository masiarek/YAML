# Flat scores 02 — runoff tie, two candidates (everyone equal)

*Generated from [`Flat_scores_ties_02_runoff_tie_2cand.yaml`](../Flat_scores_ties_02_runoff_tie_2cand.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Almond

## Scenario

Two ice-cream flavors, both scored 5 by everyone: both advance, the runoff is 0-0
Equal Support, and the cascade (highest score -> most 5s -> lot) picks Almond. BV bugs:
NaN/equal-ties #1035; lot rule #1063; tie-break export #1371 (closed). Level 101.
Lesson: Flat_scores_ties_02_runoff_tie_2cand.md  (BV id pending).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Almond, Brownie
5, 5
5, 5
```

## What the engine says

Full report from the [`_tabulated` mirror](../Flat_scores_ties_tabulated/Flat_scores_ties_02_runoff_tie_2cand_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |  * Almond   | * Brownie  |
--------------------------------------------
     * Almond > |     ---     | 0 - 2 - 0  |
    * Brownie > |  0 - 2 - 0  |    ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Almond, Brownie (pairwise ties)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Count × Almond,Brownie
    2 ×      5,      5

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Almond   2  0  0  0  0  0  |    10   5.0
Brownie  2  0  0  0  0  0  |    10   5.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Almond        -- 10 -- First place
   Brownie       -- 10 -- Second place
 Almond and Brownie advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Almond        -- 0 -- Tied for first place
   Brownie       -- 0 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Almond        -- 10 -- Tied for first place
   Brownie       -- 10 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Almond        -- 2 -- Tied for first place
   Brownie       -- 2 -- Tied for first place
 There's still a two-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Almond', 'Brownie']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Almond', 'Brownie']
  Resolved: ['Almond'] (selected by lot-number priority).

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Almond
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/Flat_scores_ties/Flat_scores_ties_02_runoff_tie_2cand.yaml
```

## See also

- [This set's lesson (README)](../README_Flat_scores_ties.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Flat_scores_ties_01_baseline_clean](Flat_scores_ties_01_baseline_clean.md) · [Flat_scores_ties_03_runoff_tie_split](Flat_scores_ties_03_runoff_tie_split.md) · [Flat_scores_ties_04_scoring_tie_2way](Flat_scores_ties_04_scoring_tie_2way.md) · [Flat_scores_ties_05_scoring_tie_3way_xmyf7k](Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md) · [Flat_scores_ties_06_scoring_tie_4way](Flat_scores_ties_06_scoring_tie_4way.md) · [Flat_scores_ties_07_fully_flat](Flat_scores_ties_07_fully_flat.md) · [Flat_scores_ties_08_all_flat_zero_count](Flat_scores_ties_08_all_flat_zero_count.md)
