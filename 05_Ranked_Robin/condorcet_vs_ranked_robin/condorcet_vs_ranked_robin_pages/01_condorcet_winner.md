# Condorcet winner exists — Ranked Robin elects it

*Generated from [`01_condorcet_winner.yaml`](../01_condorcet_winner.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

5 ranked ballots, 3 candidates. Ada beats both Ben and Cara head-to-head, so Ada is the Condorcet winner — and Ranked Robin (most pairwise wins) elects Ada. When a Condorcet winner exists, Ranked Robin and "the Condorcet winner" are the SAME answer.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Ada>Ben>Cara
Ada>Ben>Cara
Ada>Ben>Cara
Ben>Ada>Cara
Ben>Ada>Cara
```

## What the engine says

Full report from the [`_tabulated` mirror](../condorcet_vs_ranked_robin_tabulated/01_condorcet_winner_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 5 ballots (ranked ballots).

Ballots:
     3 × Ada > Ben > Cara
     2 × Ben > Ada > Cara

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    3 – 2
   Ada   beats Cara   5 – 0
   Ben   beats Cara   5 – 0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |
--------------------------------------------
   Ada > |    ---    |3 - 0 - 2 |5 - 0 - 0 |
   Ben > | 2 - 0 - 3 |   ---    |5 - 0 - 0 |
  Cara > | 0 - 0 - 5 |0 - 0 - 5 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        2–0–0         2      +6  Ben, Cara
    2  Ben        1–1–0         1      +4  Cara
    3  Cara       0–2–0         0     -10  —

Winner — Ranked Robin (RCV-RR): Ada
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/condorcet_vs_ranked_robin/01_condorcet_winner.yaml
```

## See also

- [This set's lesson (README)](../README_condorcet_vs_ranked_robin.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [02_cycle_no_condorcet](02_cycle_no_condorcet.md) · [03_real_record0_c6_b5](03_real_record0_c6_b5.md)
