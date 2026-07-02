# Tie-break 03 — runoff tie, score tied, NO fives → LOT

*Generated from [`tie_break_03_runoff_no_fives_to_lot.yaml`](../tie_break_03_runoff_no_fives_to_lot.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Alice

**Official tie-break (lot) order:** Alice > Ben — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The runoff ladder's dead-rung case. Two candidates, both finalists. They tie
head-to-head (1-1) AND tie on total score (4-4), so the runoff falls to its
second rung — most score-5 votes. But neither earned a 5, so five-star reads
0-0 and the LOT decides. lot_numbers pins Alice ahead of Ben, so Alice wins.
Contrast tie_break_04 (same tie, but a 5 exists -> five-star decides).
See 00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alice,Ben
4,0
0,4
```

## What the engine says

Full report from the [`_tabulated` mirror](../tie_break_dead_rung_tabulated/tie_break_03_runoff_no_fives_to_lot_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Alice   |  * Ben    |
-----------------------------------------
     * Alice > |    ---     |1 - 0 - 1  |
       * Ben > | 1 - 0 - 1  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Alice, Ben (pairwise ties)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Alice,Ben
    4,  0
    0,  4

[Score Distribution] (number of ballots giving each score)
       5  4  3  2  1  0  | Total   Avg
Alice  0  1  0  0  0  1  |     4   2.0
Ben    0  1  0  0  0  1  |     4   2.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alice         -- 4 -- First place
   Ben           -- 4 -- Second place
 Alice and Ben advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Alice         -- 1 -- Tied for first place
   Ben           -- 1 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Alice         -- 4 -- Tied for first place
   Ben           -- 4 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Alice         -- 0 -- Tied for first place
   Ben           -- 0 -- Tied for first place
 There's still a two-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Alice', 'Ben']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Alice', 'Ben']
  Resolved: ['Alice'] (selected by lot-number priority).

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Alice
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/tie_break_dead_rung/tie_break_03_runoff_no_fives_to_lot.yaml
```

## See also

- [This set's lesson (README)](../README_tie_break_dead_rung.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [tie_break_01_scoring_five_star_breaks](tie_break_01_scoring_five_star_breaks.md) · [tie_break_02_scoring_no_fives_to_lot](tie_break_02_scoring_no_fives_to_lot.md) · [tie_break_04_runoff_five_star_breaks](tie_break_04_runoff_five_star_breaks.md) · [tie_break_05_scoring_five_star_vs_adversarial_lot](tie_break_05_scoring_five_star_vs_adversarial_lot.md) · [tie_break_06_scoring_dead_rung_adversarial_lot](tie_break_06_scoring_dead_rung_adversarial_lot.md) · [tie_break_07_runoff_five_star_vs_adversarial_lot](tie_break_07_runoff_five_star_vs_adversarial_lot.md) · [tie_break_08_runoff_dead_rung_adversarial_lot](tie_break_08_runoff_dead_rung_adversarial_lot.md) · [tie_break_09_five_star_tied_nonzero](tie_break_09_five_star_tied_nonzero.md)
