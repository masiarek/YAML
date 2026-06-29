# Tie-Breaking in BetterVoting JSON — Format & Mapping to YAML

**One line:** a BetterVoting export **pre-draws the official tie-break order**
and ships it inside the results JSON; the converter reads it and writes it into
the YAML as `lot_numbers:`, so our re-tabulation reproduces BetterVoting's exact
winner — even when a tie comes down to the lot.

→ Companion to [`tie_breaking.md`](tie_breaking.md) (the tiebreak *ladder* and
the hand-written-YAML side). This page is the **JSON-side reference**: where the
order lives in the export, and exactly how it maps to YAML. Implemented in the
converter
([`YAML_library/1_positive/01_convert_json_yaml.py`](../../../YAML_library/1_positive/01_convert_json_yaml.py)),
guarded by
[`tests/test_lot_number_tiebreak.py`](../../../STARVote_LH_tabulation_engine/tests/test_lot_number_tiebreak.py)
· Level **301**.

---

## Why the order is in the file at all

A real STAR election resolves a perfect tie by a **lot** — a random order drawn
**once**, in public, and then used for any tie that arises. BetterVoting does
this up front and records the drawn order in the results, so the count is
**reproducible**: anyone re-tabulating the same ballots gets the same winner. Our
job in conversion is simply to **carry that order across** into the YAML, not to
re-draw it. (For *when* the order actually gets used — almost never — see the
ladder in [`tie_breaking.md`](tie_breaking.md).)

---

## Where the order lives in the JSON

The export's `Results[]` carries the tie-break order in up to three related
places. The converter reads them in this order of preference:

1. **`Results[].perm`** — a list of candidate **UUIDs** in **priority order,
   highest first**. This *is* the lot order; `perm[0]` wins any tie it's part of.
2. **`Results[].summaryData.candidates[].tieBreakOrder`** — a per-candidate
   integer, **ascending = higher priority**. This is the same information spread
   across the candidates (`perm` is just the candidates sorted by
   `tieBreakOrder`). Used **only as a fallback** when `perm` is missing (older
   exports).
3. **Neither present** — the export carries no official order. The converter does
   **not** invent one; it omits `lot_numbers` (see [the three input
   shapes](#the-three-input-shapes)).

`Results[].elected` is the winner BetterVoting computed. It is **not** used to
build the order — it's the answer key the converter and tests check our
tabulation against.

Here is the relevant slice of the Ice Cream export (UUIDs are BetterVoting's):

```jsonc
"Election": {
  "races": [{
    "candidates": [
      { "candidate_id": "c-rp3", "candidate_name": "Chocolate" },
      { "candidate_id": "c-ymx", "candidate_name": "Chocolate Chip" },
      { "candidate_id": "c-p4q", "candidate_name": "Fudge Brownie" },
      { "candidate_id": "c-34j", "candidate_name": "Vanilla" },
      { "candidate_id": "c-dym", "candidate_name": "Strawberry" },
      { "candidate_id": "c-gt7", "candidate_name": "Mango" }
    ]
  }]
},
"Results": [{
  "votingMethod": "STAR",
  "elected": [{ "id": "c-dym", "name": "Strawberry" }],
  "perm": ["c-dym", "c-p4q", "c-gt7", "c-ymx", "c-34j", "c-rp3"],
  "summaryData": {
    "candidates": [
      { "id": "c-dym", "tieBreakOrder": 0 },   // Strawberry
      { "id": "c-p4q", "tieBreakOrder": 1 },   // Fudge Brownie
      { "id": "c-gt7", "tieBreakOrder": 2 },   // Mango
      { "id": "c-ymx", "tieBreakOrder": 3 },   // Chocolate Chip
      { "id": "c-34j", "tieBreakOrder": 4 },   // Vanilla
      { "id": "c-rp3", "tieBreakOrder": 5 }    // Chocolate
    ]
  }
}]
```

Note `perm` is exactly the candidates sorted by `tieBreakOrder` ascending — the
two always agree; `perm` is just the convenient pre-sorted form.

---

## The mapping to YAML

The converter turns that order into the race's `lot_numbers:` list:

| JSON (source) | YAML (result) | Rule |
|---|---|---|
| `Results[].perm` (UUIDs) | `lot_numbers:` (cand_ids) | Translate each UUID to its `cand_id`, **preserving order**. |
| `summaryData[].tieBreakOrder` | `lot_numbers:` (cand_ids) | Fallback: sort candidates by `tieBreakOrder` ascending, then translate. |
| candidate UUID → name | `cand_id` | `cand_id` is the candidate's **real name** now, so the UUID `c-dym` becomes `Strawberry`. |
| `Results[].elected` | `expected_results.winners` | The answer key; checked, not used to build the order. |

Two invariants worth stating plainly:

- **Index 0 wins.** Earliest in `perm` / lowest `tieBreakOrder` = highest
  priority = wins ties. This carries straight through to `lot_numbers` (also
  index-0-wins).
- **Order is all that matters.** The UUIDs themselves are discarded; only the
  resulting sequence of `cand_id`s is kept.

### Worked mapping — Ice Cream

```
perm (UUIDs):   c-dym   c-p4q          c-gt7   c-ymx            c-34j     c-rp3
                  │        │              │       │               │         │
UUID → cand_id:   ▼        ▼              ▼       ▼               ▼         ▼
lot_numbers:  Strawberry, Fudge Brownie, Mango, Chocolate Chip, Vanilla, Chocolate
```

…which is exactly what lands in the generated file:

```yaml
lot_numbers: [Strawberry, Fudge Brownie, Mango, Chocolate Chip, Vanilla, Chocolate]
```

(In this particular election the lot is never actually consulted — five-star and
score settle both ties first. The order is carried anyway, so the file stays
faithful and reproducible if the ballots ever change. See the full trace in
[`tie_breaking.md`](tie_breaking.md).)

---

## The three input shapes

What the converter emits depends on what the export carries:

| Export carries | `lot_numbers` in the YAML | On a true lot tie, the re-tabulation… |
|---|---|---|
| `perm` | written from `perm` | …reproduces BetterVoting's `elected`. |
| no `perm`, but `tieBreakOrder` | written from `tieBreakOrder` | …reproduces BetterVoting's `elected`. |
| neither | **omitted** | …falls back to CSV column order — which **need not** match BetterVoting. |

The third row is the important caveat: without an official sequence we **cannot**
reproduce BetterVoting's lot tiebreak, so the converter is honest about it and
writes nothing rather than guessing. This only changes a result when an election
actually bottoms out at the lot (rare) — but when it does, the missing order is
exactly why the winners could differ.

---

## How this is guarded

[`tests/test_lot_number_tiebreak.py`](../../../STARVote_LH_tabulation_engine/tests/test_lot_number_tiebreak.py)
exercises all three shapes against a perfect symmetric tie (where the lot is the
*only* decider, so the checks aren't vacuous):

- `perm` → `lot_numbers`, reproduces `elected`;
- `tieBreakOrder` fallback when `perm` is absent;
- no sequence → `lot_numbers` omitted, column-order fallback;
- a **self-check**: scrambling the order makes the engine **disagree** with
  `elected`, proving the result genuinely hinges on the carried order.

---

## See also

- **BetterVoting's official tie-breaking protocol** — the source of the order
  carried in the export (their "Random Tie-breakers" section describes the
  candidate shuffle that becomes `perm`):
  <https://docs.bettervoting.com/help/ties.html>
- [`tie_breaking.md`](tie_breaking.md) — the tiebreak ladder (both rounds) and
  what you may set in a **hand-written** YAML.
- [`../../readme.md`](../../readme.md) — the converter in the overall pipeline.
- Glossary: **Tiebreaker** — [`../GLOSSARY.md`](../../GLOSSARY.md)
