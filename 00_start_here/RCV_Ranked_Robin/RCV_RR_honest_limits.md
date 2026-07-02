# Ranked Robin (RCV-RR) — Honest Limits

**One line:** Ranked Robin (RCV-RR) is a strong Condorcet method — it reads every rank,
allows equal ranks, passes the Equal Vote, and has **no center squeeze** — but it inherits
the two structural limits of ranked, Condorcet counting: it can hit a **cycle** with no
clear winner, and it sees only **order, not strength**, so it can crown a bland compromise.

→ Companion critical pages (parity across methods):
[STAR's limits](../STAR_Voting/STAR_honest_limits.md) ·
[Approval's limits](../Approval_Voting/approval_honest_limits.md) ·
[RCV-IRV fails the Equal Vote](../RCV_IRV/RCV_IRV_equal_vote.md). What RCV-RR *is*:
[Ranked Robin](./ranked_robin.md). Curriculum: [301.4](../CURRICULUM.md).

---

## 1. Condorcet cycles (no clear winner)

Sometimes there is **no Condorcet winner**: A beats B, B beats C, C beats A — a
rock-paper-scissors "cycle." Then RCV-RR must fall back to a **resolution rule**
(Copeland / margins), and any such rule is harder to explain and can feel arbitrary to a
voter ("why did we break it *that* way?"). **How much it matters:** cycles are rare with
real electorates, but they are the honest soft spot of every Condorcet method. See
[cycle resolution](./cycle_resolution.md).

## 2. No preference strength — the "milquetoast" winner

A ranked ballot captures *order only*, not *how much*. RCV-RR elects the candidate who wins
the most head-to-head matchups — which can be a **broadly-acceptable compromise everyone
ranks second and nobody is excited about**, over a candidate a majority passionately
prefers. That's sometimes the right, consensus-seeking answer; but the method literally
cannot see intensity, so it can't tell "warm second choice" from "grudging tolerance."
(This is the mirror image of STAR's design, which *does* read strength via the 0–5 score.)

## 3. Fails Later-No-Harm; open to burial

Like STAR and Approval, RCV-RR fails Later-No-Harm — ranking a later choice can help them.
More specifically it is open to **burial**: insincerely ranking a strong rival *last* can
flip a pairwise matchup in your favorite's favor. Honest ranking is usually best, but the
incentive exists (Gibbard again: no method is strategy-proof).

## 4. The count is harder to explain

"Add the stars" (STAR/Score) or "most approvals" (Approval) is a one-sentence tally. A
**pairwise matrix** — every candidate against every other — plus cycle-handling is more to
show a general audience, even though it's fully **summable and auditable**. Simplicity of
*explanation* is a real adoption cost.

## Keep it in perspective

RCV-RR's strengths are exactly why it's worth taking seriously: it passes the **Equal
Vote**, reads **every** rank (nothing exhausts), allows equal ranks, and avoids RCV-IRV's
center squeeze and non-monotonicity. Its limits — cycles and blindness to intensity — are
the genuine cost of a ranked, consensus-first count. Every method trades something away
(Arrow, Gibbard); the fair question is which tradeoffs you want, laid out for all four
methods on the companion pages above.
