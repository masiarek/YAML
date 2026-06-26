# Is RCV-IRV "Just Plurality in Sequence"?

*A claim you'll hear from STAR/Condorcet advocates. It's **partly right and partly overstated** — here's the precise version, so you're never caught out by it.*

---

Someone tells you "RCV-IRV is just a series of plurality elections." It's a confusing claim because there's a true idea buried inside an exaggeration. Sorting the two apart is itself good education.

## The part that's true (and worth teaching)

IRV does lean on plurality logic in a specific, defensible sense:

- **Each round is decided by first-preference plurality** among the candidates still standing. To choose who gets eliminated, IRV looks **only at each ballot's current top choice** — it does not consult your lower rankings until a higher choice is gone.
- **The final round is a two-way plurality** — whoever the remaining two are, the one with more votes wins.
- A clean way to say it: **plurality is just IRV with a ranking limit of 1.** IRV generalizes plurality by adding automatic elimination-and-transfer rounds.

This shared DNA has real consequences. Because elimination ignores lower preferences, IRV is **not pairwise** (it never asks "does A beat B head-to-head?"), which is why it can:

- **center-squeeze** a broadly-liked moderate who has few *first* choices ([center_squeeze.md](./center_squeeze.md)),
- behave **non-monotonically** ([monotonicity.md](./monotonicity.md)), and
- discard ballot information through **[exhaustion](./RCV_IRV/RCV_IRV_exhausted_ballots.md)**.

So the honest, defensible sentence is: **"IRV inherits plurality's round-by-round blindness to lower preferences — that's why it isn't pairwise and can eliminate a Condorcet-strong moderate."**

## The part that's overstated (don't say this)

The stronger slogans — *"IRV is the exact same as plurality"* or *"worse than plurality"* — don't survive scrutiny, and an informed opponent will dismantle them:

- IRV is **not** identical to plurality. It changes outcomes, and it **passes several criteria plurality fails**: the majority criterion, mutual majority, later-no-harm, Condorcet-loser, and independence of clones. It typically elects more broadly acceptable winners than first-past-the-post and removes the simplest "split the vote and lose" cases.
- Calling IRV **"worse than plurality"** is, in general, false. It's the mirror image of the marketing overclaim that IRV fixes everything. Reach for it and you forfeit the credibility the accurate critique earns you.
- **"A majority voted against the winner"** is not rigorous. In any crowded field, almost every winner — under *any* method, including STAR — is "not the first choice" of most voters. "Not first" ≠ "opposed."

## A worked illustration (center squeeze, stated carefully)

A constructed 4-candidate example (first-choice shares: Alice 27%, Bob 26%, Charlie 24%, Debora 23%; with Debora ranked 1st *or* 2nd by ~93% of voters):

Debora is the broadly-liked compromise candidate, yet she has the **fewest first choices**, so IRV **eliminates her in round 1** — before her wide second-choice support can matter. That is the center-squeeze failure, and it's the legitimate core of the "plurality-like" critique: round-one elimination is a first-preference plurality test.

*Caveat for honesty:* replaying every later transfer needs the full ballot cross-tabs, which a first/second-choice summary doesn't give. The verifiable, sufficient point is the **early elimination of a candidate with broad lower-rank support** — not a specific downstream winner.

## And to keep it balanced

Methods that avoid round-by-round elimination pay their own price. **STAR and Score fail Later-No-Harm and the Majority criterion** — a candidate a majority scores highest can still lose — and they invite **strategic min/max exaggeration**. No method escapes Gibbard–Satterthwaite. The fair claim isn't "IRV bad, STAR perfect"; it's that IRV's *elimination* mechanism has specific, well-documented failure modes that pairwise and scored methods handle differently. (See [scores_vs_ranks.md](./scores_vs_ranks.md) and [strict_vs_weak_ranks.md](./strict_vs_weak_ranks.md).)

---

## Related concept pages

- [Strict vs. weak ranks](./strict_vs_weak_ranks.md) — IRV is strict and not pairwise; other ranked methods differ
- [Center squeeze](./center_squeeze.md) — the failure this critique points at
- [Monotonicity](./monotonicity.md) — more support can hurt a candidate under IRV
- [RCV vs. IRV vs. RCV-IRV — terminology](./RCV-IRV-confusing-name.md)

## Learn more — in this library

- [In what sense is RCV-IRV the same as Plurality](https://docs.google.com/document/d/1bBops2LS5BtJ5KTtAowP9x22F5azpIGdoSutbnUeNrM/edit?tab=t.0) *(makes the stronger version of this argument)*
- [RCV IRV cons — vote splitting / spoiler effect / series of choose-one elections](https://docs.google.com/document/d/1R9HQCRpFWs1ZKUNXM52bbyjVQGJPRu9Kd_a8l2T4xIo/edit?tab=t.0)
