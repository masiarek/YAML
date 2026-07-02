# Flat scores 03 — runoff tie, an even 1-1 split

*Generated from [`Flat_scores_ties_03_runoff_tie_split.yaml`](../Flat_scores_ties_03_runoff_tie_split.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Athens

## Scenario

Two capitals chosen cleanly, then the runoff splits 1-1 (real opposing preferences).
Broken by highest score -> most 5s -> lot -> Athens. Level 201.
Lesson: Flat_scores_ties_03_runoff_tie_split.md  (BV id pending).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Athens, Berlin, Cairo
5, 4, 0
4, 5, 0
```

## What the engine says

Full report from the [`_tabulated` mirror](../Flat_scores_ties_tabulated/Flat_scores_ties_03_runoff_tie_split_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Athens  | * Berlin  |   Cairo   |
-----------------------------------------------------
    * Athens > |    ---     |1 - 0 - 1  |2 - 0 - 0  |
    * Berlin > | 1 - 0 - 1  |   ---     |2 - 0 - 0  |
       Cairo > | 0 - 0 - 2  |0 - 0 - 2  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Athens, Berlin (pairwise ties)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Athens,Berlin,Cairo
     5,     4,    0
     4,     5,    0

[Score Distribution] (number of ballots giving each score)
        5  4  3  2  1  0  | Total   Avg
Athens  1  1  0  0  0  0  |     9   4.5
Berlin  1  1  0  0  0  0  |     9   4.5
Cairo   0  0  0  0  0  2  |     0   0.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Athens        -- 9 -- First place
   Berlin        -- 9 -- Second place
   Cairo         -- 0
 Athens and Berlin advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Athens        -- 1 -- Tied for first place
   Berlin        -- 1 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Athens        -- 9 -- Tied for first place
   Berlin        -- 9 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Athens        -- 1 -- Tied for first place
   Berlin        -- 1 -- Tied for first place
 There's still a two-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Athens', 'Berlin', 'Cairo']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Athens', 'Berlin']
  Resolved: ['Athens'] (selected by lot-number priority).

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Athens
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/Flat_scores_ties/Flat_scores_ties_03_runoff_tie_split.yaml
```

## See also

- [This set's lesson (README)](../README_Flat_scores_ties.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [Vote splitting (worked set)](../../../method_comparisons/split_voting/README_split_voting.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Flat_scores_ties_01_baseline_clean](Flat_scores_ties_01_baseline_clean.md) · [Flat_scores_ties_02_runoff_tie_2cand](Flat_scores_ties_02_runoff_tie_2cand.md) · [Flat_scores_ties_04_scoring_tie_2way](Flat_scores_ties_04_scoring_tie_2way.md) · [Flat_scores_ties_05_scoring_tie_3way_xmyf7k](Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md) · [Flat_scores_ties_06_scoring_tie_4way](Flat_scores_ties_06_scoring_tie_4way.md) · [Flat_scores_ties_07_fully_flat](Flat_scores_ties_07_fully_flat.md) · [Flat_scores_ties_08_all_flat_zero_count](Flat_scores_ties_08_all_flat_zero_count.md)
