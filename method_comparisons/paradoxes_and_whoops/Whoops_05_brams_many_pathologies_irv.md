# Whoops 05 — many IRV pathologies in one election (Brams)

**Level 301 · the sampler platter.** Steven Brams' famous example (*Notices of the AMS*,
1982; via [rangevoting.org §12](https://www.rangevoting.org/rangeVirv.html)) packs
**several** IRV anomalies into one 21-voter election. IRV elects **B**, but **G is the
Condorcet winner** — and the same ballots demonstrate a no-show paradox, a truncation
incentive, favorite-betrayal, and non-monotonicity.

A ranked-ballot case (no scores invented). → fairness test:
[`reading_these_fairly.md`](reading_these_fairly.md) · [`README`](README_paradoxes_and_whoops.md)
· (the repo's standalone monotonicity demo: [`monotonicity_irv_before.yaml`](../monotonicity/monotonicity_irv_before.yaml)).

---

## The ballots (21 voters)

```
7 : B>G>N>F
6 : G>B>N>F
5 : N>G>B>F
3 : F>N>G>B
```

Source: [`Whoops_05_brams_many_pathologies_irv.yaml`](Whoops_05_brams_many_pathologies_irv.yaml).

## G beats everyone — and IRV still drops it

- **G is the Condorcet winner:** G beats B **14–7**, beats N **13–8**, beats F 18–3.
- **IRV elects B:**

```
Round 1:  B 7 · G 6 · N 5 · F 3      → F eliminated, flows to N
Round 2:  N 8 · B 7 · G 6            → G eliminated (the Condorcet winner!), flows to B
Final:    B 13 · N 8                 → B wins
```

## Four pathologies in one (per Brams / rangevoting.org)

1. **Condorcet failure** — G would beat every opponent one-on-one, yet is eliminated.
2. **No-show paradox** — if the 3 `F>N>G>B` voters had *stayed home*, G would win — an
   outcome they prefer to B. Voting *hurt* them.
3. **Truncation / favorite-betrayal incentive** — those same voters could get the better
   (for them) result by *not* fully ranking, or by insincerely ranking G top — so IRV
   pushes voters to hide or betray their true favorite (the opposite of what it promises).
4. **Non-monotonicity** — a variant where voters *raise* a candidate flips the result the
   wrong way (Brams' "raise-to-top failure").

## Why it's a fair example

Sincere ballots, a published academic source, and the anomalies are *logical
consequences* of the ballots — not artifacts of weird weights.

> ### Reading this fairly
> - **How common:** the individual anomalies are *structural* (Smith's analysis: ~15% of
>   3-candidate IRV elections are non-monotonic); getting *all four* in one tiny election
>   is a curated illustration, but each is real.
> - **Sincere or strategic:** the failures arise under **sincere** voting; the
>   truncation/betrayal points are about the *incentive* IRV creates, clearly labeled.
> - **What IRV does well:** simple, familiar, majority-of-the-final-two. These pathologies
>   are rarer in 2-strong-candidate races.
> - **The symmetric whoops:** see [Whoops 02](Whoops_02_star_misses_condorcet.md) (STAR
>   misses a Condorcet winner) and [Whoops 03](Whoops_03_condorcet_cycle_rps.md) (no
>   Condorcet winner exists). Tally in the [balance ledger](README_paradoxes_and_whoops.md#balance-ledger).
