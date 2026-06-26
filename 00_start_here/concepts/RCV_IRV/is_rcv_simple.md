# Is RCV "Simple"? — Which Half?

**One line:** ranking 1-2-3 really *is* simple to **mark** — but "simple" then gets
quietly borrowed for the whole method, when **IRV's count is the opposite of simple**.
STAR keeps *both* halves simple — and its ballot carries strength of support on top of
order.

→ Builds on [`what_is_a_voting_method.md`](../../../interviews_conversations/what_is_a_voting_method.md)
(a method = ballot **+** count) · related: [`summability.md`](../STAR_Voting/summability.md),
[`monotonicity.md`](./monotonicity.md) · step-by-step trace of both counts:
[`tabulation_star_vs_irv.md`](../tabulation_star_vs_irv.md) · Level **201**.

---

## The claim, and what's true about it

RCV advocates say: *"It's simple — look at the ballot, just rank 1-2-3."* And they're
**right about the ballot.** Marking a ranked ballot is intuitive; ranking is the easy
part. Concede that cleanly — you lose nothing.

The slip is in the next step. "Simple" is really **two different claims**, and only one
of them is true:

- **Simple to *mark*** — the ballot. True of ranking. (Also true of STAR.)
- **Simple to *count and trust*** — the tabulation. This is where "simple" gets
  borrowed for the whole method when it was only ever earned by the ballot.

A method is a ballot **and** a count (see the 101 page). "Look how simple the ballot is"
tells you nothing about the count — and the count is where the winner actually comes
from.

## Why IRV's count is the hard half

To find an IRV winner you can't just add a column. You:

1. tally everyone's **top remaining** choice;
2. if no one has a majority, **eliminate** the lowest and **transfer** each of those
   ballots to its next choice;
3. **recheck**, and **repeat** — round after round — until someone clears half.

To follow it you have to track every transfer across every round. Three consequences,
all working against "simple":

- **Not summable.** A precinct's IRV result doesn't compose with another's — you can't
  add subtotals, because who's eliminated depends on the *whole* electorate. So every
  ballot has to travel to **one central count.** (See [`summability.md`](../STAR_Voting/summability.md).)
- **Software-dependent and hard to hand-audit.** Rounds of transfers are not something
  poll workers reconcile on a precinct table; a recount means re-running the algorithm
  on all ballots at once.
- **Counterintuitive even when correct.** More support can *hurt* a candidate
  ([monotonicity](./monotonicity.md)) — so the count can behave in ways that are hard to
  explain to the voter whose ballot "did the opposite."

So the honest picture: *the ballot is simple; the count needs a computer and a central
tally.* That's the half "look how simple it is" leaves out.

## STAR is simple on *both* halves

**The ballot — at least as easy to mark:**
- 0–5 is the familiar **five-star** mental model (every rating app you already use).
  (Why a score ballot differs from a rank ballot: [`scores_vs_ranks.md`](../scores_vs_ranks.md).)
- You **rate each candidate on their own** — no forcing a complete strict order among a
  field of strangers ("is she my 4th or my 5th?").
- **Equal scores are allowed** — you can say "I like these two the same" (the repo's
  **Equal Support**). Standard IRV ballots forbid equal ranks, and many even cap how many
  you may rank.
- One ballot carries **both preference *and* strength** — order *and* how much — where a
  rank carries only order.

**The count — stays simple and summable:**
- **Round 1:** add each candidate's scores. A column sum. Precincts report totals, exactly
  like today.
- **Round 2:** one automatic runoff between the top two — a single head-to-head majority.

Two transparent steps you can do on a napkin and audit on a precinct table.

## See it — same winner, very different counts

→ [`01_Single_winner/count_simplicity_star_vs_irv.yaml`](../../../01_Single_winner/count_simplicity_star_vs_irv.yaml)
(45 voters, 5 candidates). Carmen, the broad consensus, wins under **both** methods — so
this isn't about who *should* win. It's about the *work the count takes.*

- **STAR** (`STARVote_LH_tabulation_engine/`): add the scores → Carmen & Andre are the top
  two → one runoff → Carmen. Done.
- **RCV-IRV** (`RCV_IRV_tabulation_engine/`): no first-round majority, so it eliminates
  Evan, transfers his ballots, rechecks; eliminates Dana, transfers, rechecks; *now*
  Carmen clears half — **three rounds** of eliminate-and-transfer for the same answer.

```
# run both on the one file:
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_Single_winner/count_simplicity_star_vs_irv.yaml
python3 RCV_IRV_tabulation_engine/rcv_irv_tabulation.py    01_Single_winner/count_simplicity_star_vs_irv.yaml
```

## How to say it (without attacking anyone)

Don't call it a "bait and switch" — you don't need to, and it sounds like motive-hunting.
Make it a precision point:

> *"Ranking is simple to mark — agreed, fully. But 'simple' belongs to the **ballot**, not
> the **count**. IRV's tabulation takes rounds of elimination, can't be added up from
> precinct totals, and needs software and a central count. STAR keeps the easy ballot
> **and** an addable count — and its ballot says how *much* you support each candidate,
> not just the order."*

Give credit on the ballot; hold the line on the count. That's the version no one can call
unfair.

---

## Cross-references
- [`what_is_a_voting_method.md`](../../../interviews_conversations/what_is_a_voting_method.md)
  — the 101 ballot-vs-count distinction this stands on.
- [`summability.md`](../STAR_Voting/summability.md) — why the IRV count can't be done locally.
- [`monotonicity.md`](./monotonicity.md) — why the IRV count can also be counterintuitive.
- Roadmap: pairs with **Episode 6** (Benefits — *Simple*) and **Episode 8** (Counting &
  trust). Glossary: "Summability," "Tabulation," "Equal Support."
