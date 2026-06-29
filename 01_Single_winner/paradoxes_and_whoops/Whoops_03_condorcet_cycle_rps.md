# Whoops 03 — a Condorcet cycle (rock-paper-scissors, no winner)

**Level 301 · the paradox of voting itself.** The most famous anomaly in the field, and
the one that humbles the *Condorcet* ideal: a majority can prefer **Rock over Paper,
Paper over Scissors, and Scissors over Rock** — a loop with no top. When that happens
there is **no Condorcet winner at all**, so Condorcet / Ranked Robin can't name one
without an extra cycle-breaking rule. This is *their* whoops.

→ fairness test: [`reading_these_fairly.md`](./reading_these_fairly.md)
· [`GLOSSARY` (Condorcet cycle)](../../00_start_here/GLOSSARY.md) · the set: [`README`](./README.md)
· how Condorcet methods break cycles: [Cycle resolution](../../00_start_here/concepts/RCV_Ranked_Robin/cycle_resolution.md).
↔ BV QA tracker: **BV147 / BV188** (Condorcet cycle / paradox — BV: [w7y3wv](https://bettervoting.com/w7y3wv/results), [6mbvhg](https://bettervoting.com/6mbvhg/results)).

---

## The ballots (100 voters)

```
Rock, Paper, Scissors
35 × 5, 3, 0      # Rock > Paper > Scissors
33 × 0, 5, 3      # Paper > Scissors > Rock
32 × 3, 0, 5      # Scissors > Rock > Paper
```

The cast is the lesson: it really is rock-paper-scissors. Source:
[`Whoops_03_condorcet_cycle_rps.yaml`](./Whoops_03_condorcet_cycle_rps.yaml).

## Majority rule eats its own tail

Tally the head-to-heads and you get a loop:

- **Rock beats Paper** (67–33) · **Paper beats Scissors** (68–32) · **Scissors beats Rock** (65–35).

There is no "beats everyone" candidate — majority preference is **intransitive**. So the
Condorcet question simply has *no answer* here:

```
[Condorcet Winner] No Condorcet winner (majority cycle: Rock > Paper > Scissors > Rock)
[Divergence from STAR]  STAR = Rock   ·   Approval = Paper

Scoring Round:    Rock 271 · Paper 270 · Scissors 259   (Rock & Paper advance)
Automatic Runoff: Rock beats Paper  → Rock wins (by a single point upstream)
```

The **score methods still finish** — STAR elects **Rock** (271 vs Paper's 270, razor
thin), Approval picks **Paper** — but notice they don't agree *either*, and the Condorcet
method can't even start. Full audit copy:
[`_tabulated`](../paradoxes_and_whoops_tabulated/Whoops_03_condorcet_cycle_rps_tabulated.txt).

## The teaching moment

"Let the majority decide" sounds airtight until you meet a cycle: every option loses to
*something* by a majority. It's not a bug in any one method — it's a fact about
aggregating preferences (the root of **Arrow's theorem**). Methods differ in *how they
cope*: Condorcet/Ranked Robin need a documented cycle-breaker; STAR and Approval always
return *a* winner, but which one now depends on intensities and thresholds, not on a clean
majority.

> ### Reading this fairly
> - **How common:** *rare with large, varied electorates*, but **foundational** — this is
>   the Condorcet paradox itself, not a contrived weighting. Cycles get likelier with
>   sharply divided three-way races.
> - **Sincere or strategic:** fully **sincere** — the cycle is in the honest preferences.
> - **What Condorcet/Ranked Robin do well:** when a Condorcet winner *exists* (the usual
>   case), electing them is a very strong guarantee. Cycles are the price of asking for it.
> - **The symmetric whoops:** STAR doesn't escape clean here either — its 271-vs-270 finish
>   is essentially a coin-flip margin, and it disagrees with Approval. No method makes a
>   cycle *not* be a cycle.
