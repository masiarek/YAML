# Bloc STAR Voting: 2-Seat Committee Election

*Generated from [`01_c4_b2_bloc-star-2-seats.yaml`](../01_c4_b2_bloc-star-2-seats.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Don, Cal

## Scenario

A basic multi-winner example with 4 candidates and 2 seats. It demonstrates how
Bloc STAR fills each seat sequentially through a dedicated scoring round and
automatic runoff.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ann,Bob,Cal,Don
1,  0,  4,  5
1,  2,  4,  5
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/01_c4_b2_bloc-star-2-seats_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Ann    |    Bob    |  * Cal    |  * Don    |
-----------------------------------------------------------------
         Ann > |    ---     |1 - 0 - 1  |0 - 0 - 2  |0 - 0 - 2  |
         Bob > | 1 - 0 - 1  |   ---     |0 - 0 - 2  |0 - 0 - 2  |
       * Cal > | 2 - 0 - 0  |2 - 0 - 0  |   ---     |0 - 0 - 2  |
       * Don > | 2 - 0 - 0  |2 - 0 - 0  |2 - 0 - 0  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Don — matches the STAR winner

[Divergence from STAR]
  STAR     = Don
  Approval = Cal   (differs from STAR)

--- Bloc STAR Voting Method (2 winners) ---
[Bloc STAR]
 Tabulating 2 ballots.
Ann,Bob,Cal,Don
  1,  0,  4,  5
  1,  2,  4,  5

[Score Distribution] (number of ballots giving each score)
     5  4  3  2  1  0  | Total   Avg
Ann  0  0  0  0  2  0  |     2   1.0
Bob  0  0  0  1  0  1  |     2   1.0
Cal  0  2  0  0  0  0  |     8   4.0
Don  2  0  0  0  0  0  |    10   5.0
 Want to fill 2 seats.

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Don           -- 10 -- First place
   Cal           --  8 -- Second place
   Ann           --  2
   Bob           --  2
 Don and Cal advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Don           -- 2 -- First place
   Cal           -- 0
   Equal Support -- 0
 Don wins.
   Runoff math:
     2  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           Don 2 (100%)  ·  Cal 0 (0%)

──────────────────────────────────────────────────
[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cal           -- 8 -- First place
   Ann           -- 2 -- Tied for second place
   Bob           -- 2 -- Tied for second place
 Cal advances, but there's a two-way tie for second.

[Bloc STAR: Round 2: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Ann           -- 1 -- Tied for second place
   Bob           -- 1 -- Tied for second place
   Equal Support -- 0
 There's still a two-way tie for second.

[Bloc STAR: Round 2: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Ann           -- 0 -- Tied for second place
   Bob           -- 0 -- Tied for second place
 There's still a two-way tie for second.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['Ann', 'Bob', 'Cal', 'Don']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ann', 'Bob']
  Resolved: ['Ann'] (selected by lot-number priority).

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cal           -- 2 -- First place
   Ann           -- 0
   Equal Support -- 0
 Cal wins.
   Runoff math:
     2  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           Cal 2 (100%)  ·  Ann 0 (0%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Don
 Cal
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/_main/01_c4_b2_bloc-star-2-seats.yaml
```

## See also

- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)
