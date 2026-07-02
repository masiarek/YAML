# Dead rung 01 — scoring tie, five-star rung ALIVE

*Generated from [`tie_break_05_scoring_five_star_vs_adversarial_lot.yaml`](../tie_break_05_scoring_five_star_vs_adversarial_lot.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ben

**Official tie-break (lot) order:** Cara > Ann > Ben — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Ben and Cara tie for the second finalist slot (11 points each) AND tie
pairwise (2-2). The FIVE-STAR rung decides: Ben has two 5s, Cara one, so
Ben advances — and then beats Ann in the runoff 3-2.
The lot order deliberately favors Cara: if the engine skipped the five-star
rung and went straight to the lot, Cara would advance and ANN would win.
The expected winner (Ben) therefore proves the rung was consulted.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ann,Ben,Cara
3,5,1   # Ben bloc
3,5,0   # Ben bloc
4,0,3   # Cara bloc
4,0,4   # Cara bloc
0,1,1   # low-score voter
```

## What the engine says

Full report from the [`_tabulated` mirror](../tie_break_dead_rung_tabulated/tie_break_05_scoring_five_star_vs_adversarial_lot_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ann    |  * Ben    |    Cara   |
-----------------------------------------------------
       * Ann > |    ---     |2 - 0 - 3  |3 - 1 - 1  |
       * Ben > | 3 - 0 - 2  |   ---     |2 - 1 - 2  |
        Cara > | 1 - 1 - 3  |2 - 1 - 2  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: Ben — matches the STAR winner

[Divergence from STAR]
  STAR                   = Ben
  Choose-One (Plurality) = Cara   (differs from STAR)
  RCV-IRV                = Cara   (differs from STAR)
  Approval               = Ann   (differs from STAR)
  RCV-RR                 = Ann   (differs from STAR)
  Note: 2 of 5 ballots (40%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: tie_break_dead_rung_tabulated/tie_break_05_scoring_five_star_vs_adversarial_lot_RCV-IRV_tabulated.txt
  RCV-RR round-robin: tie_break_dead_rung_tabulated/tie_break_05_scoring_five_star_vs_adversarial_lot_RCV-RR_tabulated.txt

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Ann)
 - Runoff Round Winner   = (Ben)
  Candidate Ann earned the highest total score,
  but Candidate Ben won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 5 ballots.
Ann,Ben,Cara
  3,  5,   1
  3,  5,   0
  4,  0,   3
  4,  0,   4
  0,  1,   1

[Score Distribution] (number of ballots giving each score)
      5  4  3  2  1  0  | Total   Avg
Ann   0  2  2  0  0  1  |    14   2.8
Ben   2  0  0  0  1  2  |    11   2.2
Cara  0  1  1  0  2  1  |     9   1.8

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ann           -- 14 -- First place
   Ben           -- 11 -- Second place
   Cara          --  9
 Ann and Ben advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ben           -- 3 -- First place
   Ann           -- 2
   Equal Support -- 0
 Ben wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Ben 3 (60%)  ·  Ann 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ben
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/tie_break_dead_rung/tie_break_05_scoring_five_star_vs_adversarial_lot.yaml
```

## See also

- [This set's lesson (README)](../README_tie_break_dead_rung.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [tie_break_01_scoring_five_star_breaks](tie_break_01_scoring_five_star_breaks.md) · [tie_break_02_scoring_no_fives_to_lot](tie_break_02_scoring_no_fives_to_lot.md) · [tie_break_03_runoff_no_fives_to_lot](tie_break_03_runoff_no_fives_to_lot.md) · [tie_break_04_runoff_five_star_breaks](tie_break_04_runoff_five_star_breaks.md) · [tie_break_06_scoring_dead_rung_adversarial_lot](tie_break_06_scoring_dead_rung_adversarial_lot.md) · [tie_break_07_runoff_five_star_vs_adversarial_lot](tie_break_07_runoff_five_star_vs_adversarial_lot.md) · [tie_break_08_runoff_dead_rung_adversarial_lot](tie_break_08_runoff_dead_rung_adversarial_lot.md) · [tie_break_09_five_star_tied_nonzero](tie_break_09_five_star_tied_nonzero.md)
