# RCV-IRV vs. STAR — A Side-by-Side

*A neutral overview routing to the detailed facet pages. The honest summary: each method has real, documented strengths the other lacks — this is about specific trade-offs, not one being good and the other bad.*

---

Both ask more of voters than Choose-One, and both usually beat plain plurality. They differ in **what the ballot captures** and **how it's counted**.

| | **RCV-IRV (Hare)** | **STAR** |
|---|---|---|
| Ballot | Rank candidates in order (no ties) | Score each 0–5 (ties allowed) |
| Captures | Order only | Order **+ strength** |
| Count | Eliminate fewest-first-choice, transfer, repeat | Sum scores → automatic runoff of top 2 |
| Equal preferences | ❌ Not allowed | ✅ Allowed |
| Precinct-summable | ❌ No (needs central count) | ✅ Yes |
| Exhausted ballots | ❌ Possible | ✅ Avoided (blank = 0) |
| Monotonic | ❌ No (more support can hurt) | ✅ Yes |
| Later-No-Harm | ✅ **Satisfies** | ❌ Fails |
| Majority criterion | ✅ **Satisfies** | ❌ Can fail |
| Center squeeze | ❌ Vulnerable | ✅ Resists |
| Track record at scale | ✅ Widely used (Maine, Alaska, many cities) | ⚠️ Limited adoption to date |

Read that table both ways. The rows where STAR wins (summability, monotonicity, no exhaustion, center-squeeze resistance) are real; so are the rows where **IRV** wins (Later-No-Harm, the majority criterion, and a far larger real-world track record). No method escapes Gibbard–Satterthwaite — each has scenarios where honesty is punished.

## Where each is genuinely stronger

**IRV's honest advantages.** It satisfies **Later-No-Harm** (ranking a backup can never hurt your favorite) and the **majority criterion** (a candidate who is the first choice of an outright majority always wins) — both of which STAR/Score can fail. It also has by far the **larger deployment record** in real public elections, which matters for legal precedent, vendor support, and voter familiarity.

**STAR's honest advantages.** It's **monotonic**, **precinct-summable**, doesn't **exhaust** ballots, lets voters express **strength** and **equal support**, and **resists center squeeze**. Its ballot is the familiar five-star format.

**Each one's price.** IRV's elimination mechanism produces [center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md), [non-monotonicity](RCV_IRV/RCV_IRV_non_monotonicity.md), [exhausted ballots](./RCV_IRV/RCV_IRV_exhausted_ballots.md), and [no precinct summability](RCV_IRV/RCV_IRV_lack_of_summability.md). STAR's price is failing **Later-No-Harm**, the **majority criterion**, and the **Participation criterion** (a no-show paradox — adding sincere ballots favoring a candidate can, in rare constructed cases, hurt them; this is the runoff's cost, and is *not* the same as monotonicity, which STAR does satisfy), plus an incentive toward **strategic min/max scoring**.

> **Note on Participation:** the no-show paradox is a real but *rare* failure, and IRV fails Participation too — so it isn't a STAR-vs-IRV differentiator, just an honest caveat that STAR isn't flawless. The runoff that causes it is the same step that guarantees STAR rejects a Condorcet loser. No method escapes Gibbard–Satterthwaite.

## The detailed facet pages

- [Scores vs. ranks](./scores_vs_ranks.md) · [Strict vs. weak ranks](./strict_vs_weak_ranks.md)
- [Tabulation, step by step](./tabulation_star_vs_irv.md) — same ballots, both counts
- [Center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md) · [Monotonicity](RCV_IRV/RCV_IRV_non_monotonicity.md) · [Summability](STAR_Voting/STAR_summability.md)
- [Exhausted ballots](./RCV_IRV/RCV_IRV_exhausted_ballots.md) · [Residual vote-splitting](STAR_Voting/residual_vote_splitting.md)
- [Is RCV "simple"?](RCV_IRV/RCV_IRV_is_simple.md) · [Is IRV "just plurality"?](RCV_IRV/RCV_IRV_and_plurality.md)

## Further reading — note on sources

These comparison pages are written by **advocacy organizations**; read them knowing each leans toward the method it champions, and cross-check claims against the facet pages above.

- [Equal Vote Coalition — RCV vs. STAR](https://www.equal.vote/rcv_v_star) *(pro-STAR)*
- [STAR Voting — RCV vs. STAR](https://www.starvoting.org/rcv_v_star) *(pro-STAR)*
- [FairVote](https://fairvote.org/) *(pro-RCV-IRV — the case for ranked choice)*
