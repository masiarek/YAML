# Cross-method divergence review

_Generated 2026-07-02 09:23 by `scripts/build_divergence_index.py` — do not hand-edit; rebuild._

Re-tabulates every **curated single-winner STAR** election under RCV-IRV, Ranked Robin (RCV-RR / Copeland) and Approval, and flags where they disagree with STAR. Only hand-built library elections are scanned (never random ballots), and the base rate is reported, so the collection stays honest rather than cherry-picked.

## Base rate

- Scanned **83** single-winner STAR elections (skipped 18 non-eligible files: multi-winner / Approval / RR / RCV / ranked-ballot / unparseable).
- **32** (39%) diverge from STAR under at least one method; **51** agree across the board.

| Bucket | Count |
|---|---:|
| IRV_OUTLIER_RR_WITH_STAR | 5 |
| STAR_OUTLIER_RR_WITH_IRV | 1 |
| IRV_DIFFERS_ARTIFACT | 2 |
| CYCLE_OR_THREE_WAY | 4 |
| APPROVAL_OR_MINOR | 20 |

## Score→rank conversion (recorded both ways)

- **STRICT** — equal non-zero scores broken by lot/priority order (`score_ballot_to_ranking`). Feeds RCV-IRV and the `RR_strict` / `Condorcet_strict` columns.
- **WEAK** — equal scores stay equal (no preference). Feeds `RR_weak` / `Condorcet_weak` (the natural reading of a score ballot).
- **`rr_conv_sensitive`** = RR_weak ≠ RR_strict → the RR result depends on how ties are read; treat with care.
- RCV-IRV can't represent equal ranks, so there is no weak IRV. `tie_ballots` (ballots with tied non-zero scores) and `irv_fragile` (winner flips under reversed priority) flag a tie-break artifact.

## Cases by bucket

Review order is the teaching value of each bucket. Each case links to a full teaching `.md` (ballots + every method's report + a plain-English explanation) under `cases/`. Listing is **deduped** to one entry per distinct election (32 cases; identical library copies merged).

### IRV_OUTLIER_RR_WITH_STAR — 5

_RCV-IRV is the outlier — Ranked Robin AGREES with STAR (strongest teachable: the center-squeeze story, two methods against one)_

- **[09_c4_b100_tennessee-capital](cases/IRV_OUTLIER_RR_WITH_STAR/09_c4_b100_tennessee-capital.md)** — `01_Single_winner/09_c4_b100_tennessee-capital.yaml` (4c/100b)  
    STAR=**Nashville** · IRV=Knoxville · RR=Nashville · Approval=Nashville · Condorcet=Nashville
- **[center_squeeze_star](cases/IRV_OUTLIER_RR_WITH_STAR/center_squeeze_star.md)** — `01_Single_winner/center_squeeze_star.yaml` (3c/27b)  
    STAR=**Center** · IRV=Left · RR=Center · Approval=Left · Condorcet=Center
- **[center_squeeze_voteline_1d](cases/IRV_OUTLIER_RR_WITH_STAR/center_squeeze_voteline_1d.md)** — `01_Single_winner/center_squeeze_voteline_1d.yaml` (3c/998b)  
    STAR=**Green** · IRV=Yellow · RR=Green · Approval=Green · Condorcet=Green
- **[Whoops_01_tennessee_three_winners](cases/IRV_OUTLIER_RR_WITH_STAR/Whoops_01_tennessee_three_winners.md)** — `01_Single_winner/paradoxes_and_whoops/Whoops_01_tennessee_three_winners.yaml` (4c/100b)  
    STAR=**Nashville** · IRV=Knoxville · RR=Nashville · Approval=Nashville · Condorcet=Nashville
- **[04_star_wars_vote_split](cases/IRV_OUTLIER_RR_WITH_STAR/04_star_wars_vote_split.md)** — `split_voting/04_star_wars_vote_split.yaml` (3c/100b)  
    STAR=**Leia** · IRV=Skywalker · RR=Leia · Approval=Skywalker · Condorcet=Leia

### STAR_OUTLIER_RR_WITH_IRV — 1

_STAR is the outlier — Ranked Robin sides with RCV-IRV (show it anyway, for evenhandedness: STAR isn't always the Condorcet pick)_

- **[three_winners_cw_score_runoff](cases/STAR_OUTLIER_RR_WITH_IRV/three_winners_cw_score_runoff.md)** — `01_Single_winner/three_winners_cw_score_runoff.yaml` (3c/5b)  
    STAR=**Bob** · IRV=Ann · RR=Ann · Approval=Bob · Condorcet=Ann

### IRV_DIFFERS_ARTIFACT — 2

_RCV-IRV differs but it's a score->rank tie-break artifact (tied ballots and/or flips under reversed priority) — log, do NOT bark on IRV_

- **[Approval_ballot](cases/IRV_DIFFERS_ARTIFACT/Approval_ballot.md)** — `01_Single_winner/Approval_ballot.yaml` (4c/8b)  
    STAR=**D** · IRV=A · RR=D · Approval=A · Condorcet=D  
    _flags: 4 tied-score ballot(s); IRV flips on reversed priority; RR conv-sensitive (weak=D, strict=A)_
- **[display_options_demo](cases/IRV_DIFFERS_ARTIFACT/display_options_demo.md)** — `01_Single_winner/display_options_demo.yaml` (4c/4b)  
    STAR=**Don** · IRV=Bob · RR=Don · Approval=Ann · Condorcet=Don  
    _flags: 2 tied-score ballot(s); IRV flips on reversed priority; RR conv-sensitive (weak=Don, strict=Bob)_

### CYCLE_OR_THREE_WAY — 4

_Condorcet cycle / three-way split — genuinely hard case, no clean villain_

- **[BV_Library_star_runoff_tie_score_resolves](cases/CYCLE_OR_THREE_WAY/BV_Library_star_runoff_tie_score_resolves.md)** — `01_Single_winner/BV_Library/BV_Library_star_runoff_tie_score_resolves.yaml` (2c/2b)  
    STAR=**Bill** · IRV=Bill · RR=Allison · Approval=Allison · Condorcet=none
- **[monotonicity_star_after](cases/CYCLE_OR_THREE_WAY/monotonicity_star_after.md)** — `01_Single_winner/monotonicity_star_after.yaml` (3c/34b)  
    STAR=**X** · IRV=Z · RR=X · Approval=X · Condorcet=none
- **[monotonicity_star_before](cases/CYCLE_OR_THREE_WAY/monotonicity_star_before.md)** — `01_Single_winner/monotonicity_star_before.yaml` (3c/34b)  
    STAR=**X** · IRV=X · RR=Y · Approval=Y · Condorcet=none
- **[Whoops_02_star_misses_condorcet](cases/CYCLE_OR_THREE_WAY/Whoops_02_star_misses_condorcet.md)** — `01_Single_winner/paradoxes_and_whoops/Whoops_02_star_misses_condorcet.yaml` (3c/100b)  
    STAR=**Ada** · IRV=Ada · RR=Cleo · Approval=Ada · Condorcet=Cleo  
    _flags: 25 tied-score ballot(s); IRV flips on reversed priority_

### APPROVAL_OR_MINOR — 20

_Only Approval (or a minor method) differs — usually a threshold story, not an IRV one_

- **[03b_c3_b3_1_style-protest-vote](cases/APPROVAL_OR_MINOR/03b_c3_b3_1_style-protest-vote.md)** — `01_Single_winner/03b_c3_b3_1_style-protest-vote.yaml` (3c/3b)  
    STAR=**Almond** · IRV=Almond · RR=Almond · Approval=Choco · Condorcet=Almond
- **[03b_c3_b3_2_expand_style-protest-vote](cases/APPROVAL_OR_MINOR/03b_c3_b3_2_expand_style-protest-vote.md)** — `01_Single_winner/03b_c3_b3_2_expand_style-protest-vote.yaml` (3c/3b)  
    STAR=**Almond** · IRV=Almond · RR=Almond · Approval=Choco · Condorcet=Almond
- **[04b_c4_b3_display-options-all](cases/APPROVAL_OR_MINOR/04b_c4_b3_display-options-all.md)** — `01_Single_winner/04b_c4_b3_display-options-all.yaml` (4c/3b)  
    STAR=**Strawberry** · IRV=Strawberry · RR=Strawberry · Approval=Vanilla · Condorcet=Strawberry
- **[BV_Library_star_runoff_score_tie_five_star](cases/APPROVAL_OR_MINOR/BV_Library_star_runoff_score_tie_five_star.md)** — `01_Single_winner/BV_Library/BV_Library_star_runoff_score_tie_five_star.yaml` (2c/2b)  
    STAR=**Allison** · IRV=Allison · RR=Allison · Approval=Bill · Condorcet=none  
    _flags: IRV flips on reversed priority_
- **[Black_Curtain_01_c3_b5_hidden-consensus](cases/APPROVAL_OR_MINOR/Black_Curtain_01_c3_b5_hidden-consensus.md)** — `01_Single_winner/black_curtain/Black_Curtain_01_c3_b5_hidden-consensus.yaml` (3c/5b)  
    STAR=**Cal** · IRV=Cal · RR=Cal · Approval=Bob · Condorcet=Cal
- **[Black_Curtain_02_c3_b5_near-clones](cases/APPROVAL_OR_MINOR/Black_Curtain_02_c3_b5_near-clones.md)** — `01_Single_winner/black_curtain/Black_Curtain_02_c3_b5_near-clones.yaml` (3c/5b)  
    STAR=**Cal** · IRV=Cal · RR=Cal · Approval=Ann · Condorcet=Cal
- **[Black_Curtain_03_c3_b5_polarized-on-cal](cases/APPROVAL_OR_MINOR/Black_Curtain_03_c3_b5_polarized-on-cal.md)** — `01_Single_winner/black_curtain/Black_Curtain_03_c3_b5_polarized-on-cal.yaml` (3c/5b)  
    STAR=**Cal** · IRV=Cal · RR=Cal · Approval=Ann · Condorcet=Cal
- **[count_simplicity_star_vs_irv](cases/APPROVAL_OR_MINOR/count_simplicity_star_vs_irv.md)** — `01_Single_winner/count_simplicity_star_vs_irv.yaml` (5c/40b)  
    STAR=**Carmen** · IRV=Carmen · RR=Carmen · Approval=Andre · Condorcet=Carmen
- **[Whoops_03_condorcet_cycle_rps](cases/APPROVAL_OR_MINOR/Whoops_03_condorcet_cycle_rps.md)** — `01_Single_winner/paradoxes_and_whoops/Whoops_03_condorcet_cycle_rps.yaml` (3c/100b)  
    STAR=**Rock** · IRV=Rock · RR=Rock · Approval=Paper · Condorcet=none
- **[01a_c3_b3_more-stars-fewer-voters](cases/APPROVAL_OR_MINOR/01a_c3_b3_more-stars-fewer-voters.md)** — `01_Single_winner/runoff_overturns_leader/01a_c3_b3_more-stars-fewer-voters.yaml` (3c/3b)  
    STAR=**Brownie** · IRV=Brownie · RR=Brownie · Approval=Almond · Condorcet=Brownie
- **[01b_c3_b9_overturn-holds-at-scale](cases/APPROVAL_OR_MINOR/01b_c3_b9_overturn-holds-at-scale.md)** — `01_Single_winner/runoff_overturns_leader/01b_c3_b9_overturn-holds-at-scale.yaml` (3c/9b)  
    STAR=**Brownie** · IRV=Brownie · RR=Brownie · Approval=Almond · Condorcet=Brownie
- **[02_c5_b5_leader-overturned](cases/APPROVAL_OR_MINOR/02_c5_b5_leader-overturned.md)** — `01_Single_winner/runoff_overturns_leader/02_c5_b5_leader-overturned.yaml` (5c/5b)  
    STAR=**Boston** · IRV=Boston · RR=Boston · Approval=Austin · Condorcet=Boston
- **[03_c7_b3_ice-cream-live](cases/APPROVAL_OR_MINOR/03_c7_b3_ice-cream-live.md)** — `01_Single_winner/runoff_overturns_leader/03_c7_b3_ice-cream-live.yaml` (7c/3b)  
    STAR=**ChocoAlm** · IRV=ChocoAlm · RR=ChocoAlm · Approval=ChocoDrk · Condorcet=ChocoAlm
- **[05_c3_b5_low-scores-bv1265](cases/APPROVAL_OR_MINOR/05_c3_b5_low-scores-bv1265.md)** — `01_Single_winner/runoff_overturns_leader/05_c3_b5_low-scores-bv1265.yaml` (3c/5b)  
    STAR=**A** · IRV=A · RR=A · Approval=C · Condorcet=A  
    _flags: 1 tied-score ballot(s)_
- **[Runoff_02_atom_reversal_yx9447](cases/APPROVAL_OR_MINOR/Runoff_02_atom_reversal_yx9447.md)** — `01_Single_winner/runoff_overturns_leader/Runoff_02_atom_reversal_yx9447.yaml` (3c/3b)  
    STAR=**Boston** · IRV=Boston · RR=Boston · Approval=Austin · Condorcet=Boston
- **[Runoff_03_enthusiasts_vs_majority_rkgtpk](cases/APPROVAL_OR_MINOR/Runoff_03_enthusiasts_vs_majority_rkgtpk.md)** — `01_Single_winner/runoff_overturns_leader/Runoff_03_enthusiasts_vs_majority_rkgtpk.yaml` (5c/5b)  
    STAR=**Eden** · IRV=Eden · RR=Eden · Approval=Dakota · Condorcet=Eden
- **[Runoff_04_reversal_at_scale_bfjqmg](cases/APPROVAL_OR_MINOR/Runoff_04_reversal_at_scale_bfjqmg.md)** — `01_Single_winner/runoff_overturns_leader/Runoff_04_reversal_at_scale_bfjqmg.yaml` (3c/9b)  
    STAR=**Olive** · IRV=Olive · RR=Olive · Approval=Maple · Condorcet=Olive
- **[Runoff_05_reversal_with_equal_support_xgkw3w](cases/APPROVAL_OR_MINOR/Runoff_05_reversal_with_equal_support_xgkw3w.md)** — `01_Single_winner/runoff_overturns_leader/Runoff_05_reversal_with_equal_support_xgkw3w.yaml` (3c/5b)  
    STAR=**Sage** · IRV=Sage · RR=Sage · Approval=Rosa · Condorcet=Sage  
    _flags: 2 tied-score ballot(s); IRV flips on reversed priority_
- **[Runoff_07_flat_ballot_bv_bug_tf73v9](cases/APPROVAL_OR_MINOR/Runoff_07_flat_ballot_bv_bug_tf73v9.md)** — `01_Single_winner/runoff_overturns_leader/Runoff_07_flat_ballot_bv_bug_tf73v9.yaml` (3c/4b)  
    STAR=**Blair** · IRV=Blair · RR=Blair · Approval=Alex · Condorcet=Blair  
    _flags: 1 tied-score ballot(s); IRV flips on reversed priority_
- **[star_district_B](cases/APPROVAL_OR_MINOR/star_district_B.md)** — `01_Single_winner/summability_demo/star_district_B.yaml` (3c/3b)  
    STAR=**Oak** · IRV=Oak · RR=Oak · Approval=Pine · Condorcet=Oak

## Full table

See `divergence.csv` for the machine-readable version (all columns, including the strict/weak split).

