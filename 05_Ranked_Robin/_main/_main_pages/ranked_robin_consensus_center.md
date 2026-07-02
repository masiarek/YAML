# Ranked Robin (RCV-RR) — the consensus center wins the round-robin

*Generated from [`ranked_robin_consensus_center.yaml`](../ranked_robin_consensus_center.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ben

## Scenario

13 ranked ballots, 4 candidates. Ben beats every rival head-to-head (the Condorcet / Copeland winner) and wins Ranked Robin 3-0 — even though Ada and Dan each have more first-choices. Tabulate with pref_voting_tabulation_engine/ranked_robin_report.py.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
4:Ada>Ben>Cara>Dan
4:Dan>Cara>Ben>Ada
3:Ben>Cara>Ada>Dan
2:Cara>Ben>Dan>Ada
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/ranked_robin_consensus_center_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 13 ballots (ranked ballots).

Ballots:
     4 × Ada > Ben > Cara > Dan
     4 × Dan > Cara > Ben > Ada
     3 × Ben > Cara > Ada > Dan
     2 × Cara > Ben > Dan > Ada

Round-Robin — every pair, head-to-head (For – Against):
   Ben   beats Ada    9 – 4
   Cara  beats Ada    9 – 4
   Ada   beats Dan    7 – 6
   Ben   beats Cara   7 – 6
   Ben   beats Dan    9 – 4
   Cara  beats Dan    9 – 4

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |   Dan    |
-------------------------------------------------------
   Ada > |    ---    |4 - 0 - 9 |4 - 0 - 9 |7 - 0 - 6 |
   Ben > | 9 - 0 - 4 |   ---    |7 - 0 - 6 |9 - 0 - 4 |
  Cara > | 9 - 0 - 4 |6 - 0 - 7 |   ---    |9 - 0 - 4 |
   Dan > | 6 - 0 - 7 |4 - 0 - 9 |4 - 0 - 9 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ben        3–0–0         3     +11  Cara, Ada, Dan
    2  Cara       2–1–0         2      +9  Ada, Dan
    3  Ada        1–2–0         1      -9  Dan
    4  Dan        0–3–0         0     -11  —

Winner — Ranked Robin (RCV-RR): Ben
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/_main/ranked_robin_consensus_center.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)
