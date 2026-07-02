# Approval 101 — most approvals wins

*Generated from [`approval_101_c3_b5.yaml`](../approval_101_c3_b5.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../00_start_here/Approval_Voting) · **1 seat** · **Expected winner:** Bob

## Scenario

The simplest Approval election: each voter marks 1 (approve) or 0 for every
candidate, and the most-approved candidate wins. Five voters, three
candidates. Bob is nobody's only choice, but four of five voters approve
him — the broadest support in the field.
More Approval cases: method_comparisons/BV_Library (a real BetterVoting
approval election) and method_comparisons/black_curtain (the same five
voters counted by Approval vs STAR vs RCV-IRV).

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Ann,Bob,Cal
1,1,0   # voter 1 — approves Ann and Bob
0,1,1   # voter 2 — approves Bob and Cal
1,1,0   # voter 3 — approves Ann and Bob
0,1,0   # voter 4 — approves only Bob
1,0,1   # voter 5 — approves Ann and Cal
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/approval_101_c3_b5_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (single winner) ---
 Tabulating 5 ballots (any non-zero score = approval).
   Bob -- 4 -- Elected
   Ann -- 3
   Cal -- 2

Winner — Approval Voting (single winner)
  Bob
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/_main/approval_101_c3_b5.yaml
```

## See also

- [The Black Curtain (worked set)](../../../method_comparisons/black_curtain/README_black_curtain.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)
