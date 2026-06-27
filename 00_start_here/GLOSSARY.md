# STAR Voting — Glossary

One-line definitions for the keywords used across these lessons. Grouped from
beginner vocabulary to advanced theory. Most entries end with **→** quick jumps to
the test-case YAML (demo) and/or the interview episode that show the term in action.

## Core vocabulary

- **STAR** — Score Then Automatic Runoff: score every candidate 0–5; the two highest totals advance to an automatic head-to-head runoff. → episode [`whats_so_good_about_STAR_Voting.md`](../interviews_conversations/whats_so_good_about_STAR_Voting.md)
- **Score / star rating** — a 0–5 value expressing *how much* you support a candidate (like a five-star review).
- **Scoring round** — STAR's first round: add up each candidate's scores; the top two become finalists. → demo [`equal_support_runoff_demo.yaml`](../01_Single_winner/equal_support_runoff_demo.yaml)
- **Finalists** — the two highest-scoring candidates, who advance to the runoff.
- **Automatic runoff** — STAR's second round: each ballot counts as a full vote for whichever finalist it scored higher; the preferred finalist wins. (Deep-dive deck: **Automatic Runoff** — see [`LINKS.md`](../interviews_conversations/LINKS.md).) → demo [`equal_support_runoff_demo.yaml`](../01_Single_winner/equal_support_runoff_demo.yaml); episode [`are_equal_score_votes_discounted.md`](../interviews_conversations/are_equal_score_votes_discounted.md)
- **Head-to-head / pairwise** — a direct comparison of two candidates: which one more ballots scored higher.
- **Equal Support / Equal Preference** — scoring two candidates the same; counts as "no preference" between them in the runoff. Covers two honest cases — scored both finalists high ("loved both") or both low ("neither") — both still counted in the scoring round. → episode [`are_equal_score_votes_discounted.md`](../interviews_conversations/are_equal_score_votes_discounted.md) → demo [`equal_support_runoff_demo.yaml`](../01_Single_winner/equal_support_runoff_demo.yaml); episode [`are_equal_score_votes_discounted.md`](../interviews_conversations/are_equal_score_votes_discounted.md)
- **Scored (cardinal) ballot** — rates each candidate independently 0–5; equal ratings allowed.
- **Ranked (ordinal) ballot** — orders candidates 1st, 2nd, 3rd; no ties, no degree of support.

## The problem STAR addresses

- **Choose-One / Plurality / First-Past-The-Post** — vote for exactly one candidate; most votes wins. Accurate only with two candidates. → episode [`our_voting_system_is_broken.md`](../interviews_conversations/our_voting_system_is_broken.md)
- **Vote splitting** — similar candidates divide their shared supporters, letting a less-preferred candidate win. → demos [`split_voting/`](../split_voting/); episode [`our_voting_system_is_broken.md`](../interviews_conversations/our_voting_system_is_broken.md)
- **Spoiler effect** — a candidate who cannot win still changes who does, by splitting another's support. → demo [`04_star_wars_vote_split.yaml`](../split_voting/04_star_wars_vote_split.yaml); episode [`whats_so_good_about_STAR_Voting.md`](../interviews_conversations/whats_so_good_about_STAR_Voting.md) (Seg 1)
- **Favorite betrayal** — being pressured to score/rank a front-runner above your true favorite. → episode [`favorite_betrayal_voting_301.md`](../interviews_conversations/favorite_betrayal_voting_301.md)
- **Lesser-evil voting** — backing a tolerable front-runner instead of your favorite to block a worse outcome. → episode [`our_voting_system_is_broken.md`](../interviews_conversations/our_voting_system_is_broken.md)
- **Wasted vote** — a vote that has no effect on the result.
- **Two-round system** — separate primary + general/runoff elections; STAR does both jobs on one ballot.
- **Plurality / minority winner** — a winner with the most votes but less than majority support. → episode [`our_voting_system_is_broken.md`](../interviews_conversations/our_voting_system_is_broken.md)

## Mechanics

- **Equal scores allowed** — you may give two candidates the same score; you're never forced to invent a preference. → demo [`03a_c3_b3_style-bullet-vote.yaml`](../01_Single_winner/03a_c3_b3_style-bullet-vote.yaml)
- **Exhausted ballot** — (an **RCV-IRV** term; IRV-specific, *not* all ranked methods — Ranked Robin / Condorcet counts read every rank) a ballot set aside mid-count because all its ranked candidates were eliminated. FairVote's single word covers several very different cases (voter-side vs method-caused); STAR's runoff never eliminates anyone, so it doesn't discard ballots this way. → episode [`exhausted_ballots_301.md`](../interviews_conversations/exhausted_ballots_301.md)
- **Tiebreaker** — a rule that resolves ties (for the finalists or the runoff); here, candidate priority / lot order. The full ladder (pairwise → five-star → lot, in both rounds), plus what BetterVoting JSON carries and what you may set in a hand-written YAML, is in [`concepts/tie_breaking.md`](concepts/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md).
- **Undervote / abstention** — a ballot that scores no one (blank or `~`); counts as turnout but supports no candidate.

## Properties & criteria

- **Majority finish** — STAR's runoff guarantees the winner beats the runner-up among voters who expressed a preference between them. → demo [`06b_c9_runoff-overturns-leader.yaml`](../01_Single_winner/06b_c9_runoff-overturns-leader.yaml) (runoff overturns the score leader); full walkthrough [`runoff_overturns_leader/`](../01_Single_winner/runoff_overturns_leader/README.md) (why the top-scoring candidate isn't always the winner, as a 3→9-candidate progression)
- **Runoff Reversal** — the STAR outcome where the **Scoring-Round leader loses the Automatic Runoff** to the finalist more voters prefer (the *score* winner ≠ the *STAR* winner). Not a malfunction — the runoff is enforcing majority preference between the two finalists. The plain-language house term is "the runoff overturns the score leader." → walkthrough [`runoff_overturns_leader/`](../01_Single_winner/runoff_overturns_leader/README.md)
- **Three notions of "winner"** — Condorcet (beats all head-to-head), Score (most total stars), and Runoff (majority pick between finalists) can name three *different* candidates in one election; STAR targets the runoff winner by design. → page [`STAR_three_winner_notions.md`](concepts/STAR_Voting/STAR_three_winner_notions.md); demo [`three_winners_cw_score_runoff.yaml`](../01_Single_winner/three_winners_cw_score_runoff.yaml)
- **Condorcet winner** — the candidate who beats every other head-to-head; STAR usually (not always) elects them. → demo [`equal_support_runoff_demo.yaml`](../01_Single_winner/equal_support_runoff_demo.yaml) (`show_condorcet`)
- **Condorcet efficiency** — how often a method elects the Condorcet winner (STAR's is very high).
- **Condorcet loser** — the candidate who loses every head-to-head.
- **Condorcet compliance** — *always* electing the Condorcet winner; STAR is **not** compliant (a deliberate tradeoff).
- **Center squeeze** — a broadly-liked moderate eliminated early for lacking first-choice support; an RCV-IRV failure STAR avoids. → page [`concepts/RCV_IRV_center_squeeze.md`](concepts/RCV_IRV/RCV_IRV_center_squeeze.md); demos: RCV-IRV [`squeeze`](../01_Single_winner/center_squeeze_irv.yaml) / STAR [`fix`](../01_Single_winner/center_squeeze_star.yaml)
- **Later-no-harm** — adding a lower preference never hurts your top choice; RCV-IRV has it, STAR intentionally does not. → episode [`favorite_betrayal_voting_301.md`](../interviews_conversations/favorite_betrayal_voting_301.md)
- **Monotonicity** — raising a candidate on your ballot never causes them to lose (and vice versa). → page [`RCV_IRV_non_monotonicity.md`](concepts/RCV_IRV/RCV_IRV_non_monotonicity.md); demos: RCV-IRV [`before`](../01_Single_winner/monotonicity_irv_before.yaml)/[`after`](../01_Single_winner/monotonicity_irv_after.yaml) (X loses), STAR [`before`](../01_Single_winner/monotonicity_star_before.yaml)/[`after`](../01_Single_winner/monotonicity_star_after.yaml) (X holds)
- **Participation criterion** — voting honestly never yields a worse result than not voting.
- **Favorite-betrayal criterion** — you never gain by scoring someone above your favorite. → episode [`favorite_betrayal_voting_301.md`](../interviews_conversations/favorite_betrayal_voting_301.md)
- **Summability / precinct-summable** — results can be computed by adding independent precinct totals (STAR can; RCV-IRV cannot). → page [`STAR_summability.md`](concepts/STAR_Voting/STAR_summability.md); demo [`04b_c4_b3_display-options-all.yaml`](../01_Single_winner/04b_c4_b3_display-options-all.yaml)
- **Pairwise (For / Equal / Against) matrix** — the summable head-to-head table the runoff and audits use. → demo [`04b_c4_b3_display-options-all.yaml`](../01_Single_winner/04b_c4_b3_display-options-all.yaml) (`show_matrix`)
- **Strategyproofness** — no voter can ever gain by voting insincerely; impossible for any method (Gibbard).
- **Gibbard / Gibbard–Satterthwaite theorems** — proofs that every reasonable voting method is manipulable.
- **Strategy resistance** — how rarely and riskily strategy pays; STAR is resistant, not proof.
- **Equal Vote / Test of Balance** — any support a ballot expresses can be exactly cancelled by an opposite ballot; STAR's precise sense of equal weight.
- **One-person-one-vote** — equal voting weight. (Caution: the constitutional OPOV doctrine governs district population, not ballot expressiveness.)
- **Utilitarian vs majoritarian** — maximizing total support vs guaranteeing a majority; STAR blends both.

## Other methods (for contrast)

- **Approval voting** — score each candidate 0 or 1 (approve / not); most approvals wins. → demo [`Approval_ballot.yaml`](../01_Single_winner/Approval_ballot.yaml)
- **Score voting (pure)** — score 0–5; highest total/average wins, with no runoff (more manipulable than STAR).
- **RCV (Ranked-Choice Voting)** — a ranked *ballot* type (rank candidates 1st, 2nd, 3rd). A **family**, not one method; in the US it's commonly (loosely) used to mean IRV specifically. → [`TIPS_terminology.md`](./TIPS_terminology.md); episode [`RCV_or_IRV_whats_the_right_word.md`](../interviews_conversations/RCV_or_IRV_whats_the_right_word.md)
- **IRV (Instant-Runoff Voting)** — *one tabulation* of a ranked ballot: eliminate the lowest, transfer, repeat until a majority. The single-winner method usually meant by "RCV."
- **RCV-IRV** — disambiguating label for "the RCV that is IRV"; preferred in this repo for STAR-vs-method comparisons so it's clear we mean the eliminate-and-transfer method, not the ballot family. → [`TIPS_terminology.md`](./TIPS_terminology.md); episodes [`RCV_or_IRV_whats_the_right_word.md`](../interviews_conversations/RCV_or_IRV_whats_the_right_word.md), [`exhausted_ballots_301.md`](../interviews_conversations/exhausted_ballots_301.md)
- **Ranked Robin (RCV-RR / "Consensus")** — a Condorcet tabulation of the *same* ranked ballot (most head-to-head wins, Copeland-style). Has no center squeeze; do not lump it with IRV.
- **STV (Single Transferable Vote)** — the proportional, multi-winner tabulation of ranked ballots (the proportional cousin of IRV, not IRV itself). → demo [`03a_stv_3seats.yaml`](../02_Multi_winner/03a_stv_3seats.yaml); page [`concepts/proportional_stv_vs_star.md`](./concepts/proportional_stv_vs_star.md)
- **Condorcet method** — any ranked method that *always* elects the candidate who beats every other head-to-head (the Condorcet winner) when one exists. A **family**: Ranked Robin, Ranked Pairs, Schulze, Minimax, Copeland. → family tree in [`TIPS_terminology.md`](./TIPS_terminology.md)
- **Ranked Pairs (Tideman)** — a Condorcet method: lock in the strongest pairwise victories first, skipping any that would create a cycle.
- **Schulze (beatpath)** — a Condorcet method that decides via the strongest "beatpaths" between candidates.
- **Minimax (Simpson–Kramer)** — a Condorcet method electing the candidate whose *worst* pairwise loss is the smallest.
- **Borda** — a positional ranked method (points by rank position). A ranked method but **not** Condorcet-compliant.
- **Bucklin (Grand Junction)** — a ranked, median-style method (add lower ranks until someone has a majority). Ranked but **not** Condorcet. (Spelled *Bucklin*, not "Buckling".)
- **Hare** — historically the ranked-transfer idea; single-winner = **IRV**, multi-winner = **STV** (Hare quota).
- **ballot vs tabulation** — the ballot is *what the voter marks* (ranked, or scored); the tabulation is *how it's counted* (IRV / Ranked Robin / STV for ranked; STAR / Approval / Score for scored). "RCV" names a ballot; "IRV" names a tabulation. → [`TIPS_terminology.md`](./TIPS_terminology.md); episode [`RCV_or_IRV_whats_the_right_word.md`](../interviews_conversations/RCV_or_IRV_whats_the_right_word.md)
- **Bloc STAR** — multi-winner STAR that elects the top N candidates (at-large / majoritarian — *not* proportional). → demo [`01_c4_b2_bloc-star-2-seats.yaml`](../02_Multi_winner/01_c4_b2_bloc-star-2-seats.yaml); majoritarian-vs-proportional contrast in [`concepts/proportional_stv_vs_star.md`](./concepts/proportional_stv_vs_star.md); [`CURRICULUM.md`](./CURRICULUM.md) (201.5)
- **Proportional STAR** — multi-winner methods (Reweighted Range Voting, Allocated Score, Sequentially Spent Score) that give proportional representation. → demo [`03b_star_pr_3seats.yaml`](../02_Multi_winner/03b_star_pr_3seats.yaml); page [`concepts/proportional_stv_vs_star.md`](./concepts/proportional_stv_vs_star.md) (STV vs STAR-PR); [`CURRICULUM.md`](./CURRICULUM.md) (301.1)

## Civic / adoption

- **[Equal Vote Coalition](https://equal.vote)** — the organization that developed and advocates STAR Voting.
- **[BetterVoting.com](https://bettervoting.com)** — site to try a STAR ballot and run your own elections.

---

See also: [00_START_HERE.md](./00_START_HERE.md) (teaching sequence) ·
[Why_STAR_Voting.md](./Why_STAR_Voting.md) (presentation + debate prep) ·
[CURRICULUM.md](./CURRICULUM.md) (lesson outline).
