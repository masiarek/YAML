# Tennessee Capital — classic STAR example

*Generated from [`09_c4_b100_tennessee-capital.yaml`](../09_c4_b100_tennessee-capital.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Nashville

## Scenario

The textbook Tennessee example. Memphis has the plurality (42%) but is too
far from everyone else; Nashville, the central consensus choice, wins both the
score round and the runoff. Shows why STAR rewards broad support over a large
but isolated faction.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Memphis,Nashville,Chattanooga,Knoxville
42: 5, 4, 3, 2
26: 2, 5, 4, 3
15: 2, 3, 5, 4
17: 2, 3, 4, 5
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/09_c4_b100_tennessee-capital_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |      Memphis    |  * Nashville   | * Chattanooga  |    Knoxville   |
------------------------------------------------------------------------------------------
          Memphis > |       ---       | 42 -  0 - 58   | 42 -  0 - 58   | 42 -  0 - 58   |
      * Nashville > |  58 -  0 - 42   |      ---       | 68 -  0 - 32   | 68 -  0 - 32   |
    * Chattanooga > |  58 -  0 - 42   | 32 -  0 - 68   |      ---       | 83 -  0 - 17   |
        Knoxville > |  58 -  0 - 42   | 32 -  0 - 68   | 17 -  0 - 83   |      ---       |

[Condorcet Winner]
  Condorcet Winner: Nashville — matches the STAR winner

[Divergence from STAR]
  STAR                   = Nashville
  Choose-One (Plurality) = Memphis   (differs from STAR)
  RCV-IRV                = Knoxville   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: _main_tabulated/09_c4_b100_tennessee-capital_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Memphis,Nashville,Chattanooga,Knoxville
   42 ×       5,        4,          3,        2
   26 ×       2,        5,          4,        3
   17 ×       2,        3,          4,        5
   15 ×       2,        3,          5,        4

[Score Distribution] (number of ballots giving each score)
              5   4   3   2   1   0  | Total   Avg
Memphis      42   0   0  58   0   0  |   326   3.3
Nashville    26  42  32   0   0   0  |   394   3.9
Chattanooga  15  43  42   0   0   0  |   373   3.7
Knoxville    17  15  26  42   0   0  |   307   3.1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Nashville     -- 394 -- First place
   Chattanooga   -- 373 -- Second place
   Memphis       -- 326
   Knoxville     -- 307
 Nashville and Chattanooga advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Nashville     -- 68 -- First place
   Chattanooga   -- 32
   Equal Support --  0
 Nashville wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Nashville 68 (68%)  ·  Chattanooga 32 (32%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Nashville
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/09_c4_b100_tennessee-capital.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/09_c4_b100_tennessee-capital.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
