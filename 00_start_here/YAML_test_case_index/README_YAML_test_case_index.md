# YAML test-case index — by voting method

**Auto-generated — do not edit by hand.** Run `python scripts/build_yaml_index.py` to refresh (a pytest fails if it's stale).

Election YAMLs live in many folders (the test harnesses glob specific ones, so they're indexed *in place*, not moved). Each file declares a `voting_method` and `num_winners`; this catalog groups them so you can browse by method. Excludes `_tabulated` mirrors, raw `_demo_dropbox` drops, generated copies, and deliberately-malformed negative fixtures.

Titles come from each file's **`election_title`** field (the convention — add one to make a file's title explicit & searchable). Where that's missing, a file's first `#` comment line is shown *in italics* as a fallback.

**111 election files** (105 single-winner, 6 multi-winner) across 9 method(s).

| Method | Files |
|--------|------:|
| STAR | 91 |
| RCV-IRV (Hare) | 10 |
| Ranked Robin (RCV-RR / Copeland) | 3 |
| STV (proportional RCV) | 1 |
| Bloc STAR | 1 |
| STAR-PR (Sequential Selection) | 2 |
| Reweighted Range | 1 |
| Allocated Score (STAR-PR) | 1 |
| RR | 1 |

## STAR  (91)

| File | Folder | Winners | Title / expected |
|------|--------|:------:|------------------|
| [`01a_c2_b1_two-candidates.yaml`](../../01_Single_winner/01a_c2_b1_two-candidates.yaml) | `01_Single_winner/` | 1 | The simplest possible STAR Voting example → _Chocolate_ |
| [`01a_c2_b2_two-candidates.yaml`](../../01_Single_winner/01a_c2_b2_two-candidates.yaml) | `01_Single_winner/` | 1 | Same as before - but this time two ballots → _Chocolate_ |
| [`01b_c2_b2_two-candidates.yaml`](../../01_Single_winner/01b_c2_b2_two-candidates.yaml) | `01_Single_winner/` | 1 | Again, very similar - this time second ballot is 5 and 0 → _Choco_ |
| [`01c_c2_b3_two-candidates.yaml`](../../01_Single_winner/01c_c2_b3_two-candidates.yaml) | `01_Single_winner/` | 1 | Equal support example ("I like both flavors") → _Choco_ |
| [`02a_c3_b1_three-candidates.yaml`](../../01_Single_winner/02a_c3_b1_three-candidates.yaml) | `01_Single_winner/` | 1 | Three candidates, one ballot - single-winner STAR → _Choco_ |
| [`02b_c3_b2_three-candidates.yaml`](../../01_Single_winner/02b_c3_b2_three-candidates.yaml) | `01_Single_winner/` | 1 | Three candidates, two ballots - single-winner STAR → _Vanilla_ |
| [`03a_c3_b3_style-bullet-vote.yaml`](../../01_Single_winner/03a_c3_b3_style-bullet-vote.yaml) | `01_Single_winner/` | 1 | Voting styles — a valid STAR bullet vote (3 candidates) → _Vanilla_ |
| [`03b_c3_b3_1_style-protest-vote.yaml`](../../01_Single_winner/03b_c3_b3_1_style-protest-vote.yaml) | `01_Single_winner/` | 1 | Voting styles — low-score ballots → _Almond_ |
| [`03b_c3_b3_2_expand_style-protest-vote.yaml`](../../01_Single_winner/03b_c3_b3_2_expand_style-protest-vote.yaml) | `01_Single_winner/` | 1 | Voting styles — low-score ballots (continued) → _Almond_ |
| [`04b_c4_b3_display-options-all.yaml`](../../01_Single_winner/04b_c4_b3_display-options-all.yaml) | `01_Single_winner/` | 1 | All options demo → _Strawberry_ |
| [`05a_c5_b3_unanimous-ballots.yaml`](../../01_Single_winner/05a_c5_b3_unanimous-ballots.yaml) | `01_Single_winner/` | 1 | Unanimous ballots (five candidates) → _Andre_ |
| [`06a_c9_b3_large-field-equal-support.yaml`](../../01_Single_winner/06a_c9_b3_large-field-equal-support.yaml) | `01_Single_winner/` | 1 | Large field (9 candidates) — STAR scales, and Equal Support decides → _Carmen_ |
| [`06b_c9_runoff-overturns-leader.yaml`](../../01_Single_winner/06b_c9_runoff-overturns-leader.yaml) | `01_Single_winner/` | 1 | Large field (9 candidates) — the runoff OVERTURNS the score leader → _Carmen_ |
| [`09_c4_b100_tennessee-capital.yaml`](../../01_Single_winner/09_c4_b100_tennessee-capital.yaml) | `01_Single_winner/` | 1 | Tennessee Capital — classic STAR example → _Nashville_ |
| [`Approval_ballot.yaml`](../../01_Single_winner/Approval_ballot.yaml) | `01_Single_winner/` | 1 | Approval-style & marker ballots (0/1, blanks, abstentions) under STAR |
| [`abstentions.yaml`](../../01_Single_winner/abstentions.yaml) | `01_Single_winner/` | 1 | Abstentions — blank and abstaining ballots in STAR |
| [`center_squeeze_star.yaml`](../../01_Single_winner/center_squeeze_star.yaml) | `01_Single_winner/` | 1 | Center squeeze — STAR elects the consensus (Center) → _Center_ |
| [`center_squeeze_voteline_1d.yaml`](../../01_Single_winner/center_squeeze_voteline_1d.yaml) | `01_Single_winner/` | 1 | Center squeeze — the voteline 1D spectrum (Red / Green / Yellow) → _Green_ |
| [`count_simplicity_star_vs_irv.yaml`](../../01_Single_winner/count_simplicity_star_vs_irv.yaml) | `01_Single_winner/` | 1 | Same winner, very different counts — STAR adds, IRV eliminates → _Carmen_ |
| [`display_options_demo.yaml`](../../01_Single_winner/display_options_demo.yaml) | `01_Single_winner/` | 1 | Display options demo → _Don_ |
| [`equal_support_runoff_demo.yaml`](../../01_Single_winner/equal_support_runoff_demo.yaml) | `01_Single_winner/` | 1 | Equal Support — counted in both rounds, neutral only in the tie-break → _A_ |
| [`monotonicity_star_after.yaml`](../../01_Single_winner/monotonicity_star_after.yaml) | `01_Single_winner/` | 1 | Monotonicity — STAR counterpart (AFTER — X still wins) → _X_ |
| [`monotonicity_star_before.yaml`](../../01_Single_winner/monotonicity_star_before.yaml) | `01_Single_winner/` | 1 | Monotonicity — STAR counterpart (BEFORE — X wins) → _X_ |
| [`quorum_demo_c3_b6.yaml`](../../01_Single_winner/quorum_demo_c3_b6.yaml) | `01_Single_winner/` | 1 | Quorum — an abstention still counts toward turnout → _Anna_ |
| [`quorum_fail_demo_c3_b6.yaml`](../../01_Single_winner/quorum_fail_demo_c3_b6.yaml) | `01_Single_winner/` | 1 | Quorum FAILS — won the count, but not elected |
| [`three_winners_cw_score_runoff.yaml`](../../01_Single_winner/three_winners_cw_score_runoff.yaml) | `01_Single_winner/` | 1 | Three notions of "winner" disagree — Condorcet, Score, and Runoff → _Bob_ |
| [`vote_splitting.yaml`](../../01_Single_winner/vote_splitting.yaml) | `01_Single_winner/` | 1 | Vote splitting — two chocolates split the majority → _DarkChoco_ |
| [`vote_splitting2.yaml`](../../01_Single_winner/vote_splitting2.yaml) | `01_Single_winner/` | 1 | Vote splitting — two chocolates split the majority → _DarkChoco_ |
| [`vote_splitting3.yaml`](../../01_Single_winner/vote_splitting3.yaml) | `01_Single_winner/` | 1 | Vote splitting — two chocolates split the majority → _DarkChoco_ |
| [`vote_splitting_scenario1_spoiler.yaml`](../../01_Single_winner/vote_splitting_scenario1_spoiler.yaml) | `01_Single_winner/` | 1 | Vote splitting — scenario 1 of 3 — the spoiler strikes → _DarkChoco_ |
| [`vote_splitting_scenario2_bloc_leads.yaml`](../../01_Single_winner/vote_splitting_scenario2_bloc_leads.yaml) | `01_Single_winner/` | 1 | Vote splitting — scenario 2 of 3 — no spoiler (bloc leader wins anyway) → _DarkChoco_ |
| [`vote_splitting_scenario3_outsider_wins.yaml`](../../01_Single_winner/vote_splitting_scenario3_outsider_wins.yaml) | `01_Single_winner/` | 1 | Vote splitting — scenario 3 of 3 — no spoiler (the outsider truly wins) → _Vanilla_ |
| [`Flat_scores_ties_01_baseline_clean.yaml`](../../01_Single_winner/Flat_scores_ties/Flat_scores_ties_01_baseline_clean.yaml) | `01_Single_winner/Flat_scores_ties/` | 1 | Flat scores 01 — clean top two (works-fine baseline) → _Apple_ |
| [`Flat_scores_ties_02_runoff_tie_2cand.yaml`](../../01_Single_winner/Flat_scores_ties/Flat_scores_ties_02_runoff_tie_2cand.yaml) | `01_Single_winner/Flat_scores_ties/` | 1 | Flat scores 02 — runoff tie, two candidates (everyone equal) → _Almond_ |
| [`Flat_scores_ties_03_runoff_tie_split.yaml`](../../01_Single_winner/Flat_scores_ties/Flat_scores_ties_03_runoff_tie_split.yaml) | `01_Single_winner/Flat_scores_ties/` | 1 | Flat scores 03 — runoff tie, an even 1-1 split → _Athens_ |
| [`Flat_scores_ties_04_scoring_tie_2way.yaml`](../../01_Single_winner/Flat_scores_ties/Flat_scores_ties_04_scoring_tie_2way.yaml) | `01_Single_winner/Flat_scores_ties/` | 1 | Flat scores 04 — scoring-round tie for the 2nd finalist slot (2-way) → _Aral_ |
| [`Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml`](../../01_Single_winner/Flat_scores_ties/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml) | `01_Single_winner/Flat_scores_ties/` | 1 | Flat scores 05 — scoring-round 3-way tie (BV555 / → _A_ |
| [`Flat_scores_ties_06_scoring_tie_4way.yaml`](../../01_Single_winner/Flat_scores_ties/Flat_scores_ties_06_scoring_tie_4way.yaml) | `01_Single_winner/Flat_scores_ties/` | 1 | Flat scores 06 — scoring-round 4-way tie (ties at every step) → _Ava_ |
| [`Flat_scores_ties_07_fully_flat.yaml`](../../01_Single_winner/Flat_scores_ties/Flat_scores_ties_07_fully_flat.yaml) | `01_Single_winner/Flat_scores_ties/` | 1 | Flat scores 07 — fully flat ballots (the maximal tie + abstention trap) → _Ararat_ |
| [`Flat_scores_ties_08_all_flat_zero_count.yaml`](../../01_Single_winner/Flat_scores_ties/Flat_scores_ties_08_all_flat_zero_count.yaml) | `01_Single_winner/Flat_scores_ties/` | 1 | Flat scores 08 — every ballot flat (BetterVoting counts 0) → _Anchovy_ |
| [`Whoops_01_tennessee_three_winners.yaml`](../../01_Single_winner/paradoxes_and_whoops/Whoops_01_tennessee_three_winners.yaml) | `01_Single_winner/paradoxes_and_whoops/` | 1 | Whoops 01 — same ballots, three methods, three winners (Tennessee) → _Nashville_ |
| [`Whoops_02_star_misses_condorcet.yaml`](../../01_Single_winner/paradoxes_and_whoops/Whoops_02_star_misses_condorcet.yaml) | `01_Single_winner/paradoxes_and_whoops/` | 1 | Whoops 02 — STAR misses the Condorcet winner (STAR's own whoops) → _Ada_ |
| [`Whoops_03_condorcet_cycle_rps.yaml`](../../01_Single_winner/paradoxes_and_whoops/Whoops_03_condorcet_cycle_rps.yaml) | `01_Single_winner/paradoxes_and_whoops/` | 1 | Whoops 03 — a Condorcet cycle (rock-paper-scissors, no winner) → _Rock_ |
| [`abstention_reconciliation_min_c2_b6.yaml`](../../01_Single_winner/pet_real_bv_election/abstention_reconciliation_min_c2_b6.yaml) | `01_Single_winner/pet_real_bv_election/` | 1 | Abstention vs Equal Support — the minimal reconciliation case → _Dog_ |
| [`best_pet_c7_b461.yaml`](../../01_Single_winner/pet_real_bv_election/best_pet_c7_b461.yaml) | `01_Single_winner/pet_real_bv_election/` | 1 | What Makes the Best Pet? → _Dog_ |
| [`flat_scores_abstention_c3_b8.yaml`](../../01_Single_winner/pet_real_bv_election/flat_scores_abstention_c3_b8.yaml) | `01_Single_winner/pet_real_bv_election/` | 1 | BV Abstentions and flat scores (Apple/Banana/Cherry, 8 ballots) → _Banana_ |
| [`small_abstention_c2_b5.yaml`](../../01_Single_winner/pet_real_bv_election/small_abstention_c2_b5.yaml) | `01_Single_winner/pet_real_bv_election/` | 1 | Equal Support vs Abstention — minimal STAR test (A/B, 5 ballots) → _A_ |
| [`01a_c3_b3_more-stars-fewer-voters.yaml`](../../01_Single_winner/runoff_overturns_leader/01a_c3_b3_more-stars-fewer-voters.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | More stars, fewer voters — the runoff overturns the score leader → _Brownie_ |
| [`01b_c3_b9_overturn-holds-at-scale.yaml`](../../01_Single_winner/runoff_overturns_leader/01b_c3_b9_overturn-holds-at-scale.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | The same overturn at scale — 67% to 33% → _Brownie_ |
| [`02_c5_b5_leader-overturned.yaml`](../../01_Single_winner/runoff_overturns_leader/02_c5_b5_leader-overturned.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | Five candidates — the score leader is overturned in the runoff → _Boston_ |
| [`03_c7_b3_ice-cream-live.yaml`](../../01_Single_winner/runoff_overturns_leader/03_c7_b3_ice-cream-live.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | Ice Cream — Flavor of the Year (the real recorded race) → _ChocoAlm_ |
| [`04_c4_b3_runoff-confirms-leader.yaml`](../../01_Single_winner/runoff_overturns_leader/04_c4_b3_runoff-confirms-leader.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | The control case — here the runoff CONFIRMS the score leader → _Blue_ |
| [`05_c3_b5_low-scores-bv1265.yaml`](../../01_Single_winner/runoff_overturns_leader/05_c3_b5_low-scores-bv1265.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | Low scores, switched winner — the popover example (BetterVoting BV1265) → _A_ |
| [`Runoff_01_confirms_leader_r2pvc9.yaml`](../../01_Single_winner/runoff_overturns_leader/Runoff_01_confirms_leader_r2pvc9.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | Runoff 01 — Runoff confirms the leader (control) → _Aspen_ |
| [`Runoff_02_atom_reversal_yx9447.yaml`](../../01_Single_winner/runoff_overturns_leader/Runoff_02_atom_reversal_yx9447.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | Runoff 02 — the atom (smallest runoff reversal) → _Boston_ |
| [`Runoff_03_enthusiasts_vs_majority_rkgtpk.yaml`](../../01_Single_winner/runoff_overturns_leader/Runoff_03_enthusiasts_vs_majority_rkgtpk.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | Runoff 03 — two enthusiasts vs the majority → _Eden_ |
| [`Runoff_04_reversal_at_scale_bfjqmg.yaml`](../../01_Single_winner/runoff_overturns_leader/Runoff_04_reversal_at_scale_bfjqmg.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | Runoff 04 — the reversal holds at scale (67/33) → _Olive_ |
| [`Runoff_05_reversal_with_equal_support_xgkw3w.yaml`](../../01_Single_winner/runoff_overturns_leader/Runoff_05_reversal_with_equal_support_xgkw3w.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | Runoff 05 — reversal with Equal Support → _Sage_ |
| [`Runoff_06_confirms_at_scale_d664xw.yaml`](../../01_Single_winner/runoff_overturns_leader/Runoff_06_confirms_at_scale_d664xw.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | Runoff 06 — the runoff confirms the leader at scale (control) → _Wren_ |
| [`Runoff_07_flat_ballot_bv_bug_tf73v9.yaml`](../../01_Single_winner/runoff_overturns_leader/Runoff_07_flat_ballot_bv_bug_tf73v9.yaml) | `01_Single_winner/runoff_overturns_leader/` | 1 | Runoff 07 (WIP) — flat ballot exposes the BV abstention bug → _Blair_ |
| [`star_combined.yaml`](../../01_Single_winner/summability_demo/star_combined.yaml) | `01_Single_winner/summability_demo/` | 1 | Summability demo — STAR combined A+B (Oak; precinct subtotals add up) → _Oak_ |
| [`star_district_A.yaml`](../../01_Single_winner/summability_demo/star_district_A.yaml) | `01_Single_winner/summability_demo/` | 1 | Summability demo — STAR district A (Maple wins outright) → _Maple_ |
| [`star_district_B.yaml`](../../01_Single_winner/summability_demo/star_district_B.yaml) | `01_Single_winner/summability_demo/` | 1 | Summability demo — STAR district B (Oak wins — a runoff reversal) → _Oak_ |
| [`options_examples.yaml`](../../STARVote_LH_tabulation_engine/options_examples.yaml) | `STARVote_LH_tabulation_engine/` | 1 | Display-options reference — every reporting toggle (STAR) |
| [`Flat_scores_ties_01_baseline_clean.yaml`](../../YAML_library/1_positive/Flat_scores_ties_01_baseline_clean.yaml) | `YAML_library/1_positive/` | 1 | Flat scores 01 — clean top two (works-fine baseline) → _Apple_ |
| [`Flat_scores_ties_02_runoff_tie_2cand.yaml`](../../YAML_library/1_positive/Flat_scores_ties_02_runoff_tie_2cand.yaml) | `YAML_library/1_positive/` | 1 | Flat scores 02 — runoff tie, two candidates (everyone equal) → _Almond_ |
| [`Flat_scores_ties_03_runoff_tie_split.yaml`](../../YAML_library/1_positive/Flat_scores_ties_03_runoff_tie_split.yaml) | `YAML_library/1_positive/` | 1 | Flat scores 03 — runoff tie, an even 1-1 split → _Athens_ |
| [`Flat_scores_ties_04_scoring_tie_2way.yaml`](../../YAML_library/1_positive/Flat_scores_ties_04_scoring_tie_2way.yaml) | `YAML_library/1_positive/` | 1 | Flat scores 04 — scoring-round tie for the 2nd finalist slot (2-way) → _Aral_ |
| [`Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml`](../../YAML_library/1_positive/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml) | `YAML_library/1_positive/` | 1 | Flat scores 05 — scoring-round 3-way tie (BV555 / → _A_ |
| [`Flat_scores_ties_06_scoring_tie_4way.yaml`](../../YAML_library/1_positive/Flat_scores_ties_06_scoring_tie_4way.yaml) | `YAML_library/1_positive/` | 1 | Flat scores 06 — scoring-round 4-way tie (ties at every step) → _Ava_ |
| [`Flat_scores_ties_07_fully_flat.yaml`](../../YAML_library/1_positive/Flat_scores_ties_07_fully_flat.yaml) | `YAML_library/1_positive/` | 1 | Flat scores 07 — fully flat ballots (the maximal tie + abstention trap) → _Ararat_ |
| [`Flat_scores_ties_08_all_flat_zero_count.yaml`](../../YAML_library/1_positive/Flat_scores_ties_08_all_flat_zero_count.yaml) | `YAML_library/1_positive/` | 1 | Flat scores 08 — every ballot flat (BetterVoting counts 0) → _Anchovy_ |
| [`Runoff_01_confirms_leader_r2pvc9.yaml`](../../YAML_library/1_positive/Runoff_01_confirms_leader_r2pvc9.yaml) | `YAML_library/1_positive/` | 1 | Runoff 01 — Runoff confirms the leader (control) → _Aspen_ |
| [`Runoff_02_atom_reversal_yx9447.yaml`](../../YAML_library/1_positive/Runoff_02_atom_reversal_yx9447.yaml) | `YAML_library/1_positive/` | 1 | Runoff 02 — the atom (smallest runoff reversal) → _Boston_ |
| [`Runoff_03_enthusiasts_vs_majority_rkgtpk.yaml`](../../YAML_library/1_positive/Runoff_03_enthusiasts_vs_majority_rkgtpk.yaml) | `YAML_library/1_positive/` | 1 | Runoff 03 — two enthusiasts vs the majority → _Eden_ |
| [`Runoff_04_reversal_at_scale_bfjqmg.yaml`](../../YAML_library/1_positive/Runoff_04_reversal_at_scale_bfjqmg.yaml) | `YAML_library/1_positive/` | 1 | Runoff 04 — the reversal holds at scale (67/33) → _Olive_ |
| [`Runoff_05_reversal_with_equal_support_xgkw3w.yaml`](../../YAML_library/1_positive/Runoff_05_reversal_with_equal_support_xgkw3w.yaml) | `YAML_library/1_positive/` | 1 | Runoff 05 — reversal with Equal Support → _Sage_ |
| [`Runoff_06_confirms_at_scale_d664xw.yaml`](../../YAML_library/1_positive/Runoff_06_confirms_at_scale_d664xw.yaml) | `YAML_library/1_positive/` | 1 | Runoff 06 — the runoff confirms the leader at scale (control) → _Wren_ |
| [`Runoff_07_flat_ballot_bv_bug_tf73v9.yaml`](../../YAML_library/1_positive/Runoff_07_flat_ballot_bv_bug_tf73v9.yaml) | `YAML_library/1_positive/` | 1 | Runoff 07 (WIP) — flat ballot exposes the BV abstention bug → _Blair_ |
| [`Whoops_01_tennessee_three_winners.yaml`](../../YAML_library/1_positive/Whoops_01_tennessee_three_winners.yaml) | `YAML_library/1_positive/` | 1 | Whoops 01 — same ballots, three methods, three winners (Tennessee) → _Nashville_ |
| [`Whoops_02_star_misses_condorcet.yaml`](../../YAML_library/1_positive/Whoops_02_star_misses_condorcet.yaml) | `YAML_library/1_positive/` | 1 | Whoops 02 — STAR misses the Condorcet winner (STAR's own whoops) → _Ada_ |
| [`Whoops_03_condorcet_cycle_rps.yaml`](../../YAML_library/1_positive/Whoops_03_condorcet_cycle_rps.yaml) | `YAML_library/1_positive/` | 1 | Whoops 03 — a Condorcet cycle (rock-paper-scissors, no winner) → _Rock_ |
| [`center_squeeze_voteline_1d.yaml`](../../YAML_library/1_positive/center_squeeze_voteline_1d.yaml) | `YAML_library/1_positive/` | 1 | Center squeeze — the voteline 1D spectrum (Red / Green / Yellow) → _Green_ |
| [`example_tennessee.yaml`](../../pref_voting_tabulation_engine/example_tennessee.yaml) | `pref_voting_tabulation_engine/` | 1 | Tennessee capital — cross-check demo (same ballots, three winners) |
| [`00_plurality_vs_majority.yaml`](../../split_voting/00_plurality_vs_majority.yaml) | `split_voting/` | 1 | Plurality vs Majority — most votes isn't more than half → _Blake_ |
| [`01_political_left_split.yaml`](../../split_voting/01_political_left_split.yaml) | `split_voting/` | 1 | Spoiler — a split coalition hands the seat to the minority → _Labour_ |
| [`02_icecream_chocolate_split.yaml`](../../split_voting/02_icecream_chocolate_split.yaml) | `split_voting/` | 1 | Spoiler — chocolate's majority splits, vanilla steals the win → _MilkChoco_ |
| [`03_lunch_veggie_vs_meat.yaml`](../../split_voting/03_lunch_veggie_vs_meat.yaml) | `split_voting/` | 1 | Spoiler — the veggie majority splits, the burger wins the lunch vote → _VeggieCurry_ |
| [`04_star_wars_vote_split.yaml`](../../split_voting/04_star_wars_vote_split.yaml) | `split_voting/` | 1 | The Voting Dilemma — Skywalker & Leia split the Rebel vote → _Leia_ |
| [`05a_residual_split_bullet-voting.yaml`](../../split_voting/05a_residual_split_bullet-voting.yaml) | `split_voting/` | 1 | STAR's residual split — a coalition bullet-votes itself apart → _Cara_ |
| [`05b_residual_split_expressive-fix.yaml`](../../split_voting/05b_residual_split_expressive-fix.yaml) | `split_voting/` | 1 | The cure — score your ally, and STAR's split disappears → _Ada_ |

## RCV-IRV (Hare)  (10)

| File | Folder | Winners | Title / expected |
|------|--------|:------:|------------------|
| [`RCV_ballot_example.yaml`](../../01_Single_winner/RCV_ballot_example.yaml) | `01_Single_winner/` | 1 | RCV-IRV — a basic ranked-ballot example (3 candidates) |
| [`center_squeeze_irv.yaml`](../../01_Single_winner/center_squeeze_irv.yaml) | `01_Single_winner/` | 1 | Center squeeze (RCV-IRV) — minimal 27-voter case (the moderate is eliminated) |
| [`monotonicity_irv_after.yaml`](../../01_Single_winner/monotonicity_irv_after.yaml) | `01_Single_winner/` | 1 | Non-monotonicity (RCV-IRV) — part 2: raising X makes X lose |
| [`monotonicity_irv_before.yaml`](../../01_Single_winner/monotonicity_irv_before.yaml) | `01_Single_winner/` | 1 | Non-monotonicity (RCV-IRV) — part 1: baseline, X wins |
| [`Whoops_04_ossipoff_centrist_irv.yaml`](../../01_Single_winner/paradoxes_and_whoops/Whoops_04_ossipoff_centrist_irv.yaml) | `01_Single_winner/paradoxes_and_whoops/` | 1 | Whoops 04 — IRV buries the centrist (Ossipoff 303-voter) |
| [`Whoops_05_brams_many_pathologies_irv.yaml`](../../01_Single_winner/paradoxes_and_whoops/Whoops_05_brams_many_pathologies_irv.yaml) | `01_Single_winner/paradoxes_and_whoops/` | 1 | Whoops 05 — many IRV pathologies in one election (Brams) |
| [`irv_combined.yaml`](../../01_Single_winner/summability_demo/irv_combined.yaml) | `01_Single_winner/summability_demo/` | 1 | Summability demo — RCV-IRV combined A+B (B eliminated; not summable) |
| [`irv_district_A.yaml`](../../01_Single_winner/summability_demo/irv_district_A.yaml) | `01_Single_winner/summability_demo/` | 1 | Summability demo — RCV-IRV district A (B wins) |
| [`irv_district_B.yaml`](../../01_Single_winner/summability_demo/irv_district_B.yaml) | `01_Single_winner/summability_demo/` | 1 | Summability demo — RCV-IRV district B (B wins) |
| [`example_tennessee.yaml`](../../RCV_IRV_tabulation_engine/example_tennessee.yaml) | `RCV_IRV_tabulation_engine/` | 1 | Tennessee capital — RCV-IRV engine demo |

## Ranked Robin (RCV-RR / Copeland)  (3)

| File | Folder | Winners | Title / expected |
|------|--------|:------:|------------------|
| [`ranked_robin_consensus_center.yaml`](../../01_Single_winner/ranked_robin_consensus_center.yaml) | `01_Single_winner/` | 1 | Ranked Robin (RCV-RR) — the consensus center wins the round-robin |
| [`01_condorcet_winner.yaml`](../../01_Single_winner/condorcet_vs_ranked_robin/01_condorcet_winner.yaml) | `01_Single_winner/condorcet_vs_ranked_robin/` | 1 | Condorcet winner exists — Ranked Robin elects it |
| [`02_cycle_no_condorcet.yaml`](../../01_Single_winner/condorcet_vs_ranked_robin/02_cycle_no_condorcet.yaml) | `01_Single_winner/condorcet_vs_ranked_robin/` | 1 | No Condorcet winner (a cycle) — Ranked Robin still elects one |

## STV (proportional RCV)  (1)

| File | Folder | Winners | Title / expected |
|------|--------|:------:|------------------|
| [`03a_stv_3seats.yaml`](../../02_Multi_winner/03a_stv_3seats.yaml) | `02_Multi_winner/` | 3 | STV — 3 seats, 7 candidates (proportional RCV) |

## Bloc STAR  (1)

| File | Folder | Winners | Title / expected |
|------|--------|:------:|------------------|
| [`01_c4_b2_bloc-star-2-seats.yaml`](../../02_Multi_winner/01_c4_b2_bloc-star-2-seats.yaml) | `02_Multi_winner/` | 2 | Bloc STAR Voting: 2-Seat Committee Election → _Don, Cal_ |

## STAR-PR (Sequential Selection)  (2)

| File | Folder | Winners | Title / expected |
|------|--------|:------:|------------------|
| [`02b_c5_b63_proportional-sss.yaml`](../../02_Multi_winner/02b_c5_b63_proportional-sss.yaml) | `02_Multi_winner/` | 3 | Proportional STAR — Sequentially Spent Score → _Alice, Ben, Dan_ |
| [`03b_star_pr_3seats.yaml`](../../02_Multi_winner/03b_star_pr_3seats.yaml) | `02_Multi_winner/` | 3 | Proportional STAR — same 3-seat electorate as the STV demo |

## Reweighted Range  (1)

| File | Folder | Winners | Title / expected |
|------|--------|:------:|------------------|
| [`02c_c5_b63_proportional-rrv.yaml`](../../02_Multi_winner/02c_c5_b63_proportional-rrv.yaml) | `02_Multi_winner/` | 3 | Proportional — Reweighted Range Voting → _Alice, Ben, Dan_ |

## Allocated Score (STAR-PR)  (1)

| File | Folder | Winners | Title / expected |
|------|--------|:------:|------------------|
| [`02a_c5_b63_proportional-allocated-score.yaml`](../../02_Multi_winner/02a_c5_b63_proportional-allocated-score.yaml) | `02_Multi_winner/` | 3 | Proportional STAR — Allocated Score Voting → _Alice, Ben, Dan_ |

## RR  (1)

| File | Folder | Winners | Title / expected |
|------|--------|:------:|------------------|
| [`03_real_record0_c6_b5.yaml`](../../01_Single_winner/condorcet_vs_ranked_robin/03_real_record0_c6_b5.yaml) | `01_Single_winner/condorcet_vs_ranked_robin/` | 1 | No Condorcet winner and Ranked Robin |
