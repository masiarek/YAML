# The "dead rung" in STAR's official tiebreaker ladder

*A note for the Equal Vote Coalition, from the STAR Voting education & test-case
library. All examples below are engine-verified and reproducible;
the runnable files are listed at the end.*

## Summary

The official STAR tiebreaker protocol uses a **five-star count** as its second
rung in both rounds: still-tied candidates are compared by how many **maximum**
scores they received. The rung counts the **scale's** max (literally
`score == 5`), not the highest score any voter actually used. When none of the
tied candidates earned a single 5, the rung still runs — but reads `0–0`,
separates nobody, and the tie falls straight through to random resolution. We
call this a **dead rung**. It is not exotic: cautious electorates, small
informal polls, and data rescaled onto a coarse range routinely produce ballots
that top out at 4. In exactly the elections where ties are most likely (small
ones), the ladder is effectively one rung shorter than it looks, and the lot
decides earlier and more often than the protocol's length suggests.

## The protocol as we implement it

```
SCORING ROUND — choose the two finalists
  1. PAIRWISE    — most head-to-head wins among the tied
  2. FIVE-STAR   — most score-5 votes
  3. LOT         — pre-drawn random order (last resort)

AUTOMATIC RUNOFF — choose the winner
  1. SCORE       — higher total score
  2. FIVE-STAR   — most score-5 votes
  3. LOT
```

## The minimal pair

The same two-ballot standoff, one point apart. Both verified against our
tabulation engine (a fork of Larry Hastings' `starvote`):

```
 A FIVE EXISTS — rung fires                NO FIVES — dead rung, lot decides
   Ann,Ben                                   Ann,Ben
   5,1                                       4,0
   0,4                                       0,4

 Head-to-head 1–1; scores 5–5.             Head-to-head 1–1; scores 4–4.
 Five-star: Ann 1, Ben 0 → ANN wins.       Five-star: 0–0 → the LOT decides.
```

One point of enthusiasm is the difference between "the ballots decided" and
"a coin flip decided." A subtler variant: if both candidates have the *same
nonzero* number of 5s, the rung fires, counts real votes, and still decides
nothing — equal counts fall through exactly like `0–0`.

A related scale effect: on a 0–9 ballot the same rung is a *nine-star* count.
We reconstructed a published 0–9 teaching example (four elections) on our 0–5
engine and found a 5.6-vs-5.4 score distinction that no 0–5 rescaling can
express — coarse scales both create ties and starve the rung that is supposed
to break them.

## A possible refinement: walk down the rungs

A natural generalization: if the five-star counts tie, compare **four-star**
counts, then three-star, and so on — equivalently, compare the tied candidates'
score distributions lexicographically from the top. Properties worth noting:

- **Backward compatible in outcome** wherever the current rule decides: it is
  identical to five-star whenever five-star separates the candidates.
- **Still precinct-summable** — it needs only the per-candidate score histogram
  the count already produces.
- **Nearly eliminates random resolution**: the lot is reached only when the
  tied candidates' entire score distributions are identical, which at any real
  scale essentially means a genuinely perfect tie.
- **Cost**: a longer rule to state and certify, and a spec change for every
  implementation (BetterVoting included). "Most 5s" is easy to say out loud;
  "lexicographic histogram comparison" is not, even if "if 5s tie, compare 4s,
  then 3s…" states it plainly enough for statute.

## What we do, and what we're asking

Our library follows the **official protocol unchanged** — compatibility with
Equal Vote's specification and BetterVoting's counts matters more to an
education project than a marginally better tiebreaker. But we document the dead
rung explicitly and guard it with nine engine-verified test elections, five of
which set the lot order *adversarially* so the tests fail if an implementation
consults the lot before exhausting the deterministic rungs.

Perspective: at public-election scale, ties that survive pairwise/score AND
five-star are vanishingly rare — this note is not an alarm. But BetterVoting's
bread and butter includes exactly the small polls where dead rungs are common.

Two questions for Equal Vote:

1. Is "scale max, not field max" the intended reading of the five-star rung?
   (Our engine implements it that way; BetterVoting appears to as well.)
2. Has a walk-down-the-rungs variant been considered for a future protocol
   revision — and if it was considered and rejected, we'd gladly document the
   reasoning.

## Runnable material (in the library)

- Concept page: `00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md`
- The nine test elections: `01_STAR/tie_break_dead_rung/` (cases 01–04 mirror
  the examples above; 05–09 are the adversarial-lot regression set)
- Engine: `STARVote_LH_tabulation_engine/` (vendored fork of Larry Hastings'
  `starvote`; deterministic lot order via `lot_numbers:`)

# file: dead_rung_note_for_equal_vote.md
