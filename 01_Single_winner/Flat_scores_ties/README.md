# Flat scores, ties & tie-breaking — and the BetterVoting bugs

Where **flat / tied scores** meet **tie-breaking** meet **reporting**. STAR resolves
ties with a deterministic cascade; BetterVoting (BV) currently mishandles or
under-reports several of these cases. Each lesson is a **two-view** case — BV's display
beside the LH engine's text report — built to expose exactly one tie behavior.

Each scenario has its own friendly themed cast (fruits, flavors, capitals, …) in
**lot-priority order**, so the first-named (A-initial) candidate is the one the lot
favors and the cascade stays easy to follow. **Case 05 keeps bare `A–E`** — it matches the
exact ballots in #1379 and the already-built BV election `xmyf7k`.

> **When to use two views (house principle).** Show BetterVoting *beside* the LH report
> only where the two **diverge** (the discrepancy is the lesson) or where reading **BV's
> own UI** is the point. When they *agree*, LH-only is enough — don't paste screenshots
> that just duplicate the LH numbers. This tie/abstention set is two-view *because* BV
> mishandles these cases; the [vote-splitting set](../../split_voting/README.md) is
> LH-only *because* BV and LH agree there.

> **Workflow / status.** The LH side is complete and verified. The BV side is being
> reproduced: for each case you build the BV election, drop the export + screenshots, and
> the `_<bvid>` suffix is appended to the filenames. **Case 05 is already built** (BV id
> `xmyf7k`, the documented #1379). Cases where BV diverges show BV's *incorrect* result
> with a **"bug pending"** callout linking the tracking issue (same pattern as
> [`Runoff_07`](../runoff_overturns_leader/Runoff_07_flat_ballot_bv_bug_tf73v9.md)).

Concept backing: [The Automatic Runoff Round](../../00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff.md)
· [STAR Tie-Breaking](../../00_start_here/concepts/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
· [reporting true ties](../../00_start_here/concepts/STAR_reporting/reporting_ties.md)
· [`GLOSSARY`](../../00_start_here/GLOSSARY.md).

---

## The tie-break cascade (what LH does — the reference behavior)

STAR breaks ties **deterministically**, in a fixed order, and the LH engine *prints every
step*. Two cascades, depending on where the tie is:

**Scoring Round** (which candidates become the two **Finalists**):

1. **Head-to-head** — the candidate(s) preferred in the most pairwise matchups advance.
2. **Most 5s** — the candidate(s) with the most top scores advance.
3. **Lot number** — a fixed, pre-published priority order (here: A, B, C, …). When no
   official lot numbers are supplied, the engine falls back to ballot-column order and
   says so.

**Automatic Runoff** (which finalist **wins**):

1. **Highest score** — the higher total wins.
2. **Most 5s** — the more top scores wins.
3. **Lot number** — as above.

The point of the lot number is **reproducibility**: any auditor with the same ballots and
the same lot order gets the same winner. BV has **recently added** its tie-break priority
sequence to the JSON export ([#1371](https://github.com/Equal-Vote/bettervoting/issues/1371)),
(now **closed**) so an outside engine can import that order and reproduce BV's result — the
LH engine already accepts an imported lot order for exactly this. What's still open is a
**pre-published** lot number (a public draw before the election) rather than a post-hoc
random shuffle ([#1063](https://github.com/Equal-Vote/bettervoting/issues/1063)), and the
finalist/winner divergence + missing human-readable explanation in
[#1379](https://github.com/Equal-Vote/bettervoting/issues/1379).

## The cases

Each scenario has its own friendly cast (fruits, flavors, capitals, lakes, names,
mountains, pizza); the names are in lot-priority order (the first one — A-initial — wins
the lot), so the cascade and winner stay easy to read. **Case 05 keeps bare `A–E`** — it's
the exact ballots in #1379 and the already-built BV election `xmyf7k`, so renaming would
desync from that screenshot.

| # | Lesson | Cast | Where the tie is | Level | LH winner | BV status |
|---|--------|------|------------------|:---:|:---:|---|
| 01 | [clean top two (baseline)](./Flat_scores_ties_01_baseline_clean.md) | fruits | none — control | 101 | Apple | agrees ✅ |
| 02 | [runoff tie, two candidates](./Flat_scores_ties_02_runoff_tie_2cand.md) | ice cream | runoff (all Equal Support) | 101 | Almond | NaN on equal ties ⚠️ #1035 |
| 03 | [runoff tie, even 1-1 split](./Flat_scores_ties_03_runoff_tie_split.md) | capitals | runoff (real split) | 201 | Athens | check ⚠️ |
| 04 | [scoring tie for 2nd slot (2-way)](./Flat_scores_ties_04_scoring_tie_2way.md) | lakes | scoring round | 201 | Aral | check ⚠️ |
| 05 ⚠️ | [scoring 3-way tie **(BV555/#1379)**](./Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md) | A–E | scoring round | 201/301 | A | **picks C — wrong** ❌ #1379 |
| 06 | [scoring 4-way tie (ties every step)](./Flat_scores_ties_06_scoring_tie_4way.md) | names | both rounds | 301 | Ava | "no ballots cast" msg ⚠️ #1052 |
| 07 | [fully flat ballots (maximal tie)](./Flat_scores_ties_07_fully_flat.md) | mountains | both rounds | 301 | Ararat | abstention mis-file ⚠️ #1407 |
| 08 | [every ballot flat → BV counts 0](./Flat_scores_ties_08_all_flat_zero_count.md) | pizza | both rounds | 301 | Anchovy | **0 ballots** (all abstentions) ⚠️ #1407 |

**"But 5,5,5,0 works fine?"** Worth flagging: `5,5,5,0` does **not** sidestep the problem —
in STAR it's a genuine **3-way tie** (all three total 10), the same shape as case 05.
What actually "works fine" — BV and LH agreeing with no tie-break at all — is when the
scores leave an **unambiguous top two and a decisive runoff** (case **01**). So the honest
contrast isn't "flat vs not-flat," it's **"tie vs no-tie."** Flat-looking high scores are
fine *until* they produce an exact tie.

## BetterVoting bug tracker (the reports these cases document)

| Report | What it's about | Cases |
|--------|-----------------|-------|
| [#1379 — BV555, scoring-round 3-way tie](https://github.com/Equal-Vote/bettervoting/issues/1379) | BV picks different finalists than the reference engine **and** exports no tie-break explanation | 05 |
| [#1371 — JSON: add tie-break priority sequence](https://github.com/Equal-Vote/bettervoting/issues/1371) ✅ **closed** | the randomized tie-break order is now in the export, so another engine can import it and reproduce the result | all |
| [#1063 — deterministic lot-number tie-breaking](https://github.com/Equal-Vote/bettervoting/issues/1063) | implement the published-lot-number final rule (the fix LH already has) | all |
| [#242 — Approval/Plurality tie handling](https://github.com/Equal-Vote/bettervoting/issues/242) · [PR #229](https://github.com/Equal-Vote/bettervoting/pull/229) | tabulators break when random tie-breakers are disabled | method note |
| [PR #1385](https://github.com/Equal-Vote/bettervoting/pull/1385) | tie-break related fix | — |
| [#1052 — BV126, "no ballots cast" message](https://github.com/Equal-Vote/bettervoting/issues/1052) | wrong "no ballots have been cast" message when ties hit every step (ballots exist) | 06 |
| [#1035 — BV200, "NaN" on equal ties/prefs](https://github.com/Equal-Vote/bettervoting/issues/1035) | NaN displayed for equal ties & equal preferences | 02, 07 |
| [#1407 — flat ballot mis-filed as abstention](https://github.com/Equal-Vote/bettervoting/issues/1407) | a fully-flat (every-candidate-equal) ballot is dropped as an abstention | 07 |
| [#906 — BV1805, Average Supporter Profile](https://github.com/Equal-Vote/bettervoting/issues/906) | "Stats for Nerds" profile wrong under pending tie-breaking | reporting note |
| [#885 — Ranked Robin result counts](https://github.com/Equal-Vote/bettervoting/issues/885) | voter-count / win-count confusion (tangential, RR not STAR) | reporting note |

Design docs: [tie-breaking lot numbers / scenarios](https://docs.google.com/document/d/15NvrJoZ0f_Zhr3vh5uE2LVw-D8EZhBI2PFnTowYgoZM/edit?tab=t.0)
· [tie scenarios (2)](https://docs.google.com/document/d/1KqWriu7rTduQf1esebH5iMvcgueCdkLvBB02NS9MZ5Y/edit?tab=t.0).

## 💡 Proposal (idea — not yet adopted): color-coded coalition casts

> **Status: discussion only.** This is a proposed convention for tie-breaking /
> coalition examples, recorded here so it isn't lost. It is **not** a house rule yet —
> don't apply it to existing cases until it's decided. (Today's casts follow the standard
> rule: a fresh, friendly, distinct-initial set per scenario.)

**The idea.** For examples that turn on *coalitions* or *vote-splitting*, encode the
coalition structure into the candidate names/colors so the structure is visible at a
glance:

- **Hue = coalition / faction** — greens together, reds together.
- **Shade = candidate within the coalition** — *dark green* vs *light green* are two
  center candidates competing for the **same** voters.
- **Vote-splitting then looks like what it is:** one big coalition's support sliced into
  two thinner same-hue bars under Plurality (a spoiler), versus holding together under
  STAR's runoff. Same colors, opposite outcome.

**Why it could help tie-breaking examples specifically.** A tie is often *because* two
near-identical candidates draw equal support; same-hue/different-shade names make "these
two are basically the same coalition" obvious, which is exactly the intuition behind why
they tied and how the lot order separates them. Pairs nicely with the engine's existing
`blocs:` vote-splitting check (see CLAUDE.md → Engines).

**Open questions for the vote:** (1) does color/shade naming fight the "distinct initials,
phonetically distinct" rule? (2) accessibility — names must still work in plain text and
for color-blind readers (so the *word* "green-dark" carries it, not the color alone);
(3) scope — coalition/vote-splitting demos only, or any multi-candidate tie? Decide, then
promote to CLAUDE.md / AGENTS.md if adopted.

## Run them yourself

```
cd STARVote_LH_tabulation_engine
python starvote_larry_hastings.py "../01_Single_winner/Flat_scores_ties/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml"
```

Every file writes a full audit copy to its `Flat_scores_ties_tabulated/` sibling. All
seven also live as flat-schema positive test cases in `YAML_library/1_positive/`
(deterministic winner A via the published lot order).
