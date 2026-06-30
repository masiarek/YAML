# Concepts — deep-dive pages for the important terms

**New here? Start with [Ballot & Terminology Basics](ballot_and_terminology_basics.md)** — a short
4-page reading path through the ideas people most often get wrong (terminology, scores vs. ranks,
what counts as "ranked," and strict vs. weak ranks).

Not every glossary term needs its own page — most are fine as a one-liner in
[`../GLOSSARY.md`](GLOSSARY.md). This folder holds the handful of concepts that
are **load-bearing in debates** and worth a focused page with a worked example and
**links to the test-case YAMLs** that demonstrate them.

The pages are grouped to mirror the folders: **general / cross-method** ideas sit at
the top level, IRV-specific problems live in [`RCV_IRV/`](RCV_IRV/), and STAR's own
properties live in [`STAR_Voting/`](STAR_Voting/).

**Two ways to browse.** The authoritative pages are organized **by method** (below). Ideas
that cut across methods also have a **by-topic** view in [`topics/`](topics/README_topics.md) —
thin hubs that link to each method's treatment of one idea (so you can browse by topic in
the GitHub file tree, not just by method). First hub: [Summability](topics/summability/README_summability.md).

### General & cross-method

| Concept | One line | Page |
|---------|----------|------|
| **Ballot & terminology basics** | the 4 ideas people most often get wrong — start here | [ballot_and_terminology_basics.md](ballot_and_terminology_basics.md) |
| **Scores vs. ranks (don't confuse them!)** | order-only (ranks) vs. order+strength (scores) — relative vs. absolute preference | [scores_vs_ranks.md](scores_and_ranks/scores_vs_ranks.md) |
| **Scoring methods aren't RCV** | scoring methods (Approval, STAR) rate candidates and sit *outside* the ranked-voting family | [scoring-methods-vs-ranked-voting.md](scoring-methods-vs-ranked-voting.md) |
| **Strict vs. weak ranks** | many ranked methods allow equal ranks & compare pairwise — RCV-IRV does neither | [strict_vs_weak_ranks.md](scores_and_ranks/strict_vs_weak_ranks.md) |
| **"Preference" (a slippery word)** | everyday opinion vs. technical "ranking"; why "Preferential Voting" is a misnomer | [preference.md](preference.md) |
| **Ranked Robin / RCV-RR (Consensus Voting; = Copeland)** | a Condorcet method: ranks + equal ranks, every pair compared head-to-head; tabulable via the pref_voting engine | [RCV_Ranked_Robin/ranked_robin.md](RCV_Ranked_Robin/ranked_robin.md) |
| **Proportional Representation** | multi-seat — coalitions get proportional seats; STV ≈ STAR-PR, Bloc differs (301) | [proportional_representation/](proportional_representation/README_proportional_representation.md) ([STV vs STAR-PR](proportional_representation/stv/proportional_stv_vs_star.md) · [STAR-PR methods](proportional_representation/STAR_PR/README_STAR_PR.md)) |
| **Tabulation, step by step (201)** | the same ballots counted both ways — STAR's 2 steps vs IRV's elimination rounds | [tabulation_star_vs_irv.md](tabulation_star_vs_irv.md) |
| **RCV-IRV vs. STAR (side-by-side)** | balanced comparison hub — real strengths on both sides — routing to the facet pages | [rcv_irv_vs_star.md](rcv_irv_vs_star.md) |
| **Tabulation engines — BV, LH, RCV-IRV** | why an election has two reports (BetterVoting's visual display + the LH engine's text report), how they map, and the convert→validate→test pipeline; hub for the per-engine folders | [tabulation_engines/](tabulation_engines/bettervoting_and_the_engine.md) |
| **STAR Reporting — reading & comparing results** | how a result is reported: scores, runoff, percentages, Equal Support/abstentions; LH vs BetterVoting and where they differ; the Score Distribution and Preference Matrix up close | [STAR_reporting/](STAR_reporting/README_STAR_reporting.md) |
| **Quorum — did enough show up?** | a turnout threshold separate from who wins; abstentions count toward it; an unmet quorum means no winner — won the count but not elected | [quorum.md](quorum.md) |

### RCV-IRV — problems specific to instant-runoff

| Concept | One line | Page |
|---------|----------|------|
| **RCV is a confusing name** | "RCV" is an umbrella for many ranked methods; in the US it usually means RCV-IRV (Hare) | [RCV-IRV-confusing-name.md](RCV_IRV/RCV-IRV-confusing-name.md) |
| **Is IRV "just plurality"?** | the defensible kernel (round-by-round first-choice elimination) vs. the overclaim | [RCV_IRV_and_plurality.md](RCV_IRV/RCV_IRV_and_plurality.md) |
| **Is RCV "simple"? (201)** | ranking is simple to *mark*; IRV's *count* isn't | [RCV_IRV_is_simple.md](RCV_IRV/RCV_IRV_is_simple.md) |
| **Center squeeze** | a broadly-liked moderate eliminated early under IRV; STAR avoids it | [RCV_IRV_center_squeeze.md](RCV_IRV/RCV_IRV_center_squeeze.md) |
| **IRV non-monotonicity** | under IRV, *more* first-choice support can make the winner **lose** | [RCV_IRV_non_monotonicity.md](RCV_IRV/RCV_IRV_non_monotonicity.md) |
| **Exhausted ballots** | a validly-cast ranked ballot can stop counting; IRV's "majority" is of active ballots | [RCV_IRV_exhausted_ballots.md](RCV_IRV/RCV_IRV_exhausted_ballots.md) |
| **IRV isn't summable** | the winner depends on elimination order, so every ballot must be counted centrally | [RCV_IRV_lack_of_summability.md](RCV_IRV/RCV_IRV_lack_of_summability.md) |

### STAR Voting — STAR's properties & strengths

| Concept | One line | Page |
|---------|----------|------|
| **STAR's hybrid nature** | expressive scoring to find the finalists + a majority runoff to pick the winner — the design the rest of these pages build on | [STAR_hybrid_nature.md](STAR_Voting/STAR_hybrid_nature.md) |
| **The Automatic Runoff Round** | STAR's second step, end to end — finalists, the For/Against/Equal Support counts, percentages, tie-breaking, and Runoff Reversal; the hub for all runoff topics | [STAR_Automatic_Runoff.md](STAR_Voting/STAR_Automatic_Runoff.md) |
| **Runoff Reversal — top scorer ≠ winner** | the Scoring Round picks two finalists; the Automatic Runoff lets the *majority-preferred* finalist win — even with fewer total stars | [runoff_overturns_leader/](../01_Single_winner/runoff_overturns_leader/README_runoff_overturns_leader.md) |
| **The LH starvote engine** | what the engine is (a thin fork + a thick reporting wrapper) and our improvements — the minimal **echo** vs the always-full **`_tabulated`** mirror, the matrix/divergence/runoff-funnel reporting, and multi-method dispatch | [LH_starvote/](tabulation_engines/LH_starvote/README_LH_starvote.md) |
| **Reading a STAR report (201)** | the full engine report, section by section — matrix, divergence, both rounds, winner — and which parts to show 101 vs 201 vs 301 | [reading_a_star_report.md](tabulation_engines/LH_starvote/reading_a_star_report.md) |
| **Reading the runoff percentages** | the same runoff vote shown two ways — % of all voters vs % of the voters *with a preference*; why the winner needs a majority of the decided voters, and where Equal Support goes | [runoff_percentages.md](STAR_Voting/runoff_percentages.md) |
| **Three notions of "winner"** | Condorcet vs Score vs Runoff can name three different candidates in one election | [STAR_three_winner_notions.md](STAR_Voting/STAR_three_winner_notions.md) |
| **STAR is monotone** | raising a candidate's score can never make them lose — the failure IRV has, STAR doesn't | [STAR_monotonicity.md](STAR_Voting/STAR_monotonicity.md) |
| **STAR is summable** | tally by adding independent precinct totals; precinct-auditable, meaningful partials | [STAR_summability.md](STAR_Voting/STAR_summability.md) |
| **Residual vote-splitting** | STAR ends *forced* splitting; the narrow leftover is self-inflicted bullet-voting / the chicken dilemma | [residual_vote_splitting.md](STAR_Voting/residual_vote_splitting.md) |
| **Tie-breaking — the full chain** | ties fall through pairwise → five-star → lot order, in both rounds | [Tie_Breaking_STAR/tie_breaking.md](STAR_Voting/Tie_Breaking_STAR/tie_breaking.md) |
| **Tie-breaking in BetterVoting JSON** | how a BV export pre-draws the official lot order, and its YAML mapping | [Tie_Breaking_STAR/tie_breaking_JSON.md](STAR_Voting/Tie_Breaking_STAR/tie_breaking_JSON.md) |

Deeper conversation/debate scripts live in
[`../../interviews_conversations/`](../interviews_conversations/) (e.g.
`favorite_betrayal_voting_301.md`, `exhausted_ballots_301.md`); these pages are the
shorter, reference-style explainers the glossary links to.
