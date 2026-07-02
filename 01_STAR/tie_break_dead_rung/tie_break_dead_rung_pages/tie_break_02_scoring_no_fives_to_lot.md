# Tie-break 02 — scoring-round tie, NO fives, five-star is a dead rung → LOT

*Generated from [`tie_break_02_scoring_no_fives_to_lot.yaml`](../tie_break_02_scoring_no_fives_to_lot.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Alice

**Official tie-break (lot) order:** Alice > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The same tie structure as tie_break_01, but every score is capped at 4, so NO
candidate has a single max-score (5) vote. Alice leads (8); Ben and Cara tie at
4 and are tied head-to-head (pairwise 1-1). The five-star rung still runs, but
reads 0-0 — it cannot separate them — so the tie falls through to the LOT.
lot_numbers pins the order, so Ben advances by lot priority (not by five-star).
The eventual winner is still Alice; what changed is WHICH rung chose the second
finalist. See 00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alice,Ben,Cara
4,4,2
4,0,2
```

## What the engine says

Full report from the [`_tabulated` mirror](../tie_break_dead_rung_tabulated/tie_break_02_scoring_no_fives_to_lot_tabulated.txt) (regenerated on every run; every analysis forced on):

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
    4,  4,   2
    4,  0,   2

[Score Distribution] (number of ballots giving each score)
       5  4  3  2  1  0  | Total   Avg
Alice  0  2  0  0  0  0  |     8   4.0
Ben    0  1  0  0  0  1  |     4   2.0
Cara   0  0  0  2  0  0  |     4   2.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alice         -- 8 -- First place
   Ben           -- 4 -- Tied for second place
   Cara          -- 4 -- Tied for second place
 Alice advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Ben           -- 1 -- Tied for second place
   Cara          -- 1 -- Tied for second place
   Equal Support -- 0
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Ben           -- 0 -- Tied for second place
   Cara          -- 0 -- Tied for second place
 There's still a two-way tie for second.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Alice', 'Ben', 'Cara']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ben', 'Cara']
  Resolved: ['Ben'] (selected by lot-number priority).

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
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/tie_break_dead_rung/tie_break_02_scoring_no_fives_to_lot.yaml
```

## See also

- [This set's lesson (README)](../README_tie_break_dead_rung.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [tie_break_01_scoring_five_star_breaks](tie_break_01_scoring_five_star_breaks.md) · [tie_break_03_runoff_no_fives_to_lot](tie_break_03_runoff_no_fives_to_lot.md) · [tie_break_04_runoff_five_star_breaks](tie_break_04_runoff_five_star_breaks.md) · [tie_break_05_scoring_five_star_vs_adversarial_lot](tie_break_05_scoring_five_star_vs_adversarial_lot.md) · [tie_break_06_scoring_dead_rung_adversarial_lot](tie_break_06_scoring_dead_rung_adversarial_lot.md) · [tie_break_07_runoff_five_star_vs_adversarial_lot](tie_break_07_runoff_five_star_vs_adversarial_lot.md) · [tie_break_08_runoff_dead_rung_adversarial_lot](tie_break_08_runoff_dead_rung_adversarial_lot.md) · [tie_break_09_five_star_tied_nonzero](tie_break_09_five_star_tied_nonzero.md)
