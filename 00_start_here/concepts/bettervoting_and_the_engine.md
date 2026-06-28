# BetterVoting and the LH Engine — One Election, Two Reports

**One line:** the same STAR election shows up in these materials as **two** result
reports — BetterVoting's **live visual display** (what voters see) and the LH `starvote`
**engine's text report** (the full audit/teaching tabulation). They're independent
implementations of the *same* STAR method, so they **agree** on the winner, the scores,
and the runoff. Two reports, one count.

→ The engine report section by section: [reading a STAR report](./STAR_Voting/reading_a_star_report.md).
The runoff percentages in both: [runoff percentages](./STAR_Voting/runoff_percentages.md).
Glossary: [`BetterVoting`](../GLOSSARY.md).

---

## Why there are two reports

| | **BetterVoting** (bettervoting.com) | **LH `starvote` engine** (this repo) |
|---|---|---|
| What it is | the live web app voters run elections on | a text tabulator for study, teaching, auditing |
| Audience | voters, organizers | presenters, auditors, this curriculum |
| Output | interactive charts + Race Details tables | a full plain-text report (the `_tabulated.txt` copy) |
| Strength | one-click, visual, shareable | every step shown: matrix, divergence, both rounds |

They are not rivals and they don't disagree: STAR is STAR. Feed both the same ballots and
you get the same finalists, the same runoff counts, the same winner. When a lesson shows a
BetterVoting screenshot *and* an engine report, they're two views of one count — pick
whichever makes the point clearer.

How the pieces line up (same Dog/Cat race):

| BetterVoting shows … | … the engine shows the same as |
|---|---|
| **Scoring Round** bars | **Scoring Round** block (total stars; top two advance) |
| **Automatic Runoff** bars / pie | **Automatic Runoff Round** block (finalist counts + Equal Support) |
| **% Between Finalists** (52 / 48) | the `show_runoff_percent` line — *Voters with a preference: 363…* |
| **Race Details** tables | the **Preference Matrix** (For–Equal–Against) + runoff block |

## How a real election becomes a trusted example

The two reports are tied together by a pipeline. A real ballot file — a BetterVoting JSON
export, or data in ABIF / CSV / BLT / ranked form — is converted to a **YAML election**,
validated, and tabulated, then **cross-checked against BetterVoting's own result** before
it's saved as a trusted test case:

![Workflow: if a file isn't already YAML, convert it from the source format (ABIF, Larry Hastings format, CSV/TXT, BLT, ranks) to YAML; validate the YAML (consistency, formatting, plausibility, required sections); if checks fail, correct and re-validate; load into BetterVoting for regression / unit testing; if the results, reports and statistics are correct, mark expected results approved in the YAML and save to the test library; if not, file a GitHub bug report with the YAML attached](./img/workflow_convert_validate_test.png)

That loop is why the examples here can be trusted: every saved election has been tabulated
*and* cross-checked, and the engine's answer key is only marked "approved" once it matches.
The BetterVoting-JSON → YAML converter is `YAML_library/1_positive/01_convert_json_yaml.py`,
and a guard test (`STARVote_LH_tabulation_engine/tests/test_json_to_yaml_conversion.py`)
re-converts a real export and confirms the engine reproduces the stated winner. Two
independent implementations cross-checking each other is a *feature* — it's how you trust
a count.

## "Two engines" under the hood

"Two tabulation engines" also describes the repo itself. Score ballots and ranked ballots
are counted in fundamentally different ways, so each has its own engine:

- **`STARVote_LH_tabulation_engine`** (Larry Hastings' `starvote`) — the **score** methods:
  STAR, Bloc / Proportional STAR, Approval.
- **`RCV_IRV_tabulation_engine`** (vendored **pyrankvote**) — **ranked** ballots, for the
  RCV-IRV comparisons.

The main engine auto-dispatches: a file with ranked `A>B>C` ballots (or `voting_method:
RCV_IRV`) is handed to the RCV-IRV engine; score grids stay with `starvote`. Why the two
*counts* differ so much — even on identical preferences — is
[STAR vs RCV-IRV, step by step](./tabulation_star_vs_irv.md).
