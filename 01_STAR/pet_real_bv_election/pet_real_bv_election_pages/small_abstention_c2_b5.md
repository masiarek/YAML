# Equal Support vs Abstention — minimal STAR test (A/B, 5 ballots)

*Generated from [`small_abstention_c2_b5.yaml`](../small_abstention_c2_b5.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

A REAL BetterVoting election (BV id 3w6v4b), captured 2026-06-28, run as the
smallest case that proves how BetterVoting and the LH engine differ on a
"no-preference" ballot. Frozen raw export:
small_abstention_c2_b5_bv_export.json. Full write-up:
small_case_abstention_lesson.md.
How to read this report (LH): 00_start_here/STAR_reporting/reporting_LH/

Five ballots, two candidates:

  A,B
  0,5   prefers B
  4,0   prefers A
  5,5   Equal Support — loves BOTH equally (a cast vote, NOT an abstention)
  5,0   prefers A
  -,-   blank — the one true abstention

BetterVoting reports: nAbstentions = 2, nTallyVotes = 3 — i.e. it files the
5,5 ballot AND the blank under "abstention." The LH engine counts all 5 cast
ballots, treats only the blank as an abstention, and puts the 5,5 in Equal
Support (counted in the score round, neutral in the runoff). Same winner (A);
the single-ballot difference is the 5,5.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
A, B
0, 5
4, 0
5, 5
5, 0
-, -
```

## What the engine says

Full report from the [`_tabulated` mirror](../pet_real_bv_election_tabulated/small_abstention_c2_b5_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |   * B     |
-----------------------------------------
         * A > |    ---     |2 - 2 - 1  |
         * B > | 1 - 2 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: A — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 5 ballots. Note: 1 of 5 ballots is marked as an abstention.
A,B
0,5
4,0
5,5
5,0
-,-
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[Score Distribution] (number of ballots giving each score)
   5  4  3  2  1  0  Abs  | Total   Avg
A  2  1  0  0  0  1    1  |    14   3.5
B  2  0  0  0  0  2    1  |    10   2.5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 14 -- First place
   B             -- 10 -- Second place
 A and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 2 -- First place
   B             -- 1
   Equal Support -- 2
 A wins.
   Runoff math:
     5  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           A 2 (67%)  ·  B 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/pet_real_bv_election/small_abstention_c2_b5.yaml
```

## See also

- [This set's lesson (README)](../README_pet_real_bv_election.md) — the hand-written teaching context for every case in this folder
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [abstention_reconciliation_min_c2_b6](abstention_reconciliation_min_c2_b6.md) · [best_pet_c7_b461](best_pet_c7_b461.md) · [flat_scores_abstention_c3_b8](flat_scores_abstention_c3_b8.md)
