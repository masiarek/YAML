# What Is a Voting Method? — Ballot vs Count, Plurality vs Majority
### A recorded conversation — Larry (host) & Adam (expert) · Voting 101 · the foundation

The **primer** episode — the one that comes before everything. Before spoilers,
runoffs, or STAR, Larry and Adam settle what a "voting method" even *is*, and untangle
the two words people mix up most: **plurality** and **majority**. Keep this one slow
and friendly; every later episode assumes it.

Cues: **[DEMO]** run a file live · **[SLIDE]** show a slide · **[REPO]** lesson file.

---

## Part 1 — What is a voting method?

## Segment 1 — The two parts

**Larry:** Start at zero for me. What *is* a voting method?

**Adam:** It's the rule that turns a stack of individual ballots into one collective
decision. And the key thing — the single most useful idea in this whole topic — is
that it's really **two parts**, not one. First, **the ballot:** what voters get to
express — pick one, rank them, score them, or choose several. Second, **the count:**
how you turn those marks into a winner — add them up, average them, simulate a runoff,
or check who beats whom head-to-head.

**Larry:** And those two are independent?

**Adam:** The format is — the same ballot can be counted several different ways, and
they can crown *different* winners. A ranked ballot can be run as instant-runoff, or
as a Condorcet "who-beats-everyone" count, or proportionally. But here's the catch,
and it's the whole reason to name both parts: a method is a ballot **and** a count
working *together*, and you can't judge one without the other. The ballot is the easy,
likeable half — the part you're shown. The count is where the winner actually comes
from — and it's the half people get talked into ignoring.

**Larry:** So "ranked-choice" only tells me the ballot.

**Adam:** Exactly. Someone says "ranked-choice is great" and they've described the
*ballot* — they haven't told you how it's counted, which is the part that decides the
election. The trick isn't to admire the two parts apart; it's to never let them be
split — when someone praises a ballot, ask, "fine, now how do you count it?"

> [REPO] `CLAUDE.md` terminology policy and `00_start_here/GLOSSARY.md` —
> "Ballot," "Tabulation," "Voting method."

---

## Segment 2 — Why it matters that there's a choice at all

**Larry:** Does the method really change anything, or is it just plumbing that reports
what people want?

**Adam:** It's not neutral plumbing — it's part of what *decides* the outcome.
Different methods can pick **different winners from the exact same ballots.** That gap
is widest in two situations: when there are several similar candidates — that's where
"vote splitting" bites — and when opinion is polarized or the question's more
complicated than a simple yes/no.

**Larry:** So picking the method is itself a real decision.

**Adam:** Right. One honest, careful version of the claim: richer ballots — ranking
or scoring — can capture *more information* than choose-one, and that added
expressiveness matters more as the questions get harder. 

> [SLIDE] Full Deck — "Rating vs Ranking" (more expressive ballots carry more info).

---

## Part 2 — Plurality vs Majority

## Segment 3 — Two different bars

**Larry:** You always tell me to keep "plurality" and "majority" straight. What's the
difference?

**Adam:** They're two different winning thresholds. **Plurality** means the *most*
votes wins — even if that's well under half; that's "first-past-the-post" or
"choose-one." **Majority** means *more than half* — fifty percent plus one. In a
two-way race they're the same thing: the most votes *is* over half. The gap only
opens up with **three or more candidates.**

**Larry:** And that gap is where the trouble lives?

**Adam:** That gap *is* the trouble. Let me show you the smallest version.

> [REPO] `00_start_here/GLOSSARY.md` — "Plurality / minority winner," "Majority finish."

---

## Segment 4 — The 40% winner a majority voted against

**Larry:** Show me.

**Adam:** A hundred voters, three candidates. First choices: Andre forty, Blake
thirty-five, Carmen twenty-five. Under plurality, Andre wins — most votes. But look:
sixty of a hundred wanted *someone else.* Andre has no majority. And if Blake and
Carmen are two flavors of the same coalition, choose-one just **split** a
sixty-vote bloc and crowned the one candidate a majority actively opposed.

**Larry:** So the winner is the candidate most people were against.

**Adam:** Exactly — and a majority rule wouldn't accept that. Since nobody cleared
half, it demands another step: a runoff. STAR's automatic runoff is that step — after
scoring, the top two meet head-to-head, and the winner holds a majority *between those
two.* Said precisely: that's a majority over the other finalist — not a proof the
winner is everyone's favorite across the whole field, but exactly the thing plurality
never even checks.

> [DEMO] `split_voting/00_plurality_vs_majority.yaml` — Choose-One elects Andre
> (40%, a candidate 60% voted against); STAR elects Blake, the coalition's consensus.
> `[Divergence from STAR]` shows **Choose-One (Plurality) = Andre** disagreeing with
> STAR, and the `[Vote-splitting check]` prints the 60-vote coalition in numbers.

---

## Segment 5 — The two takeaways

**Larry:** Give me the lines I can walk away with.

**Adam:** Two of them. The first is the framing: *"A voting method is a ballot **and**
a count — and you have to judge them together. The ballot is the part you're shown;
the count is where the winner actually comes from. So when someone praises the ballot,
ask how it's counted."* The second is the warning: *"'Most votes' isn't 'over
half.' Choose-one plurality is the method that most easily crowns the candidate a
majority voted against."*

---

## Where this fits in the overall teaching

- **Level:** Voting 101 — **the foundation.** Play it before the "is the system
  broken?" diagnosis and the spoiler-effect mechanism; both assume ballot-vs-count and
  plurality-vs-majority are already clear.
- **Pairs with:** `our_voting_system_is_broken.md` (the diagnosis that builds on this)
  and `whats_so_good_about_STAR_Voting.md` (the fix). This episode is purely
  definitional — no STAR pitch yet beyond showing the runoff as "the majority step."
- **Terminology:** keep `Choose-One` / `Plurality` for a public audience. Hold the
  ballot-vs-tabulation distinction precisely — it's the spine of the whole curriculum.

Cross-references:
- `00_start_here/GLOSSARY.md` — "Ballot," "Tabulation," "Choose-One / Plurality /
  First-Past-The-Post," "Plurality / minority winner," "Majority finish," "Vote splitting."
- `interviews_conversations/our_voting_system_is_broken.md` — the next episode (1.5).
- `split_voting/00_plurality_vs_majority.yaml` — the live demo for Segment 4.
- `LINKS.md` → **Full Deck 2025** ("Rating vs Ranking," "Problem: Vote-Splitting").
- Source: Google Doc **"Voting Method - what is it?"** (the ballot/count framing and
  the Andre/Blake/Carmen plurality table this episode is built from).

<!-- Sourced framing: a voting method = ballot (what voters express) + count (how a
winner is derived); the two are independent. Plurality = most votes; majority = >50%;
they diverge only with 3+ candidates. STAR's automatic runoff yields a majority
between the two finalists (not a field-wide majority claim). -->

# file: what_is_a_voting_method.md
