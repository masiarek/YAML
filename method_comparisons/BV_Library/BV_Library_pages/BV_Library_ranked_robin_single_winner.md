# BV parity — Ranked Robin: Condorcet winner (equal ranks allowed)

*Generated from [`BV_Library_ranked_robin_single_winner.yaml`](../BV_Library_ranked_robin_single_winner.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Alice

## Scenario

Ported from BetterVoting's tabulator unit tests (RankedRobin.test.ts :: "Single winner test").
BetterVoting supplies rank ballots (1 = best) including EQUAL ranks and an abstention.
Converted here to score ballots for the LH engine (higher score = more preferred,
equal scores = equal rank, blank = unranked): rank 1->4, 2->3, 3->2, 4->1, unranked->0.
One original out-of-bounds mark (rank -1 for Dave) becomes a blank. Alice wins every
head-to-head (Condorcet winner); Copeland scores match BetterVoting (Alice 3, Bob 2,
Carol 1, Dave 0).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Alice,Bob,Carol,Dave
4,3,2,0
4,3,2,1
4,3,2,1
4,4,3,2
4,4,3,2
3,4,2,1
3,4,2,1
3,2,4,1
3,2,1,4
-,-,-,-
3,2,1,-
```

## What the engine says

Full report from the [`_tabulated` mirror](../BV_Library_tabulated/BV_Library_ranked_robin_single_winner_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 11 ballots (score ballots).

Ballots:
   columns = Alice, Bob, Carol, Dave      (scores  →  the ranking Ranked Robin reads;  "=" = tied)
     1 × 4, 3, 2, 0   →   Alice > Bob > Carol > Dave
     2 × 4, 3, 2, 1   →   Alice > Bob > Carol > Dave
     2 × 4, 4, 3, 2   →   Alice=Bob > Carol > Dave
     2 × 3, 4, 2, 1   →   Bob > Alice > Carol > Dave
     1 × 3, 2, 4, 1   →   Carol > Alice > Bob > Dave
     1 × 3, 2, 1, 4   →   Dave > Alice > Bob > Carol
     1 × 0, 0, 0, 0   →   Alice=Bob=Carol=Dave
     1 × 3, 2, 1, 0   →   Alice > Bob > Carol > Dave

Round-Robin — every pair, head-to-head (For – Against):
   Alice  beats Bob     6 – 2
   Alice  beats Carol   9 – 1
   Alice  beats Dave    9 – 1
   Bob    beats Carol   9 – 1
   Bob    beats Dave    9 – 1
   Carol  beats Dave    9 – 1

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |   Alice   |   Bob    |  Carol   |  Dave    |
--------------------------------------------------------
  Alice > |    ---    |6 - 3 - 2 |9 - 1 - 1 |9 - 1 - 1 |
    Bob > | 2 - 3 - 6 |   ---    |9 - 1 - 1 |9 - 1 - 1 |
  Carol > | 1 - 1 - 9 |1 - 1 - 9 |   ---    |9 - 1 - 1 |
   Dave > | 1 - 1 - 9 |1 - 1 - 9 |1 - 1 - 9 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Alice      3–0–0         3     +20  Bob, Carol, Dave
    2  Bob        2–1–0         2     +12  Carol, Dave
    3  Carol      1–2–0         1      -8  Dave
    4  Dave       0–3–0         0     -24  —

Winner — Ranked Robin (RCV-RR): Alice
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/BV_Library_ranked_robin_single_winner.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_plurality_single_winner](BV_Library_plurality_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
