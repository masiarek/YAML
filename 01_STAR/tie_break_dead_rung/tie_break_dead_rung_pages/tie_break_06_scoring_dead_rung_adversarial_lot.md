# Dead rung 02 — same tie, but nobody scored a 5

*Generated from [`tie_break_06_scoring_dead_rung_adversarial_lot.yaml`](../tie_break_06_scoring_dead_rung_adversarial_lot.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ann

**Official tie-break (lot) order:** Cara > Ann > Ben — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The SAME shape as case 01 with every top score capped at 4: Ben and Cara
still tie on points (9-9) and pairwise (2-2) for the second finalist slot —
but now NOBODY scored the maximum, so the five-star rung reads 0-0 and is
a DEAD RUNG. The tie falls through to the lot, which favors Cara; Ann then
beats Cara in the runoff 3-1.
One point of enthusiasm is the whole difference: case 01 is decided by
ballots (five-star), case 02 by the pre-drawn lot. See
00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ann,Ben,Cara
3,4,1   # Ben bloc — tops out at 4
3,4,0   # Ben bloc
4,0,3   # Cara bloc
4,0,4   # Cara bloc
0,1,1   # low-score voter
```

## What the engine says

Full report from the [`_tabulated` mirror](../tie_break_dead_rung_tabulated/tie_break_06_scoring_dead_rung_adversarial_lot_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ann    |    Ben    |  * Cara   |
-----------------------------------------------------
       * Ann > |    ---     |2 - 0 - 3  |3 - 1 - 1  |
         Ben > | 3 - 0 - 2  |   ---     |2 - 1 - 2  |
      * Cara > | 1 - 1 - 3  |2 - 1 - 2  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: Ben — STAR elected Ann instead (Ben was eliminated in the scoring round)

[Divergence from STAR]
  STAR                   = Ann
  Choose-One (Plurality) = Cara   (differs from STAR)
  RCV-IRV                = Cara   (differs from STAR)
  Note: 2 of 5 ballots (40%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: tie_break_dead_rung_tabulated/tie_break_06_scoring_dead_rung_adversarial_lot_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 5 ballots.
Ann,Ben,Cara
  3,  4,   1
  3,  4,   0
  4,  0,   3
  4,  0,   4
  0,  1,   1

[Score Distribution] (number of ballots giving each score)
      5  4  3  2  1  0  | Total   Avg
Ann   0  2  2  0  0  1  |    14   2.8
Ben   0  2  0  0  1  2  |     9   1.8
Cara  0  1  1  0  2  1  |     9   1.8

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ann           -- 14 -- First place
   Ben           --  9 -- Tied for second place
   Cara          --  9 -- Tied for second place
 Ann advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Ben           -- 2 -- Tied for second place
   Cara          -- 2 -- Tied for second place
   Equal Support -- 1
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Ben           -- 0 -- Tied for second place
   Cara          -- 0 -- Tied for second place
 There's still a two-way tie for second.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Cara', 'Ann', 'Ben']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ben', 'Cara']
  Resolved: ['Cara'] (selected by lot-number priority).

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ann           -- 3 -- First place
   Cara          -- 1
   Equal Support -- 1
 Ann wins.
   Runoff math:
     5  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     4  voters with a preference  (majority = 3)
           Ann 3 (75%)  ·  Cara 1 (25%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ann
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/tie_break_dead_rung/tie_break_06_scoring_dead_rung_adversarial_lot.yaml
```

## See also

- [This set's lesson (README)](../README_tie_break_dead_rung.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [tie_break_01_scoring_five_star_breaks](tie_break_01_scoring_five_star_breaks.md) · [tie_break_02_scoring_no_fives_to_lot](tie_break_02_scoring_no_fives_to_lot.md) · [tie_break_03_runoff_no_fives_to_lot](tie_break_03_runoff_no_fives_to_lot.md) · [tie_break_04_runoff_five_star_breaks](tie_break_04_runoff_five_star_breaks.md) · [tie_break_05_scoring_five_star_vs_adversarial_lot](tie_break_05_scoring_five_star_vs_adversarial_lot.md) · [tie_break_07_runoff_five_star_vs_adversarial_lot](tie_break_07_runoff_five_star_vs_adversarial_lot.md) · [tie_break_08_runoff_dead_rung_adversarial_lot](tie_break_08_runoff_dead_rung_adversarial_lot.md) · [tie_break_09_five_star_tied_nonzero](tie_break_09_five_star_tied_nonzero.md)
