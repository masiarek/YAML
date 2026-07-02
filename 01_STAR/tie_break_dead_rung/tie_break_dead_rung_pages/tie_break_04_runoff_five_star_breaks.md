# Tie-break 04 — runoff tie, score tied, FIVE-STAR breaks it (a 5 exists)

*Generated from [`tie_break_04_runoff_five_star_breaks.yaml`](../tie_break_04_runoff_five_star_breaks.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Alice

## Scenario

The runoff ladder's working case. Two candidates tie head-to-head (1-1) and tie
on total score (5-5), so the runoff falls to its second rung — most score-5
votes. Alice has one 5, Ben has none, so Alice wins WITHOUT reaching the lot.
Contrast tie_break_03 (same tie, no 5 exists -> the lot decides).
See 00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alice,Ben
5,1
0,4
```

## What the engine says

Full report from the [`_tabulated` mirror](../tie_break_dead_rung_tabulated/tie_break_04_runoff_five_star_breaks_tabulated.txt) (regenerated on every run; every analysis forced on):

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

[Divergence from STAR]
  STAR    = Alice
  RCV-IRV = Ben   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: tie_break_dead_rung_tabulated/tie_break_04_runoff_five_star_breaks_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Alice,Ben
    5,  1
    0,  4

[Score Distribution] (number of ballots giving each score)
       5  4  3  2  1  0  | Total   Avg
Alice  1  0  0  0  0  1  |     5   2.5
Ben    0  1  0  0  1  0  |     5   2.5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alice         -- 5 -- First place
   Ben           -- 5 -- Second place
 Alice and Ben advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Alice         -- 1 -- Tied for first place
   Ben           -- 1 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Alice         -- 5 -- Tied for first place
   Ben           -- 5 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Alice         -- 1 -- First place
   Ben           -- 0
 Alice wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Alice
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/tie_break_dead_rung/tie_break_04_runoff_five_star_breaks.yaml
```

## See also

- [This set's lesson (README)](../README_tie_break_dead_rung.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [tie_break_01_scoring_five_star_breaks](tie_break_01_scoring_five_star_breaks.md) · [tie_break_02_scoring_no_fives_to_lot](tie_break_02_scoring_no_fives_to_lot.md) · [tie_break_03_runoff_no_fives_to_lot](tie_break_03_runoff_no_fives_to_lot.md) · [tie_break_05_scoring_five_star_vs_adversarial_lot](tie_break_05_scoring_five_star_vs_adversarial_lot.md) · [tie_break_06_scoring_dead_rung_adversarial_lot](tie_break_06_scoring_dead_rung_adversarial_lot.md) · [tie_break_07_runoff_five_star_vs_adversarial_lot](tie_break_07_runoff_five_star_vs_adversarial_lot.md) · [tie_break_08_runoff_dead_rung_adversarial_lot](tie_break_08_runoff_dead_rung_adversarial_lot.md) · [tie_break_09_five_star_tied_nonzero](tie_break_09_five_star_tied_nonzero.md)
