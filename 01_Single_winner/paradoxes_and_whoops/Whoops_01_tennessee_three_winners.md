# Whoops 01 — same ballots, three methods, three winners (Tennessee)

**Level 201 · the headline whoops.** The classic Tennessee state-capital puzzle. Four
cities, one set of sincere ballots — and **three different methods crown three different
cities.** It's the cleanest demonstration that "the winner" isn't a property of the
voters; it's a property of the *rule*.

→ fairness test: [`reading_these_fairly.md`](./reading_these_fairly.md)
· the set: [`README`](./README.md) · [`GLOSSARY`](../../00_start_here/GLOSSARY.md).

---

## The setup (100 voters on a map)

Tennessee wants one capital. Everyone wants it **close to home**, so preferences track
geography: Memphis (far west), Nashville (central), Chattanooga (southeast), Knoxville
(east).

```
Memphis, Nashville, Chattanooga, Knoxville
42 × 5, 2, 1, 0      # Memphis voters
26 × 1, 5, 3, 2      # Nashville voters
15 × 0, 3, 5, 4      # Chattanooga voters
17 × 0, 3, 4, 5      # Knoxville voters
```

Scores are a simple distance model (home city 5, falling off with distance). Source:
[`Whoops_01_tennessee_three_winners.yaml`](./Whoops_01_tennessee_three_winners.yaml).

## Three methods, three winners

- **Plurality → Memphis.** Memphis has the most first-choices (42%) — and *only* 42%. A
  clear majority (58%) would rather have almost anywhere else, but Plurality never asks.
- **RCV-IRV → Knoxville.** Chattanooga is eliminated first (fewest firsts) and flows to
  Knoxville; then Nashville is eliminated and *also* flows east; Knoxville wins 58–42. The
  central compromise (Nashville) is squeezed out before the final count.
- **Condorcet & STAR → Nashville.** Nashville beats every other city head-to-head and has
  the highest score total — the geographic compromise nobody is far from. STAR advances it
  to the runoff on strength of support and it wins.

```
[Condorcet Winner] Nashville — matches the STAR winner
[Divergence from STAR]
  STAR                   = Nashville
  Choose-One (Plurality) = Memphis     (differs)
  RCV-IRV                = Knoxville    (differs)

Scoring Round:   Nashville 310 · Chattanooga 263 · Memphis 236 · Knoxville 197
Automatic Runoff: Nashville 68 (68%) vs Chattanooga 32 (32%)  → Nashville wins
```

Full audit copy: [`_tabulated`](../paradoxes_and_whoops_tabulated/Whoops_01_tennessee_three_winners_tabulated.txt).

## Why it's the perfect opener

No one voted strategically; the ballots are honest geography. The disagreement is purely
about **what question each method asks** — most-first-choices (Plurality), last-one-
standing (IRV), or beats-everyone-else (Condorcet/STAR). Same data, three answers.

> ### Reading this fairly
> - **How common:** *structural* — three-way disagreements are routine whenever a centrist
>   sits between two larger wings; Tennessee is the canonical illustration, not a one-off.
> - **Sincere or strategic:** fully **sincere** — no manipulation needed.
> - **What each does well:** Plurality is dead simple; IRV guarantees a majority of the
>   *final two* and handles many fields fine. The catch here is specific to the centrist
>   geometry.
> - **The symmetric whoops:** STAR isn't immune to weird results either — it just gets
>   *this* one right. See [Whoops 02](./Whoops_02_star_misses_condorcet.md), where STAR is
>   the one that stumbles.
