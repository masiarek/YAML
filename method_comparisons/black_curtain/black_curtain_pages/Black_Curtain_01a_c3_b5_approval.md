# The Black Curtain

*Generated from [`Black_Curtain_01a_c3_b5_approval.yaml`](../Black_Curtain_01a_c3_b5_approval.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../00_start_here/Approval_Voting) · **1 seat** · **Expected winner:** Bob

## Scenario

The SAME five voters as Black_Curtain_01_c3_b5_hidden-consensus.yaml, counted as
an Approval election. In the video, "approve" = any 0–9 score of 5 or more
(on this repo's 0–5 scale: 3 or more). Bob — every voter's strong second —
is approved by all 5 voters and wins; Cal (the Choose-One / RCV-IRV / STAR
winner) gets only 3 approvals. Same ballots, different question, different
winner. See README_black_curtain.md.
Source video: https://www.youtube.com/watch?v=5_ZMruwOZgw
Notes doc: https://docs.google.com/document/d/1ntOS5PQ_kkPnaZpDeqLShGv2pz_k6Zom9LnTEdjjd4o
BetterVoting template: https://bettervoting.com/p9gwc3/vote
This folder on GitHub: https://github.com/masiarek/YAML/tree/master/method_comparisons/black_curtain

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Ann,Bob,Cal
0,1,1   # voter 1 — approves Bob (8) and Cal (9)
0,1,1   # voter 2 — approves Bob (8) and Cal (9)
0,1,1   # voter 3 — approves Bob (8) and Cal (9)
1,1,0   # voter 4 — approves Ann (9) and Bob (8)
1,1,0   # voter 5 — approves Ann (9) and Bob (8)
```

## What the engine says

Full report from the [`_tabulated` mirror](../black_curtain_tabulated/Black_Curtain_01a_c3_b5_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (single winner) ---
 Tabulating 5 ballots (any non-zero score = approval).
   Bob -- 5 -- Elected
   Cal -- 3
   Ann -- 2

Winner — Approval Voting (single winner)
  Bob
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/black_curtain/Black_Curtain_01a_c3_b5_approval.yaml
```

## See also

- [This set's lesson (README)](../README_black_curtain.md) — the hand-written teaching context for every case in this folder
- [The Black Curtain (worked set)](../README_black_curtain.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Black_Curtain_01_c3_b5_hidden-consensus](Black_Curtain_01_c3_b5_hidden-consensus.md) · [Black_Curtain_02_c3_b5_near-clones](Black_Curtain_02_c3_b5_near-clones.md) · [Black_Curtain_03_c3_b5_polarized-on-cal](Black_Curtain_03_c3_b5_polarized-on-cal.md) · [Black_Curtain_04_c4_b5_four-candidates](Black_Curtain_04_c4_b5_four-candidates.md)
