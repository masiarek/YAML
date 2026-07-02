# No Condorcet winner (a cycle) — Ranked Robin still elects one

*Generated from [`02_cycle_no_condorcet.yaml`](../02_cycle_no_condorcet.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

7 ranked ballots, 3 candidates, in a rock-paper-scissors cycle: Ada beats Ben, Ben beats Cara, Cara beats Ada. NO candidate beats both others, so there is NO Condorcet winner. Ranked Robin still produces a winner: everyone has a 1-1 record, so it breaks the tie by total margin — Ada (strongest margins) wins. This is where Ranked Robin and "the Condorcet winner" PART WAYS: the Condorcet winner is undefined, Ranked Robin is not.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Ada>Ben>Cara
Ada>Ben>Cara
Ada>Ben>Cara
Ben>Cara>Ada
Ben>Cara>Ada
Cara>Ada>Ben
Cara>Ada>Ben
```

## What the engine says

Full report from the [`_tabulated` mirror](../condorcet_vs_ranked_robin_tabulated/02_cycle_no_condorcet_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 7 ballots (ranked ballots).

Ballots:
     3 × Ada > Ben > Cara
     2 × Ben > Cara > Ada
     2 × Cara > Ada > Ben

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    5 – 2
   Cara  beats Ada    4 – 3
   Ben   beats Cara   5 – 2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |
--------------------------------------------
   Ada > |    ---    |5 - 0 - 2 |3 - 0 - 4 |
   Ben > | 2 - 0 - 5 |   ---    |5 - 0 - 2 |
  Cara > | 4 - 0 - 3 |2 - 0 - 5 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        1–1–0         1      +2  Ben
    2  Ben        1–1–0         1      +0  Cara
    3  Cara       1–1–0         1      -2  Ada

Winner — Ranked Robin (RCV-RR): Ada
   *** 3 candidates tie on wins (Ada, Ben, Cara) — a Condorcet cycle. Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 00_start_here/RCV_Ranked_Robin/cycle_resolution.md.)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/condorcet_vs_ranked_robin/02_cycle_no_condorcet.yaml
```

## See also

- [This set's lesson (README)](../README_condorcet_vs_ranked_robin.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01_condorcet_winner](01_condorcet_winner.md) · [03_real_record0_c6_b5](03_real_record0_c6_b5.md)
