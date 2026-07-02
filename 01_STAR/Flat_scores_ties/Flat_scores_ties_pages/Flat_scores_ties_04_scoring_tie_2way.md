# Flat scores 04 — scoring-round tie for the 2nd finalist slot (2-way)

*Generated from [`Flat_scores_ties_04_scoring_tie_2way.yaml`](../Flat_scores_ties_04_scoring_tie_2way.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Aral

## Scenario

Aral leads outright; Baikal and Crater tie for the second finalist slot. The cascade
(head-to-head -> most 5s -> lot) advances Baikal; Aral then wins the runoff cleanly.
BV bugs: wrong finalists #1379; lot rule #1063; tie-break export #1371 (closed). Level 201.
Lesson: Flat_scores_ties_04_scoring_tie_2way.md  (BV id pending).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Aral, Baikal, Crater
5, 4, 4
5, 4, 4
5, 0, 0
```

## What the engine says

Full report from the [`_tabulated` mirror](../Flat_scores_ties_tabulated/Flat_scores_ties_04_scoring_tie_2way_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Aral   | * Baikal  |   Crater  |
-----------------------------------------------------
      * Aral > |    ---     |3 - 0 - 0  |3 - 0 - 0  |
    * Baikal > | 0 - 0 - 3  |   ---     |0 - 3 - 0  |
      Crater > | 0 - 0 - 3  |0 - 3 - 0  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Aral — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots.
Count × Aral,Baikal,Crater
    2 ×    5,     4,     4
    1 ×    5,     0,     0

[Score Distribution] (number of ballots giving each score)
        5  4  3  2  1  0  | Total   Avg
Aral    3  0  0  0  0  0  |    15   5.0
Baikal  0  2  0  0  0  1  |     8   2.7
Crater  0  2  0  0  0  1  |     8   2.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Aral          -- 15 -- First place
   Baikal        --  8 -- Tied for second place
   Crater        --  8 -- Tied for second place
 Aral advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Baikal        -- 0 -- Tied for second place
   Crater        -- 0 -- Tied for second place
   Equal Support -- 3
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Baikal        -- 0 -- Tied for second place
   Crater        -- 0 -- Tied for second place
 There's still a two-way tie for second.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Aral', 'Baikal', 'Crater']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Baikal', 'Crater']
  Resolved: ['Baikal'] (selected by lot-number priority).

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Aral          -- 3 -- First place
   Baikal        -- 0
   Equal Support -- 0
 Aral wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Aral 3 (100%)  ·  Baikal 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Aral
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/Flat_scores_ties/Flat_scores_ties_04_scoring_tie_2way.yaml
```

## See also

- [This set's lesson (README)](../README_Flat_scores_ties.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Flat_scores_ties_01_baseline_clean](Flat_scores_ties_01_baseline_clean.md) · [Flat_scores_ties_02_runoff_tie_2cand](Flat_scores_ties_02_runoff_tie_2cand.md) · [Flat_scores_ties_03_runoff_tie_split](Flat_scores_ties_03_runoff_tie_split.md) · [Flat_scores_ties_05_scoring_tie_3way_xmyf7k](Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md) · [Flat_scores_ties_06_scoring_tie_4way](Flat_scores_ties_06_scoring_tie_4way.md) · [Flat_scores_ties_07_fully_flat](Flat_scores_ties_07_fully_flat.md) · [Flat_scores_ties_08_all_flat_zero_count](Flat_scores_ties_08_all_flat_zero_count.md)
