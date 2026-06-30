# Cycle Resolution — why Minimax, Ranked Pairs, and Schulze exist

> **Status: draft / Level 301.** A learning page on what happens to Condorcet methods
> when there's *no* Condorcet winner — and why a whole family of methods exists just to
> answer that. All examples below are verified with the `pref_voting` engine.

**One line:** when a [Condorcet winner](../GLOSSARY.md) exists, **every** Condorcet
method elects them — Ranked Robin, Minimax, Ranked Pairs, Schulze all agree. They differ
*only* when majority preference forms a **cycle** (A beats B, B beats C, C beats A, with no
one beating all). "Cycle resolution" is the rule a method uses to pick a winner in that
case — and it's the *entire* difference between these methods.

→ the cycle itself: [Whoops_03 — Condorcet cycle](../../01_Single_winner/paradoxes_and_whoops/Whoops_03_condorcet_cycle_rps.md)
· the base method: [Ranked Robin](ranked_robin.md) · [`GLOSSARY`](../GLOSSARY.md).

---

## The problem: majority rule can eat its own tail

Usually one candidate beats every other head-to-head — the **Condorcet winner** — and the
choice is obvious. But majority preference isn't guaranteed to be transitive. Sometimes:

> a majority prefers **A > B**, a majority prefers **B > C**, *and* a majority prefers
> **C > A**.

There is no "beats everyone" candidate — the result is a **cycle** (the
[Condorcet paradox](../../01_Single_winner/paradoxes_and_whoops/Whoops_03_condorcet_cycle_rps.md),
known since the 1780s). Now "elect the candidate the majority prefers" has *no* answer, and
a method has to break the tie somehow. *How* it breaks it is what separates the methods.

## Why Ranked Robin / Copeland is tie-prone

[Ranked Robin (Copeland)](ranked_robin.md) scores by **pairwise wins − losses**. That's
beautifully simple — but in a cycle, candidates tend to share the same record, so it often
**can't pick a unique winner**. Concrete example (21 voters, 4 candidates; verified):

```
10 : A>B>C>D       Head-to-heads in the top cycle:
 6 : B>C>A>D            A beats B by 9      B beats C by 11      C beats A by 1
 5 : C>A>B>D       (everyone ranks D last, so A, B, C each beat D)
```

Win–loss record: **A +1, B +1, C +1**, D −3 → **Copeland ties A, B, and C.** The simple
count throws up its hands. That tie-proneness is exactly why the refined methods below
exist: they look at *how strong* each defeat is, not just who-beat-whom.

## The three cycle-resolution methods (same ballots, different rule)

On that same example, each refined method gives a **unique** winner — here, all three pick
**A** (the candidate whose only loss, to C, is the smallest at margin 1):

**Minimax** *(simplest)* — elect the candidate whose **worst single defeat is the least
bad**. A's biggest loss is just 1; B's is 9; C's is 11 → **A wins.** Intuition: "least
strongly beaten." (Caveat: in 4+ candidate fields Minimax can occasionally pick a candidate
outside the top cycle / Smith set.)

**Ranked Pairs (Tideman)** — sort every pairwise victory by margin, **largest first**, and
"lock in" each one *unless* it would create a cycle with the ones already locked. Here:
lock B>C (11), then A>B (9); C>A (1) would close a cycle, so **skip it**. The locked
relations read A > B > C → **A wins.**

**Schulze (beatpath)** — A "beats" B if the **strongest chain of defeats** from A to B
(its weakest link is its strength) is stronger than the strongest chain back. Follow the
strong links and **A wins** here too. (Widely used in practice — Debian, Wikimedia, Ubuntu.)

## …but they don't always agree

In the example above all three landed on A. They **needn't.** A nastier 5-candidate cycle
(the classic "Heitzig–Schulze–Tideman disagree" profile, 100 voters; verified):

| Method | Winner |
|---|---|
| Ranked Robin / **Copeland** | **B** |
| **Ranked Pairs** | **B** |
| **Minimax** | **A** |
| **Schulze** | **A** |

Same ballots, **two different winners** depending on the cycle-resolution rule. This is the
whole point: "Condorcet method" names a *family*, and once you're inside a cycle, the family
splits. (Outside cycles — i.e. almost always — they're identical.)

## What they share (the good news)

- **Condorcet-consistent:** all elect the Condorcet winner whenever one exists — which, with
  many voters and realistic preferences, is the overwhelming majority of elections.
- **Smith-efficient (the good ones):** Ranked Pairs, Schulze, and Copeland always elect from
  the **Smith set** (the smallest group that beats everyone outside it). Minimax can miss it.
- **Clone-independent & monotone:** Ranked Pairs and Schulze add these guarantees; that
  robustness is why they're the "serious" cycle-resolvers despite being harder to explain.

## Where Ranked Robin and STAR fit

- **Ranked Robin (Equal Vote)** is essentially **Copeland + a margins tiebreak** — a
  pragmatic choice: cycles are rare, so the simple win-loss count plus a sum-of-margins
  fallback is usually plenty. (Consensus Choice uses a different fallback, "Most Wins,
  Smallest Loss" — same family, different cycle rule.) See [`ranked_robin.md`](ranked_robin.md).
- **STAR is *not* a Condorcet method** and doesn't try to resolve cycles at all. Its
  score-then-runoff just produces a winner, which *can* differ from the Condorcet winner
  ([Whoops_02](../../01_Single_winner/paradoxes_and_whoops/Whoops_02_star_misses_condorcet.md)).
  The trade: these ranked methods capture *pure majority preference* but ignore *intensity*;
  STAR captures intensity (how much, not just which) at the cost of strict Condorcet
  guarantees. Neither is "the" right answer — it's a values choice.

## How often do cycles even happen?

Rarely, but not never. Cycles get likelier in **small, sharply three-way-divided** races and
much rarer as the electorate grows and preferences spread along a spectrum. As with the
[runoff-reversal frequency](../../01_Single_winner/runoff_overturns_leader/README_runoff_overturns_leader.md) caveat:
any rate you quote depends on the voter model, so state the assumptions rather than a bare
number.

## Try it yourself / verify

`pref_voting` computes all of these (`copeland`, `minimax`, `beat_path` = Schulze,
`ranked_pairs`) — that's how the winners above were checked
([cross-check engine](../tabulation_engines/cross_checking_with_pref_voting.md)). For a quick
manual run, paste a `count:A>B>C` block into
[LeGrand's calculator](https://www.cs.angelo.edu/~rlegrand/rbvote/calc.html), which reports
Minimax, Ranked Pairs, Schulze, Copeland and more side by side.

## Learn more (external)

- Ranked Pairs — [Wikipedia](https://en.wikipedia.org/wiki/Ranked_pairs) · [electowiki](https://electowiki.org/wiki/Ranked_Pairs)
- Schulze method — [Wikipedia](https://en.wikipedia.org/wiki/Schulze_method) · [electowiki](https://electowiki.org/wiki/Schulze_method)
- Minimax — [Wikipedia](https://en.wikipedia.org/wiki/Minimax_Condorcet_method) · [electowiki](https://electowiki.org/wiki/Minimax)
- Smith set — [Wikipedia](https://en.wikipedia.org/wiki/Smith_set)

---

*Draft — open questions to refine later: add runnable YAMLs for the two worked profiles;
decide whether this lives here (Condorcet-family folder) or graduates to a `topics/` hub if
we add more cross-method deep-dives.*
