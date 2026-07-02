# Center squeeze (RCV-IRV) — minimal 27-voter case (the moderate is eliminated)

*Generated from [`center_squeeze_irv.yaml`](../center_squeeze_irv.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Left

## Scenario

The minimal center-squeeze electorate, counted by RCV-IRV: 27 voters on a
1-D spectrum. Center is every faction's acceptable second choice and beats
either pole head-to-head — but holds the FEWEST first choices (6), is
eliminated in round one, and polar Left wins. The matched file
center_squeeze_star.yaml scores the same profile 0-5 and elects Center.
See center_squeeze_voteline_1d.yaml for the spectrum picture and the
center-squeeze topic hub for the cross-method view.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:Left>Center>Right
9:Right>Center>Left
6:Center>Left>Right
```

## What the engine says

Full report from the [`_tabulated` mirror](../center_squeeze_tabulated/center_squeeze_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Center squeeze (RCV-IRV) — minimal 27-voter case (the moderate is eliminated)
 Tabulating 27 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Left              12  Hopeful
Right              9  Hopeful
Center             6  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Left              18  Elected
Right              9  Rejected
Center             0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Left
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/center_squeeze/center_squeeze_irv.yaml
```

## See also

- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README_center_squeeze.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [center_squeeze_star](center_squeeze_star.md) · [center_squeeze_voteline_1d](center_squeeze_voteline_1d.md)
