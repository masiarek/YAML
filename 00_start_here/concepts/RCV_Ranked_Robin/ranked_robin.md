# Ranked Robin (aka Consensus Voting) — RCV-RR

*A ranked method that compares every candidate head-to-head and elects whoever beats the most rivals. Same ranked ballot as IRV, but a completely different — and far more transparent — way of counting it.*

→ **Run it / tabulated example:** [`summability_demo/`](../../../01_Single_winner/summability_demo/)
shows the **pairwise matrix** (the Ranked Robin tally) computed and *added across precincts*;
the [`pref_voting` engine](../../../pref_voting_tabulation_engine/README.md) reports the
**Copeland = Ranked Robin** winner on any election (`python pref_voting_tabulation.py example_tennessee.yaml`).
· Topic hub: [Summability](../topics/summability/README.md).

---

**Ranked Robin** (also marketed as **Consensus Voting**, and abbreviated **RCV-RR**) is a **Condorcet** method: it's a round-robin tournament among the candidates. You rank the candidates — and crucially, **you may rank candidates equally** — then the count compares **every pair** of candidates head-to-head and elects the one who **wins the most matchups** (ties broken by the sum of win margins).

Because it's computed entirely from the **pairwise matrix** (for each pair, how many voters preferred A to B), it has the properties IRV lacks while using essentially the same ballot voters already know.

> **Sibling branding — "Consensus Choice."** The same core Condorcet idea is promoted by *Better Choices for Democracy* as **Consensus Choice** (often paired with a "Top 4" open primary front end). It allows equal ranks, compares every pair head-to-head, and is precinct-summable. It differs from Equal Vote's Ranked Robin mainly in packaging and in its **cycle-resolution rule** ("Most Wins, Smallest Loss" vs. RR's sum-of-margins). Treat "Ranked Robin," "Consensus Voting," and "Consensus Choice" as close cousins in the Condorcet family, not identical algorithms.

## How it differs from RCV-IRV (Hare)

| | **RCV-IRV (Hare)** | **Ranked Robin (RCV-RR)** |
|---|---|---|
| Ballot | Rank, **no equal ranks** | Rank, **equal ranks allowed** |
| How it counts | Eliminate fewest-first-choice, transfer, repeat | Compare **every pair**; most head-to-head wins |
| Uses your lower ranks? | Only after higher ones are eliminated | **Always** — every ranking counts against every opponent |
| Pairwise (head-to-head)? | ❌ No | ✅ **Yes** |
| Elects the Condorcet winner? | Not always (can center-squeeze) | ✅ Yes, when one exists |
| Monotonic? | ❌ No | ✅ Yes |
| Precinct-summable? | ❌ No | ✅ Yes (add pairwise matrices) |
| Exhausted ballots? | Possible | No — all rankings are read |

The headline: the two things people *assume* "RCV" does — let you mark ties and compare candidates head-to-head — are exactly what **RCV-RR (Ranked Robin)** does and what **RCV-IRV (Instant-Runoff Voting)** does not. (See [strict_vs_weak_ranks.md](../strict_vs_weak_ranks.md) and [RCV_IRV_and_plurality.md](../RCV_IRV/RCV_IRV_and_plurality.md).)

## Why it matters

Because it reads every ranking against every opponent, Ranked Robin elects the candidate **most voters prefer in head-to-head comparison** — the "consensus" / Condorcet winner — which is precisely the broadly-liked moderate that IRV can [center-squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) out. It's also **monotonic** and **summable** by adding precinct pairwise matrices, so it avoids two of IRV's biggest mechanical problems while keeping a familiar ranked ballot.

## For balance — its limits

Ranked Robin isn't a cure-all. Like all ranked methods it captures **order only, not strength** — it can't tell a near-tie from a landslide ([scores_vs_ranks.md](../scores_vs_ranks.md)) — so it carries less information than a scored method like STAR. When there's a **Condorcet cycle** (A beats B, B beats C, C beats A, with no candidate beating all others), there is no Condorcet winner and the method falls back on a tiebreak rule (sum of margins), which reasonable people can debate. And no method escapes Gibbard–Satterthwaite. Its real-world **adoption is limited** so far compared with IRV.

## Now you can tabulate it — the `pref_voting` engine

The repo's new [`pref_voting_tabulation_engine/`](../../../pref_voting_tabulation_engine/README.md)
computes this method on any example election, under its **academic name, Copeland**.

**Copeland = Ranked Robin = Consensus Voting = RCV-RR** — *the same core method wearing
different brand names from different proponent groups:*

| Name | Who calls it that |
|------|-------------------|
| **Copeland's method** | academic social-choice literature (order candidates by pairwise **wins − losses**) |
| **Ranked Robin** | the **Equal Vote Coalition** |
| **Consensus Voting / Consensus Choice** | **Better Choices for Democracy** |
| **RCV-RR** | this repo's house compound (ranked ballot + Ranked-Robin count) |

They're the **same idea**: elect whoever wins the most head-to-head matchups (the
Condorcet/Copeland winner). They agree on the winner whenever a Condorcet winner exists —
i.e. almost always — and differ *only* in the **cycle/tie-break rule** (Ranked Robin: sum
of margins; Consensus Choice: "Most Wins, Smallest Loss"; textbook Copeland: by score). So
treat them as one method with several brands, not byte-identical algorithms.

> **House naming (which word when).** Say **Ranked Robin (RR)** to people — it's the
> friendliest adopted name. Use **RCV-RR** in method comparisons and engine output, exactly
> parallel to **RCV-IRV** (ranked ballot + which count). Use **Copeland** when talking to
> the *engine* or academics (it's what `pref_voting` calls it). Mention **Consensus
> Voting / Consensus Choice** once as the advocacy brand, then move on. (Same
> meet-them-where-they-are rule as [`TIPS_terminology.md`](../../TIPS_terminology.md).)

```bash
# run Copeland (= Ranked Robin) on any election, beside the other methods:
cd pref_voting_tabulation_engine
python pref_voting_tabulation.py example_tennessee.yaml
#   Copeland   pref_voting=Nashville   (= the Ranked Robin / Consensus winner)
```

Since BetterVoting ships a Ranked Robin tabulator too, this gives you an **independent
Python reference** to reconcile BV's RCV-RR results against — the same cross-checking we do
for STAR and RCV-IRV. Details:
[`cross_checking_with_pref_voting.md`](../tabulation_engines/cross_checking_with_pref_voting.md).

---

## Related concept pages

- [Ranked Robin is summable](./RCV_RR_summability.md) — the pairwise matrix adds across precincts (and the topic hub: [Summability](../topics/summability/README.md))
- [Strict vs. weak ranks](../strict_vs_weak_ranks.md) — Ranked Robin allows equal ranks; IRV doesn't
- [Center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) — the failure RR avoids and IRV doesn't
- [Is IRV "just plurality"?](../RCV_IRV/RCV_IRV_and_plurality.md) — why IRV isn't pairwise
- [Scores vs. ranks](../scores_vs_ranks.md) — RR is still order-only, unlike STAR
- [RCV-IRV vs. STAR (side-by-side)](../rcv_irv_vs_star.md)
- [RCV vs. IRV vs. RCV-IRV — terminology](../RCV_IRV/RCV-IRV-confusing-name.md)

## Learn more — external

- [Equal Vote Coalition — Ranked Robin](https://www.equal.vote/ranked_robin) *(pro-Ranked-Robin advocacy)*
- [Better Choices for Democracy — Consensus Choice FAQs](https://www.betterchoices.vote/faqs) *(advocacy; the same Condorcet idea, "Top 4" + Consensus Choice branding)*
