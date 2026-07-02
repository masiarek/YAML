# "Aren't Equal-Score Votes Just Discounted?"
### A recorded conversation — Larry (channels the critic) & Adam (expert)

An **objection-handling** episode. The FairVote line is that a STAR ballot which
scores both finalists the same (e.g. 5/5) is "discounted" — ignored in the
runoff. Larry plays the skeptic; Adam answers honestly: concede the mechanical
point, reframe the meaning, contrast it with RCV-IRV's exhausted ballots, and be
candid about the one place the criticism actually has weight.

This is **Tier 2–3 / debate-prep material** — for skeptics and the RCV crowd, not
a first-contact public talk. See "Where this fits" at the end.

Cues: **[DEMO]** run a file live · **[SLIDE]** show a slide · **[REPO]** lesson file.

---

## Segment A — the accusation

**Larry:** Here's the criticism I keep hearing, and honestly it sounds damning.
In STAR, if I score both finalists a 5, my ballot is tagged "no preference" and
ignored in the final count. So a bunch of ballots — sometimes a lot of them —
don't count in the round that picks the winner. Isn't that just a discounted
vote?

**Adam:** I'm going to give you something you don't usually get in these debates:
I'll agree with the mechanical part, completely. If you score both finalists the
same, your ballot does not move the margin between them. That's true. Where I
part ways is the word "discounted," because it smuggles in a conclusion that
isn't true.

**Larry:** Go on — why isn't "discounted" fair?

**Adam:** Because "discounted" implies the voter tried to say something and the
system threw it away. That's not what happened. The voter looked at the two
finalists and said, explicitly, "these two are equal to me." The system recorded
that exactly. A tie vote can't break a tie — but it wasn't ignored, it was
*counted as what it was*: **Equal Support** — neutral between those two. (That's the
exact label STAR's runoff gives it: "Equal Support," aka Equal Preference / No <!-- terminology-ok: documents the aka -->
Preference.)

**Larry:** And "Equal Support" is one bucket for everyone who tied the two finalists?

**Adam:** One label, two honest opposites inside it. Some scored *both* finalists
high — "I'd be glad with either." Some scored *both* low — "I wanted neither of
these two." Either way it's no preference *between these two*, and either way it was
counted in the scoring round that chose the finalists. On a results pie it's the
thin slice that makes the two finalists' shares add up to a bit under 100% — present
voters, not missing ones. It's also exactly what the STAR ballot's own instruction
means — *"equal scores indicate no preference"* is about the **runoff**, not the
scoring round, where those ballots counted in full.

> [SLIDE] Full Deck — "NO-PREFERENCE VOTES IN THE STAR RUNOFF."
> [SLIDE] STAR-vs-RCV Template — the "Results" pie ("Supported both" ★ / "Supported
> neither" ✗, both = Equal Support).

---

## Segment B — the key reframe (declared tie vs lost voice)

**Larry:** But my critic would say: the voter clearly cared — they gave both a 5!
That's strong support, and it bought them nothing in the final round.

**Adam:** Here's the exact comparison to make. In RCV-IRV, if you don't rank the
two finalists — maybe you ran out of rankings, maybe the ballot only allowed three —
your ballot is *exhausted*: set aside because the system doesn't know what you
think about A versus B. Nobody calls *that* discounted, even though it's a voter
whose voice genuinely dropped out.

A STAR equal-score ballot is the opposite situation. The system knows exactly
what you think about A versus B — you told it they're equal. So the one-liner is:

> **In RCV-IRV, an exhausted ballot is a voter who lost their voice.
> In STAR, an equal-score ballot is a voter who declared a tie.**

**Larry:** So one is missing data and the other is present data that says "tie."

**Adam:** Exactly. One ran out of information; the other supplied information that
happens to be neutral. Treating "I am equally happy with either winner" as a
*failure* is the part of the criticism that doesn't survive contact.

> [REPO] `00_start_here/GLOSSARY.md` — "Equal Support", "Exhausted ballot."

---

## Segment C — but they ARE counted (the demo)

**Larry:** Prove to me these ballots actually did something. Show me they're not
just dead weight.

**Adam:** Let's run an election where the equal-score ballots are the reason the
finalists exist.

> [DEMO] `01_Single_winner/equal_support_runoff_demo.yaml`
> 100 voters. 40 score **both A and B a 5** (love both, C=0). 35 prefer A
> (A=5, B=3). 25 prefer C.
> - **Scoring Round:** A and B have the top totals and advance — and it's those
>   40 equal-A-B ballots that pushed them both over C. *They picked the
>   finalists.* That's them being counted.
> - **Automatic Runoff:** A beats B, decided by the 35 voters who actually
>   preferred one. The 40 equal ballots (and the 25 C-voters who scored both
>   finalists 0) are "Equal Support" — neutral, because they *are* neutral.

**Adam (after demo):** So those ballots were fully counted in round one — they
literally chose who's in the final — and then they were neutral in round two,
because their voters had no preference there. "Counted in both rounds, decisive
in neither tie they had no stake in" is a very different story than "discounted."

---

## Segment D — the honest concession (where the critic has a point)

**Larry:** You said you'd be honest about where this criticism lands. Where does
it?

**Adam:** The coarseness of the scale. Here's the real version of the objection,
and it's legitimate: suppose I like A a *tiny* bit more than B, but I think
they're both excellent — and I want to make sure they both beat C. On a 0–5
scale I might give both a 5 to keep them strong. Now I've genuinely got a
preference, A over B, but I recorded a tie. The ballot design failed to capture
a real preference I had.

**Larry:** So in that case it *is* a kind of self-inflicted discount.

**Adam:** Yes — and I won't pretend otherwise. In one Oregon Independent Party
race, nearly 30% of ballots landed as "no preference" in the runoff, and some of
those were surely people who had a faint preference but maxed both out. That's a
fair, objective criticism of *cardinal scales with few levels*. The honest answer
is: score your true preference order between the front-runners — if you like A
more, give A the 5 and B a 4. The runoff only works if you show the gap you feel.

> [SLIDE] Full Deck — "COMBATTING STRATEGIC VOTING" (show your preference order
> between the frontrunners).

---

## Segment E — the counter (RCV-IRV wastes votes in worse ways)

**Larry:** Okay, but doesn't this still mean STAR "wastes" votes, just like the
thing it criticizes RCV-IRV for?

**Adam:** No — and here's the asymmetry. A STAR equal-score ballot is *voluntary
neutrality*: the worst case is a voter who maxed two candidates they both love.
RCV-IRV's wasted votes are *involuntary* and they hit voters who had explicit
preferences:
- **Voter errors / voided ballots** — equal or skipped rankings can spoil the
  whole ballot, and that falls hardest on marginalized voters.
- **Favorite eliminated in the final round** — if your favorite makes it to the
  last two and loses, your other rankings are never counted at all.
- **Your next choice already gone** — by the time your vote is ready to transfer,
  the candidate it would've gone to may already be eliminated.

So the move in a debate is: concede the equal-score mechanic, then ask the critic
to account for *those* — the ones where a voter had a real preference and the
system still threw it out. That's not symmetric.

> [SLIDE] Full Deck — "RANKED CHOICE DEAL BREAKERS" and the exhausted-ballot
> slides; Torrance deck — the scorecard row "Wasted Votes / Exhausted Ballots."
> [REPO] `00_start_here/Why_STAR_Voting.md` Part 2 — Tier 1 #4 (usability /
> exhausted ballots).

---

## Segment F — close

**Larry:** Give me the sentence I can repeat.

**Adam:** "An equal-score ballot isn't a discounted vote — it's a voter who told
us, in their own hand, that they're equally happy with either finalist. It was
counted in the round that picked the finalists, and it stayed neutral in the one
tie it had no stake in. If you *do* have a preference, STAR rewards you for
showing it — so show it."

---

## Where this fits in the overall teaching

This is **not** an introductory beat — don't raise "discounted votes" with a
first-contact audience; you'd be planting a doubt they didn't have. Place it as:

- **A standalone debate-prep clip** (Episode 11 in the series roadmap), released
  for the skeptic / RCV-advocate audience.
- **A pull-out you only deploy when asked.** In the flagship script
  (`whats_so_good_about_STAR_Voting.md`), it hangs off **Segment 4** (where
  "Equal Support" is first introduced) and **Segment 7** (STAR vs RCV-IRV). Add a one-
  line pointer there: *"If someone pushes the 'discounted votes' line, see the
  Equal-Support episode."*
- **Mapped to the debate tiers** in `Why_STAR_Voting.md`: it's the runoff/Equal-
  Support counterpart to Tier 3 #9 (later-no-harm / center squeeze) — same shape,
  concede-then-reframe-then-counter.

Cross-references: `LINKS.md` →
**"Discounted votes — RCV-IRV FairVote False Talking Points"**,
**"Equal Support vs Equal Preference"**, **"Exhausted Ballots"**. <!-- terminology-ok: slide titles -->
