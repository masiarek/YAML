# STV — 3 seats, 7 candidates (proportional RCV)

*Generated from [`03a_stv_3seats.yaml`](../03a_stv_3seats.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STV (proportional, ranked ballots)](../../../00_start_here/proportional_representation) · **3 seats** · **Expected winners:** Housing, Schools, SmallBiz

## Scenario

STV — the proportional method for RANKED ballots — fills 3 seats from a
100-voter, 7-candidate field: a 58-voter community-services wing and a
42-voter business wing. Proportionality gives the majority two seats
(Housing, Schools) and the minority one (SmallBiz), where Bloc voting would
hand the majority a 3-0 sweep. Score-ballot counterpart: 03_STAR_PR/
(same electorate logic under sss / allocated / rrv).

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
29:Housing>Schools>Parks>Transit>SmallBiz>BigBiz>TaxCuts
15:Schools>Housing>Parks>Transit>SmallBiz>BigBiz>TaxCuts
13:Parks>Schools>Housing>Transit>SmallBiz>BigBiz>TaxCuts
1:Transit>Schools>Housing>Parks>SmallBiz>BigBiz>TaxCuts
22:SmallBiz>BigBiz>TaxCuts>Housing>Schools>Parks>Transit
17:BigBiz>SmallBiz>TaxCuts>Housing>Schools>Parks>Transit
3:TaxCuts>SmallBiz>BigBiz>Housing>Schools>Parks>Transit
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/03a_stv_3seats_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- STV / Single Transferable Vote (multi-winner — 3 seats) ---
  STV — 3 seats, 7 candidates (proportional RCV)
 Tabulating 100 ballots (ranked ballots).
 3 seats; Droop quota = 26 (26.0% of 100).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Housing           29  Elected
SmallBiz          22  Hopeful
BigBiz            17  Hopeful
Schools           15  Hopeful
Parks             13  Hopeful
TaxCuts            3  Hopeful
Transit            1  Hopeful

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
Housing        25.00  Elected
SmallBiz       22.00  Hopeful
Schools        19.00  Hopeful
BigBiz         17.00  Hopeful
Parks          13.00  Rejected
TaxCuts         3.00  Rejected
Transit         1.00  Rejected

ROUND 3
Candidate      Votes  Status
-----------  -------  --------
Housing        25.00  Elected
Schools        33.00  Elected
SmallBiz       25.00  Hopeful
BigBiz         17.00  Hopeful
Parks           0.00  Rejected
TaxCuts         0.00  Rejected
Transit         0.00  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Housing        25.00  Elected
Schools        25.00  Elected
SmallBiz       33.00  Elected
BigBiz         17.00  Rejected
Parks           0.00  Rejected
TaxCuts         0.00  Rejected
Transit         0.00  Rejected


Winner(s) — STV / Single Transferable Vote (multi-winner — 3 seats)
  Housing
  Schools
  SmallBiz
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py other_methods/_main/03a_stv_3seats.yaml
```

## See also

- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [RCV_ballot_example](RCV_ballot_example.md)
