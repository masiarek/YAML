# Display options demo

*Generated from [`display_options_demo.yaml`](../display_options_demo.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Don

## Scenario

A single-winner race that turns on the preference matrix (finalists only) and
the Condorcet line while hiding the score-distribution table — to show how the
`options:` block controls what gets printed.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ann,Bob,Cal,Don
  3,  4,  2,  5  
  3,  4,  2,  5  
  3,  4,  2,  4  
  3,  5,  2,  3
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/display_options_demo_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Ann    |  * Bob    |    Cal    |  * Don    |
-----------------------------------------------------------------
         Ann > |    ---     |0 - 0 - 4  |4 - 0 - 0  |0 - 1 - 3  |
       * Bob > | 4 - 0 - 0  |   ---     |4 - 0 - 0  |1 - 1 - 2  |
         Cal > | 0 - 0 - 4  |0 - 0 - 4  |   ---     |0 - 0 - 4  |
       * Don > | 3 - 1 - 0  |2 - 1 - 1  |4 - 0 - 0  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Don — matches the STAR winner

[Divergence from STAR]
  STAR                   = Don
  Choose-One (Plurality) = Bob   (differs from STAR)
  RCV-IRV                = Bob   (differs from STAR)
  Approval               = Ann   (differs from STAR)
  Note: 2 of 4 ballots (50%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: _main_tabulated/display_options_demo_RCV-IRV_tabulated.txt

[Vote-splitting check]
  Choose-One first choices: Bob 2, Don 2, Ann 0, Cal 0
  Plurality winner: Bob (2, 50.0%)
  Bloc 'faction1' = Ann, Don: combined 2 (50.0%); winner Bob is OUTSIDE it.
  => No vote splitting: even combined (2), the 'faction1' bloc does not
     outpoll Bob (2).
  Bloc 'faction2' = Bob, Cal: combined 2 (50.0%); winner Bob is INSIDE it.
  => No vote splitting: the bloc's own front-runner (Bob) also wins Choose-
     One overall.

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 4 ballots.
Count × Ann,Bob,Cal,Don
    2 ×   3,  4,  2,  5
    1 ×   3,  4,  2,  4
    1 ×   3,  5,  2,  3

[Score Distribution] (number of ballots giving each score)
     5  4  3  2  1  0  | Total   Avg
Ann  0  0  4  0  0  0  |    12   3.0
Bob  1  3  0  0  0  0  |    17   4.2
Cal  0  0  0  4  0  0  |     8   2.0
Don  2  1  1  0  0  0  |    17   4.2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bob           -- 17 -- First place
   Don           -- 17 -- Second place
   Ann           -- 12
   Cal           --  8
 Bob and Don advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Don           -- 2 -- First place
   Bob           -- 1
   Equal Support -- 1
 Don wins.
   Runoff math:
     4  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Don 2 (67%)  ·  Bob 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Don
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/display_options_demo.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_DIFFERS_ARTIFACT/display_options_demo.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
