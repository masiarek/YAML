# Favorite Betrayal — Does *Only* RCV Avoid It?
### Voting 301 · advanced · the deep-dive behind Slide 4

This is the hardest-to-keep-straight idea in the whole STAR-vs-RCV debate, so this
file goes slow and over-explains on purpose. If you only remember one thing:

> **"Favorite Betrayal" and "Later-No-Harm" are two DIFFERENT promises. RCV-IRV keeps
> the second one and breaks the first. People — including RCV advocates — mix
> them up constantly.**

---

## 1. The context — what was actually challenged

**The slide.** In the deck `00_start_here/Why_STAR_Voting.md`, **Slide 4** is titled
**"You Never Have to Betray Your Favorite,"** with bullets like *"Score both high —
no forced ranking, no wasted vote"* and *"Honesty is your best ballot."*

**The challenge (Adam → the slide).** "This isn't *completely* true, right? And
RCV-IRV proponents claim that **only** in IRV do you never betray your favorite,
and that STAR *can* make you betray your favorite. Are they right?"

**The short answer.** The slide is true in the everyday, practical sense, and
overstated only as a strict theorem. And the RCV-IRV claim is **false** — RCV-IRV does
*not* protect you from favorite betrayal; it protects a *different* thing. Below
is why, with numbers.

---

## 2. Two promises that sound identical but aren't

Imagine you sincerely like **A (favorite) > B (compromise) > C (worst).**

### Promise A — Favorite Betrayal Criterion (FBC)
> *"It is always safe to support your favorite the most. You never get a better
> result by pretending someone else is your favorite."*

A method **passes FBC** if you can always put A at the top (rank 1, or score 5)
without that choice ever backfiring. A method **fails FBC** if there are
situations where you'd get a better outcome by *insincerely* ranking/scoring B
above A — i.e., **betraying** your favorite A.

### Promise B — Later-No-Harm (LNH)
> *"Adding or raising a LOWER choice can never hurt your favorite."*

A method **passes LNH** if marking B and C *at all* (after A) can never cause A to
lose. It **fails LNH** if expressing support for your second choice can pull the
win away from your first choice.

### The crucial difference
- **FBC is about your FIRST mark** — is it safe to put your favorite on top?
- **LNH is about your LATER marks** — is it safe to also support your backups?

They are not the same question, and — this is the punchline — **no voting method
can satisfy both at once** (Section 6). So every method has to give up at least
one. RCV-IRV gives up FBC. Cardinal methods (Approval/Score) give up LNH.

---

## 3. Why everyone conflates them

When an RCV advocate says *"in Ranked Choice you never have to betray your
favorite,"* they are almost always describing the feeling of **Later-No-Harm**:
"I can rank my favorite first AND rank my backups, and ranking the backups won't
hurt my favorite." That part is true of RCV-IRV.

But "you never have to betray your favorite" is the **FBC** sentence, and RCV-IRV
**fails** that one. The advocate has swapped a true LNH claim for a false FBC
claim without noticing. Your job in a debate is to gently separate the two.

---

## 4. Worked example: RCV-IRV *fails* favorite betrayal (Alaska 2022)

This is the cleanest real-world proof. Three candidates, roughly on a spectrum:

- **Peltola** (Democrat / left)
- **Begich** (Republican / center-right)
- **Palin** (Republican / right)

**Approximate first-choice tally:**

| Candidate | First choices |
|-----------|---------------|
| Peltola | ~40% |
| Palin | ~31% |
| Begich | ~29% |

**What RCV-IRV does:** Begich has the *fewest* first choices, so he's **eliminated
first**. His ballots transfer (mostly to Palin, some to Peltola, some exhausted).
In the final round **Peltola beats Palin ~51.5% to 48.5%.** Peltola wins.

**But look at the head-to-heads (who beats whom one-on-one):**
- Begich beats Peltola (~53–47).
- Begich beats Palin (~61–39).

So **Begich beats *both* others head-to-head — he's the candidate a majority
actually preferred** (the Condorcet winner). RCV-IRV eliminated him in the first round
because few people ranked him *first*. That's the **center squeeze.**

**Now the favorite-betrayal part — the key move, read slowly:**

Take the **Palin voters.** They ranked Palin 1st (honest), Begich 2nd, Peltola
last. By being honest:
- Begich (their 2nd choice) got eliminated,
- Palin (their 1st) then lost the final,
- so they ended up with **Peltola — their LAST choice.**

If *enough* of those Palin voters had **betrayed Palin** and ranked **Begich 1st**
instead, Begich would not have been eliminated, and Begich would have **won**
(he beats Peltola head-to-head). Begich is their 2nd choice — strictly better than
Peltola, their 3rd.

> **Ranking their true favorite (Palin) first gave them their worst outcome.
> Betraying her gave them a better one. That is a favorite-betrayal failure — in a
> real, high-profile election.** RCV-IRV did exactly the thing its advocates say only
> it prevents.

(Burlington, Vermont 2009 is the same story with a left-leaning twist: Montroll
was the head-to-head winner, eliminated early for too few first-place votes.)

---

## 5. "But you admit STAR fails FBC too!" — yes, and here's the honest difference

Concede it cleanly: **STAR is also not formally FBC-compliant.** Equal Vote's own
pass/fail chart marks STAR ❌ on Favorite Betrayal — *but* at roughly **98%** (the
chart is binary; "98% is still a fail" under a pass/fail lens).

So why does STAR fail it at all, and why is that different from RCV-IRV?

**Where STAR's tiny FBC leak comes from — the runoff.**
- **Pure Score voting PASSES FBC.** You can always give your favorite a 5; since
  the winner is just the highest total, maxing your favorite can never hurt you.
- But pure Score has a different weakness: **exaggeration** ("I'll give my favorite
  5 and everyone else 0 to inflate them"). That distorts results.
- **STAR adds the automatic runoff to neutralize that exaggeration.** And it works
  — but the runoff is *also* what introduces the sliver of FBC vulnerability,
  because now your scores can change *which two candidates are finalists*, and in
  rare, delicately balanced cases moving your favorite's score can change the
  finalist pairing in a way that helps you.

So STAR's ~98% FBC is a **deliberate trade**: it gives up a sliver of FBC to buy a
genuine majority finish and immunity to score-exaggeration.

**Why STAR's failure is in a different league than RCV-IRV's:**
- STAR's FBC failures are **rare and fragile** — they need near-perfect knowledge
  of how everyone else votes, and a wrong guess backfires. They essentially don't
  show up in real elections.
- RCV-IRV's FBC failure is **structural and common** — it's the *center squeeze*, and
  it bites exactly in the competitive 3-viable-candidate races reform is meant to
  fix (Alaska, Burlington). It's not a corner case; it's the main event.

> **One-liner:** *"Neither of us is favorite-betrayal-proof. You fail it in
> realistic center-squeeze races; STAR fails it only in rare, hand-built
> constructions you couldn't pull off in a real election."*

---

## 6. The theorem that ends the argument: you can't have both

**Favorite-Betrayal and Later-No-Harm are provably incompatible.** No deterministic
ranked or rated method can satisfy both at the same time. (Woodall-style
impossibility; the synced deck states it as *"Many criteria are mutually
exclusive, including 'Favorite Betrayal' and 'Later No Harm.'"*)

So *every* method must give up at least one:

| Method | Favorite Betrayal (safe to top your favorite?) | Later-No-Harm (safe to mark backups?) |
|--------|:---:|:---:|
| Choose-One Plurality | ❌ | n/a (only one mark) |
| **RCV / IRV** | **❌** (center squeeze) | ✅ |
| Approval | ✅ | ❌ |
| Score | ✅ | ❌ |
| **STAR** | ~98% (rare fails) | ~ (rare fails) |

Read across the STAR row: it refuses to fully commit to either, and instead lands
~98% on **both** — the "best of both worlds" compromise, by design.

**The reframe to leave them with:** Later-No-Harm sounds nice, but it's the very
property that *forces* center squeeze — guaranteeing your later choices never help
your favorite is mathematically the same as guaranteeing a broadly-liked
compromise can't be rescued by being everyone's strong second. STAR gives that up
on purpose, because "your honest support for a compromise should be allowed to
help elect them" is the *better* value.

---

## 7. The conversation (Larry ↔ Adam) — recording cut

**Larry:** An RCV friend told me Ranked Choice is the only system where you never
have to betray your favorite — and that STAR can force you to. True?

**Adam:** It's the most common mix-up in this whole debate, so let me pull two
ideas apart that sound like one. There's "is it safe to put my favorite *first*?"
— that's called Favorite Betrayal. And there's "is it safe to also mark my
*backups*?" — that's a different thing called Later-No-Harm. RCV-IRV keeps the second
promise. It does **not** keep the first.

**Larry:** Wait — RCV doesn't protect your favorite?

**Adam:** Not the way people think. Alaska, 2022. Begich beat both other
candidates head-to-head — a majority preferred him to each. But he had the fewest
*first*-place votes, so Ranked Choice eliminated him first, and a lot of voters who
honestly ranked Palin first ended up with Peltola — their *last* choice. If those
Palin voters had **betrayed** Palin and ranked Begich first, they'd have gotten
Begich — better for them. Ranking their true favorite first actively hurt them.
That's a favorite-betrayal failure, in a real election.

**Larry:** Okay, but doesn't STAR have this problem too? You're always honest with
me about the limits.

**Adam:** It does, technically — STAR isn't 100% favorite-betrayal-proof either,
about 98%. But here's the difference that matters. There's a theorem: no method can
promise both of those things at once, so everyone gives up one. Pure Score voting
keeps favorites perfectly safe but invites exaggeration; STAR adds a runoff to kill
the exaggeration, and that runoff is what costs it that last 2%. The failures are
rare, fragile, and basically impossible to exploit in a real election. RCV-IRV's
failure is the opposite: it's structural, it's the center squeeze, and it shows up
in exactly the competitive races we're trying to fix.

**Larry:** So the honest scorecard is…?

**Adam:** "Neither of us is favorite-betrayal-proof. You fail it in real
center-squeeze races; we fail it only in lab constructions. And what you're
*calling* 'no favorite betrayal' is actually a different promise — Later-No-Harm —
which we gave up on purpose, because honest support for a compromise *should* be
able to help them win."

---

## 8. How to deploy it

- **Don't open with this.** It's Voting 301. Raise it only when an RCV advocate
  makes the "only RCV avoids favorite betrayal" claim. With a general audience,
  Slide 4 stands on its own.
- **Lead by separating the two criteria** before you argue — half the disagreement
  evaporates once "first mark" vs "later marks" is on the table.
- **Concede STAR's ~98% immediately.** Your candor is the credibility that makes
  the center-squeeze point land.
- **End on the value, not the math:** Later-No-Harm *causes* center squeeze; STAR
  trades it away so a consensus candidate can actually win.

## 9. A mental model to hold onto

- **Favorite Betrayal** = *the front door.* Is it safe to walk your favorite in
  first? (RCV-IRV: no. Score/Approval: yes. STAR: almost always.)
- **Later-No-Harm** = *the back door.* Is it safe to let your backups in too? (RCV-IRV:
  yes. Score/Approval: no. STAR: almost always.)
- You **cannot** lock both doors. RCV-IRV locks the back and leaves the front open
  (center squeeze). STAR keeps both ~98% shut and refuses to fully sacrifice
  either.

---

## Cross-references
- Slide 4 in `00_start_here/Why_STAR_Voting.md` (the claim this defends) and its
  Part 2 talking point **#12**.
- `interviews_conversations/are_equal_score_votes_discounted.md` — the runoff /
  Equal-Support sibling of this concede-then-reframe argument.
- `LINKS.md` → **Full Deck 2025** ("RCV Common False Claims", "Alaska '22",
  "Burlington 2009", the pass/fail criteria slides); **Why STAR 2**.
