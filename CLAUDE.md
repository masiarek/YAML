# CLAUDE.md — working guidance for this repo

Standing instructions for Claude when working in this project — and the house
conventions for anyone contributing (human front door: [CONTRIBUTING.md](CONTRIBUTING.md)).
The Claude-only operational grants live at the [bottom of this file](#agent-operations-claude-specific).

## What this is
A **STAR Voting education** repo built on a fork of Larry Hastings' `starvote`
(single-winner STAR engine + extra reporting), plus a vendored RCV-IRV engine,
example YAML elections, teaching docs, and Larry↔Adam conversation scripts.
Audience: voters, presenters, and debaters learning/teaching STAR.

---

## Terminology policy (important — keep it consistent & correct)

**Background:** "RCV" is widely used loosely to mean IRV (FairVote-era usage that
also trained most AIs to be sloppy). We meet people where they are, but we stay
precise. The key idea: **RCV names a BALLOT (ranked); IRV names one TABULATION of
it.** Other tabulations of the *same* ranked ballot: **Ranked Robin** (Condorcet
/ "consensus"), **STV** (proportional).

**House style:**
- **Default to `RCV-IRV`** in this repo's method comparisons, engine output, and
  debate/teaching docs. Unambiguous, and already the engine's term.
- **Use `IRV`** in technical/critical passages — center squeeze, exhausted
  ballots, non-monotonicity are **IRV-specific**, *not* properties of all ranked
  ballots (Ranked Robin isn't squeezed). Saying "RCV does X" there is imprecise
  and an easy target.
- **Reserve bare `RCV`** for "the ranked-ballot family," and say so when used that
  way.
- **Name `Ranked Robin` / `STV`** explicitly; never fold them into "RCV" = IRV.
- **Don't be a purist who derails.** When others use "RCV" loosely, keep their
  word, correct once, move on. Don't fight the wind.

**US-usage caveat (the nuance):** `RCV-IRV` is a deliberate *house* compound, **not
standard US usage** — appending "IRV" can look odd or confusing to a general
public audience, who only know "RCV." So:
- **Technical / debate / engine / docs → `RCV-IRV` (or `IRV`).** Precision wins.
- **Public-facing copy (slides, intro talk) → "RCV" is fine**, but clarify *once*
  on first mention: e.g. *"RCV — ranked ballots counted by instant runoff (IRV)."*
  Then use the familiar word.

Family tree, when-to-use table, and glossary are canonical — **do not restate the
taxonomy from memory:** see `07_Concepts/tips/TIPS_terminology.md` and `GLOSSARY.md`.

**Other voting-term canon:**
- **STAR** = Score Then Automatic Runoff (a *score* ballot + that tabulation; the
  same ballot can be Approval / Score / Proportional STAR).
- **Equal Support** is the canonical label for the no-preference runoff bucket
  (matrix legend *and* runoff) — printed **plain**, just "Equal Support". The aka
  (Equal Preference / No Preference) is documented once in `GLOSSARY.md`, **not**
  shown on screen on every runoff line. Do **not** reintroduce "Equal Preference" as the
  lead term.
- **Favorite Betrayal Criterion ≠ Later-No-Harm** — keep distinct. Neither STAR
  nor IRV is FBC-compliant; RCV-IRV fails it structurally (center squeeze), STAR
  only in rare constructions. See `01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md`.
- Spelling: **Bucklin** (not "Buckling"). **Hare ≈ IRV** single-winner, **STV**
  multi-winner. Borda & Bucklin are ranked but **not** Condorcet.

---

## Repo conventions (so output stays consistent)
- **Case files carry NO `options:` block (settled 2026-08-09).** The display flags
  were maintainer conveniences that had accreted into ~10 lines of noise per file —
  a quarter of a median case file — and a case file should read as a plain-text
  election scenario: title → description → method → ballots → expected winners.
  The engine's own defaults ARE the house on-screen style now — one
  `DEFAULT_OPTIONS` dict in `starvote_larry_hastings.py`: finalists matrix ON, the
  self-reconciling runoff summary ON, description / Condorcet / score-distribution
  OFF, ballots collapsed with `×`. Two auto-gates cover what files used to
  hand-set: the matrix switches itself off for **multi-winner** races (a "Top 2
  Finalist" grid is a single-winner concept, misleading for PR/Bloc) and for
  **2-candidate** races (it would just echo the runoff); and **Ranked Robin prints
  its pairwise table by default** (the round-robin table IS the method; the Smith
  block stays a separate opt-in). The saved `_tabulated` copy still renders
  **maximum info automatically**, and the **`--full`** CLI flag puts that same
  everything-on render on screen — with one seam (closed 2026-08-09): for a
  **multi-winner** race the forced-on grid prints as a plain, unmarked
  **"Preference Matrix"** (the "Top 2 Finalist" markers came from a silent
  seats=1 STAR analysis; an "Informational only — not part of the N-winner
  count" legend line replaces them, and the same unmarked grid is what a
  `show_matrix: true` override puts on screen). Consequences:
  - **Don't add an `options:` block to a case file.** A lesson that wants a heavier
    section on the page (score distribution, full grid, Smith set) links the case's
    generated page / `_tabulated` mirror — which force everything on — or pastes
    from a `--full` run; it does not flip flags in the yaml.
  - A file MAY still set `options:` to override any default. That is **reserved**
    for the option-demo files (`04b_…display-options-all`, `display_options_demo`,
    and the engine's `options_examples.yaml` reference — they exist to showcase the
    feature) and rare deliberate special renders. When one is used, booleans are
    the long `true` / `false` form (the parser also accepts t/f/y/n/etc.).
  - The `[Divergence from STAR]` block prints whenever methods differ, regardless
    of options — comparative demos keep their punch with no flags at all.
  - History: before 2026-08-09 every case file restated a 10-line "house minimal
    block" (501 files, ~5,000 lines); the sweep deleted them all, and the render
    diffs were machine-verified (no winner line changed). `show_irv` was already
    vestigial — the divergence block always prints — and survives only so old
    blocks still parse. The defaults + auto-gates are locked by
    `tests/test_default_render.py`.
- **`show_runoff_percent`** (engine default **`true`** since 2026-08-09): prints the
  two-line, **self-reconciling** runoff summary under the Automatic Runoff winner —
  e.g. `Voters with a preference: 363 of 461 (98 Equal Support). Dog 190 (52%) vs
  Cat 173 (48%); majority = 182` — using the **decided-voters** denominator (Equal
  Support excluded) but stating it against the total ballots with the Equal Support
  gap named inline, so the denominator never has to be inferred. The always-full
  `_tabulated` copy expands it into a "Runoff math" funnel (`461 − 98 = 363`,
  majority) — don't hand-set that. The wording/funnel/default are locked by
  `tests/test_runoff_percent.py`; change them together.
- **`show_smith_set`** (Ranked Robin only): still **opt-in on screen** (engine
  default `false`) and **always forced on in the `_tabulated` mirror** —
  deliberately NOT dragged along by RR's default-on matrix (a dedicated `smith`
  gate in the RR echo keeps them separate). Prints the **Smith set** (the smallest
  group whose every member beats every candidate outside it), says whether that's a
  lone Condorcet winner, a top **cycle**, an all-draws **dead heat**, or a **mixed**
  group held open by draws (some members beat others but no loop closes — "not all
  draws" does NOT imply "cycle"), and whether the winner landed inside it. The shape
  call is one shared classifier (`_group_shape`, on `_all_pairs_draw` + the
  beats-loop DFS) asked by both the RR winner line and the Smith block, so the two
  lines can't contradict each other about the same matrix — keep it shared.
  **RCV-IRV mirrors get the same block automatically** (no option — the IRV path
  has no options plumbing). The two uses are opposite: RR is Smith-efficient so the
  block is descriptive; RCV-IRV is not, so it's a genuine pass/fail. Wording locked
  by `tests/test_smith_set.py`; concept page `07_Concepts/topics/smith_set.md`.
- **The RCV-IRV transfer block** (added 2026-08-10, no option — mirror-always,
  screen under `--full`, same contract as the Smith block). `pyrankvote` prints
  each round as a column of totals, which omits the two numbers this repo's
  exhausted-ballot and center-squeeze pages are *about*: where a transferred vote
  came FROM, and how many ballots have stopped counting — so IRV's "majority" can
  finally be reconciled against all ballots cast instead of asserted. Built by
  `build_transfer_block()` in `rcv_irv_tabulation.py`. Three rules it encodes:
  **the eliminations are read back from `pyrankvote`, never recomputed** (else the
  block can contradict the table above it on a tie settled by the second-choices
  ladder); **the final round transfers nothing** whatever its Status column says —
  the runner-up is marked "Rejected" but the count has already stopped, so instead
  of inventing a round the block names the ballots that stayed active to the end
  and still had a lower ranking go unread (the *nonexhausted-untransferred* case);
  and **STV gets no block at all**, because surplus transfers are fractional and
  are not modelled — silence beats a plausible wrong number. Verified against
  **RCTab 2.0.0**, which reports the same transfers and the same shrinking
  thresholds. Wording locked by `tests/test_irv_transfers.py`. Changing the block
  means re-running every ranked case (179 files) and rebuilding pages.
- **The machine-readable result contract (`--json`) → load the `result-contract` skill.** The one rule worth carrying without it: every number in the JSON comes from the same function the printed report calls, so adding a family means extending the shared tally and **never** writing a second count inside [`result_json.py`](STARVote_LH_tabulation_engine/result_json.py).
- **Voter counts — keep examples SMALL.** Default to the *fewest ballots* that
  make the point; prefer **individual ballots** (one row per voter, a handful of
  them) over large weighted blocs. A 3-voter example that shows the effect beats a
  100-voter one. Only scale up when a larger electorate is genuinely essential
  (e.g., percentages or proportional seats). When you *do* weight, `Count` values
  must be **≥ 6** (avoid collision with 0–5 scores); scaling all weights ×N
  preserves STAR/proportional winners. See `07_Concepts/tips/TIPS_choosing_voter_counts.md`.
- **QUOTE a candidate or contest name that YAML would retype — machine-checked**
  (`check_yaml_name_types`, gated by `tests/test_md_links.py`, added 2026-08-10).
  PyYAML resolves bare scalars with YAML 1.1 rules, so an unquoted `No` arrives as
  `False`, `Yes` as `True`, `Off` as `False`, `null` as `None`, `1.10` as `1.1`, and
  `12:30` as **750** (base 60). The corpus is mostly protected *by accident*:
  candidate names live inside the `ballots: |-` block literal, which YAML hands over
  as one opaque string for the engine's own parser, so the scalar resolver never sees
  them — meaning a tidier-looking redesign that promoted candidates to a real YAML
  list would **reintroduce** the bug. What is genuinely exposed is `expected_winners:`
  and `election_title:`, which are resolved scalars; the check covers those. The
  trip-wire is not exotic — the natural way to add a ballot-measure case is a contest
  whose options are *Yes* and *No*, and then `expected_winners: [No]` parses as
  `[False]`, so a **correct** winner fails its own answer key and reads like an engine
  bug. History worth knowing: the project used **StrictYAML** for exactly this reason
  (*"securely handles the string-to-dictionary parse to avoid type coercion"* — README,
  May 2026; `from strictyaml import load` in `996016b`), and both the code and the
  rationale were lost in a later rewrite. The fuller replacement is Pydantic models,
  which would also emit the JSON Schema a conformance contract wants — see
  [`star_reference_package.md`](07_Concepts/tabulation_engines/star_reference_package.md).
- **A ballot's weight goes BEFORE the scores — machine-checked**
  (`check_ballot_weight_side`, gated by `tests/test_md_links.py`). One election is
  written one way everywhere: `Count × Ada,Ben,Cara` over `3 × 5,2,0`. That is the
  YAML schema (`Count:Ada,Ben,Cara` / `15:5,2,0`) and it is what the engine echoes
  back (`Count × Memphis,…` / `42 × 5,4,3,2`). A *source* file cannot drift — the
  parser only ever matches a **leading** weight — so `0,4,5   ×3` only ever shows up
  in **hand-authored Markdown**, the one surface with neither a parser nor a
  generator holding the line. Eight pages had accumulated it by 2026-08-07, and it
  hides well: each page is internally consistent, so the inconsistency is only
  visible to someone reading two of them. A reader who meets both forms has to work
  out, per page, which number is the ballot and which is the bloc size — on a
  three-candidate row (`0,4,5   ×3`) the trailing count looks exactly like a fourth
  candidate's score. The check also fires on **YAML comments and
  `scenario_description` prose**, which teach the wrong form just as loudly and ride
  into the `_tabulated` mirror and the generated page. Note the trailing form's best
  hiding place is an *annotation*, not a bare row —
  `5,4,0   ← the 3-voter majority (×3)` states the weight twice, in words and in a
  glyph, and neither one is where the schema puts it; write the count in the column
  and let the note say what the bloc *is*.
- **Candidate names — a fresh, easy cast per scenario; the same cast within one.**
  Prefer a *new* set of names for each scenario (memorable beats uniform — "the
  Ada/Ben/Cara split," "the Tennessee cities") over one fixed roster. Four rules:
  (1) **common and easy to say** — no obscure or confusable names (the "Cy" problem);
  (2) **distinct initials, in order** — A, B, C, D… so names line up with the ballot
  columns and reading order; (3) **phonetically distinct within a scenario** — avoid
  rhyming/blurring pairs (Dana/Hana, Ben/Glen) that don't carry when spoken aloud in a
  recording; (4) **use a theme when one fits** (Star Wars, cities, flavors) — that's
  the best kind of variety. **Variety _between_ scenarios, consistency _within_:** a
  matched pair or family (e.g. `05a`/`05b`) keeps the *same* cast — it's the same
  election with one thing changed, so new names would imply a different election. Use
  bare `A/B/C/D` only for purely abstract/academic illustrations where names are noise.
  **Canonical reusable elections** (Ann/Bob/Cal, the team lunch, the runoff reversal,
  Tennessee, the pets) are registered in `07_Concepts/tips/TIPS_canonical_elections.md`
  with their jobs and the two rules — *one election per page* and *canonical = frozen
  ballots* (same cast ⇒ same election; a new lesson gets a new cast, never a tweak).
  Reuse a canonical for generic examples instead of minting a new cast.
- **Markers (all tabulate as 0):** `-` blank · `~` race abstention · `&` candidate
  abstention · `?` spoiled · `%` spoiled+reissued. **No `^`** (removed). Approval
  ballots accept only `0`/`1` (+ blank/marker = not approved).
- **Levels (101/201/301)** live ONLY in the curriculum — now a hub
  (`07_Concepts/CURRICULUM.md`) plus one page per level
  (`07_Concepts/curriculum/CURRICULUM_101.md` / `_201.md` / `_301.md`); the hub links them and holds no
  level content itself, so there's a single source of truth per level (no sync
  drift). Don't tag every file. Example folders stay content-typed
  (`01_STAR/`…`05_Ranked_Robin/`, `method_comparisons/`, `06_Other/`).
- **One door per voting method (reorganized 2026-07-29).** A method's concept
  pages live **inside that method's folder**, in its `01_Learn/` bucket —
  `01_STAR/01_Learn/` (incl. `01_Learn/reporting/`), `03_STAR_PR/01_Learn/`,
  `04_Approval/01_Learn/`, `05_Ranked_Robin/01_Learn/`. The two 06_Other
  methods still use the older `concepts/` name:
  `06_Other/RCV_IRV/concepts/`, `06_Other/Range/concepts/`. The folder's
  `README.md` is that method's **start-here** (what it is → its concepts → its
  runnable examples).
- **The method-folder spine (reorganized 2026-08-02).** Inside `01_STAR/`…
  `05_Ranked_Robin/`, the second level is a fixed, ordered set of buckets —
  `01_Learn/`, `02_Examples/`, `03_Criteria/`, `04_Real_Elections/`,
  `05_Practice/`, `09_Parked/` — and each method takes only the ones it needs.
  Adding a case set? Put it in the bucket that fits rather than creating a new
  second-level sibling. **Capitalize the word after the number** (`02_Examples`,
  not `02_examples`): MkDocs derives sidebar labels from folder names and
  renders an all-lowercase name lowercase. **Difficulty stays out of the folder
  names** — a case is often 101 for its basic idea and 301 for the deep dive, so
  levels live in `07_Concepts/CURRICULUM.md` and per-set tables, never in a path. They previously lived in a parallel `07_Concepts/<Method>/`
  tree, which gave each method two competing front doors. **`07_Concepts/` is now
  cross-method only** (topics, paradoxes, scores_and_ranks, curriculum, glossary,
  engines, tips, books) — don't put method-specific pages back into it.
  **Moving concept pages again?** Use
  `tools_adam/scripts/migrate_concept_links.py` (resolves relative links per
  source file — a blind string replace corrupts them), run it **before** the
  `git mv`, and add a `redirect_maps` entry per moved page. Those redirects are
  **permanent**: published URLs are quoted in BetterVoting election descriptions
  that can never be edited, so a deleted redirect is an unfixable 404.
  **Three things that script will NOT do for you** — each one fails silently,
  and all three bit the 2026-08-02 reorganization:
  1. **Repoint existing redirect DESTINATIONS.** You must pass `--exclude
     mkdocs.yml` (its redirect *keys* are historical URLs and must never move),
     but that also leaves every *value* pointing into the folder you just moved.
     Those already-published URLs then 404 — the exact outcome the redirects
     exist to prevent. Freeze the keys, repoint the values by hand, and assert
     every destination exists on disk afterward — **machine-checked since
     2026-08-21** (`check_redirect_maps` in `check_repo_hygiene.py`, gated by
     `tests/test_md_links.py`), which also refuses a *duplicate* key: PyYAML
     keeps the last value, which is how two 2026-08-02 leftovers kept the docs
     deploy red for 14 commits after `04a8eea` deleted their targets.
  2. **Fix segment-wise paths in Python.** `REPO_ROOT / "01_STAR" / "_main"`
     contains no literal `01_STAR/_main`, so the literal pass cannot see it, and
     a glob over the now-missing directory yields **nothing without erroring** —
     parameterized cases just vanish. `tests/test_case_roots_exist.py` now fails
     the suite when a test module names a path that doesn't resolve; keep it.
  3. **Touch `.claude/`.** It is in the script's `SKIP_DIRS`, so paths inside
     the repo's own skill files survive every rename. Grep it by hand.
  And re-read the *prose* afterward: the literal pass cannot tell a live path
  from a sentence about the old path, and a link whose visible label is a
  backticked folder name keeps saying the old name after its target is
  repointed — the label is text, not a path.
- **Where text lives:** per-file context in the YAML (`scenario_description`
  printable, `video_script` = notes, never shown on screen); cross-file teaching in
  Markdown. No hand-authored `.md` per YAML (the generated pages are the exception —
  see next bullet). See `YAML_library/ORGANIZATION.md`.
- **Folder overview pages are named exactly `README.md`** (not `README_<folder>.md`).
  GitHub only auto-renders a file named `README.md` in a folder's tree view, so each
  folder's landing/overview page **must** be `README.md` — that's what makes the folder
  show a friendly page instead of a bare file list. Keep the descriptive title in the
  file's `# H1` (e.g. `# 01_STAR — single-winner STAR`). A folder may keep *secondary*
  docs under descriptive names (e.g. `README_larry_hastings.md`, `FORK_NOTES.md`), but
  the one overview is always `README.md`.
- **The repo publishes as a searchable website** — <https://masiarek.github.io/star-voting-library/>, built by root `mkdocs.yml` (MkDocs Material) straight from the repo's own Markdown and deployed by `.github/workflows/docs.yml` on every push to master. Two rules stay here because they bite outside any site task: **`site/` is generated output — never commit**, and a **`redirects.redirect_maps` entry is permanent** — published URLs are quoted in BetterVoting election descriptions that can never be edited, so a deleted redirect is an unfixable 404. For everything else — the plugin-vs-hook decision, `NAV_ORDER` and sidebar order, local preview, the two kinds of redirect and when to retire one → **load the `site-build` skill**. Details + known nits: [`website_build.md`](07_Concepts/about_this_repo/website_build.md).
- **Companion repo — research-paper topics live OUTSIDE this repo.**
  <https://github.com/masiarek/star-voting-research-topics> (**private**) holds the
  vetted research-paper prospectuses that use this library as their reproducibility
  artifact — one `topics/NN_<slug>.md` per topic, plus a `README.md` slate table.
  Each topic page follows a fixed structure: status/venues/supporting-library header,
  Abstract, Research question, Methodology, Literature gap and closest prior work,
  Cautions and framing corrections, Supporting assets in star-voting-library (links
  into *this* repo at `blob/master/…`), Execution sketch. Topics 1–5 were produced by
  a 12-agent workflow (2026-07-24) and each passed a five-agent **adversarial novelty
  check**; anything added later must state its vetting level honestly rather than
  inherit that badge (topic 6, the metric distortion of STAR, started with a
  *preliminary* check and passed the full five-agent protocol on 2026-07-26 —
  its status line records the run and the residual caveats). **Don't search this repo for research topics —
  they aren't here**; clone the companion, match the house structure, update the
  README slate table, and keep the two repos pointing at each other. Working the
  other direction: when a teaching page states an open gap in print (as
  `07_Concepts/topics/distortion.md` does for STAR's missing distortion bound), that's exactly
  the raw material for a new topic page.
- **When creating education pages or cross-referencing, prefer the `.md` page over
  the raw `.yaml` (and MD/links in general).**
  The generated per-election pages (`<set>_pages/<name>.md`, built by
  `STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`) are the reader-friendly surface: **lead with them**
  in tables, navs, and cross-references (left-most / primary link). Link a `.yaml`
  only when the *tabulatable source* is genuinely the point (e.g. a "run this file"
  command), and **demote** it (right-most column / secondary link). Page structure is
  **teaching first, raw tally last**: the `scenario_description` and educational value
  up top, then the **ballots**, then the **results** — with the full engine detail (the
  same content as the `_tabulated` mirror, or the mirror embedded) at the **bottom** of
  the page, so the reader gets the lesson before the numbers.
- **Link a folder by naming its `README.md` — machine-checked** (`check_folder_links`,
  gated by `tests/test_md_links.py`). Write `[label](some_folder/README.md)`, never
  `[label](some_folder/)`, `[label](some_folder)`, or `[label](some_folder/#anchor)`.
  The bare forms are seductive because they work on **two of the three surfaces**: GitHub's
  tree view renders the folder's README, and the built site serves its `index.html`. The
  one that fails is the one that matters — **MkDocs does not rewrite a bare folder link**;
  its build log says *"contains an unrecognized relative link … it was left as is"* and the
  raw href ships to the published page, which then 404s. A plain local Markdown viewer
  can't open it either. That is how **635 dead links** accumulated before the 2026-08 sweep
  (~1,000 rewritten across 400 files). Two notes: the check is the *complement* of the
  broken-link check — `check_links` already flagged folder links whose folder has **no**
  README, so between them every folder link is either named or reported; and
  **`build_yaml_pages.py` is a source of these too** (its `METHOD_DOCS` map and the
  `07_Concepts` fallback feed the generated `**Method:**` line on all 507 case pages), so
  fix the generator, not its output.
- **A repo path in backticks must be a LINK, not bare code text — machine-checked**
  (`check_code_span_paths`, gated by `tests/test_md_links.py`). Writing
  `` `07_Concepts/tips/TIPS_terminology.md` `` on a page under
  `06_Other/RCV_IRV/concepts/variants/` reads as *"go look at this file"* — but the path
  is **root-relative while every reader resolves it from the page's own folder**, so the
  desktop app and any local Markdown viewer open
  `…/variants/07_Concepts/tips/TIPS_terminology.md` and report the file missing. Put the
  backticks in the *label* and a real relative path in the *href*:

  ```markdown
  BAD   `07_Concepts/tips/TIPS_terminology.md`
  GOOD  [`TIPS_terminology.md`](../../../../07_Concepts/tips/TIPS_terminology.md)
  ```

  This one hides better than the folder-link bug, because on GitHub and the built site the
  code span is **inert** — it renders as grey text and 404s nowhere, so only a reader who
  tries to *follow* it ever finds out. `check_links` cannot see it either (it's not a
  link), which is exactly why it rotted: **not being links, these were invisible to
  `migrate_concept_links.py`** during the 2026-08-02 reorganization, so four still named
  pre-reorg paths (`07_Concepts/residual_vote_splitting.md`, `split_voting/*.yaml`) weeks
  after those files moved. The check fires only when the path resolves **from the repo
  root but not from the containing page** — provably a real repo file written the wrong
  way round. A path that resolves from neither is left alone: that's a reference to
  *another* codebase (BetterVoting's `packages/frontend/src/i18n/en.yaml`), which is what
  code text is legitimately for. Generated pages are exempt (`_hand_authored_pages()`
  skips them), so the `divergence_review` index may keep printing source paths as data.
- **Voice — learner by default; "how to teach it" is a folder, not a mode.**
  The asymmetry decides it: a learner page serves a presenter fine (they read
  *"you score every candidate 0–5"* and say *"you all score…"*), but a presenter
  page **fails** a learner — someone who lands on *"explain to your audience
  that…"* has been handed a script for a job they didn't take. Traffic runs one
  way too: every inbound link from the wild delivers a learner; presenters are a
  small group who deliberately walk into `hands_on/`. So:
  - **learner-you** — the default. The `01_Learn` spine, `getting_started/`,
    `voting_styles/`, every `start_here`.
  - **reference-neutral** (third person, the `**One line:** …` openers) — the
    201/301 property and theory pages: `properties_and_limits/`, `the_count/`,
    most of `07_Concepts/topics/`.
  - **presenter-you** — `hands_on/` and slide decks **only**.
  - **Never two voices in one page.** If a learner page needs a presenter aside,
    *link* to `hands_on/`; don't switch person mid-page. (This is the drift that
    let `teaching_star_voting.md` claim it owned `STAR_start_here.md`'s
    structure.)
  - **Titles name the subject, not the reader's task** — "The STAR ballot &
    voting styles", not "How to learn the ballot". The exception is `hands_on/`,
    where the task *is* the subject ("Count a STAR election by hand").
- **`**Level:**` — one shape, machine-checked** (`check_repo_hygiene.py`):
  `**Level: <rung> · <audience>**`, where **rung** is `101` / `201` / `301` /
  `401`, an arrow range (`201 → 301`), or `reference`; and **audience** is
  `for voters` · `for presenters` · `for debaters` · `deep dive`. No "Voting"
  prefix, no trailing period inside the bold, no parenthetical inside the token —
  put any elaboration *after* the closing `**`. The audience token is what makes
  the voice rule above enforceable, so pick it before you write the page, not
  after. Untagged pages are fine (the 101 spine mostly is); a *malformed* tag is
  not.
- **External sourcing — match the source to the claim, and disclose the lean.**
  Cite by tier: **electowiki** for *niche/branded method definitions & mechanics*
  (Ranked Robin, STAR variants, exotic methods — where Wikipedia is thin, it's the
  clearest); **Wikipedia** for the *neutral family term, notability, and any
  criteria/critical claim* (it has NPOV pressure, electowiki doesn't); **academic**
  (Stanford Encyclopedia, papers) for *rigor* (impossibility theorems, VSE math,
  proofs). electowiki and the campaign sites (equal.vote, starvoting.org,
  electionscience.org, fairvote.org, rangevoting.org) are **advocacy-adjacent** —
  fine for *definitions*, weak for *verdicts*; **whenever we lean on one, disclose
  its lean inline** (as the naming decoder, `how_to_learn`, and the "leans toward"
  table do). Never trade the repo's neutrality for better niche coverage.
- **Link key terms on first meaningful use — with restraint** (a gentle habit, not
  an enforced gate). The first time a page uses a *jargon* term that has a canonical
  home (a `topics/` hub, a concept page, or a `GLOSSARY` entry) — Condorcet
  winner/loser, center squeeze, monotonicity, later-no-harm, favorite betrayal,
  Equal Support, exhausted ballots, mutual majority, VSE, summability, Copeland /
  Ranked Robin, spoiler effect, the impossibility theorems — link it there so a
  newcomer can click through. But follow the overlinking discipline: (1) link to
  *aid*, not decorate — skip common words and what the audience plainly knows;
  (2) **never self-link** the page's own subject; (3) link a term **once** per page,
  not every occurrence; (4) prefer the **topic hub** if one exists, else the concept
  page, else the glossary; (5) **in a parallel list, link all or none** — when a
  bullet list, table column, or run-on sentence names several methods side by side
  (STAR · RCV-IRV · Ranked Robin · Plurality), linking only some of them reads as
  arbitrary even when each individual choice was defensible. Decide once for the
  whole list. (Rule 3 still wins: a term already linked earlier on the page stays
  unlinked, and the list is consistent *because* of that, not in spite of it — say
  so in the commit if it looks uneven. **One carve-out, added 2026-08-07:** rule 3
  forbids repeating a *destination*, not linking one term at two anchors that answer
  two different questions — the definition where a summary table needs it, the
  evidence where the prose leaning on it sits. Rare and deliberate: **18 of 602**
  hand-authored pages do it, 3%. Don't reach for the looser count as licence —
  *pages linking any target at 2+ anchors* is 92/602, but that tallies **different**
  terms and says nothing about this one. That conflation is what made the carve-out
  necessary: it was first argued from a "487 pages" figure that was neither pages
  nor hand-authored, but (file, target) **pairs** over the whole tree.) When in
  doubt, fewer links read better than
  a wall of blue. (Not machine-checked — the failure mode is over-linking, not
  under-linking; rule 5 is the exception, where the failure mode is *partial*
  linking, and only a human reading the rendered page will catch it.)
- **Case-folder layout — README-alone, sources in `cases/` (repo standard, 2026-07-20).**
  In a teaching case folder, the **source files (`.yaml`, `_bv_export.json`) live in a
  `cases/` subfolder**, and only the `README.md` (plus any hand-authored teaching `.md`)
  sits at the folder top — so opening the folder shows the *explanation*, not a wall of
  data. Because the engine derives output paths from the yaml's parent
  (`p.parent / (p.parent.name + "_tabulated")`, and the parent is now `cases`), the
  generated **`_tabulated`** mirrors and built **`_pages`** nest *inside* `cases/` as
  **`cases/cases_tabulated/`** and **`cases/cases_pages/`** (e.g.
  `method_comparisons/black_curtain/cases/cases_tabulated/`). Regenerate mirrors by
  re-running the YAMLs; pages via `build_yaml_pages.py`; both always show full context.
  **New case folders follow this** (README at top, sources in `cases/`). Folders
  **without** a `README.md` keep the flat layout (yamls at top — e.g. the `jfk7pd` /
  `three_way_dead_rung_tie` sub-cases, `split_voting/_main`); **engine/tool folders and
  test-fixture folders (`2_negative`, `harness_cases`) are never reorganized.** Test
  discovery and `discover()` glob both `*.yaml` and `cases/*.yaml`, so either layout works.
- **Markdown prose: do NOT hard-wrap paragraphs (Adam's preference).** Write each
  paragraph as a single unwrapped line (soft wrap) — no fixed ~76/80-char line limit. Hard-wrapping is cosmetic: Markdown collapses single newlines inside a paragraph into spaces, so wrapped and unwrapped prose render identically. Keep real line breaks only where they're semantic: blank lines between paragraphs, fenced code blocks, tables, and list items.
- **Embedding an engine report or an output snippet in a Markdown page → load the `embedding-reports` skill.** The two rules that bite without it: engine reports are **generated** into a page (`<!-- report:<stem> -->` … `<!-- /report -->`), never hand-pasted; and an **annotated or curated** fence is never convertible — label it `title="Abridged for the lesson — not verbatim engine output"` rather than replacing it.
- **Companion pages carry a generated `case-meta` block.** A case with both a generated page
  (`<set>/cases/cases_pages/<stem>.md`) and a hand-authored companion (`<set>/<stem>.md`) gets a
  method / seats / expected-winners line plus a full-count link under the companion's H1,
  written by `build_yaml_pages.py` between `<!-- case-meta:start -->` / `<!-- case-meta:end -->`.
  **Don't hand-edit inside the markers or restate those facts alongside them** — change the YAML
  and rerun the generator. `tests/test_yaml_pages_current.py` fails when a block drifts.
- **Ballot art, and showing a case's ballots on a page → load the `ballot-art` skill.** Art is drawn by `tools_adam/scripts/build_style_ballot_images.py`, never hand-embedded, and a hand-authored page shows its election with a `<!-- ballots:<stem> -->` block rather than a retyped Markdown table — the block already carries the numbers.
- **Cross-reference slides by title** via `07_Concepts/LINKS.md`
  short names — never page numbers or `#slide=id…` deep links.
- **Case-file naming.** **LH-only** cases (no BV election) → descriptive name, no bvid
  segment. **BV-backed** cases lead with the bvid — `b<bvid>_<descriptor>`, or
  `bv<testid>_<bvid>_<descriptor>` when a sheet Test ID already exists; details in the
  **`bettervoting` skill**. Applies to the whole case group — `.yaml`, `.md`, frozen
  `_bv_export.json`, `_tabulated` mirror. Older cases keep their names; re-align
  only if you're already touching them. **This applies to a MULTIRACE set too — one
  election backing several cases still prefixes every file** (settled 2026-08-05, after
  it was briefly gotten wrong). The tempting objection is that a shared prefix
  "discriminates nothing"; the answer is that the **suffix** carries the discrimination
  and the reading order (`bv2145_6fj2kg_irv` / `_ranked_robin` / `_star`;
  `bv2275_6mcgkq_a0_plurality` / `_ahalf_borda` / `_a1_negative`), while the prefix makes
  `rg <bvid>` return the whole set at once. 33 of the repo's 45 multi-yaml elections
  already do this. Name the shared frozen export for the set —
  `bv<testid>_<bvid>_bv_export.json` — and put `bv_test_id` / `bv_election_id` /
  `bv_results_url` in **every** yaml of the set (that is what `build_bv_registry.py`
  reads, so all of them index individually).
- **A frozen `_bv_export.json` records what BetterVoting PERMANENTLY stores — never migrate it**
  (learned the hard way 2026-08-22). BV descriptions cannot be edited, so the frozen export
  is the repo's only evidence of what a public, unchangeable artifact actually says. Its
  paths are therefore *historical*, exactly like `mkdocs.yml`'s redirect keys, and for the
  same reason. The 2026-08-02 reorganization rewrote paths inside **22** of them, because
  `migrate_concept_links.py` has `.json` in its `TEXT_EXT` — so the frozen copies read
  `01_STAR/05_Practice/` while the live BV descriptions still say `01_STAR/exercises/`. Two
  harms, and the second is the nastier: the file asserts something BV never said, *and* the
  edit conceals that BV's permanent text now names a folder that does not exist. The script
  now skips `*_bv_export.json` (`SKIP_FILE_SUFFIXES`), and the 22 were restored from the live
  API. **To audit:** fetch `/API/Election/<bvid>` for every `bv_election_id:` in the corpus
  and diff `description` against the frozen copy — they must be identical. Worth knowing what
  the same sweep found *undamaged*: all 38 clickable `masiarek.github.io` URLs inside BV
  descriptions still resolve, because `redirects.redirect_maps` covers them. It is the **bare
  path** references that rot, since nothing redirects those — 23 live elections (BV2188–2209,
  all minted before the reorganization) name four folders that no longer exist. Those are
  permanent and unfixable; the lesson for new mints is to put the *published URL* in a
  description, never a bare repo path.
- **Filed a bug upstream? Add a row to `07_Concepts/about_this_repo/upstream_bug_reports.md`.**
  Running one election through several engines is a good bug detector, so this repo files a
  fair number of reports against projects it doesn't own — BetterVoting, Larry's `starvote`,
  once GitHub Pages. They then get forgotten, because the page that motivated the report goes
  on to say something else. That page is the standing follow-up list (18 rows as of
  2026-08-09, 16 open), and it holds the API one-liner that re-checks every state at once.
  Two rules: it tracks only reports **we opened** — not every upstream issue the repo cites,
  which need no follow-up from us; and a **missing-guard** finding in BetterVoting goes to
  Arend privately *before* it goes on any page (the `bettervoting-qa` ground rule outranks
  the table). When one closes, the job isn't to flip the word — it's to ask what this repo
  teaches that the fix invalidates.
- **BetterVoting (BV) work → load the `bettervoting` skill.** Everything BV-specific lives
  there and loads on demand: minting with `create_bv_test_election.py` / `bv_election_specs.py`,
  fetching exports with `fetch_bv_export.py`, screenshots in `img/<bvid>_<what>.png`, the
  clickable `/results` lead line, the BV→repo description backlink, the `BV<n>` collision
  rule, `BV_registry.md` regeneration, and BV's method strings + bloc multi-winner.
  **Read it BEFORE creating or fetching any BV election** — BV titles, descriptions and
  numbers are PERMANENT and unfixable, so those rules have to be right the first time.
- **BetterVoting *documentation* work → load the `bv-docs` skill.** A different job from
  the one above, so a different skill: BV's help site (docs.bettervoting.com) is Jekyll +
  just-the-docs built by GitHub Pages from `docs/` in the BV checkout, and the skill holds
  the local Docker preview (plus its three traps), the front-matter `parent:` exact-match
  rule, the `.md` link convention, the eight doc URLs the *app* hardcodes (two of them deep
  anchors, so heading text is load-bearing), the verified election-state facts, and the
  fork/PR path. Load it before writing or moving any BV help page — and note the real
  bottleneck is that ~60 pages sit unpublished in Google Docs, so the job is usually
  publish/dedupe/shelve rather than write.

## Scratch drafting (any method)

Draft new scenarios in `trash_delete.yaml` and tabulate until the behavior shows (a tie
rung, a method divergence, a criterion failure…). Nothing there is permanent; iterate
freely, keep examples small. **Two gotchas:** there is **no separate `candidates:` key** —
the **first line of the `ballots:` block is the candidate header**, comma-separated; and
weighted rows use a `Count:` header (`Count:Ada,Ben,Cara` then `15:5,2,0` per bloc).
A third: the title key is **`election_title:`**, not `title:` — the engine accepts bare
`title` as an alias so a scratch file *runs* either way, but it is not in the documented
schema, so `check_top_level_keys` fails the moment that scratch case is promoted to a
real one (which is exactly how 8 files drifted before 2026-08-07).

```yaml
election_title: Scratch (delete me)
voting_method: STAR
num_winners: 1
ballots: |-
  Ada,Ben,Cara
  5,2,0
  0,4,5
  2,5,4
expected_winners: [Ben]
```

(No `options:` block — the engine's defaults are the house style; add `--full`
to the run for the everything-on render.)

Tabulate with `.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py trash_delete.yaml`.
The run writes `_tabulated` mirrors into a sibling `<parentdir>_tabulated/` folder — for a
scratch file at the repo root that's a junk `YAML_tabulated/` directory; **delete it (and
the scratch files) when done, never commit them.**

**Promoting a scratch case to a real one:** LH-only cases (no BetterVoting election — e.g.
a reproduction of a Larry `starvote` test file) go straight to case files + `_tabulated`
mirror + indexes + commit. For a **BV-backed** case, the full nine-step mint/freeze/
reproduce loop is in the **`bettervoting` skill**.

## Engines
- `STARVote_LH_tabulation_engine/starvote_larry_hastings.py` — STAR + Bloc/
  proportional; reporting options; `blocs:` vote-splitting check; quorum;
  `[Divergence from STAR]` comparison; optional `show_runoff_percent` runoff
  summary line (decided-voters denominator; forced on in `_tabulated`).
  Auto-dispatches to RCV-IRV / Approval / **Ranked Robin** by `voting_method`, or
  to RCV-IRV when ballots contain ranked `>` (comments with `->` are ignored).
  **Ranked Robin (RCV-RR / Copeland)** is first-class: `voting_method: RankedRobin`
  (aliases `RCV_RR` / `Copeland` / `Consensus`) prints the round-robin report
  (ballots + pairwise table + win-loss record), flags a Condorcet cycle, and
  writes its `_tabulated` mirror — it does **not** fall through to the IRV rounds.
  **Bloc RR (multi-winner):** `num_winners > 1` now elects the **top-N by the
  same ladder as single-winner RR** (Copeland → 1st Degree → 2nd Degree → lot),
  printing a seats list and flagging a lot-decided
  last seat — it no longer silently downgrades to one winner. **Multi-winner
  Plurality = SNTV / Bloc Plurality** (`run_plurality_multi`): `Plurality` +
  `num_winners > 1` elects the top-N by first-choice count (ties → lot);
  single-winner Plurality prints its own choose-one report (`run_plurality_single`
  — it no longer falls through to the STAR path). So LH multi-winner
  coverage is now complete for BV's bloc set: STAR→**Bloc STAR**,
  Approval→**Approval_Multi_Winner**, RankedRobin→**Bloc RR**, Plurality→**SNTV**,
  plus STV and STAR_PR/allocated/sss/rrv. (The old "LH has no Plurality" caveat is
  retired — single-winner via `run_plurality_single`, multi-winner via SNTV.
  The full tie-break ladders, per method and per engine, are written down in
  `07_Concepts/tabulation_engines/tiebreak_ladders.md`.)
  **RR triple-check — always cross-verify a Ranked Robin case three ways:** this
  native tally, BetterVoting's `RankedRobin.ts` (the frozen `_bv_export.json`
  Results), and **`pref_voting`'s independent Copeland** via
  `tools_adam/pref_voting_tabulation_engine/ranked_robin_report.py` (declared in
  `pyproject.toml`; `uv sync` then `uv run …`). The `pref_voting` leg is the
  **third-party cross-check** — a library nobody here wrote — and it is the one that
  makes an RR result trustworthy rather than self-confirming, so **run it on every
  RR case, not just the awkward ones**. On a tie it reports the whole Copeland
  **leader set** and declines to pick, then tells you whether LH's winner sits
  inside that set (`CONSISTENT ✓`) — which is exactly the check you want, since the
  disagreement between engines is never about the tally, only about the tiebreak.

  **Tiebreak ladder — the method publishes one, and follow it (corrected 2026-08-19).**
  Ranked Robin's own protocol (electowiki, *Degrees of ties*) resolves a Copeland tie
  by the **1st Degree** — each tied finalist's sum of win margins **over the other
  finalists** — and only then by the **2nd Degree**, margins **over all candidates**.
  It defines a 3rd and 4th Degree but explicitly does not recommend them for public
  elections, preferring a lot. LH now implements exactly that: Copeland → 1st Degree
  → 2nd Degree → **lot** (`lot_numbers`, published in the YAML). **Two things this
  ordering makes true, both of which were got wrong for two years:** with exactly two
  finalists the 1st Degree *is* their head-to-head, so **BV's head-to-head rung was
  right and LH's total-margin rung was not** — the "LH vs BV rung 2 divergence"
  documented across this repo was our bug, and correcting it changed the winner on
  **11 of 100** RR cases, every one a two-way tie whose head-to-head was decisive;
  and BV, which has no rung at all for 3+ tied candidates, sends every
  three-candidate cycle straight to its shuffle (filed as bettervoting#1469, fix
  written, parked behind the PR freeze). The remaining genuine divergence is only the
  last rung: LH's published lot vs BV's seeded shuffle. Full account, with the two
  discriminating cases:
  `05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md`. The engine's win-loss
  table prints a **"vs finalists"** column whenever there is a tie for the lead — that
  column is the 1st Degree, and it is what makes the winner checkable by hand.

  **BV's JSON export records the tie-breaking SEQUENCE just fine — don't repeat the
  old "can't be frozen" claim** (corrected 2026-07-29). BV's rung 3 is labelled
  `"random"` but is a **seeded shuffle**, documented as deliberately deterministic in
  `shuffleCandidatesForRandomTiebreak.ts`: `seed = (rawVoteCount + hash(raceId)) >>> 0`,
  shuffled once by TinyRand, each candidate's index written back as `tieBreakOrder`.
  The export publishes the **complete order** — `perm` (ids in tiebreak order),
  per-candidate `tieBreakOrder`, `tied[]` and `other[]` sorted by it, `tieBreakType`,
  and a `logs` line — so winner **and** runners-up survive, and a re-tally reproduces
  them. Pin `lot_numbers:` to BV's `perm` and LH replays the draw exactly. Verified
  live at 3 candidates (**BV2261** `y2fbpc`) and 9 (**BV2262** `2gvwr9`, all nine
  positions matched). Replay the shuffle yourself with
  `tools_adam/bv_replay_tiebreak.py <frozen export>` (stdlib-only Python port).
  **The real limit is narrower:** BV's order is *recorded* but not *derivable* — a
  function of the ballot **count** and the race id, **never of how anyone voted** —
  so a case whose **winner** turns on it is still **LH-only** (only LH's published
  lot lets a reader derive the result from the file). Publishing such a case on BV is
  fine when the *recording mechanism* is the subject and the page says to ignore who
  won. Worked: `05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md`,
  `05_Ranked_Robin/03_Criteria/rr_tiebreaks/bv2261_…md` / `bv2262_…md`.
- **Minimax and Coombs are tabulable** (added 2026-08-07) —
  `tools_adam/pref_voting_tabulation_engine/minimax_report.py` and
  `coombs_report.py`, each cross-checked against `pref_voting` on every run.
  Neither method exists in the LH engine or on BetterVoting, which is why
  Felsenthal's §A7 and §A10 examples were prose for so long; all 18 are now
  runnable case files in `method_comparisons/felsenthal_paradoxes/cases/`.
  Two things to know before quoting a Minimax result: **"worst loss" has three
  published readings** (winning votes = Felsenthal's, margins = `pref_voting`'s,
  pairwise opposition), which agree on an odd electorate with no drawn pairs and
  need not otherwise; and **a truncated ballot's unstated pair is a convention,
  not arithmetic** — this repo counts it for neither candidate, Felsenthal splits
  it ½–½ (`--equal-prob`), and Example 31's winner changes with the choice. Say
  which convention a number came from.
- **Successive elimination and the grade methods are tabulable too** (added
  2026-08-07) — `successive_elimination_report.py` (the parliamentary agenda
  procedure) and `grade_methods_report.py` (Range = mean, Majority Judgment =
  median + Balinski–Laraki), completing Felsenthal's five uncountable
  procedures. Two things that are easy to get wrong: **successive elimination
  takes the agenda as an argument**, not a default — under a cycle the
  agenda-setter picks the winner, so `--agenda` is required and a tied round is
  broken by an explicitly-chosen `--tiebreak` (the published examples disagree:
  alphabetical in Ex.11/12, "random" in Ex.10). And **grade cases are not LH
  election files**: Felsenthal's 1–10 and A–J scales fit neither the engine's
  0–5 validation nor BetterVoting, so they carry a `grades:` block instead of
  `ballots:` — which keeps them invisible to `check_top_level_keys` and
  `check_descriptions` (both gate on `ballots`) and means no `_tabulated`
  mirror and no generated page. Their counts live on the concept pages.
  Rescaling to 0–5 to make them engine-runnable would change the published
  numbers, which is why it wasn't done. **A grade file's scale may be words**
  (`grade_scale: "To Reject|Poor|Acceptable|Good|Very Good|Excellent"`), which is
  what Majority Judgment actually asks for — B&L's claim is not "six levels" but
  a shared *common language*, so the method's own front door
  (`06_Other/Majority_Judgment/`) uses it and its ballots are drawn. **Two
  published tie-breaks, not one:** this tool implements the *iterative* rule
  (strip a shared median, recompute, repeat); `pref_voting` implements the
  **majority gauge** (share above the median vs share below), and on a profile
  where both tied candidates have more detractors than supporters at the median
  the gauge as implemented compares only the losing shares and returns a **tie**
  where the iteration separates them — an observed DISAGREE, not a bug in either.
  Say which reading a number came from.
- `06_Other/RCV_IRV/RCV_IRV_tabulation_engine/rcv_irv_tabulation.py` — vendored pyrankvote; reads
  ranked (`A>C>B`) or score ballots.
- `06_Other/abcvoting_tabulation_engine/abc_tabulation.py` — multi-winner Approval (ABC)
  rules via Martin Lackner's `abcvoting` (in the `dev` dependency group since
  2026-08, so `uv sync` brings it in and the cross-check actually runs — locally
  and in CI). `av` doubles as an independent cross-check of the LH bloc-Approval
  count; `seqpav` / `pav` / `seqphragmen` add the proportional rules the LH
  engine doesn't have. Tested by `tests/test_abcvoting_crosscheck.py` (still
  guards on the import for bare-pip environments).
- **Score / range voting & the 0–5 cap (don't misstate this).** Larry's underlying
  `starvote` engine is *range-parametric*: `starvote.election(starvote.star, rows,
  maximum_score=N)` tabulates any range (verified at 0–10 → C). The **0–5 limit is the
  fork's teaching guardrail, NOT an engine limit** — `validate_star_rows(…,
  max_score=5)` in `starvote_larry_hastings.py` (def ~L2239, called with `max_score=5`
  ~L2366) rejects scores >5 on the YAML-CLI path because STAR ballots are 0–5 by
  convention; it's a single adjustable arg. **Pure Score / Range IS tabulable** — via
  `pref_voting.grade_methods` (`score_voting` = mean, `greatest_median` = the median
  variant, plus `star` / `approval` / `majority_judgement`), `starvote`'s RRV
  (`Reweighted_Range_Voting`, range-based PR), and the sim/divergence tools
  (`06_Other/simulations/star_vs_approval_divergence.py`, `tools_adam/find_divergence.py`)
  which compute the score-total winner. The STAR **Scoring Round** output is itself the
  score tally (the Score-Voting winner = whoever leads the scoring round before the
  runoff). What's absent is only a first-class `voting_method: Score` on the teaching
  CLI — **capability is not the blocker.**
- Quick checks can use system `python3` (engines are vendored); the user runs via
  their `.venv` / `uv`.
- The engine errors *clearly* (no tracebacks) for the common mistakes: bad YAML,
  no `ballots:` block / old nested schema (prints the key-components template),
  wrong column counts, invalid chars / out-of-range scores, ranked ballots under a
  score method, and method/seats mismatches. Missing `voting_method` / `num_winners`
  is a non-fatal NOTE (defaults to STAR / 1). Generated `_tabulated.txt` files are
  refused as input.

## Tests
The suite lives in `STARVote_LH_tabulation_engine/tests/`; read the modules for what each one covers. Four things about it are not visible from the code:
- **`test_harness_selfcheck.py` exists to prove the winner check is not vacuous** — deliberately-wrong answer keys in `tests/harness_cases/` must NOT match the engine's real result. Don't "fix" a failing harness case; it is supposed to disagree.
- **`test_json_to_yaml_conversion.py` was written for a specific class of breakage** — engine-signature drift, of which the `parse_ballots_from_string` arity bug was the instance. It converts a real export in an isolated tmp dir, so it catches the drift a unit test on the converter would miss.
- **Run from the engine dir**, not the repo root: `pytest tests/test_single_winner_positive.py tests/test_negative_validation.py`.
- **The pre-commit hook is wired by hand and does not survive a fresh clone:**
  `git config core.hooksPath STARVote_LH_tabulation_engine/tools_adam/scripts/git-hooks`

## Git
- **Commit after every significant addition or completed piece of work** (Adam's
  standing rule) — don't leave finished work sitting uncommitted. Write a real
  commit message: short imperative summary line, then a body listing what
  changed and why. Include regenerated `_tabulated`/`_pages`/index files in the
  same commit as their source changes.
- **This checkout is often open in two sessions at once, sharing one working tree,
  one index, and one HEAD — so a pathspec commit is not as scoped as it looks.** The
  mechanism is worth knowing, because it is not obvious: for `git commit -- <paths>`
  git builds a **temporary** index and points `GIT_INDEX_FILE` at it, so anything the
  pre-commit hook stages lands in *your* commit even though you scoped it. (`git
  commit`, `-a` and `--amend` all get the main index instead.) The hook auto-stages the
  four regenerated index/registry surfaces, and until 2026-08-06 it did so with a
  folder-wide `git add` that adopted everything dirty in those directories: a 3-file
  commit landed as 18, another as 11, once carrying a concurrent session's deletions.
  **The hook now hashes its output paths before and after each generator and stages
  only what that run actually changed**, so a colleague's untouched edits are left
  alone (`stage_regenerated`, covered by `tests/test_precommit_staging.py` — which
  tests *both* directions, since staging too little silently ships a stale index).
  What still legitimately rides along is a regenerated index reflecting work the other
  session has already **committed**; that is the hook doing its job. So keep the
  verification habit: `git show --stat HEAD` afterwards, and specifically `git show
  --diff-filter=D --name-only HEAD` for deletions. Additions and coherent
  regenerations are harmless — leave them and say so in your report. **Deletions are
  the case to stop on:** if one removes a file something still links to, don't push —
  work out whether the other session's generator pruned it deliberately (is it also
  gone from *disk*? does anything still reference it?) or whether it's a half-finished
  state you'd be freezing.
- **Adding an entry to a shared index file? Re-fetch and check `origin/master`
  immediately before the commit — not just at the start of the task.**
  `07_Concepts/GLOSSARY.md`, the `YAML_test_case_index` tables, `PARADOX_index.md`, a
  folder README's case table: these are where sessions converge, because writing the
  index entry is the natural *last* step of whoever built the thing being indexed.
  Worktree isolation makes this **worse**, not better — a colleague's entry sits on
  their branch with no trace in this working tree until they push, so the tree looks
  empty right up to the moment it isn't. 2026-08-09: asked for a `Vote unitarity`
  glossary entry, a main-tree session checked, correctly found none, and wrote one —
  while the worktree session that had just built
  `03_STAR_PR/03_Criteria/vote_unitarity/README.md` was writing its own as the last
  step of that same job. Both were right when they looked; the two entries collided on
  the merge an hour later and one was discarded. Note *what* was stale: the page was
  already upstream when the task began, and the **entry** appeared between the first
  check and the commit — which is exactly why the fetch has to be late. No git setting
  prevents this; it is a coordination gap, not a merge conflict.
- **Don't rewrite history to unpick a sweep**, even unpushed. A `reset`/`rebase` in a
  shared checkout drops the other session's commits into the working tree. Report the
  muddled attribution instead — the content is what matters, and it's recoverable.
- **Transient breakage is normal while the other session is mid-operation.** A held
  `.git/index.lock` (wait for it, never delete it), a `git ls-files` that reports
  committed files as untracked, and hygiene/test runs that suddenly report huge numbers
  of failures — 101 broken links and 4 failing tests in one run on 2026-08-05 — are
  almost always someone else's half-applied rename, not your bug. Wait for the tree to
  settle and re-run before "fixing" any of it. **Never `git stash`** here.
- **`check_repo_hygiene.py` warns about links whose target isn't committed yet**
  (`check_untracked_link_targets`) — the one failure the other checks structurally
  cannot see, because `check_links()` resolves against the working tree where the file
  exists, while CI builds the committed tree where it doesn't and `mkdocs build
  --strict` then fails the whole docs deploy. If it fires on another session's
  in-flight files, that's not noise: **wait for them to land before pushing**, or you
  redden the build for everyone.

## When unsure
Consistency matters more than cleverness here. If a terminology or convention
question isn't covered by the `07_Concepts/` docs, ask rather than guess.

---

## Agent operations (Claude-specific)

*Everything below is operational instruction from Adam to Claude — human
contributors can stop reading here.*

### File access (standing permission from Adam)

Adam grants Claude permission to **read, edit, and delete** files anywhere in
this repo's working copy — whether that's the T7 checkout
(`/Volumes/T7/Voting/Larry Hastings/YAML`) or a fresh clone of
`masiarek/star-voting-library`. No need to ask before modifying or removing
files here as part of a requested task. (Note: file *deletion* is also gated by
the app's permission layer, so a new session may still prompt once to enable
it — approve and proceed.)

### Working autonomy (standing instruction from Adam — 2026-07-24)

**Be self-driven. Don't wait for approval.** Adam's words: *"You have very good
sense of direction — I agree with 99%, and even if we go the wrong direction these
are educational materials, mostly. This is not critical code that must be carefully
reviewed. I am reading these pages and coming back to you if I find something
questionable. So please be more self-driven, no need to wait for my approvals."*

So: when you've analyzed a task and have a clear, sensible direction, **just do it** —
build the page, write the case, make the edit, commit, and push. Don't stop to ask
"want me to build this?" or offer a menu of options and wait. **Tell Adam what you
did** (a short summary + what changed), and flag anything genuinely uncertain so he
can spot-check while reading. Adam is the reviewer-after-the-fact, not a gate you
wait at.

Still confirm for the genuinely irreversible / outward-facing (per the safety rules):
creating **permanent public BetterVoting elections** (they can't be deleted — lock
the ballot set first), sending anything on Adam's behalf, or a destructive action you
can't undo. Everything internal to this repo — edits, new pages, deletions, commits,
pushes (standing auth) — proceeds without asking.
