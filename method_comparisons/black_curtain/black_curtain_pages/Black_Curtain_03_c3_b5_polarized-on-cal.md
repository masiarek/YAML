# The Black Curtain

*Generated from [`Black_Curtain_03_c3_b5_polarized-on-cal.yaml`](../Black_Curtain_03_c3_b5_polarized-on-cal.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cal

## Scenario

Election 3 of 4 from "The Black Curtain". Same five voters, same first
choices as before — but now the MINORITY bloc's favorite Ann is everyone's
strong pick (8 or 9 from all five voters), while 3-voter favorite Cal is
hated by the other bloc. Choose-One, RCV-IRV, and STAR still elect Cal
(runoff 3 to 2); Approval and pure Score elect Ann (approved 5×, avg 8.4).
Original 0–9 video scores mapped to 0–5: 0→0, 1→1, 4→2, 5→3, 8→4, 9→5.
See README_black_curtain.md.
Source video: https://www.youtube.com/watch?v=5_ZMruwOZgw
Notes doc: https://docs.google.com/document/d/1ntOS5PQ_kkPnaZpDeqLShGv2pz_k6Zom9LnTEdjjd4o
BetterVoting template: https://bettervoting.com/p9gwc3/vote
This folder on GitHub: https://github.com/masiarek/YAML/tree/master/method_comparisons/black_curtain

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ann,Bob,Cal
4,0,5   # voter 1 — video 0-9: A=8 B=0 C=9
4,0,5   # voter 2 — video 0-9: A=8 B=0 C=9
4,0,5   # voter 3 — video 0-9: A=8 B=0 C=9
5,1,0   # voter 4 — video 0-9: A=9 B=1 C=0
5,1,0   # voter 5 — video 0-9: A=9 B=1 C=0
```

## What the engine says

Full report from the [`_tabulated` mirror](../black_curtain_tabulated/Black_Curtain_03_c3_b5_polarized-on-cal_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ann    |    Bob    |  * Cal    |
-----------------------------------------------------
       * Ann > |    ---     |5 - 0 - 0  |2 - 0 - 3  |
         Bob > | 0 - 0 - 5  |   ---     |2 - 0 - 3  |
       * Cal > | 3 - 0 - 2  |3 - 0 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Cal — matches the STAR winner

[Divergence from STAR]
  STAR     = Cal
  Approval = Ann   (differs from STAR)

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Ann)
 - Runoff Round Winner   = (Cal)
  Candidate Ann earned the highest total score,
  but Candidate Cal won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 5 ballots.
Count × Ann,Bob,Cal
    3 ×   4,  0,  5
    2 ×   5,  1,  0

[Score Distribution] (number of ballots giving each score)
     5  4  3  2  1  0  | Total   Avg
Ann  2  3  0  0  0  0  |    22   4.4
Bob  0  0  0  0  2  3  |     2   0.4
Cal  3  0  0  0  0  2  |    15   3.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ann           -- 22 -- First place
   Cal           -- 15 -- Second place
   Bob           --  2
 Ann and Cal advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cal           -- 3 -- First place
   Ann           -- 2
   Equal Support -- 0
 Cal wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Cal 3 (60%)  ·  Ann 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cal
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/black_curtain/Black_Curtain_03_c3_b5_polarized-on-cal.yaml
```

## See also

- [This set's lesson (README)](../README_black_curtain.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/Black_Curtain_03_c3_b5_polarized-on-cal.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [The Black Curtain (worked set)](../README_black_curtain.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Black_Curtain_01_c3_b5_hidden-consensus](Black_Curtain_01_c3_b5_hidden-consensus.md) · [Black_Curtain_01a_c3_b5_approval](Black_Curtain_01a_c3_b5_approval.md) · [Black_Curtain_02_c3_b5_near-clones](Black_Curtain_02_c3_b5_near-clones.md) · [Black_Curtain_04_c4_b5_four-candidates](Black_Curtain_04_c4_b5_four-candidates.md)
