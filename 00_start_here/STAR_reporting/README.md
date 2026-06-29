# STAR Reporting — reading and comparing results

**One line:** how a STAR result is *reported* — the numbers (scores, runoff counts,
percentages), what a "no preference" ballot means (**Equal Support** vs **abstention**),
and how the two reports in this repo — **BetterVoting**'s visual display and the **LH
`starvote` engine**'s text report — present the same election (and where they
occasionally diverge).

This folder is a **hub**: short, reporting-focused pages that link out to the
canonical deep-dives rather than restate them.

---

## What's in a STAR result

A STAR result is a short funnel, and every report shows the same stages:

1. **Counts / scores** — add every star; each candidate gets a total. (STAR is
   *summable*: precinct totals add up. → [STAR summability](../STAR_Voting/STAR_summability.md))
2. **Finalists** — the two highest scorers advance.
3. **Automatic Runoff** — each ballot goes to whichever finalist it scored higher.
4. **Percentages** — the winner needs a majority of the voters **with a preference**
   between the two finalists. (→ [Runoff percentages — two denominators](../STAR_Voting/runoff_percentages.md))
5. **No-preference ballots** — ballots that score the two finalists equally are
   **Equal Support** (counted in the score round, set aside from the runoff
   percentage); a fully blank ballot is an **abstention**. (→ [`GLOSSARY`](../GLOSSARY.md))

## The two reports

| Page | What it covers |
|---|---|
| **[How the LH engine reports](reporting_LH/README.md)** | the text/audit report — score distribution, matrix, both rounds, the self-reconciling runoff line + "Runoff math" funnel |
| **[How BetterVoting reports](reporting_BV/README.md)** | the live visual — scoring bars, runoff bars/pie, the two percent columns, abstention count |
| **[Where the two reports differ](reporting_diff_BV_LH.md)** | same winner, different abstention/score-total bookkeeping — the flat-ballot reconciliation |

## Report elements, up close

| Page | What it explains |
|---|---|
| **[Score Distribution](reporting_LH/score_distribution.md)** | the per-score breakdown (how many 5s, 4s … 0s, blanks); Total and Avg; `0` vs blank |
| **[Preference Matrix & Condorcet](reporting_LH/matrix.md)** | head-to-head `For – Equal Support – Against`; two-candidate vs full N×N; `show_condorcet` |
| **[Reporting true ties](reporting_ties.md)** | how a tie shows up in each report; why the runoff-percentage line is suppressed on an exact tie |
| **[LH reporting options](reporting_LH/options.md)** | what each `options:` flag (`show_matrix`, `show_condorcet`, `brief`, `show_runoff_percent` …) adds to or removes from the report |

## Canonical deep-dives (linked, not duplicated)

- [Reading a STAR report](../tabulation_engines/LH_starvote/reading_a_star_report.md) — the LH report, section by section.
- [BetterVoting and the LH engine](../tabulation_engines/bettervoting_and_the_engine.md) — why one election has two reports, and how they map.
- [Runoff percentages](../STAR_Voting/runoff_percentages.md) — the two-denominator idea.
- [Tabulation, step by step](../tabulation_star_vs_irv.md) — STAR's two steps vs IRV's rounds.

## Worked examples — always two views

House rule: every reporting example carries **two views of the same election** — the
**BetterVoting** result (by its BV election ID) and the **LH engine** result (the BV
JSON tabulated by LH, i.e. the `_tabulated` mirror). Compare them side by side.

| Example | BetterVoting (election ID) | LH engine (tabulated mirror) |
|---|---|---|
| Pet race, 461 ballots | **`pet`** → [bettervoting.com/pet/results](https://bettervoting.com/pet/results) | [`best_pet_c7_b461_tabulated.txt`](../../01_Single_winner/pet_real_bv_election_tabulated/best_pet_c7_b461_tabulated.txt) · [lesson](../../01_Single_winner/pet_real_bv_election/README.md) |
| 3-candidate flat-scores | **`dq2dmm`** | [`flat_scores_abstention_c3_b8_tabulated.txt`](../../01_Single_winner/pet_real_bv_election_tabulated/flat_scores_abstention_c3_b8_tabulated.txt) · [lesson](../../01_Single_winner/pet_real_bv_election/small_case_abstention_lesson.md) |
| 2-candidate minimal | **`3w6v4b`** | [`small_abstention_c2_b5_tabulated.txt`](../../01_Single_winner/pet_real_bv_election_tabulated/small_abstention_c2_b5_tabulated.txt) · [lesson](../../01_Single_winner/pet_real_bv_election/small_abstention_c2_b5_lesson.md) |
| Runoff tie | *(create one — see [ties](reporting_ties.md))* | [`02b_c3_b2_three-candidates_tabulated.txt`](../../01_Single_winner_tabulated/02b_c3_b2_three-candidates_tabulated.txt) |
