# Tie-break 01 — scoring-round tie, FIVE-STAR breaks it (a 5 exists)

*Generated from [`tie_break_01_scoring_five_star_breaks.yaml`](../tie_break_01_scoring_five_star_breaks.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Alice

## Scenario

A scoring-round tie for the second finalist slot that the five-star rung DOES
resolve, because a max-score (5) vote exists. Alice leads (10); Ben and Cara
tie at 6 and are also tied head-to-head (pairwise 1-1), so the tie falls to the
second rung — most score-5 votes. Ben has one 5, Cara has none, so Ben advances.
Contrast with tie_break_02 (same shape, capped so no 5 exists -> the lot decides).
See 00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md ("dead rung").

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alice,Ben,Cara
5,5,3
5,1,3
```

## What the engine says

Full report from the [`_tabulated` mirror](../tie_break_dead_rung_tabulated/tie_break_01_scoring_five_star_breaks_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Alice   |  * Ben    |    Cara   |
-----------------------------------------------------
     * Alice > |    ---     |1 - 1 - 0  |2 - 0 - 0  |
       * Ben > | 0 - 1 - 1  |   ---     |1 - 0 - 1  |
        Cara > | 0 - 0 - 2  |1 - 0 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Alice — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Alice,Ben,Cara
    5,  5,   3
    5,  1,   3

[Score Distribution] (number of ballots giving each score)
       5  4  3  2  1  0  | Total   Avg
Alice  2  0  0  0  0  0  |    10   5.0
Ben    1  0  0  0  1  0  |     6   3.0
Cara   0  0  2  0  0  0  |     6   3.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alice         -- 10 -- First place
   Ben           --  6 -- Tied for second place
   Cara          --  6 -- Tied for second place
 Alice advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Ben           -- 1 -- Tied for second place
   Cara          -- 1 -- Tied for second place
   Equal Support -- 0
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Ben           -- 1 -- Second place
   Cara          -- 0
 Alice and Ben advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Alice         -- 1 -- First place
   Ben           -- 0
   Equal Support -- 1
 Alice wins.
   Runoff math:
     2  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     1  voters with a preference  (majority = 1)
           Alice 1 (100%)  ·  Ben 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Alice
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/tie_break_dead_rung/tie_break_01_scoring_five_star_breaks.yaml
```

## See also

- [This set's lesson (README)](../README_tie_break_dead_rung.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [tie_break_02_scoring_no_fives_to_lot](tie_break_02_scoring_no_fives_to_lot.md) · [tie_break_03_runoff_no_fives_to_lot](tie_break_03_runoff_no_fives_to_lot.md) · [tie_break_04_runoff_five_star_breaks](tie_break_04_runoff_five_star_breaks.md) · [tie_break_05_scoring_five_star_vs_adversarial_lot](tie_break_05_scoring_five_star_vs_adversarial_lot.md) · [tie_break_06_scoring_dead_rung_adversarial_lot](tie_break_06_scoring_dead_rung_adversarial_lot.md) · [tie_break_07_runoff_five_star_vs_adversarial_lot](tie_break_07_runoff_five_star_vs_adversarial_lot.md) · [tie_break_08_runoff_dead_rung_adversarial_lot](tie_break_08_runoff_dead_rung_adversarial_lot.md) · [tie_break_09_five_star_tied_nonzero](tie_break_09_five_star_tied_nonzero.md)
