# Flat scores 08 — every ballot flat (BetterVoting counts 0)

*Generated from [`Flat_scores_ties_08_all_flat_zero_count.yaml`](../Flat_scores_ties_08_all_flat_zero_count.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Anchovy

## Scenario

Five voters, every ballot FLAT at a different level: 1s..5s. Each pizza totals 15 — a
3-way tie LH resolves by lot to Anchovy. BetterVoting mis-files ALL FIVE as abstentions,
so its ballot count reads 0. Intersects #1407, BV126 #1052, BV200 #1035. Level 301.
Lesson: Flat_scores_ties_08_all_flat_zero_count.md  (BV id pending).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Anchovy, Basil, Caper
1, 1, 1
2, 2, 2
3, 3, 3
4, 4, 4
5, 5, 5
```

## What the engine says

Full report from the [`_tabulated` mirror](../Flat_scores_ties_tabulated/Flat_scores_ties_08_all_flat_zero_count_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |  * Anchovy  |  * Basil   |    Caper   |
---------------------------------------------------------
    * Anchovy > |     ---     | 0 - 5 - 0  | 0 - 5 - 0  |
      * Basil > |  0 - 5 - 0  |    ---     | 0 - 5 - 0  |
        Caper > |  0 - 5 - 0  | 0 - 5 - 0  |    ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Anchovy, Basil, Caper (pairwise ties)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 5 ballots.
Anchovy,Basil,Caper
      1,    1,    1
      2,    2,    2
      3,    3,    3
      4,    4,    4
      5,    5,    5

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Anchovy  1  1  1  1  1  0  |    15   3.0
Basil    1  1  1  1  1  0  |    15   3.0
Caper    1  1  1  1  1  0  |    15   3.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Anchovy       -- 15 -- Tied for first place
   Basil         -- 15 -- Tied for first place
   Caper         -- 15 -- Tied for first place
 There's a three-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Anchovy       -- 0 -- Tied for first place
   Basil         -- 0 -- Tied for first place
   Caper         -- 0 -- Tied for first place
   Equal Support -- 5
 There's still a three-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   Anchovy       -- 1 -- Tied for first place
   Basil         -- 1 -- Tied for first place
   Caper         -- 1 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Anchovy', 'Basil', 'Caper']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Anchovy', 'Basil', 'Caper']
  Resolved: ['Anchovy', 'Basil'] (selected by lot-number priority).

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Anchovy       -- 0 -- Tied for first place
   Basil         -- 0 -- Tied for first place
   Equal Support -- 5
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Anchovy       -- 15 -- Tied for first place
   Basil         -- 15 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Anchovy       -- 1 -- Tied for first place
   Basil         -- 1 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['Anchovy', 'Basil']
  Resolved: ['Anchovy'] (selected by lot-number priority).

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Anchovy
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/Flat_scores_ties/Flat_scores_ties_08_all_flat_zero_count.yaml
```

## See also

- [This set's lesson (README)](../README_Flat_scores_ties.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Flat_scores_ties_01_baseline_clean](Flat_scores_ties_01_baseline_clean.md) · [Flat_scores_ties_02_runoff_tie_2cand](Flat_scores_ties_02_runoff_tie_2cand.md) · [Flat_scores_ties_03_runoff_tie_split](Flat_scores_ties_03_runoff_tie_split.md) · [Flat_scores_ties_04_scoring_tie_2way](Flat_scores_ties_04_scoring_tie_2way.md) · [Flat_scores_ties_05_scoring_tie_3way_xmyf7k](Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md) · [Flat_scores_ties_06_scoring_tie_4way](Flat_scores_ties_06_scoring_tie_4way.md) · [Flat_scores_ties_07_fully_flat](Flat_scores_ties_07_fully_flat.md)
