# STAR Voting — Glossary

One-line definitions for the keywords used across these lessons. Grouped from
beginner vocabulary to advanced theory.

## Core vocabulary

- **STAR** — Score Then Automatic Runoff: score every candidate 0–5; the two highest totals advance to an automatic head-to-head runoff.
- **Score / star rating** — a 0–5 value expressing *how much* you support a candidate (like a five-star review).
- **Scoring round** — STAR's first round: add up each candidate's scores; the top two become finalists.
- **Finalists** — the two highest-scoring candidates, who advance to the runoff.
- **Automatic runoff** — STAR's second round: each ballot counts as a full vote for whichever finalist it scored higher; the preferred finalist wins.
- **Head-to-head / pairwise** — a direct comparison of two candidates: which one more ballots scored higher.
- **Equal Support / Equal Preference** — scoring two candidates the same; counts as "no preference" between them in the runoff.
- **Scored (cardinal) ballot** — rates each candidate independently 0–5; equal ratings allowed.
- **Ranked (ordinal) ballot** — orders candidates 1st, 2nd, 3rd; no ties, no degree of support.

## The problem STAR addresses

- **Choose-One / Plurality / First-Past-The-Post** — vote for exactly one candidate; most votes wins. Accurate only with two candidates.
- **Vote splitting** — similar candidates divide their shared supporters, letting a less-preferred candidate win.
- **Spoiler effect** — a candidate who cannot win still changes who does, by splitting another's support.
- **Favorite betrayal** — being pressured to score/rank a front-runner above your true favorite.
- **Lesser-evil voting** — backing a tolerable front-runner instead of your favorite to block a worse outcome.
- **Wasted vote** — a vote that has no effect on the result.
- **Two-round system** — separate primary + general/runoff elections; STAR does both jobs on one ballot.
- **Plurality / minority winner** — a winner with the most votes but less than majority support.

## Mechanics

- **Equal scores allowed** — you may give two candidates the same score; you're never forced to invent a preference.
- **Exhausted ballot** — (a ranked-method term) a ballot discarded mid-count because it ranked no remaining candidate; STAR's runoff doesn't discard ballots this way.
- **Tiebreaker** — a rule that resolves ties (for the finalists or the runoff); here, candidate priority / lot order.
- **Undervote / abstention** — a ballot that scores no one (blank or `~`); counts as turnout but supports no candidate.

## Properties & criteria

- **Majority finish** — STAR's runoff guarantees the winner beats the runner-up among voters who expressed a preference between them.
- **Condorcet winner** — the candidate who beats every other head-to-head; STAR usually (not always) elects them.
- **Condorcet efficiency** — how often a method elects the Condorcet winner (STAR's is very high).
- **Condorcet loser** — the candidate who loses every head-to-head.
- **Condorcet compliance** — *always* electing the Condorcet winner; STAR is **not** compliant (a deliberate tradeoff).
- **Center squeeze** — a broadly-liked moderate eliminated early for lacking first-choice support; an RCV-IRV failure STAR avoids.
- **Later-no-harm** — adding a lower preference never hurts your top choice; RCV-IRV has it, STAR intentionally does not.
- **Monotonicity** — raising a candidate on your ballot never causes them to lose (and vice versa).
- **Participation criterion** — voting honestly never yields a worse result than not voting.
- **Favorite-betrayal criterion** — you never gain by scoring someone above your favorite.
- **Summability / precinct-summable** — results can be computed by adding independent precinct totals (STAR can; RCV-IRV cannot).
- **Pairwise (For / Equal / Against) matrix** — the summable head-to-head table the runoff and audits use.
- **Strategyproofness** — no voter can ever gain by voting insincerely; impossible for any method (Gibbard).
- **Gibbard / Gibbard–Satterthwaite theorems** — proofs that every reasonable voting method is manipulable.
- **Strategy resistance** — how rarely and riskily strategy pays; STAR is resistant, not proof.
- **Equal Vote / Test of Balance** — any support a ballot expresses can be exactly cancelled by an opposite ballot; STAR's precise sense of equal weight.
- **One-person-one-vote** — equal voting weight. (Caution: the constitutional OPOV doctrine governs district population, not ballot expressiveness.)
- **Utilitarian vs majoritarian** — maximizing total support vs guaranteeing a majority; STAR blends both.

## Other methods (for contrast)

- **Approval voting** — score each candidate 0 or 1 (approve / not); most approvals wins.
- **Score voting (pure)** — score 0–5; highest total/average wins, with no runoff (more manipulable than STAR).
- **RCV (Ranked-Choice Voting)** — a ranked *ballot* type (rank candidates 1st, 2nd, 3rd). A **family**, not one method; in the US it's commonly (loosely) used to mean IRV specifically.
- **IRV (Instant-Runoff Voting)** — *one tabulation* of a ranked ballot: eliminate the lowest, transfer, repeat until a majority. The single-winner method usually meant by "RCV."
- **RCV-IRV** — disambiguating label for "the RCV that is IRV"; preferred in this repo for STAR-vs-method comparisons so it's clear we mean the eliminate-and-transfer method, not the ballot family.
- **Ranked Robin (RCV-RR / "Consensus")** — a Condorcet tabulation of the *same* ranked ballot (most head-to-head wins, Copeland-style). Has no center squeeze; do not lump it with IRV.
- **STV (Single Transferable Vote)** — the proportional, multi-winner tabulation of ranked ballots.
- **Condorcet method** — any ranked method that *always* elects the candidate who beats every other head-to-head (the Condorcet winner) when one exists. A **family**: Ranked Robin, Ranked Pairs, Schulze, Minimax, Copeland.
- **Ranked Pairs (Tideman)** — a Condorcet method: lock in the strongest pairwise victories first, skipping any that would create a cycle.
- **Schulze (beatpath)** — a Condorcet method that decides via the strongest "beatpaths" between candidates.
- **Minimax (Simpson–Kramer)** — a Condorcet method electing the candidate whose *worst* pairwise loss is the smallest.
- **Borda** — a positional ranked method (points by rank position). A ranked method but **not** Condorcet-compliant.
- **Bucklin (Grand Junction)** — a ranked, median-style method (add lower ranks until someone has a majority). Ranked but **not** Condorcet. (Spelled *Bucklin*, not "Buckling".)
- **Hare** — historically the ranked-transfer idea; single-winner = **IRV**, multi-winner = **STV** (Hare quota).
- **ballot vs tabulation** — the ballot is *what the voter marks* (ranked, or scored); the tabulation is *how it's counted* (IRV / Ranked Robin / STV for ranked; STAR / Approval / Score for scored). "RCV" names a ballot; "IRV" names a tabulation.
- **Condorcet method** — any method that always elects the Condorcet winner when one exists.
- **Bloc STAR** — multi-winner STAR that elects the top N candidates (at-large / majoritarian).
- **Proportional STAR** — multi-winner methods (Reweighted Range Voting, Allocated Score, Sequentially Spent Score) that give proportional representation.

## Civic / adoption

- **Equal Vote Coalition** — the organization that developed and advocates STAR Voting.
- **BetterVoting.com** — site to try a STAR ballot and run your own elections.

---

See also: [00_START_HERE.md](./00_START_HERE.md) (teaching sequence) ·
[Why_STAR_Voting.md](./Why_STAR_Voting.md) (presentation + debate prep) ·
[CURRICULUM.md](./CURRICULUM.md) (lesson outline).
