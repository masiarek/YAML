# No Condorcet winner and Ranked Robin

*Generated from [`03_real_record0_c6_b5.yaml`](../03_real_record0_c6_b5.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** B

**Official tie-break (lot) order:** A > B > C > D > E > F — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

STAR elects B; so does Ranked Robin. But NO candidate beats all five rivals head-to-head, so there is no Condorcet winner (the Condorcet column in the sweep CSV is blank). 
Ranked Robin still produces a winner —  whoever wins the most matchups — and that is B.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C,D,E,F
3,3,0,2,4,3
3,2,3,2,4,1
4,1,2,1,0,4
2,4,5,4,1,2
0,5,0,5,2,3
```

## What the engine says

Full report from the [`_tabulated` mirror](../condorcet_vs_ranked_robin_tabulated/03_real_record0_c6_b5_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 5 ballots (score ballots).

Ballots:
   columns = A, B, C, D, E, F      (scores  →  the ranking Ranked Robin reads;  "=" = tied)
     1 × 3, 3, 0, 2, 4, 3   →   E > A=B=F > D > C
     1 × 3, 2, 3, 2, 4, 1   →   E > A=C > B=D > F
     1 × 4, 1, 2, 1, 0, 4   →   A=F > C > B=D > E
     1 × 2, 4, 5, 4, 1, 2   →   C > B=D > A=F > E
     1 × 0, 5, 0, 5, 2, 3   →   B=D > F > E > A=C

Round-Robin — every pair, head-to-head (For – Against):
   A  ties  B   2 – 2
   A  beats C   2 – 1
   A  beats D   3 – 2
   E  beats A   3 – 2
   A  ties  F   1 – 1
   C  beats B   3 – 2
   B  beats D   1 – 0
   B  beats E   3 – 2
   B  beats F   3 – 1
   C  beats D   3 – 2
   E  beats C   3 – 2
   F  beats C   3 – 2
   D  beats E   3 – 2
   D  beats F   3 – 2
   F  beats E   3 – 2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |     A     |    B     |    C     |    D     |    E     |    F     |
--------------------------------------------------------------------------
  A > |    ---    |2 - 1 - 2 |2 - 2 - 1 |3 - 0 - 2 |2 - 0 - 3 |1 - 3 - 1 |
  B > | 2 - 1 - 2 |   ---    |2 - 0 - 3 |1 - 4 - 0 |3 - 0 - 2 |3 - 1 - 1 |
  C > | 1 - 2 - 2 |3 - 0 - 2 |   ---    |3 - 0 - 2 |2 - 0 - 3 |2 - 0 - 3 |
  D > | 2 - 0 - 3 |0 - 4 - 1 |2 - 0 - 3 |   ---    |3 - 0 - 2 |3 - 0 - 2 |
  E > | 3 - 0 - 2 |2 - 0 - 3 |3 - 0 - 2 |2 - 0 - 3 |   ---    |2 - 0 - 3 |
  F > | 1 - 3 - 1 |1 - 1 - 3 |3 - 0 - 2 |2 - 0 - 3 |3 - 0 - 2 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  B          3–1–1       3.5      +3  D, E, F
    2  A          2–1–2         3      +1  C, D
    3  C          2–3–0         2      -1  B, D
    4  D          2–3–0         2      -1  E, F
    5  E          2–3–0         2      -1  A, C
    6  F          2–2–1       2.5      -1  C, E

Winner — Ranked Robin (RCV-RR): B
   the most head-to-head wins (3).
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/condorcet_vs_ranked_robin/03_real_record0_c6_b5.yaml
```

## See also

- [This set's lesson (README)](../README_condorcet_vs_ranked_robin.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01_condorcet_winner](01_condorcet_winner.md) · [02_cycle_no_condorcet](02_cycle_no_condorcet.md)
