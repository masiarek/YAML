# Flat scores 06 — scoring-round 4-way tie (ties at every step)

*Generated from [`Flat_scores_ties_06_scoring_tie_4way.yaml`](../Flat_scores_ties_06_scoring_tie_4way.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ava

## Scenario

Ava, Ben, Cara, Dan tie at 10; ties persist through every score-based tiebreaker, the
lot picks two finalists, and the runoff also ties -> lot again -> Ava. BV bugs: 'no
ballots cast' under multi-step ties (BV126 #1052); wrong finalists #1379; tie-break export #1371 (closed).
Level 301. Lesson: Flat_scores_ties_06_scoring_tie_4way.md  (BV id pending).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ava, Ben, Cara, Dan, Eve
5, 5, 5, 5, 1
5, 5, 5, 5, 1
```

## What the engine says

Full report from the [`_tabulated` mirror](../Flat_scores_ties_tabulated/Flat_scores_ties_06_scoring_tie_4way_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ava    |  * Ben    |    Cara   |    Dan    |    Eve    |
-----------------------------------------------------------------------------
       * Ava > |    ---     |0 - 2 - 0  |0 - 2 - 0  |0 - 2 - 0  |2 - 0 - 0  |
       * Ben > | 0 - 2 - 0  |   ---     |0 - 2 - 0  |0 - 2 - 0  |2 - 0 - 0  |
        Cara > | 0 - 2 - 0  |0 - 2 - 0  |   ---     |0 - 2 - 0  |2 - 0 - 0  |
         Dan > | 0 - 2 - 0  |0 - 2 - 0  |0 - 2 - 0  |   ---     |2 - 0 - 0  |
         Eve > | 0 - 0 - 2  |0 - 0 - 2  |0 - 0 - 2  |0 - 0 - 2  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Ava, Ben, Cara, Dan (pairwise ties)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Count × Ava,Ben,Cara,Dan,Eve
    2 ×   5,  5,   5,  5,  1

[Score Distribution] (number of ballots giving each score)
      5  4  3  2  1  0  | Total   Avg
Ava   2  0  0  0  0  0  |    10   5.0
Ben   2  0  0  0  0  0  |    10   5.0
Cara  2  0  0  0  0  0  |    10   5.0
Dan   2  0  0  0  0  0  |    10   5.0
Eve   0  0  0  0  2  0  |     2   1.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ava           -- 10 -- Tied for first place
   Ben           -- 10 -- Tied for first place
   Cara          -- 10 -- Tied for first place
   Dan           -- 10 -- Tied for first place
   Eve           --  2
 There's a four-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Ava           -- 0 -- Tied for first place
   Ben           -- 0 -- Tied for first place
   Cara          -- 0 -- Tied for first place
   Dan           -- 0 -- Tied for first place
   Equal Support -- 2
 There's still a four-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   Ava           -- 2 -- Tied for first place
   Ben           -- 2 -- Tied for first place
   Cara          -- 2 -- Tied for first place
   Dan           -- 2 -- Tied for first place
 There's still a four-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ava', 'Ben', 'Cara', 'Dan', 'Eve']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ava', 'Ben', 'Cara', 'Dan']
  Resolved: ['Ava', 'Ben'] (selected by lot-number priority).

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ava           -- 0 -- Tied for first place
   Ben           -- 0 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Ava           -- 10 -- Tied for first place
   Ben           -- 10 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Ava           -- 2 -- Tied for first place
   Ben           -- 2 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ava', 'Ben']
  Resolved: ['Ava'] (selected by lot-number priority).

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ava
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/Flat_scores_ties/Flat_scores_ties_06_scoring_tie_4way.yaml
```

## See also

- [This set's lesson (README)](../README_Flat_scores_ties.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Flat_scores_ties_01_baseline_clean](Flat_scores_ties_01_baseline_clean.md) · [Flat_scores_ties_02_runoff_tie_2cand](Flat_scores_ties_02_runoff_tie_2cand.md) · [Flat_scores_ties_03_runoff_tie_split](Flat_scores_ties_03_runoff_tie_split.md) · [Flat_scores_ties_04_scoring_tie_2way](Flat_scores_ties_04_scoring_tie_2way.md) · [Flat_scores_ties_05_scoring_tie_3way_xmyf7k](Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md) · [Flat_scores_ties_07_fully_flat](Flat_scores_ties_07_fully_flat.md) · [Flat_scores_ties_08_all_flat_zero_count](Flat_scores_ties_08_all_flat_zero_count.md)
