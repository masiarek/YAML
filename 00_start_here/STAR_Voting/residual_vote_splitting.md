# STAR's Residual Vote-Splitting

**One line:** STAR removes the *forced* vote-splitting that wrecks Choose-One — you
can score two similar candidates both high, so running an ally doesn't bleed your
support. What survives is a **narrow, self-inflicted** residual in the top-two
runoff: a faction can still split itself if it refuses to use the score ballot, or
tries to game which ally claims the second finalist slot.

→ Glossary: [`spoiler effect`](../GLOSSARY.md) · related: [`RCV_IRV_center_squeeze.md`](../RCV_IRV/RCV_IRV_center_squeeze.md)
· debate version: [`favorite_betrayal_voting_301.md`](../../interviews_conversations/favorite_betrayal_voting_301.md)

---

## Why STAR kills the ordinary spoiler

Choose-One forces every voter to name **one** candidate, so two similar candidates
mechanically divide their shared support and a minority can slip through. STAR's
**scoring round** removes that: a coalition voter gives Ada a 5 *and* ally Ben a 4,
so Ben's presence costs Ada nothing. Add a clone, lose nothing. That is the whole
spoiler-resistance pitch, and it is real.

## Where the residual lives — the top-two runoff

Only the **two highest score totals** advance to the automatic runoff. That single
fact is the only place a split can sneak back, and it takes voter behavior to
trigger it. Two flavors:

**1. Self-inflicted split (bullet-voting).** If a faction tribally bullet-votes —
Ada-fans give ally Ben a 0, Ben-fans give Ada a 0 — they divide their own score
totals, and the opponent can grab a finalist slot on the split field. Nothing about
the electorate's true preferences caused this; the voters declined to express the
support they actually feel. The cure is on the ballot: score your ally even a 3 and
the split vanishes.

**2. The "chicken dilemma" (strategic).** When two allies both could make the
runoff, each wing has a *tiny* incentive to under-score the other ally so that
*their* favorite, not the ally, claims the second seat. If only one wing does it, it
may work; if **both** do it, they knock their shared side down and hand the seat to
the opponent. It needs accurate polling and coordination, and it **backfires when
you guess wrong**.

## Minimal test case — run the matched pair

Same three candidates and the same true preferences; only the *expressiveness*
changes (60 voters on the Ada/Ben side, 40 for opponent Cara):

→ [`05a_residual_split_bullet-voting.yaml`](../../method_comparisons/split_voting/_main/05a_residual_split_bullet-voting.yaml)
 · [`05b_residual_split_expressive-fix.yaml`](../../method_comparisons/split_voting/_main/05b_residual_split_expressive-fix.yaml)

| File | Ada/Ben behavior | Scores (Ada / Ben / Cara) | STAR winner |
|------|------------------|--------------------------|-------------|
| 05a | bullet-vote (ally = 0) | 175 / 125 / **200** | **Cara** (minority) — split not rescued |
| 05b | score ally a 3 | **250** / 230 / 200 | **Ada** (majority side) — split fixed |

In 05a the engine's `[Vote-splitting check]` is honest: it flags the majority
coalition, then reports *"STAR elected Cara"* — STAR does **not** paper over a split
the voters inflicted on themselves. In 05b, `[Divergence from STAR]` shows
Choose-One still electing Cara while STAR diverges and keeps the seat on the majority
side.

## Why it's a narrow edge case, not the spoiler all over again

- **The ordinary spoiler is automatic** — it needs no coordination and happens
  whenever similar candidates run. Splitting is the *default*.
- **STAR's residual is the exception** — it needs a near-tie for the second runoff
  slot, accurate prediction, coordinated mis-scoring, and it **backfires if you're
  wrong**. The brute-force simulation in [`../../simulations/`](../../simulations)
  finds that a favorite-betrayal-style play in STAR helps only ~2% of the time it
  changes the result — it backfires ~98% of the time. So honest, expressive scoring
  stays your safest ballot.

Same root cause as STAR's [favorite-betrayal](../../interviews_conversations/favorite_betrayal_voting_301.md)
and [center-squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) edge cases: all three come from "only the
top two advance."

## How to say it honestly

Not *"STAR eliminates vote-splitting"* (full stop) but *"STAR ends forced
vote-splitting and shrinks the rest to a narrow, hard-to-coordinate, backfire-prone
edge case — dramatically reduces, doesn't claim to eliminate."* The honest version
is still the winning version.
