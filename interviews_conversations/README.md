# Interviews & Conversations — STAR Voting

A series of recorded **Larry (host) ↔ Adam (expert)** conversations that teach
STAR Voting through Q&A plus live demos run from this repo. This folder holds the
scripts; the demos come from `00_start_here/`, `01_Single_winner/`, and
`split_voting/`.

Start here:
[whats_so_good_about_STAR_Voting.md](./whats_so_good_about_STAR_Voting.md) — the
flagship episode that introduces the whole arc.

---

## Where to start & how to organize

**Record one flagship episode first** (the "What's so good…" script), because it
forces you to nail the core arc end-to-end. Then break that arc into **short,
single-topic clips** you can release on their own and reuse. The flagship doubles
as the table of contents.

**Format that works for recording:** Larry asks the naive-but-smart question;
Adam answers in 2–4 sentences; then a **live demo** or a **slide**. Keep Adam's
turns short — it's spoken, not a lecture. Every segment should end on either a
demo or a memorable one-liner.

### Proposed episode roadmap

| # | Episode (clip) | Core question | Repo demo | Source slides |
|---|----------------|---------------|-----------|---------------|
| 0 | Why do you love STAR? (cold open) | the personal "why" | — | Full Deck title + dilemma |
| 1 | What's so good about STAR? | the whole pitch in one arc | flagship file's demos | Full Deck (all) |
| 1.5 | Is our voting system broken? (Problem with Plurality) | is it broken — frequent? serious? worsening? | `split_voting/01*`, `04*` | "Problem: Vote-Splitting", "The Voting Dilemma" |
| 2 | The spoiler effect | why Choose-One breaks with 3+ | `split_voting/01*`, `03*` | "Vote-Splitting", "Domino Effect" |
| 3 | Ranks vs Scores | why scores carry more info | (whiteboard) + `00a` | "Rating vs Ranking" |
| 4 | The STAR ballot | how do I vote? | — | "Instructions" / 5-star ballot |
| 5 | The two rounds | why Score *then* Runoff? | `00a_c2_b1`, `vote_splitting2` | "How STAR Works", Dual-Nature doc |
| 6 | Benefits of STAR | Simple/Honest/Expressive/Accurate/Equal | accuracy demos | "What do we want", accuracy chart |
| 7 | STAR vs RCV-IRV | pros & cons, honestly | 4-cand `show_irv` divergence | Scorecard, Burlington, Alaska |
| 7.5 | RCV or IRV? (nomenclature, **201**) | which word, and why | — | "About Ranked Choice" |
| 8 | Counting & trust | summability, audits | any file's matrix | "Summability" slides |
| 9 | Multi-winner & proportional | electing several seats | `02_Multi_winner/*` | "Proportional Representation" |
| 10 | The honest limits | "resistant, not proof" | — | "Voting Theory Facts" |
| 11 | "Discounted votes?" (objection) | are equal-score votes ignored? | `01_Single_winner/equal_support_runoff_demo.yaml` | "No-Preference Votes in the Runoff" |
| 12 | Favorite betrayal (Voting 301) | does *only* RCV avoid it? | — | "RCV Common False Claims", "Alaska '22", pass/fail criteria |
| 13 | "Exhausted ballots," untangled (301) | what FairVote's word actually hides | `equal_support_runoff_demo` (contrast) | "Ranked Choice Deal Breakers", "Alaska '22", Exhausted Ballots deck |

Episodes 1, 2, 5, and 7 are the highest-value if you only make four. Episode 11
([are_equal_score_votes_discounted.md](./are_equal_score_votes_discounted.md)) is
debate-prep — deploy it only when a skeptic raises the FairVote "discounted
votes" line; don't lead with it.

### Suggested additional topics (good standalone clips)
- "Equal Preference / no-preference in the runoff" — what an equal score does.
- "Bullet voting — is it a strategy?" (it isn't; show why).
- "The preference matrix, read out loud" — using the engine's `show_matrix`.
- "Abstentions, blanks, and 0s" — what the ballot markers mean (use the engine's
  legend + the `Abs` score-distribution bucket).

---

## Cross-referencing the presentations

You have four decks/docs in play. Treat them as **source slides**, not as the
script — pull individual slides into the relevant segment.

| Short name | What it's best for | Link |
|------------|--------------------|------|
| **Full Deck 2025** | the canonical slide library; nearly every segment | docs.google.com/presentation/d/1wyR_1aSlATkOzcbGhWCD0_mRtRK60PDS3INIazhQl1w |
| **Automatic Runoff** | deep-dive visuals for Segment 5 (the runoff) | docs.google.com/presentation/d/1DNJg5kbsNbNQFV3bosm4KZmgJtNfIbQdpirhm5XlCqY |
| **Torrance LWV (Arend)** | the cleanest single-talk flow + the scorecard table | docs.google.com/presentation/d/1xPVPWnqJJPrkdm68uuZ9dYKqCsPqV1zgOcRnRBhZaAM |
| **Dual Nature (doc)** | the "strength vs numbers" framing for Segment 5 | docs.google.com/document/d/1n3pkr_S9MBucJMg7ANhk5ZZ00OLTW3Kj5Bp-vruW10k |

**Turning Arend's Torrance deck into Q&A:** it already moves in a teachable order
(problem → spoiler → alternatives → RCV facts → STAR → scorecard). The best
approach is to **keep his slide order as the spine and convert each slide title
into Larry's question**:
- "PROBLEM: VOTE-SPLITTING" → *Larry: "What actually goes wrong with more than
  two candidates?"*
- "ABOUT RANKED CHOICE" → *"People love RCV — what does it get right, and where
  does it fall down?"*
- "Single-Winner Voting Method Scorecard" → *"Can you put STAR, RCV, and
  Choose-One side by side?"* (then show the table as the answer).
Each slide becomes one Q→A→[show slide] beat. His scorecard slide is the single
strongest asset you have for Segment 7 — lead the comparison with it.

**For the "Dual Nature" doc you need to turn into a presentation:** it's already
structured as an argument (cardinal phase / ordinal phase / why it matters /
strategy). Convert each bold heading into one slide and one Larry question:
- "Scoring Phase (Cardinal)" → slide: *strength of support*.
- "Runoff Phase (Ordinal)" → slide: *number of supporters*.
- "Why This Matters" → slide: *cardinal is expressive but gameable; ordinal
  resists gaming but splits votes; STAR uses each to cover the other's weakness*.
- Close on the Tim Peters quote — it's a great mic-drop slide.
This is Segment 5's deck; build it once and reuse it.

### Suggested changes / new presentations
- **New: a 5-slide "Scores vs Ranks" micro-deck** (Segment 3). None of the
  existing decks isolate this cleanly, and it's the conceptual hinge.
- **New: a "Live Demo" deck** that is mostly blank frames cueing you to switch to
  the STAR engine — so the recording cuts cleanly between slide and terminal.
- **Change to the Full Deck:** it has several near-duplicate "vote-splitting"
  slides with identical speaker notes. For the recordings, make a trimmed
  *recording cut* that keeps one of each, so you're not paging past repeats.
- **Add a Burlington + Alaska "real failures" two-slide pair** to the front of
  Segment 7 — concrete beats abstract.

---

## Keeping presentations & Google Doc links in sync

Google Slides/Docs don't auto-sync with this repo, so don't try to mirror their
*content* here. Instead keep a **single source-of-truth link registry** and a
**mapping**, and let each live in its own home:

1. **One `LINKS.md`** (I can create it) listing every deck/doc: short name, URL,
   one-line purpose, and "last reviewed" date. Every script links by *short name*,
   never by raw URL — so when a URL changes you fix it in one place.
2. **Map, don't copy.** Scripts reference slides as `[SLIDE] Full Deck — "title"`.
   That survives slide reordering far better than slide-number links.
3. **Stable anchors.** In Slides, give key slides a short, searchable title (you
   already do). Searching the title is more durable than a `#slide=id…` deep link,
   which breaks on copy/duplicate.
4. **One-way canonical direction.** Pick the canonical artifact per topic (e.g.
   Arend's deck is canonical for the scorecard) and have others *point to it*
   rather than duplicating it.
5. **Review cadence.** When you edit a deck, bump its "last reviewed" date in
   `LINKS.md` and grep the scripts for its short name to catch stale references.

The repo's own files (engine output, example YAMLs) *are* canonical and version-
controlled — so prefer them for anything you want to stay exactly in sync (the
live demos), and treat the Google decks as the visual layer on top.

---

## Demo software: BetterVoting vs the STAR engine

(From your "pros and cons" note — summarized with a recommendation.)

**Use both, in this order:**

1. **Drive the teaching with the STAR engine in this repo** (the `starvote_…`
   fork). It's *dynamic*: you can change a ballot on the fly to make a scenario
   land, the reporting options show exactly what you want (Condorcet, RCV-IRV,
   Approval, the vote-splitting check), and every example is a saved, repeatable
   file. That's perfect for "watch what happens when I move this one score."
2. **Send the audience to BetterVoting.com to *participate*.** Beautiful graphics,
   a real shareable ballot link, and audience engagement (have them vote on their
   phones). That's the call-to-action moment.

**Why not BetterVoting for the teaching demos:** casting each ballot one-by-one is
slow and error-prone on camera, you can't tweak scores live, the sandbox's
reporting is incomplete, and (per your notes) it mishandles ties — which is
exactly the kind of edge case a teaching demo wants to be correct about.

**Make the engine demos better for recording:**
- Pre-stage the exact files (see the flagship's demo index) so you never type
  ballots live.
- Turn on only the output you'll narrate (`options: { show_matrix: t,
  show_condorcet: t, show_irv: t }`) and hide the rest, so the screen isn't busy.
- Keep a blank "Live Demo" slide to cut to, so the video editor has a clean seam.
- For the spoiler beat, the `[Vote-splitting check]` block gives you the punchline
  in numbers — read it out loud.

**Honest caveat from your own note:** after the engine demo you'll still point
people to BetterVoting to actually try it — so frame the engine as *your*
teaching instrument and BetterVoting as *their* hands-on tool. They're
complementary, not competing.

---

## Files in this folder
- `whats_so_good_about_STAR_Voting.md` — the flagship Larry↔Adam script.
- `README.md` — this plan (roadmap, slide map, sync strategy, demo software).
