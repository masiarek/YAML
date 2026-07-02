# BV parity — Ranked Robin: Copeland tie broken by tiebreak order

*Generated from [`BV_Library_ranked_robin_ties.yaml`](../BV_Library_ranked_robin_ties.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Alice

## Scenario

Ported from BetterVoting's tabulator unit tests (RankedRobin.test.ts :: "Ties").
Alice and Bob split the head-to-head (3-3), tying on Copeland score; BetterVoting
breaks the tie by tiebreak (lot) order and elects Alice. Rank ballots (1 = best)
converted to scores for the LH engine (rank 1->4, 2->3, 3->2, 4->1).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alice,Bob,Carol,Dave
4,3,2,1
4,3,2,1
4,3,2,1
3,4,2,1
3,4,2,1
3,4,2,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../BV_Library_tabulated/BV_Library_ranked_robin_ties_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 6 ballots (score ballots).

Ballots:
   columns = Alice, Bob, Carol, Dave      (scores  →  the ranking Ranked Robin reads;  "=" = tied)
     3 × 4, 3, 2, 1   →   Alice > Bob > Carol > Dave
     3 × 3, 4, 2, 1   →   Bob > Alice > Carol > Dave

Round-Robin — every pair, head-to-head (For – Against):
   Alice  ties  Bob     3 – 3
   Alice  beats Carol   6 – 0
   Alice  beats Dave    6 – 0
   Bob    beats Carol   6 – 0
   Bob    beats Dave    6 – 0
   Carol  beats Dave    6 – 0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |   Alice   |   Bob    |  Carol   |  Dave    |
--------------------------------------------------------
  Alice > |    ---    |3 - 0 - 3 |6 - 0 - 0 |6 - 0 - 0 |
    Bob > | 3 - 0 - 3 |   ---    |6 - 0 - 0 |6 - 0 - 0 |
  Carol > | 0 - 0 - 6 |0 - 0 - 6 |   ---    |6 - 0 - 0 |
   Dave > | 0 - 0 - 6 |0 - 0 - 6 |0 - 0 - 6 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Alice      2–0–1       2.5     +12  Carol, Dave
    2  Bob        2–0–1       2.5     +12  Carol, Dave
    3  Carol      1–2–0         1      -6  Dave
    4  Dave       0–3–0         0     -18  —

Winner — Ranked Robin (RCV-RR): Alice
   *** 2 candidates tie on wins (Alice, Bob) — a Condorcet cycle. Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 00_start_here/RCV_Ranked_Robin/cycle_resolution.md.)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/BV_Library_ranked_robin_ties.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../split_voting/README_split_voting.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_plurality_single_winner](BV_Library_plurality_single_winner.md) · [BV_Library_ranked_robin_single_winner](BV_Library_ranked_robin_single_winner.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
