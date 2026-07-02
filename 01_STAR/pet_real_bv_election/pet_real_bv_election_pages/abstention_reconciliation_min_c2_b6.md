# Abstention vs Equal Support — the minimal reconciliation case

*Generated from [`abstention_reconciliation_min_c2_b6.yaml`](../abstention_reconciliation_min_c2_b6.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Dog

## Scenario

The smallest election that reproduces the LH-engine ↔ BetterVoting count
reconciliation (the full version is the 461-ballot pet race in this folder).
Two candidates, six ballots, one of each "no-preference" kind so every
denominator is visible at a glance:

  Dog,Cat
  5,0   Dog  — a clear preference (decides the runoff)
  4,0   Dog  — a clear preference (decides the runoff)
  0,5   Cat  — a clear preference (decides the runoff)
  5,5   Equal Support — a CAST ballot that rates both finalists the same
  0,0   all-zero — a CAST ballot that supports neither (an explicit zero)
  -,-   blank — a true ABSTENTION: no score recorded for anyone

How the LH engine counts it:
  • Ballots cast: 6 (all six are counted).
  • Abstention note: 1 — only the blank "-,-" ballot. The all-zero "0,0" is
    a cast ballot ("I rate you both zero"), NOT an abstention.
  • Automatic Runoff: Dog 2, Cat 1, Equal Support 3. The three no-preference
    ballots (5,5 + 0,0 + blank) all score Dog == Cat, so all three land in
    Equal Support and are set aside from the runoff PERCENTAGE.
  • Voters with a preference (the runoff denominator): 3 → Dog 2 (67%) wins.

The teaching point: "no preference" is one runoff bucket (Equal Support), but
it is reached three different ways — an explicit equal score (5,5), an explicit
all-zero (0,0), and a blank/abstention (-,-). Only the last is an *abstention*.
Tabulators differ in how they file these (see the README and the GitHub
reconciliation note), which is the entire 461-vs-455 gap in the pet race.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Dog,Cat
5,0   # clear preference: Dog
4,0   # clear preference: Dog
0,5   # clear preference: Cat
5,5   # Equal Support: cast ballot, rates both finalists the same
0,0   # all-zero: cast ballot, supports neither (NOT an abstention)
-,-   # blank: a true abstention (no score for anyone)
```

## What the engine says

Full report from the [`_tabulated` mirror](../pet_real_bv_election_tabulated/abstention_reconciliation_min_c2_b6_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Dog    |  * Cat    |
-----------------------------------------
       * Dog > |    ---     |2 - 3 - 1  |
       * Cat > | 1 - 3 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Dog — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 6 ballots. Note: 1 of 6 ballots is marked as an abstention.
Dog,Cat
  5,  0
  4,  0
  0,  5
  5,  5
  0,  0
  -,  -
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[Score Distribution] (number of ballots giving each score)
     5  4  3  2  1  0  Abs  | Total   Avg
Dog  2  1  0  0  0  2    1  |    14   2.8
Cat  2  0  0  0  0  3    1  |    10   2.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dog           -- 14 -- First place
   Cat           -- 10 -- Second place
 Dog and Cat advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Dog           -- 2 -- First place
   Cat           -- 1
   Equal Support -- 3
 Dog wins.
   Runoff math:
     6  ballots cast
   − 3  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Dog 2 (67%)  ·  Cat 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Dog
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/pet_real_bv_election/abstention_reconciliation_min_c2_b6.yaml
```

## See also

- [This set's lesson (README)](../README_pet_real_bv_election.md) — the hand-written teaching context for every case in this folder
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [best_pet_c7_b461](best_pet_c7_b461.md) · [flat_scores_abstention_c3_b8](flat_scores_abstention_c3_b8.md) · [small_abstention_c2_b5](small_abstention_c2_b5.md)
