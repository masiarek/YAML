# How the LH engine reports a STAR result

**One line:** the LH `starvote` engine prints a **full text audit report** — every
number that produced the winner, in order — and saves a maximal `_tabulated.txt`
copy of it. This page is the reporting-lens summary; the section-by-section walk is
[Reading a STAR report](../../tabulation_engines/LH_starvote/reading_a_star_report.md).

→ Hub: [STAR Reporting](../README_STAR_reporting.md) · the engine itself: [BetterVoting and the LH engine](../../tabulation_engines/bettervoting_and_the_engine.md) · [`GLOSSARY`](../../GLOSSARY.md).

---

## What the report shows, top to bottom

- **`Tabulating N ballots.`** — the count, plus a note for any **abstention** (a
  fully blank ballot; an explicit all-zero is a *cast* ballot, not an abstention).
- **[Score Distribution](score_distribution.md)** *(optional)* —
  per-candidate spread of 0–5 scores, with an **Abs** column for blanks.
- **Scoring Round** — total stars per candidate; the **top two advance**.
- **[Preference Matrix](matrix.md)** — head-to-head table, legend
  **For – Equal Support – Against**, and the Condorcet check.
- **Automatic Runoff Round** — each finalist's vote count plus **Equal Support** (the
  ballots that scored the two finalists equally).
- **The runoff percentage line** — on screen, a **self-reconciling** two-line summary:

  ```
  Voters with a preference: 363 of 461 (98 Equal Support).
  Dog 190 (52%) vs Cat 173 (48%); majority = 182.
  ```

  It names the decided count *against the total* with the Equal Support gap inline,
  so the denominator never has to be inferred. (→ the two-denominator idea:
  [Runoff percentages](../../STAR_Voting/runoff_percentages.md).)
- **"Runoff math" funnel** — in the saved `_tabulated.txt`, the same line expands so
  the arithmetic is explicit:

  ```
     Runoff math:
       461  ballots cast
     −  98  Equal Support (no preference between the two finalists)
       ───
       363  voters with a preference  (majority = 182)
             Dog 190 (52%)  ·  Cat 173 (48%)
  ```
- **Condorcet check / [Divergence from STAR]** — whether the pairwise winner matches,
  and a flag when methods would disagree.
- **Winner.**

## On-screen vs the saved copy

The on-screen echo honors the file's `options:` (house default is minimal). The
`_tabulated.txt` sibling is always the **maximal** render — every analysis on, the
runoff line expanded into the funnel — so the saved audit copy is fully
self-explanatory. Which flag shows which section: [**LH reporting options**](options.md).
(House defaults: `CLAUDE.md`.)

See it on a real election: [the pet race report](../../../01_STAR/pet_real_bv_election/README_pet_real_bv_election.md).
