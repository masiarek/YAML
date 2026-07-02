# The Equally Weighted Vote — the Equal Vote Criterion & the Test of Balance

**One line:** a method gives an **equally weighted vote** if, however you fill out your
ballot, someone else can fill out the *exact opposite* ballot and the two together change
nothing. STAR passes this (so do Score and Approval); **Choose-One** and **RCV-IRV** do
not — and that failure is precisely what causes vote-splitting and the spoiler effect.

→ Curriculum: [301.4 — honest limits & theory](../CURRICULUM.md) (the "Test of Balance").
Glossary: [`Equally Weighted Vote`](../GLOSSARY.md). The narrow leftover STAR *doesn't*
erase: [residual vote-splitting](residual_vote_splitting.md). Why RCV-IRV fails the same
test: [RCV-IRV fails the Equal Vote](../RCV_IRV/RCV_IRV_equal_vote.md).

---

## The Test of Balance

Equal weight has been tested the same way since antiquity: **balance**. Two objects weigh
the same if they balance on opposite pans of a scale. The Equal Vote Coalition's founder,
Mark Frohnmayer, applied that to ballots — a method treats votes as equal only if, for any
ballot one voter casts, another voter can cast one that "you should be able to vote in an
equal and opposite fashion." If an election were tied and one ballot came in, there must
always be a single ballot that brings it back to a tie.

Pass that **Test of Balance** and you satisfy the **Equal Vote Criterion** (a.k.a. the
Equality Criterion, or *Frohnmayer balance*). Fail it and some voters' ballots are worth
more than others'.

## The picture: two exactly opposite ballots

Two voters who disagree on *every* candidate, on a 0–5 ballot. Their scores are exact
opposites — each pair sums to 5 (an opposite score is `5 − s`):

| Candidate | Voter 1 | Voter 2 | Sum |
|-----------|:------:|:------:|:---:|
| Abby | 2 | 3 | 5 |
| Ben | 1 | 4 | 5 |
| Carmen | 0 | 5 | 5 |
| DeAndre | 1 | 4 | 5 |
| Eric | 5 | 0 | 5 |
| Freya | 4 | 1 | 5 |

Add both ballots to *any* election and nothing moves:

- **Scoring round:** every candidate gains exactly **5** stars (Voter 1 + Voter 2 = 5 for
  each). Everyone rises by the same amount, so the ordering is untouched.
- **Automatic runoff:** whichever finalist Voter 1 prefers, Voter 2 prefers the other by
  the same margin — they cancel **1–1**.

So if the race was tied before these two ballots, it is still tied after. Neither ballot
outweighed the other. That is an equally weighted vote, demonstrated.

## Why this is the root of vote-splitting

Choose-One (plurality) **fails** the Test of Balance. If you vote for A, there is no
ballot anyone can cast to cancel it — a Choose-One ballot can only *add* a mark to some
candidate, never subtract from A. With no balancing vote available, a cluster of similar
candidates splits its shared supporters and a less-preferred candidate can slip through.
Vote-splitting and the spoiler effect are not separate bugs; they are the visible symptom
of an **unequal vote**. STAR ends forced vote-splitting for exactly one reason: every
ballot can be perfectly cancelled, so adding a similar candidate can't dilute anyone.

## Which methods pass, which fail

| Method | Equal Vote / Test of Balance |
|--------|------------------------------|
| **STAR**, Score, Approval | ✅ pass — every ballot has an exact opposite that cancels (STAR *guarantees* it: the runoff is binary, so any non-blank ballot is equally weighted) |
| Condorcet methods that allow equal ranks and read every rank (e.g. **Ranked Robin**) | ✅ generally pass |
| Ranked STAR (ranked ballot, added up) | ✅ passes |
| **Choose-One plurality** | ❌ fails whenever there are 3+ candidates — the structural source of vote-splitting |
| **RCV-IRV** | ❌ fails — opposite ballots don't reliably cancel under sequential elimination ([why](../RCV_IRV/RCV_IRV_equal_vote.md)) |

One caveat both sides agree on: with only **two** candidates, *every* method passes — the
equal-vote problem only appears once there are three or more.

## One person, one vote (the legal thread)

The equal-vote idea is the mathematical face of **"one person, one vote."** In *Wesberry
v. Sanders* (1964) the U.S. Supreme Court held that the weight and worth of each citizen's
vote must, as nearly as is practicable, be the same. Choose-One honors that only in a
two-candidate race; with more candidates, voters who have several candidates "on their
side" are systematically disadvantaged, which is why voters are pushed toward the
"lesser of two evils" and third parties get blamed as spoilers. Advocates argue an equal
vote is therefore not just a nicety but the constitutional standard, and that vote-splitting
(unlike gerrymandering) is fully solvable.

**The other side, fairly stated:** RCV-IRV advocates (e.g. FairVote) argue RCV-IRV upholds
one-person-one-vote better than Choose-One. That debate — and why the equal-vote camp says
RCV-IRV still fails the balance test in competitive races — is on the companion page,
[RCV-IRV fails the Equal Vote](../RCV_IRV/RCV_IRV_equal_vote.md).

## The formal criterion (deep 301)

The informal Test of Balance has been formalized two ways (BTernaryTau):

- **Cancellation criterion** — for every ballot there exists *some* other ballot such that
  adding both never changes the result.
- **Opposite cancellation criterion** — stronger: that other ballot must be the *literal
  opposite* set of preferences (the picture above). It implies the plain cancellation
  criterion, and it rules out ballot formats where no true opposite exists.

Keep this distinct from **reversal symmetry**, a *different* criterion (if every voter
flips their preferences, the winner should flip). Equality/balance is about one ballot
having an equal-and-opposite partner; reversal symmetry is about flipping the *whole*
electorate.

For **multi-winner** elections the equal-vote idea extends to **Vote Unitarity** (Keith
Edmonds) — an equal vote *plus* proportionate spending — which motivates proportional
score methods like **Sequentially Spent Score (SSS)**. See
[proportional: STV vs STAR-PR](../proportional_representation/stv/proportional_stv_vs_star.md) for that thread.

## Sources

- Equal Vote Coalition — the Equal Vote / Equally Weighted Vote: <https://www.equal.vote/equalvote>
- Mark Frohnmayer — *Frohnmayer balance* / the Test of Balance (Equal Vote Coalition).
- electowiki — [Equal Vote Criterion](https://electowiki.org/wiki/Equal_Vote_Criterion) · [Vote unitarity](https://electowiki.org/wiki/Vote_unitarity)
- BTernaryTau — [cancellation criterion](https://bternarytau.github.io/miscellaneous/voting-theory/cancellation-criterion) · [opposite cancellation criterion](https://bternarytau.github.io/miscellaneous/voting-theory/opposite-cancellation-criterion)
- *Wesberry v. Sanders*, 372 U.S. 1 (1964) — "one person, one vote."
- FairVote (the contrasting view): [How RCV survives the one-person-one-vote challenge](https://fairvote.org/how_ranked_choice_voting_survives_the_one_person_one_vote_challenge/)
