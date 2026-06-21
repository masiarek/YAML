# "Exhausted Ballots" — What FairVote's Word Actually Hides
### Voting 301 · advanced · an RCV-IRV misconceptions reference

The deepest RCV-IRV terminology trap, so this file goes slow. If you remember one
thing:

> **"Exhausted ballot" is ONE word stretched over several very different things.**
> That vagueness is the whole problem: it lets proponents wave the issue away by
> pointing at the harmless cases, while the *method-caused* cases — where a voter
> ranked everyone correctly and still had rankings thrown out — hide under the same
> label.

This is a **clarity** document, not a hit piece. We state FairVote's own
definition and steelman their defense, then show the distinctions they leave out.
Throughout, the contrast is STAR: **STAR counts every ballot in both rounds, so
nothing is ever "exhausted."**

Cues: **[DEMO]** run a file · **[SLIDE]** show a slide · **[REPO]** lesson file.

---

## 1. Precision first: exhaustion is an **IRV** thing, not a ranked-ballot thing

The single most useful correction: ballot exhaustion is a property of **IRV's
eliminate-and-transfer count**, *not* of ranked ballots in general. The *same*
ranked ballot, counted by **Ranked Robin** or any Condorcet method, reads **every**
ranking — nothing exhausts. Most voters actually assume that's how their ranked
ballot is counted; almost everywhere it isn't (it's IRV).

So the precise sentence is *"**RCV-IRV** has exhausted ballots,"* never *"RCV has
exhausted ballots."* (See `00_start_here/TIPS_terminology.md`.)

---

## 2. What "exhausted" actually conflates — the taxonomy

FairVote's own definition (their FAQ) gives three reasons a ballot goes "inactive /
exhausted": (1) the voter didn't rank all candidates and all their ranked
candidates got eliminated — *"voluntary abstention,"* their most common case; (2)
an administrator **ranking limit** (e.g. cap of 3) eliminated all their ranked
candidates — *"involuntary";* (3) ballot **error**, e.g. the same rank twice (rare).
Accurate as far as it goes — but it blurs two very different buckets:

**Bucket A — "this can happen under Choose-One too" (mostly voter-side):**
- **Overvotes** — marking two candidates at one rank; spoils that rank.
- **Undervotes / skipped ranks** — note the trap: in Choose-One an *undervote* is a
  blank, uncounted ballot; in RCV-IRV an "undervote" is a *single skipped ranking*,
  and the ballot may still count. Same word, different thing.
- **Voluntary truncation / bullet voting** — the voter chose to rank only one or a few.

These are roughly comparable to a Choose-One voter who skips the race or backs a
sure loser. Concede them; they're not the interesting part.

**Bucket B — "purely a product of the elimination count" (the ones glossed over):**
- **Involuntary truncation (ranking limits).** You'd have ranked more, but the
  ballot only allowed 3–5; all of them got eliminated. You did nothing wrong.
- **Exhausted-untransferable.** Your *lower* choices were eliminated *before* your
  favorite, so when your favorite finally loses, the vote has nowhere left to go.
- **Nonexhausted-untransferred.** Your top *remaining* choice reaches the final
  round and **loses** — your lower preferences are simply never read, because
  counting stopped. (This one isn't even *labeled* "exhausted," yet the rankings
  still don't count — which is exactly why the famous promise is false.)

Bucket B is the part that's *purely* an artifact of IRV's round-by-round
elimination. A voter who ranked everyone, correctly and completely, can still have
real preferences discarded. *(On the Exhausted Ballots deck these are the **yellow**
box = ranking-limit truncation, **red** box = exhausted-untransferable, and **blue**
box = nonexhausted-untransferred.)*

> [SLIDE] **Exhausted Ballots** (deck) — the red-box / blue-box flow chart (see
> `interviews_conversations/LINKS.md`).
> [REPO] full source notes: **Exhausted Ballots (doc)** in `LINKS.md`.

---

## 3. The false claim that the vague word protects

The line you'll hear: **"If your first choice is eliminated, your next choice will
be counted."** It is false, and the fuzziness of "exhausted" is what lets it pass:

- If your favorite makes the **final two and loses**, your other rankings are
  *never read* — that's the nonexhausted-untransferred case.
- Your next choice may **already be eliminated** by the time your vote is free to
  move, so it transfers to nobody.
- Even the softer phrasing — *"next choice"* instead of *"second choice"* — is only
  *less wrong*, not right. And note the smuggled conflation of **"first choice"**
  with **"first round."**

The honest version is: *which* of your rankings get counted depends on the
**order of elimination** — something you can't see or control.

---

## 4. The "manufactured majority" — majority of *remaining* ballots

Because exhausted ballots leave the count, IRV's "50% + 1" is a majority of the
ballots **still active**, not of all ballots cast. **Alaska 2022 (US House special):**
when Begich was eliminated, **11,243 ballots exhausted**; Peltola's 91,266 votes were
**51.5% of the *remaining* ballots but only 48.4% of all Round-1 ballots** — a
"majority winner" on a shrinking denominator.

It's systematic, not a one-off. A peer-reviewed study (Burnett & Kogan, *Electoral
Studies*, 2015) of 600,000+ ballots across four California IRV elections found
final-round exhaustion from **~9.6% to 27.1%** (Oakland's 2014 mayoral race ~24%) —
and in **all four, the winner won with less than a majority of all ballots cast.**

---

## 5. The honest steelman — and the precise response

**FairVote's defense:** *"In Choose-One, every vote not for the winner is 'wasted'
too — so what's new?"* Fair, for **Bucket A**: a first-round bullet vote or a
spoiled ballot really is comparable to Choose-One. Concede that cleanly.

**The response:** the comparison breaks on **Bucket B**. Those losses happen in
**later** rounds, to voters who ranked **fully and correctly** — information they
*did* express is discarded purely because of the elimination order. Choose-One has
no equivalent, because Choose-One never asked for more than one mark. *That*
asymmetry — not the harmless first-round cases — is the real criticism, and it's
the one the overloaded word "exhausted" is so good at hiding.

---

## 6. The STAR contrast (the payoff)

This is why STAR sidesteps the entire mess: **STAR counts every ballot in both
rounds.** Nothing is eliminated, so nothing exhausts. And a STAR **"no-preference"**
ballot (equal scores on the two finalists) is the *opposite* of an exhausted one:
it's **present data** — a voter who *declared a tie* — that **still counted in the
scoring round** to help pick the finalists. It isn't missing information thrown
away; it's information that says "I'm equally happy with either."

That distinction — *declared tie* (STAR) vs *lost voice* (IRV exhaustion) — is the
hinge, and it's developed in full in the companion episode.

> [REPO] `interviews_conversations/are_equal_score_votes_discounted.md` — the
> STAR-side of this same contrast (Segment B: "declared tie vs lost voice").
> [DEMO] `01_Single_winner/equal_support_runoff_demo.yaml` — no-preference ballots
> that *picked the finalists*, then stayed neutral in the runoff.

---

## 7. The conversation (Larry ↔ Adam) — recording cut

**Larry:** RCV folks say "your vote always counts — if your first choice loses,
your next choice is counted." That sounds reassuring. True?

**Adam:** It's the most oversold sentence in the whole debate. It's only true if
your favorite is eliminated *early*. If your favorite instead makes the final two
and loses, none of your other rankings are ever read — the count already stopped.
And sometimes your second choice is gone before your vote can even move. So "your
next choice will be counted" is, for a lot of voters, just false.

**Larry:** But they call those ballots "exhausted," like the voter ran out of choices.

**Adam:** That's the sleight of hand. "Exhausted" is one word covering five
different situations — overvotes, skipped ranks, bullet votes, ranking limits, and
the elimination-order cases. Some are the voter's doing and totally fair. But
others happen to people who ranked everyone correctly, purely because of the order
candidates dropped out. Lumping all five under one fuzzy word lets you point at the
harmless cases and pretend the others don't exist.

**Larry:** And STAR?

**Adam:** STAR never eliminates anyone, so nothing exhausts — every ballot is read
in both rounds. The closest thing, an equal-score "no-preference" ballot, is a
voter telling us they like both finalists the same. That's *information*, and it
still counted to pick the finalists. It's a declared tie, not a lost voice.

---

## 8. How to deploy it

- **Don't open with this.** It's 301, and it requires the audience already grasp
  IRV's round-by-round elimination. With a general audience, the one-liner
  ("declared tie, not lost voice") is enough.
- **Lead by splitting the word.** Half the disagreement evaporates the moment you
  separate Bucket A (fair) from Bucket B (method-caused).
- **Concede Bucket A immediately** — the candor is what earns the room for Bucket B.
- **End on STAR, not on RCV's flaws:** "counts every ballot, in both rounds."

---

## Where this fits in the overall teaching

- **Level:** Voting 301 — pairs with `favorite_betrayal_voting_301.md` (the *other*
  IRV-internals deep dive) and `are_equal_score_votes_discounted.md` (the STAR
  no-preference side of this exact contrast).
- **Terminology:** strictly **RCV-IRV / IRV** here — exhaustion is IRV-specific;
  Ranked Robin and the Condorcet methods read every ranking.

Cross-references:
- `00_start_here/GLOSSARY.md` — "Exhausted ballot," "Equal Support / No Preference."
- `00_start_here/TIPS_terminology.md` — exhaustion is IRV-specific, not all RCV.
- `00_start_here/CURRICULUM.md` — 301.6.
- `LINKS.md` → **Exhausted Ballots (doc)**, **Exhausted Ballots (deck)**,
  **Full Deck 2025** ("Ranked Choice Deal Breakers" / exhausted-ballot slides), and
  the **RCV-IRV exhausted-ballot source notes** group (wasted-votes glossary,
  ranking-limit, definition, tabulation-transparency, commentary).

<!-- Sourced facts (verified 2026-06): Alaska 2022 US House special — 11,243
ballots exhausted on Begich's elimination; Peltola 91,266 = 51.5% of remaining /
48.4% of Round-1 ballots (Alaska Div. of Elections RCV tabulation; arXiv 2303.00108).
Final-round exhaustion 9.6%–27.1% across four California IRV elections, winner < a
majority of all ballots cast in all four: Burnett & Kogan, Electoral Studies 2015
(SSRN 2519723; 600,000+ ballots; Oakland 2014 mayoral ~24%). FairVote's 3-reason
definition: fairvote.org RCV FAQ. -->

# file: exhausted_ballots_301.md
