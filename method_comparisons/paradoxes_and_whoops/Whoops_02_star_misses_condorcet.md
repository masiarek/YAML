# Whoops 02 — STAR misses the Condorcet winner (STAR's own whoops)

**Level 301 · the one where STAR stumbles.** No method is perfect, and this is STAR's
signature failure. **Cleo is the Condorcet winner** — she beats Ada *and* Bruno
one-on-one — yet STAR elects **Ada**, because Cleo is a low-scored compromise who never
reaches the runoff. Same family as IRV's center squeeze: the broadly-acceptable middle is
excluded *before* the decisive comparison.

→ the three "winners" STAR can name: [`STAR_three_winner_notions`](../../00_start_here/STAR_Voting/STAR_three_winner_notions.md)
· STAR's limits: [AR hub](../../00_start_here/STAR_Voting/STAR_Automatic_Runoff.md#what-the-runoff-buys-you--and-its-limits)
· the ranked cousin: [center squeeze](../../00_start_here/RCV_IRV/RCV_IRV_center_squeeze.md)
· fairness test: [`reading_these_fairly.md`](reading_these_fairly.md).
↔ BV QA tracker: **BV149** (STAR fails to elect the Condorcet winner).

---

## The ballots (100 voters)

```
Ada, Bruno, Cleo
40 × 5, 1, 2      # Ada > Cleo > Bruno
35 × 1, 5, 2      # Bruno > Cleo > Ada
25 × 3, 3, 5      # Cleo > (Ada = Bruno)
```

Cleo is everyone's acceptable middle — but the two wings only score her a **2**. Source:
[`Whoops_02_star_misses_condorcet.yaml`](Whoops_02_star_misses_condorcet.yaml).

## Cleo wins every head-to-head — and still loses

- **Cleo vs Ada:** 60–40 for Cleo (the 35 Bruno voters + 25 Cleo voters prefer her).
- **Cleo vs Bruno:** 65–35 for Cleo.
- So **Cleo is the Condorcet winner** — a majority prefers her to each rival.

But STAR's first step is the **score total**, and the wings' stingy 2s sink her:

```
[Condorcet Winner] Cleo — STAR elected Ada instead (Cleo was eliminated in the scoring round)
[Divergence from STAR]  STAR = Ada   ·   Condorcet = Cleo

Scoring Round:    Ada 310 · Bruno 290 · Cleo 275   → Cleo finishes 3rd, misses the runoff
Automatic Runoff: Ada 40 (53%) vs Bruno 35 (47%)   (Cleo isn't in it) → Ada wins
```

Cleo (275) lands just behind Ada (310) and Bruno (290), so the **two polarizing wings
advance instead of the consensus pick**, and the runoff is held between them. The
candidate a majority actually preferred over both finalists never got to the final.

Full audit copy: [`_tabulated`](paradoxes_and_whoops_tabulated/Whoops_02_star_misses_condorcet_tabulated.txt).

## Why this one matters (don't bury it)

This is the honest counterweight to STAR's usual win over IRV. STAR's scoring round can
**exclude the Condorcet winner from the runoff** for the very same reason IRV eliminates a
centrist early: she's many people's strong *second*, few people's *first/high*. STAR is
much better at avoiding this than IRV — but "better" is not "immune," and a fair gallery
says so out loud.

> ### Reading this fairly
> - **How common:** *rare but structural.* STAR elects the Condorcet winner in roughly
>   **98%+** of spatial-model elections; this is the residual case where a low-scored
>   compromise is squeezed out of the top two. Real, not a knife-edge — but uncommon.
> - **Sincere or strategic:** fully **sincere.** No one gamed anything; honest stingy
>   scores from the wings are enough.
> - **What STAR does well:** usually *does* elect the Condorcet winner, keeps an expressive
>   ballot honest, and guarantees a majority-of-the-final-two winner. The miss is the
>   exception, not the rule.
> - **The symmetric whoops:** this is the **score-method twin of IRV center squeeze**
>   ([RCV_IRV_center_squeeze](../../00_start_here/RCV_IRV/RCV_IRV_center_squeeze.md)).
>   Different mechanism, same victim: the broadly-liked middle.
