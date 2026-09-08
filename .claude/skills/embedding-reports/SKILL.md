---
name: embedding-reports
description: How an engine report or output snippet gets into a hand-authored Markdown page in this repo — the generated `report:` block, matching depth to the election, routing a short snippet to the full report, and why an annotated or curated fence must be labelled abridged instead of converted. Load before pasting or embedding any engine output on a teaching page.
---

# Embedding an engine report in a page

*Migrated out of `CLAUDE.md` on 2026-09-08 so it loads on demand instead of in every session. The rules below are unchanged.*

**Embed LH output as text in Markdown (Adam's preference), sized to the election.**
When a teaching/reporting `.md` discusses a result, paste the actual LH output inline
as a fenced code block (strip ANSI) rather than only linking the `_tabulated` file —
the reader should see the output on the page. **Match the depth to the election:**
- **Small / simple** examples → embed the **short on-screen report** (the on-screen render with
  the file's minimal options), not a full dump.
- **Large or complex** elections (many ballots/candidates), or docs whose point *is*
  the matrix / Condorcet / score-distribution detail → embed the fuller
  **`_tabulated`** report, or just the specific section being discussed.

Either way, keep a link to the full `_tabulated` mirror too.
- **Route the short snippet to the full report (Adam likes the long LH reports).** When a
  hand-authored teaching page embeds a *short* on-screen snippet **and the example is a real
  case file**, add a one-click pointer to that case's **full generated page**
  (`…/cases_pages/<stem>.md`, which carries the matrix / Condorcet / score-distribution audit)
  or its `_tabulated` mirror — e.g. *"Want the whole count? see the full LH report → `…/cases_pages/<stem>.md`."* Keep
  the crisp snippet for the lesson; the full report stays one click away and never drifts (the
  link auto-updates; a pasted long report would go stale). **Skip this for *generic
  illustrations*** (invented candidates with no backing case file) — a "full report" link there
  is a dead end. Prefer the generated page over pasting the long report inline on a teaching
  page, which buries the lesson (e.g. the runoff page is *about* the reversal, not the matrix).
- **Engine reports get GENERATED into the page, never hand-pasted.** To show a case's
  count, mark the spot and let `build_yaml_pages.py` fill it:

  ```
  <!-- report:<stem> -->
  <!-- /report -->
  ```

  The generator copies in the report fence from that case's generated page
  (`<set>/cases/cases_pages/<stem>.md`, wrapped there in `[start:report]` / `[end:report]`
  markers for exactly this), so there is still one source of truth and
  `tests/test_yaml_pages_current.py::test_report_blocks_are_current` fails on drift.
  Same contract as `case-meta` and `ballots:` — inside the markers is generated, outside
  is yours. The `<stem>` is a bare case stem, no path: generated-page stems are unique
  repo-wide. Reach for a *different* case's stem when the block is a different election —
  a page can show several (`ex06_bullet_backfire.md` embeds `ex06_bullet_honest` for its
  honest-ballot half).
  **Do NOT use `--8<-- "…:report"` for this** (the idiom this replaced, 2026-08-04).
  `pymdownx.snippets` is a MkDocs extension, so the include renders on the site and
  prints as a **line of literal text on GitHub** — 82 pages showed a "the LH report"
  heading followed by `--8<-- "…"` and no report at all to anyone reading the repo on
  GitHub. `test_no_snippet_report_includes_remain` now fails on a new one. Snippets are
  still right for whole-file embeds *inside* a fence (a `.yaml`, say):
  `--8<-- "<repo-relative path>"`, paths resolving from the repo root, `title="…"` naming
  the file — those degrade to a visible placeholder inside a code block rather than to
  broken prose. **Never embed the `_tabulated` mirror** — it drags in its ~50-line YAML
  echo and, for a big field like `Runoff_08_ca_governor_reversal_gvdy42`, 785 lines of
  audit; link it instead.
  `check_repo_hygiene.py::check_pasted_reports` (gated by `tests/test_md_links.py`) fails
  on a new ≥8-line engine-shaped fence that is outside a `report:` block and not labelled
  abridged.
- **Deliberate compressions stay — label them, don't convert them.** Put
  `title="Abridged for the lesson — not verbatim engine output"` on the fence: it renders as
  a visible caption and satisfies the gate. `bv750_tie_breaking_bloc.md`'s
  `a 15 ; b 15 ; c 15  ← three-way tie` is the lesson, not stale output.
- **An annotated fence is NEVER convertible.** If a block carries `←` margin notes
  (`Ada -- 15  ← Ada is now THIRD`), a `#` aside, or `·`-joined tallies, it is a rendition
  the author built for the lesson — replacing it with an include deletes the annotation that
  was the entire point. Nine were destroyed that way before this was written down; they are
  restored and labelled. **Annotation ⇒ abridged, always.** The same goes for a *curated
  excerpt* (just the matrix, just the divergence block): the selection is authorial, so
  label it rather than swapping in the whole report.
