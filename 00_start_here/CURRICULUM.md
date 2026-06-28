# STAR Voting — Curriculum (Voting 101 / 201 / 301)

The authoritative **learning-path map**. Difficulty lives *here*, not in the
folder names or in every file — so a single example can be 101 for its basic idea
and reappear at 301 for the deep dive, without being duplicated or moved. (This is
the "curriculum map, keep folders" approach; see
[ORGANIZATION.md](./ORGANIZATION.md).)

Each entry lists its **objective**, **key terms** (see [GLOSSARY.md](./GLOSSARY.md)),
the **files/episodes** to use, and **what to emphasize**. Example YAMLs stay in
their content-typed folders (`01_Single_winner/`, `02_Multi_winner/`,
`split_voting/`); conversation scripts live in `interviews_conversations/`.

---

# Voting 101 — Basics (the ballot, the two rounds, the spoiler)

> Audience: general public, first contact. The goal is intuition, not theory.

## 101.0 — Why: the problem before the method
- **Objective:** Make the audience *feel* the failure of Choose-One first.
- **Key terms:** Choose-One / plurality, vote splitting, spoiler effect, lesser-evil voting.
- **Material:** [00_START_HERE.md](./00_START_HERE.md); episode `why_do_you_love_STAR_Voting.md` (cold open).

## 101.1 — Mechanics: the two rounds (2 candidates)
- **Objective:** See the Scoring Round and Automatic Runoff once, slowly.
- **Key terms:** score 0–5, scoring round, finalists, automatic runoff, equal scores.
- **Files:** `01_Single_winner/00a*`, `01a*`, `01b*`, `01c*`.
- **Emphasize:** with two candidates STAR == ordinary voting — that's *why* we start here.

## 101.2 — Why it matters: add a third candidate
- **Objective:** Watch the winner become the broad compromise.
- **Files:** `01_Single_winner/02*`; `01_Single_winner/vote_splitting.yaml`.
- **Emphasize:** adding a candidate you love never splits your vote.

## 101.3 — How you're allowed to vote
- **Objective:** Remove the fear of "voting wrong."
- **Key terms:** bullet vote, equal scores, partial ballot, blank vs explicit 0.
- **Files:** `01_Single_winner/03*`; large field (9 candidates) `06a` (STAR scales; Equal Support decides the runoff) and `06b` (the runoff overturns the score leader).
- **The headline lesson — top scorer ≠ winner:** the dedicated walkthrough [`01_Single_winner/runoff_overturns_leader/`](../01_Single_winner/runoff_overturns_leader/README.md) collects this as an approachable 3→9-candidate progression (with a confirm-case control), answering BetterVoting's *"why is the top-scoring candidate different from the winner?"*
- **Ballot note:** the ballot's own line *"equal scores indicate no preference"* means no preference *in the runoff* — those ballots still count in the scoring round. (That's the Equal Support point; see `interviews_conversations/are_equal_score_votes_discounted.md`.)

## 101.4 — The payoff: the spoiler, in numbers
- **Objective:** Land the whole case in one race.
- **Files:** `split_voting/01–03`, `01_Single_winner/vote_splitting2.yaml`, `09_*` (Tennessee); the `blocs:` vote-splitting check.
- **Episode:** `whats_so_good_about_STAR_Voting.md` (flagship).

## 101.5 — One foundational idea: ballot vs tabulation
- **Objective:** A *ballot* is what you mark; a *tabulation* is how it's counted.
- **Material:** [TIPS_terminology.md](./TIPS_terminology.md) (top section).
- **Why here:** it unlocks 201's nomenclature and every later comparison.

---

# Voting 201 — Intermediate (reading results, comparisons, multi-winner intro)

> Audience: engaged learners, officials, the curious. Now we name things precisely
> and compare methods.

## 201.1 — Reading the results (transparency)
- **Key terms:** preference matrix, For/Equal/Against, Condorcet winner, summability, score distribution.
- **Files:** `01_Single_winner/04*` with `options: { show_matrix, show_condorcet }`.
- **Emphasize:** the pairwise matrix is the auditable, precinct-summable heart.
- **Two reports, one count:** an election appears both as BetterVoting's visual display and
  the LH engine's text report; why there are two, how they map, and the convert→validate→test
  pipeline are in [`concepts/tabulation_engines/bettervoting_and_the_engine.md`](./concepts/tabulation_engines/bettervoting_and_the_engine.md).
- **The full audit report:** the generated `_tabulated.txt` siblings carry the complete
  engine report (matrix + score distribution + the plain-English *Majority Preference*
  block). The Runoff Reversal lesson (101.3) shows the *minimal* on-screen view; reading
  the **full** report of those same elections (e.g.
  `01_Single_winner/runoff_overturns_leader_tabulated/`) is the 201 skill — and *why* the
  on-screen echo is minimal by default (don't overwhelm a beginner).
- **Worked walkthrough:** [`concepts/tabulation_engines/LH_starvote/reading_a_star_report.md`](./concepts/tabulation_engines/LH_starvote/reading_a_star_report.md)
  — a full LH report (BV1265) annotated section by section, with a "show which parts to
  101 / 201 / 301" table.
- **Reading the runoff percentages:** [`concepts/STAR_Voting/runoff_percentages.md`](./concepts/STAR_Voting/runoff_percentages.md)
  — the BetterVoting runoff shown two ways: % of *all* voters vs % of those *with a
  preference* (the two denominators), and why the majority bar is half of the decided
  voters, not half of everyone. The LH engine prints this same decided-voters share as
  a one-line summary — enable with `options: { show_runoff_percent: true }` (forced on
  in the `_tabulated` copy). Pairs with 301.3 (Equal Support).
- **A real election, end to end:** [`01_Single_winner/pet_real_bv_election/`](../01_Single_winner/pet_real_bv_election/README.md)
  — a real BetterVoting STAR election ("What Makes the Best Pet?", 7 pets, 461 ballots),
  the actual export YAML plus its full engine report, read section by section (scoring →
  runoff → runoff % → Condorcet check), including the real-ballot distinction between an
  abstention (blank) and an explicit-zero ballot.

## 201.2 — Edge cases & trust
- **Key terms:** unanimous ballots, ties / tiebreaker, abstention, equal-max ballot.
- **Files:** `01_Single_winner/05*`.

## 201.3 — Nomenclature: RCV vs IRV vs RCV-IRV
- **Objective:** Stop conflating the ranked *ballot* (RCV) with one *count* (IRV).
- **Material:** [TIPS_terminology.md](./TIPS_terminology.md); episode `RCV_or_IRV_whats_the_right_word.md`.
- **Emphasize:** center squeeze / exhausted ballots are **IRV**-specific, not all ranked methods (Ranked Robin isn't squeezed).

## 201.4 — STAR vs RCV-IRV (the honest comparison)
- **Key terms:** exhausted ballots, center squeeze, wasted votes, the method scorecard.
- **Episode:** flagship Segment 6; `Why_STAR_Voting.md` Part 2 Tier 1.
- **Files:** any 4-candidate file with `show_irv` → the `[Divergence from STAR]` block.

## 201.5 — Multi-winner intro: Bloc STAR
- **Objective:** Electing several seats with a majoritarian/at-large method.
- **Key terms:** Bloc STAR, seats, at-large.
- **Files:** `02_Multi_winner/01_c4_b2_bloc-star-2-seats.yaml`.
- **Emphasize:** a cohesive majority can sweep all seats — which motivates 301's proportional methods.

---

# Voting 301 — Advanced (proportional, criteria, debate theory)

> Audience: skeptics, academics, RCV advocates, deep self-study. Concede limits
> honestly; that candor is the credibility.

## 301.1 — Proportional STAR (and STV)
- **Objective:** Give a cohesive minority the representation it earned.
- **Key terms:** proportional representation, Droop quota, Allocated Score, Sequentially Spent Score (SSS), Reweighted Range Voting (RRV), STV.
- **Files:** `02_Multi_winner/02a–02c` (allocated / sss / rrv). Compare with Bloc STAR.
- **STV comparison:** `02_Multi_winner/03a_stv_3seats.yaml` (STV) vs `03b_star_pr_3seats.yaml` (STAR-PR) — same electorate, same proportional slate; Bloc STAR differs. Page: `concepts/proportional_representation/` (STV vs STAR-PR + STAR-PR methods).
- **Emphasize:** STV is the proportional multi-winner *cousin of IRV*, not IRV; proportional methods seat coalitions in proportion, Bloc STAR lets a majority sweep.

## 301.2 — Favorite betrayal: does *only* "RCV" avoid it?
- **Key terms:** Favorite-Betrayal Criterion, Later-No-Harm, center squeeze, the incompatibility theorem.
- **Episode:** `favorite_betrayal_voting_301.md`; `Why_STAR_Voting.md` Part 2 #12.
- **Emphasize:** neither STAR nor RCV-IRV is FBC-proof; RCV-IRV fails it structurally (Alaska '22), STAR only in lab cases.

## 301.3 — "Are equal-score votes discounted?"
- **Key terms:** Equal Support / No Preference, exhausted vs no-preference.
- **Episode:** `are_equal_score_votes_discounted.md`; demo `01_Single_winner/equal_support_runoff_demo.yaml`.
- **In the result display:** [`concepts/STAR_Voting/runoff_percentages.md`](./concepts/STAR_Voting/runoff_percentages.md)
  shows exactly where Equal Support lands in BetterVoting's runoff — counted in full in
  the score round, then set aside to form the "voters with a preference" denominator (so
  the winner's majority is of the decided voters, not of everyone).

## 301.4 — The honest limits & theory
- **Key terms:** Gibbard / Gibbard–Satterthwaite, strategy resistance vs proofness, Condorcet efficiency, Test of Balance.
- **Material:** `Why_STAR_Voting.md` Part 2 Tier 2–3; "resistant, not proof."

## 301.5 — The vote-splitting formula (blocs)
- **Objective:** Confirm a spoiler in numbers for a declared bloc.
- **Material:** the `blocs:` field + `[Vote-splitting check]` (see the engine); `split_voting/`.

## 301.6 — When Condorcet, Score, and Runoff disagree (and how often)
- **Objective:** "Winner" isn't one thing — three reasonable definitions can name three
  different candidates; STAR targets the runoff winner *by design* (it is not a Condorcet method).
- **Material:** `concepts/STAR_Voting/STAR_three_winner_notions.md` (CW = Ann, Score = Carl,
  Runoff = Bob); builds on the 101 Runoff Reversal lesson `01_Single_winner/runoff_overturns_leader/`.
- **Frequency:** `simulations/runoff_reversal_simulation.py` measures how often score and
  runoff diverge — and shows the rate swings with the model (impartial vs spatial), the
  electorate size, and the tie rule. **Lesson: never quote a rate without the model + size + tie split.**
- **Emphasize:** the methodological habit (measure it, report the assumptions) is as much
  the point as the numbers.

## 301.6 — "Exhausted ballots": what FairVote's word hides
- **Objective:** Untangle the overloaded RCV-IRV term — separate the fair, voter-side
  cases from the method-caused ones a fully and correctly ranked ballot still suffers.
- **Key terms:** ballot exhaustion, inactive ballot, exhausted-untransferable,
  nonexhausted-untransferred, ranking limit, majority-of-remaining-ballots.
- **Episode:** `exhausted_ballots_301.md`; contrast `are_equal_score_votes_discounted.md`.
- **Emphasize:** exhaustion is **IRV**-specific (Ranked Robin reads every rank); STAR
  counts every ballot in both rounds, so nothing exhausts.

---

## Suggested pacing by audience

- **Public talk (15–20 min):** 101 only (0 → 1 brief → 2 → payoff). Skip theory.
- **Workshop (60–90 min):** all of 101 + 201.1–201.4, hands-on with the files.
- **Officials / administrators:** 101.0, then 201.1 (summability/audit) + the scorecard.
- **Academic / skeptic / RCV advocate:** 101 fast, then 301 with the precise caveats.

## Designing your own examples
See [TIPS_choosing_voter_counts.md](./TIPS_choosing_voter_counts.md) (voter counts)
and [ORGANIZATION.md](./ORGANIZATION.md) (where scenario text lives, clean-demo
flags). Term definitions: [GLOSSARY.md](./GLOSSARY.md).
