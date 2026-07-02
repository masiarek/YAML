# STAR Tie-Breaking — The Full Chain

**One line:** ties don't get resolved by a coin flip first — they fall through a
**fixed ladder** of deterministic tests (pairwise → five-star → …), and only if
*every* rung is still tied does a pre-drawn **lot order** decide it. Most
elections never reach the lot.

→ Builds on the **Automatic Runoff** and **Head-to-head / pairwise** glossary
entries · JSON-side companion: [`tie_breaking_JSON.md`](tie_breaking_JSON.md)
(format & mapping) · related:
[`tabulation_star_vs_irv.md`](../../tabulation_star_vs_irv.md) ·
operational companions: the JSON→YAML converter
([`YAML_library/1_positive/01_convert_json_yaml.py`](../../../YAML_library/1_positive/01_convert_json_yaml.py))
and its tests
([`tests/test_lot_number_tiebreak.py`](../../../STARVote_LH_tabulation_engine/tests/test_lot_number_tiebreak.py))
· Level **301**.

---

## Why tie-breaking gets complicated fast

A STAR election has **two rounds** — a **Scoring Round** (pick the top two
finalists) and an **Automatic Runoff** (the two finalists go head-to-head). A
tie can happen in **either** round, and each round has its **own** ladder of
tiebreakers. So a single election can break ties more than once, in two
different places, by two different rules. (The worked example below does exactly
that.)

The thing to hold onto: **the random "lot" order is the *last* resort, not the
first.** Almost everything is settled by deterministic tests before the lot is
ever consulted. The lot exists only so that a genuinely perfect tie still
produces a single, *reproducible* winner instead of an error.

---

## The ladder (both rounds)

```
SCORING ROUND  — choose the two finalists
  0. Two highest total scores advance.
  └─ tie for the last finalist slot?
     1. PAIRWISE     — advance whoever is preferred in the most head-to-head matchups
     2. FIVE-STAR    — still tied? advance whoever has the most score-5 votes
     3. LOT ORDER    — still tied? the highest-priority lot number advances

AUTOMATIC RUNOFF  — choose the winner from the two finalists
  0. The finalist preferred head-to-head (more ballots scored higher) wins.
  └─ tie?
     1. SCORE        — the higher total score wins
     2. FIVE-STAR    — still tied? the most score-5 votes wins
     3. LOT ORDER    — still tied? the highest-priority lot number wins
```

Note the two ladders are **not** identical. In the Scoring Round, pairwise is
the *first* tiebreaker; in the Runoff, total score is the first tiebreaker
(pairwise *is* the runoff, so it can't also break the runoff). Five-star is the
second tiebreaker in both. The lot is the floor of both.

"Five-star" means "votes of the maximum score" (5 on a 0–5 ballot). **Equal
Support** in the output is not a candidate — it's the no-preference bucket
(ballots that scored the two compared candidates the same), shown so the pairwise
math adds up.

---

## Edge case: "five-star" is a *dead rung* when nobody scored the max

The five-star rung counts votes equal to the **scale maximum** — literally
`score == 5` on a 0–5 ballot. (In the engine this is `_maximum_score_count_round`,
which compares each score to `maximum_score`, the *option* — **not** the highest
score any voter actually used.) Two consequences that surprise people:

1. **If none of the tied candidates earned a single 5, the rung is inert.** It
   still runs, and the report still prints it, but every count is `0`, so it
   can't separate anyone — the tie falls straight through to the **lot**.
2. **It's the scale's max, not the field's max.** On a 0–9 ballot
   (`maximum_score: 9`) the same rung becomes a *nine-star* count. A cautious
   electorate that tops out at 4s hands the rung nothing to weigh, so the ladder
   is effectively one rung shorter: pairwise/score → **lot**.

The same two ballots, capped a single point apart, decide the second finalist by
two different rules — five-star in one, the lot in the other:

```
 FIVE-STAR PRESENT (a 5 exists)              NO FIVES (all scores ≤ 4)
   Alice,Ben,Cara                              Alice,Ben,Cara
   5,5,3                                        4,4,2
   5,1,3                                        4,0,2

 Ben & Cara tie 6–6; pairwise 1–1            Ben & Cara tie 4–4; pairwise 1–1
 Second tiebreaker — FIVE-STAR:              Second tiebreaker — FIVE-STAR:
   Ben  1  → advances (Second place)            Ben 0, Cara 0  → STILL TIED
                                              *** No lot numbers provided …
                                              [Tiebreaker: Lot Number Priority]
                                                Resolved: Ben (by lot / column order)
```

The **runoff** ladder does the same thing: when the two finalists are tied
head-to-head **and** tied on total score, five-star is consulted — but if neither
finalist earned a 5, it reads `0–0` and the **lot** decides. (Constructed cases:
`Alice,Ben / 5,1 / 0,4` → five-star breaks it; `Alice,Ben / 4,0 / 0,4` → no fives,
lot decides. Both verified against the engine.)

**Why it matters.** The "deterministic tests settle almost everything, the lot is
rare" framing holds for typical elections, where leading candidates attract *some*
5s. But in **low-score / conservative-grading** contests — or real data compressed
onto a coarse scale that never reaches the top — the five-star rung can quietly do
nothing, and the **lot decides more often than the ladder's length suggests**. When
you build or read a close example, check whether the tied candidates actually have
max-score votes before crediting the outcome to five-star.

Runnable cases (all four verified in the test suite):
[`01_STAR/tie_break_dead_rung/`](../../../01_STAR/tie_break_dead_rung/README_tie_break_dead_rung.md)
— five-star-breaks vs no-fives-→-lot, in both the scoring round and the runoff.

---

## Worked example — Ice Cream, 6 flavors (ties in *both* rounds)

Two ballots, six flavors. This is the canonical "it tied twice" case — and,
importantly, **the lot order is never reached**; deterministic tests settle
everything.

```
Ballots:
Chocolate,Chocolate Chip,Fudge Brownie,Vanilla,Strawberry,Mango
        4,             5,            4,      1,         2,    -
        1,             0,            0,      4,         5,    4

Tabulation:
        
[Scoring Round]  The two highest-scoring candidates advance.
   Strawberry     -- 7 -- First place
   Chocolate      -- 5 -- Tied for second place
   Chocolate Chip -- 5 -- Tied for second place
   Vanilla        -- 5 -- Tied for second place
   Fudge Brownie  -- 4
   Mango          -- 4
   → Strawberry advances; three-way tie for second.

[Scoring Round: First tiebreaker]  Most head-to-head matchups (PAIRWISE).
   Chocolate      -- 2
   Chocolate Chip -- 2
   Vanilla        -- 2
   → still a three-way tie.

[Scoring Round: Second tiebreaker]  Most score-5 votes (FIVE-STAR).
   Chocolate Chip -- 1 -- Second place
   Chocolate      -- 0
   Vanilla        -- 0
   → Chocolate Chip advances. Finalists: Strawberry, Chocolate Chip.

[Automatic Runoff Round]  Preferred head-to-head wins.
   Chocolate Chip -- 1 -- Tied for first
   Strawberry     -- 1 -- Tied for first
   → two-way tie for first.

[Automatic Runoff Round: First tiebreaker]  Highest total score (SCORE).
   Strawberry     -- 7 -- First place
   Chocolate Chip -- 5
   → Strawberry wins.
```

So this election tied **twice** — a three-way tie for the second finalist slot,
then a two-way tie in the runoff — and resolved both *without* the lot:
five-star settled the first, total score settled the second. The file's
`lot_numbers:` was present (carried over from BetterVoting) but **never
consulted**. That is the normal case.

The lot only decides when pairwise **and** score **and** five-star are *all*
tied — e.g. a perfect symmetric election.

---

## The lot order (the floor of both ladders)

When the ladder bottoms out, the engine consults a **lot order**: a list of
candidates in **priority order, highest first**. The tied candidate that appears
*earliest* in the list wins. (In code this is the `LotNumberTiebreaker`;
`index 0 = highest priority = wins ties`.)

This mirrors how real STAR elections handle a true tie: officials draw a random
order **once**, publish it, and use it for any tie that arises. Publishing it up
front is what makes the result **reproducible and auditable** — anyone can re-run
the count and get the same winner.

---

## Where the order comes from (imported elections)

For elections imported from BetterVoting, the lot order isn't ours to draw —
BetterVoting pre-draws it and ships it in the export, and the converter carries
it into the YAML's `lot_numbers:` so our re-tabulation reproduces their official
winner. The export records it as `Results[].perm` (or per-candidate
`tieBreakOrder`), the converter translates those UUIDs to our `cand_id`s, and a
generated file ends up with a line like:

```yaml
lot_numbers: [Strawberry, Fudge Brownie, Mango, Chocolate Chip, Vanilla, Chocolate]
```

The exact JSON fields, the field-by-field mapping, the fallbacks, and the worked
Ice Cream mapping are in the companion page:
**[`tie_breaking_JSON.md`](tie_breaking_JSON.md)**.

---

## What you may set in a hand-written YAML

`lot_numbers:` is **optional**. Two cases:

**You provide it.** Write an inline list of `cand_id`s in priority order, highest
first:

```yaml
lot_numbers: [Strawberry, Fudge Brownie, Mango, Chocolate Chip, Vanilla, Chocolate]
```

- Entries must be existing `cand_id`s — i.e. the names in the ballot header.
- Only the relative order among the *tied* candidates matters, but listing **all**
  candidates is the clear, safe habit (and matches what the converter writes).
- It can sit at the **race** level (normal) or the **election** level; the race
  value wins if both are present.

**You omit it.** The engine **assumes the CSV ballot-column order** as the lot
priority — i.e. left-to-right, so the **first column wins** a pure lot tie. This
is a deliberate, deterministic fallback, not randomness.

### When to set it vs. omit it

| Situation | Recommendation |
|---|---|
| Imported real election (BetterVoting) | **Always carry the provider's order.** The converter does this automatically — don't hand-edit it. Reproducibility/audit depends on it. |
| Hand-written teaching demo | **Usually omit.** Keep the example small enough that ties resolve before the lot (the Ice Cream case), or accept column order as the tiebreak. |
| Demo that *shows* a lot-decided tie | **Set it explicitly**, so the lesson is pinned and obvious (a symmetric tie where only the lot can decide). |

The practical upshot: for most hand-built examples you never write `lot_numbers`
at all, because well-chosen small ballots either avoid a lot tie or the
column-order fallback is exactly what you want.

---

## Quick rules

- **Lot order is last.** Pairwise / score / five-star resolve almost everything
  first. Don't reach for `lot_numbers` to explain a winner unless the output
  literally shows a lot tiebreaker firing.
- **Index 0 wins.** Earliest in `lot_numbers` (or leftmost ballot column, if
  omitted) = highest priority = wins the tie.
- **Two rounds, two ladders.** Scoring Round: pairwise → five-star → lot. Runoff:
  score → five-star → lot. An election can break ties in both.
- **Five-star needs actual 5s.** That rung counts votes of the *scale maximum*
  (5). If no tied candidate earned one, it reads 0–0 and the tie drops to the lot —
  common in low-score elections. See "dead rung" above.
- **Imported files carry the order; hand-written files usually don't need to.**
- **`-` / blank = 0.** A blank or marker cell counts as score 0 (no support); it
  doesn't affect the tiebreak ladder beyond its zero contribution.

---

## See also

- **BetterVoting's official tie-breaking protocol** (the authoritative source for
  the ladder above, and the "shuffle the candidates" random order our
  `lot_numbers` carries): <https://docs.bettervoting.com/help/ties.html>
- Glossary: **Tiebreaker**, **Head-to-head / pairwise**, **Automatic runoff**,
  **Equal Support** — [`GLOSSARY.md`](../../GLOSSARY.md)
- Equal-score handling in the runoff:
  [`are_equal_score_votes_discounted.md`](../../../interviews_conversations/are_equal_score_votes_discounted.md)
  · demo [`equal_support_runoff_demo.yaml`](../../../01_STAR/_main/equal_support_runoff_demo.yaml)
- Converter + engine wiring and the full test matrix (perm, `tieBreakOrder`,
  no-sequence, manual override, column-order fallback, and the non-vacuous
  self-check): [`tests/test_lot_number_tiebreak.py`](../../../STARVote_LH_tabulation_engine/tests/test_lot_number_tiebreak.py)
