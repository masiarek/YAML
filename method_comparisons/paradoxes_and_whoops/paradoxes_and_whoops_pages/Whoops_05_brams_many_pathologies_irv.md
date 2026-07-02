# Whoops 05 — many IRV pathologies in one election (Brams)

*Generated from [`Whoops_05_brams_many_pathologies_irv.yaml`](../Whoops_05_brams_many_pathologies_irv.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** B

## Scenario

Steven Brams' example (Notices of the AMS, 1982; via rangevoting.org). IRV elects B,
but G is the Condorcet winner (beats B 14-7, beats everyone). The same election shows
a no-show paradox, a truncation incentive, favorite-betrayal, and non-monotonicity —
several IRV pathologies at once. Sincere, academically sourced, ranked ballots.
Approval/STAR/Condorcet/Ranked Robin would elect G. Level 301.
Source: https://www.rangevoting.org/rangeVirv.html (section 12); Brams 1982.
Lesson: Whoops_05_brams_many_pathologies_irv.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
7:B>G>N>F
6:G>B>N>F
5:N>G>B>F
3:F>N>G>B
```

## What the engine says

Full report from the [`_tabulated` mirror](../paradoxes_and_whoops_tabulated/Whoops_05_brams_many_pathologies_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
 Tabulating 21 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
B                  7  Hopeful
G                  6  Hopeful
N                  5  Hopeful
F                  3  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
N                  8  Hopeful
B                  7  Hopeful
G                  6  Rejected
F                  0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
B                 13  Elected
N                  8  Rejected
G                  0  Rejected
F                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  B
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/paradoxes_and_whoops/Whoops_05_brams_many_pathologies_irv.yaml
```

## See also

- [This set's lesson (README)](../README_paradoxes_and_whoops.md) — the hand-written teaching context for every case in this folder
- [Monotonicity (topic hub)](../../../00_start_here/topics/monotonicity/README_monotonicity.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Whoops_01_tennessee_three_winners](Whoops_01_tennessee_three_winners.md) · [Whoops_02_star_misses_condorcet](Whoops_02_star_misses_condorcet.md) · [Whoops_03_condorcet_cycle_rps](Whoops_03_condorcet_cycle_rps.md) · [Whoops_04_ossipoff_centrist_irv](Whoops_04_ossipoff_centrist_irv.md)
