# Our Voting System Is Broken — The Problem with Plurality
### A recorded conversation — Larry (host) & Adam (expert) · Voting 101 · foundational

The **diagnosis** episode — the "why fix anything at all?" that comes *before* the
spoiler-effect mechanism and the STAR pitch. Larry presses on whether the problem
is real, frequent, and serious; Adam concedes what's true, then shows why
Choose-One Plurality can't be trusted to find the majority's choice — and how STAR
settles it on a single ballot.

Cues: **[DEMO]** run a file live · **[SLIDE]** show a slide · **[REPO]** lesson file.

---

## Segment 1 — Is the system actually broken?

**Larry:** You keep saying "our voting system is broken and needs fixing." Before I
buy the fix, sell me the problem. Is our current system actually prone to failure?
And if it is — have these failures been *frequent*? Were they *serious* when they
happened? Are they likely to get *worse*?

**Adam:** Four fair questions, and I'll take them honestly. The fundamental problem
with Choose-One Plurality isn't really in dispute: the rules allow a candidate who
is the *least* preferred choice of a majority of voters to be declared the winner.
A majority can be against you and you can still win — just by leading a divided
field. Nobody seriously argues that's democratic; it plainly violates majority
rule. The only open question is the one you put your finger on: is it worth doing
something about?

> [SLIDE] Full Deck — "PROBLEM: VOTE-SPLITTING"; Arend (Torrance) — "SPOILER EFFECT."
> [REPO] `00_start_here/GLOSSARY.md` — "Choose-One / Plurality," "Plurality / minority winner."

---

## Segment 2 — "But usually the front-runner really is the favorite, right?"

**Larry:** Come on — most of the time the person with the most votes really is the
one most people want. Isn't this a problem on paper more than in practice?

**Adam:** Usually, yes — and I won't pretend otherwise. When you have richer
ballots to check against, the plurality front-runner *usually* does turn out to be
the broader choice too; in Australia's ranked elections the first-preference leader
goes on to win about **90%** of the time. But flip that around: roughly **one race
in ten** is decided differently once you look past first choices. And here's the
catch — a Choose-One ballot gives you **no way to tell which kind of race you're
in.** You can't know, from the marks on the ballot, whether your plurality winner
is the majority's real choice or an accident of vote-splitting.

**Larry:** So the ballot itself hides the answer.

**Adam:** Exactly. That hidden answer is precisely what STAR puts back on the table —
but hold that thought for a second.

> [REPO] `00_start_here/GLOSSARY.md` — "Condorcet winner," "Head-to-head / pairwise."

---

## Segment 3 — How often, and how serious? (the two-party mask)

**Larry:** If it's only one in ten, why has nobody noticed?

**Adam:** Because for decades two dominant parties *masked* it. Squeeze almost every
race into two big tents and you rarely see a third candidate split the vote — the
flaw was real but invisible. That's been changing. The moment serious independents
show up — Perot-style or otherwise — we snap right back to plurality winners
instead of majority winners. In 1992, with Perot in the race, Bill Clinton won an
outright *majority* of the popular vote in exactly **one state — his home state of
Arkansas** (plus the District of Columbia). Every other state was carried with a
plurality, not a majority: a president elected while 49 states out of 50 never gave
*any* candidate more than half their vote.

**Larry:** So it's not a fluke of one strange year.

**Adam:** It's structural. The instant voters have more than two real choices —
which is exactly what most people *say* they want — Choose-One starts handing out
minority winners and punishing the voters who dared back a third option. That's
vote-splitting and the spoiler effect, and as the two-party grip loosens it's
getting *more* common, not less. So: prone to failure, yes; serious when it
happens, yes; and trending worse. That's three yeses — which is why it's worth
fixing.

> [DEMO] `split_voting/01_political_left_split.yaml` — a 60–66% coalition splits and
> Choose-One hands the seat to a candidate the majority ranked last; the
> `[Vote-splitting check]` block says it in numbers.
> [REPO] the spoiler mechanism in detail: `whats_so_good_about_STAR_Voting.md`
> Segment 1, plus the `split_voting/` demos.

---

## Segment 4 — How STAR fixes it (the pivot)

**Larry:** Okay, I feel the problem. Why is STAR the answer, and not just "try harder"?

**Adam:** Because STAR removes the two things that break Plurality. First, you're
never punished for honesty: you score every candidate 0–5, so backing your favorite
*and* a compromise can't split your own side. Second — and this answers your earlier
question directly — STAR doesn't just *hope* the winner has majority support, it
*checks*. The automatic runoff is a head-to-head majority test between the top two,
and the preference matrix shows you exactly who beats whom. The very thing
Choose-One hides — "is this winner actually the majority's choice?" — STAR prints
right on the result, from one single ballot.

**Larry:** So "is the plurality winner the real winner?" stops being a guess.

**Adam:** Right. Under Choose-One you *can't know*. Under STAR you *read it off the
result.* That's the whole difference between hoping for majority rule and measuring
it.

> [DEMO] `split_voting/04_star_wars_vote_split.yaml` — Choose-One elects Vader (40%,
> the candidate 60% ranked last); STAR elects Leia, the majority's real choice, and
> the `[Divergence from STAR]` line shows **Choose-One (Plurality)** disagreeing with
> STAR while STAR matches the Condorcet (head-to-head) winner.
> [SLIDE] Full Deck — "THE VOTING DILEMMA" (Skywalker / Vader / Leia).

---

## Segment 5 — The one-liner

**Larry:** Give me the sentence I can repeat.

**Adam:** "Choose-One can crown the candidate a majority likes *least*, and the
ballot itself won't tell you when that's happened. STAR refuses to split your vote,
then *proves* the winner has majority support — on one ballot, in plain sight."

---

## Where this fits in the overall teaching

- **Level:** Voting 101 — **foundational**. This is the *diagnosis*; play it before
  the spoiler-effect mechanism and the STAR pitch.
- **Pairs with:** the spoiler effect (flagship Segment 1 / roadmap Episode 2) and
  the `split_voting/` demos — this episode argues *that* the system is broken; those
  show *how*. Then `whats_so_good_about_STAR_Voting.md` delivers the fix.
- **Terminology:** keep it `Choose-One` / `Plurality` for a public audience; the
  point is method-accurate for Plurality specifically. (Reworked from a classic
  pro-reform passage that originally leaned on IRV; here the resolution is STAR's
  majority runoff + preference matrix, which answer "is the plurality winner the
  real winner?" directly, on one ballot.)

Cross-references:
- `00_start_here/GLOSSARY.md` — "Choose-One / Plurality / First-Past-The-Post,"
  "Plurality / minority winner," "Vote splitting," "Spoiler effect," "Majority finish."
- `00_start_here/Why_STAR_Voting.md` — Part 1 problem bullets.
- `interviews_conversations/whats_so_good_about_STAR_Voting.md` — Segment 1 (the spoiler).
- `LINKS.md` → **Full Deck 2025** ("PROBLEM: VOTE-SPLITTING," "THE VOTING DILEMMA"),
  **Torrance LWV (Arend)** ("SPOILER EFFECT").

<!-- Sourced facts: Clinton 1992 won an absolute majority of the popular vote only
in Arkansas (53.2%) and DC (every other state a plurality). In Australian IRV
elections the first-preference leader wins ~90% of seats (≈1 in 10 differ from
first-past-the-post). -->

# file: our_voting_system_is_broken.md
