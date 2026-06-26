# STAR Tie-Breaking — The Full Chain

**One line:** ties don't get resolved by a coin flip first — they fall through a
**fixed ladder** of deterministic tests (pairwise → five-star → …), and only if
*every* rung is still tied does a pre-drawn **lot order** decide it. Most
elections never reach the lot.

→ Builds on the **Automatic Runoff** and **Head-to-head / pairwise** glossary
entries · JSON-side companion: [`tie_breaking_JSON.md`](./tie_breaking_JSON.md)
(format & mapping) · related:
[`tabulation_star_vs_irv.md`](./tabulation_star_vs_irv.md) ·
operational companions: the JSON→YAML converter
([`YAML_library/1_positive/01_convert_json_yaml.py`](../../YAML_library/1_positive/01_convert_json_yaml.py))
and its tests
([`tests/test_lot_number_tiebreak.py`](../../STARVote_LH_tabulation_engine/tests/test_lot_number_tiebreak.py))
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
**[`tie_breaking_JSON.md`](./tie_breaking_JSON.md)**.

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
- **Imported files carry the order; hand-written files usually don't need to.**
- **`-` / blank = 0.** A blank or marker cell counts as score 0 (no support); it
  doesn't affect the tiebreak ladder beyond its zero contribution.

---

## See also

- **BetterVoting's official tie-breaking protocol** (the authoritative source for
  the ladder above, and the "shuffle the candidates" random order our
  `lot_numbers` carries): <https://docs.bettervoting.com/help/ties.html>
- Glossary: **Tiebreaker**, **Head-to-head / pairwise**, **Automatic runoff**,
  **Equal Support** — [`GLOSSARY.md`](../GLOSSARY.md)
- Equal-score handling in the runoff:
  [`are_equal_score_votes_discounted.md`](../../interviews_conversations/are_equal_score_votes_discounted.md)
  · demo [`equal_support_runoff_demo.yaml`](../../01_Single_winner/equal_support_runoff_demo.yaml)
- Converter + engine wiring and the full test matrix (perm, `tieBreakOrder`,
  no-sequence, manual override, column-order fallback, and the non-vacuous
  self-check): [`tests/test_lot_number_tiebreak.py`](../../STARVote_LH_tabulation_engine/tests/test_lot_number_tiebreak.py)
