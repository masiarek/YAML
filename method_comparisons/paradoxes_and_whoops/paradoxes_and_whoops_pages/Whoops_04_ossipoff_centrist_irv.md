# Whoops 04 — IRV buries the centrist (Ossipoff 303-voter)

*Generated from [`Whoops_04_ossipoff_centrist_irv.yaml`](../Whoops_04_ossipoff_centrist_irv.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** D

## Scenario

Mike Ossipoff's 1-D example (via rangevoting.org). Candidate C is the centrist:
C is the PLURALITY winner (100 first-choices, most of any) AND the Condorcet winner
(beats every rival ~2:1). Yet RCV-IRV ELIMINATES C in round 3 and elects D. Sincere
ballots; a realistic 'one-dimensional politics' taper. Ranked-ballot case (no scores
invented). Approval/STAR/Condorcet/Ranked Robin would all elect C. Level 301.
Source: https://www.rangevoting.org/rangeVirv.html (section 12).
Lesson: Whoops_04_ossipoff_centrist_irv.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
50:A>B>C>D>E
51:B>A>C>D>E
100:C>D>B>E>A
53:D>E>C>B>A
49:E>D>C>B>A
```

## What the engine says

Full report from the [`_tabulated` mirror](../paradoxes_and_whoops_tabulated/Whoops_04_ossipoff_centrist_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
 Tabulating 303 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
C                100  Hopeful
D                 53  Hopeful
B                 51  Hopeful
A                 50  Hopeful
E                 49  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
D                102  Hopeful
C                100  Hopeful
B                 51  Hopeful
A                 50  Rejected
E                  0  Rejected

ROUND 3
Candidate      Votes  Status
-----------  -------  --------
D                102  Hopeful
B                101  Hopeful
C                100  Rejected
A                  0  Rejected
E                  0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
D                202  Elected
B                101  Rejected
C                  0  Rejected
A                  0  Rejected
E                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  D
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/paradoxes_and_whoops/Whoops_04_ossipoff_centrist_irv.yaml
```

## See also

- [This set's lesson (README)](../README_paradoxes_and_whoops.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Whoops_01_tennessee_three_winners](Whoops_01_tennessee_three_winners.md) · [Whoops_02_star_misses_condorcet](Whoops_02_star_misses_condorcet.md) · [Whoops_03_condorcet_cycle_rps](Whoops_03_condorcet_cycle_rps.md) · [Whoops_05_brams_many_pathologies_irv](Whoops_05_brams_many_pathologies_irv.md)
