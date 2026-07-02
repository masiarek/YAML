# The "dead rung" — when STAR's five-star tiebreaker can't fire

*Four tiny constructed elections that isolate one fact: STAR's **five-star**
tiebreaker counts votes equal to the **scale maximum (5)**. If none of the tied
candidates earned a 5, the rung reads `0–0` and the tie falls through to the
**lot** — in **both** rounds.*

Backs the "dead rung" section of the canonical
[`tie_breaking.md`](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
(Level 301). Run any file:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py \
  01_STAR/tie_break_dead_rung/tie_break_01_scoring_five_star_breaks.yaml
```

## The two ladders (recap)

```
SCORING ROUND  finalists:  pairwise → five-star → lot
AUTOMATIC RUNOFF winner:    score    → five-star → lot
```

"Five-star" = votes of score **5** (the scale max), regardless of whether any
voter actually used a 5. That's the pivot these four cases turn on.

## The four cases

| File | Round | 5 present? | Second rung (five-star) | Decided by | Winner |
|---|---|:--:|---|---|---|
| `tie_break_01_scoring_five_star_breaks` | Scoring | yes | Ben 1, Cara 0 → Ben advances | **five-star** | Alice |
| `tie_break_02_scoring_no_fives_to_lot`  | Scoring | no  | Ben 0, Cara 0 → still tied | **lot** | Alice |
| `tie_break_03_runoff_no_fives_to_lot`   | Runoff  | no  | Alice 0, Ben 0 → still tied | **lot** | Alice |
| `tie_break_04_runoff_five_star_breaks`  | Runoff  | yes | Alice 1, Ben 0 → Alice wins | **five-star** | Alice |

Cases 01/02 are the **same** tie shape one point apart (5s vs capped at 4); 03/04
likewise. Note the eventual **winner is Alice in all four** — the point isn't who
wins these toy races, it's **which rung decides**. In a closer election that
difference chooses the winner (see the scale-granularity case in
[`scale_granularity_flips_the_winner.md`](../../00_start_here/scores_and_ranks/scale_granularity_flips_the_winner.md)).

## The adversarial set (05–09): the rung must CHANGE the winner

Cases 01–04 teach, but they can't *catch a regression*: Alice wins whether or
not the engine consults five-star. Cases 05–09 close that hole — each sets
`lot_numbers:` to favor the **wrong** candidate, so the expected winner is only
elected if the ladder runs in the right order. If the engine ever skipped a
rung (or consulted the lot early), these tests fail.

| File | Round | Rung state | Lot favors | Winner proves |
|---|---|---|---|---|
| `tie_break_05_scoring_five_star_vs_adversarial_lot` | Scoring | alive (Ben 2, Cara 1) | Cara | **Ben** — five-star outranks the lot; Ben then wins the runoff |
| `tie_break_06_scoring_dead_rung_adversarial_lot` | Scoring | dead (all ≤ 4) | Cara | **Ann** — lot advances Cara, who loses the runoff to Ann |
| `tie_break_07_runoff_five_star_vs_adversarial_lot` | Runoff | alive (Ann 1, Ben 0) | Ben | **Ann** — five-star outranks the lot |
| `tie_break_08_runoff_dead_rung_adversarial_lot` | Runoff | dead (both top out at 4) | Ben | **Ben** — the lot, not column order, resolves it |
| `tie_break_09_five_star_tied_nonzero` | Runoff | alive but **non-separating** (one 5 each) | Ben | **Ben** — a rung can run, count real votes, and decide nothing |

05/06 are again the same tie shape one point apart — but here that one point of
enthusiasm **changes the elected winner** (Ben vs Ann), not just the deciding
rung. Case 09 adds the subtler failure mode: the rung isn't dead, it's
*uninformative* — equal nonzero five-star counts fall through to the lot just
like `0–0` does.

All nine files carry `expected_winners:` and are auto-discovered by
`test_single_winner_positive.py`.

## Why it matters

The usual framing — "deterministic tests settle almost everything; the lot is
rare" — assumes leading candidates attract some 5s. In **low-score /
conservative-grading** elections, or data compressed onto a coarse scale that
never reaches the top, the five-star rung quietly does nothing and the **lot
decides earlier and more often than the ladder's length suggests**. On a 0–9
ballot the same rung is a *nine-star* count; a field that tops out at 7 gives it
nothing to weigh.

*Cases 02 and 03 set `lot_numbers:` explicitly so the lot outcome is pinned and
obvious; 01 and 04 never reach the lot.*

# file: README_tie_break_dead_rung.md
