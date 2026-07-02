# Approval-style & marker ballots (0/1, blanks, abstentions) under STAR

*Generated from [`Approval_ballot.yaml`](../Approval_ballot.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** D

## Scenario

Despite the name, this is a STAR file: it shows that approval-style 0/1
scoring and every ballot marker are LEGAL on a STAR ballot. Eight ballots
exercise the whole marker set — blanks (-), a race abstention (~), an
all-zero ballot, and a max-everything 5,5,5,5 — all tabulating as documented
(markers count 0 and are reported honestly). D wins. For real Approval
counting (most approvals wins), see 04_Approval/.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
A,B,C,D
-,-,1,1
-,-,0,0
1,0,0,1
1,1,0,1
~,~,~,~
0,0,0,0
5,5,5,5
-,-,-,-
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/Approval_ballot_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |     B     |     C     |   * D     |
-----------------------------------------------------------------
         * A > |    ---     |1 - 7 - 0  |2 - 5 - 1  |0 - 7 - 1  |
           B > | 0 - 7 - 1  |   ---     |1 - 6 - 1  |0 - 6 - 2  |
           C > | 1 - 5 - 2  |1 - 6 - 1  |   ---     |0 - 6 - 2  |
         * D > | 1 - 7 - 0  |2 - 6 - 0  |2 - 6 - 0  |   ---     |

[Condorcet Winner]
  Condorcet Winner: D — matches the STAR winner

[Divergence from STAR]
  STAR                   = D
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Approval               = A   (differs from STAR)
  Note: 4 of 8 ballots (50%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: _main_tabulated/Approval_ballot_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 8 ballots. Note: 2 of 8 ballots are marked as abstentions.
A,B,C,D
-,-,1,1
-,-,0,0
1,0,0,1
1,1,0,1
~,~,~,~
0,0,0,0
5,5,5,5
-,-,-,-
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[Score Distribution] (number of ballots giving each score)
   5  4  3  2  1  0  Abs  | Total   Avg
A  1  0  0  0  2  1    4  |     7   1.8
B  1  0  0  0  1  2    4  |     6   1.5
C  1  0  0  0  1  4    2  |     6   1.0
D  1  0  0  0  3  2    2  |     8   1.3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   D             -- 8 -- First place
   A             -- 7 -- Second place
   B             -- 6
   C             -- 6
 D and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   D             -- 1 -- First place
   A             -- 0
   Equal Support -- 7
 D wins.
   Runoff math:
     8  ballots cast
   − 7  Equal Support (no preference between the two finalists)
     ─
     1  voters with a preference  (majority = 1)
           D 1 (100%)  ·  A 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 D
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/Approval_ballot.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_DIFFERS_ARTIFACT/Approval_ballot.md) — its entry in the divergence review ledger
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
