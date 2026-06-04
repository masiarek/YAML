# Better Voting Test Library (STAR Voting, Approval Voting, RCV Methods: Pydantic Schema Validation

A standardized, strongly-typed schema for defining election test cases that support Better Voting methods.

---

## Overview

This library provides a robust validation layer for election data. By bundling **Global Election Parameters** (voting method, seat count, candidate roster, and edge-case rules) directly with ballot data using **StrictYAML** and **Pydantic**, this schema ensures that data is explicitly understood, correctly validated, and safely handed off to downstream tabulation engines.

---
---

## Quick Start

### 1. Install

```bash
pip install better-voting-test-lib
```

### 2. Create a test case file

Create a file called `testcase.yaml` in a new directory (e.g., `tests/star_basic/testcase.yaml`):

```yaml
# tests/star_basic/testcase.yaml

election_parameters:
  election_id: e_001
  election_title: STAR Voting — Basic 3-Candidate Race
  description: >
    A simple single-winner STAR Voting election with 7 ballots.
    Cal wins the scoring round; Bob wins the runoff.

race_1:
  voting_method: STAR
  seats: 1
  candidates:
    - name: Ann
    - name: Bob
    - name: Cal
  ballots: |
    Ann,Bob,Cal
    5,4,3
    0,3,5
    0,3,5
    5,1,0
    1,5,3
    3,5,2
    2,4,5

expected_results:
  race_1:
    status: completed
    winners:
      - Bob
    detailed_metrics:
      total_ballots_cast: 7
      scoring_round_winner: Cal
      runoff_round_winner: Bob
      runoff_equal_preference_count: 0
    edge_cases:
      tie_occurred: false
      tie_resolution_method: none
```

### 3. Validate it

```bash
python -m bettervoting_testlib validate tests/star_basic/testcase.yaml
```

A passing validation produces:

```
✅  e_001 — STAR Voting — Basic 3-Candidate Race
    race_1: 7 ballots parsed, 0 errors.
    Schema valid. Baselines written to tests/star_basic/
```

### 4. What just happened?

| Step | What the library did |
|---|---|
| **Parsed** | StrictYAML read the file without any type-coercion guessing. |
| **Validated** | Pydantic confirmed candidate names match the ballot header, seat count is valid, and all ballot lines conform to STAR format. |
| **Asserted** | The `expected_results` block was stored as a reference baseline for downstream engine verification. |
| **Serialized** | A `testcase.json` and `testcase.toml` baseline were written alongside the YAML for use by external tabulation engines. |

> **Next steps:** Try adding a spoiled ballot (`?`) or a race-level abstention (`~,~,~`) to see how the schema captures edge cases — and run the validator again to confirm the metadata changes.

---
## Why StrictYAML & Pydantic?

### The "Missing Schema" Problem: Context-Blind Data

Passing around a CSV is like passing around an untyped data payload without a header — the system is forced to guess how to parse it. This is dangerous for something as precise as election tabulation.

Consider a system that receives the following CSV input:

```
A,B,C,D,E
1,1,0, ,0
```

Notice the empty space for Candidate D. What does that space mean? Did the voter skip it? Did the scanner fail to read it? Is it a typo that will crash the parser?

Without a strongly defined schema, the tabulation engine has no way to interpret this ballot correctly. Depending on missing context, the exact same data string could be valid or entirely corrupt:

| Voting Method | Interpretation |
|---|---|
| **Ranked Voting** | ❌ Invalid — expects preference syntax (e.g., `A>B>C`), not a score array. |
| **Plurality** | ❌ Invalid — two candidates selected is an overvote; ballot should be voided. |
| **Approval Voting** | ✅ Valid — voter approved A and B; blank space means "unapproved." |
| **STAR Voting (single-winner)** | ✅ Valid — candidates A and B scored 1 star, rest scored 0. |
| **Bloc STAR (3 seats, min. 3 selections)** | ❌ Invalid — only two candidates scored, violating the minimum selection rule. |

By bundling Global Election Parameters directly with ballot data, this library ensures a ballot like `1,1,0, ,0` is instantly validated, explicitly understood, or correctly rejected based on the actual rules of that specific race.

---

### The Ambiguity of Zeros and Blanks

Historically, election data files have used `0` or empty spaces to represent anything that isn't a valid vote. This creates dangerous ambiguity between developers, management, and election stakeholders. If a tabulation engine receives a `0` or a blank, what does it actually mean?

- Did the voter **intentionally leave the candidate blank** (mathematically equivalent to zero)?
- Was the **ballot spoiled or voided** entirely?
- Did the voter **explicitly abstain** — for a specific candidate, or across the entire race?

While a blank space, an explicit abstention, and a voided ballot may all produce "zero points" during calculation, they represent **fundamentally different scenarios** when determining election metadata. Without differentiating voter intent, it is impossible to:

- Accurately calculate **quorums**.
- Define exact **majority thresholds** (e.g., whether explicit abstentions are included in or excluded from the valid ballot count).
- Generate accurate **statistical reports** on voter behavior and spoiled ballots.

Resolving this ambiguity — and ensuring edge cases are explicitly preserved from the ballot box to the final report — was a primary driver for creating this schema library.

---

### Solving Type Coercion: StrictYAML + Pydantic

Because ballot data relies on multi-line text (especially for STAR Voting score arrays), standard YAML parsers are prone to **type-coercion errors** (e.g., the "Norway Problem," where `NO` is parsed as a boolean).

- **StrictYAML** acts as a secure, human-authored interface. It handles the string-to-dictionary parse without guessing types, and passes the resulting dictionary to Pydantic.
- **Pydantic** acts as an industrial-grade gatekeeper. It performs deep cross-field validation, ensures the structural integrity of data objects, and easily serializes validated cases into strict JSON/TOML baselines for secondary systems.

---

## Purpose & Scope

### ✅ What This Library DOES

| Capability | Description |
|---|---|
| **Strict Input Validation** | Parses and validates the logic, structure, and consistency of election data. |
| **Schema Enforcement** | Ensures Global Election Parameters (ID, title, format, quorum rules) and Race/Ballot structures adhere strictly to defined formats. |
| **Edge Case Preservation** | Captures complex ballot statuses using standardized special characters, giving tabulation engines the exact denominator needed for majorities, statistics, and quorums. |
| **Error Handling Verification** | Confirms that malformed inputs trigger the correct schema validation errors. |

### ❌ What This Library DOES NOT DO

| Limitation | Description |
|---|---|
| **Calculate Winners** | This is not an election calculation engine. |
| **Dictate Results** | Expected outcomes (winners, round-by-round results) included in test cases are **reference data only**, used to verify the accuracy of external engines. |

> **Downstream engines this library supports include:**
> [Better Voting](https://github.com/example/bettervoting), [starvote](https://github.com/larryhastings/starvote), and others.

---

## Test Case Architecture

### The "Test Case Bundle"

Each test case is a self-contained bundle. The `testcase.yaml` is the **single source of truth**.

**Execution order:**
1. **YAML First** — `testcase.yaml` is written and locked in.
2. **Parser Validation** — The Python runner validates the YAML structure. For `negative/` bundles, the runner asserts that the parser raises an exception matching the exact string in `expected_error.txt`.
3. **Baseline Generation** — Once parsing is clean, the runner serializes the validated data into JSON/TOML baselines stored alongside the YAML.

### Test Case Types

| Type | Purpose |
|---|---|
| **Positive** | Validates that correct configurations process cleanly and produce expected winners. Used for audits, certifications, and IT reviews. |
| **Negative** | Validates that purposefully flawed data raises the exact expected error messages (e.g., inconsistent settings, format violations, internal consistency failures). |

### Primary Voting Methods Covered

- STAR Voting (Single-Winner)
- STAR Multi-Winner (Bloc STAR, STAR-PR)
- Approval Voting
- RCV-RR (Ranked-Choice Voting — Reweighted Range)

---

## Schema Structure

Each `testcase.yaml` consists of three main sections:

| Section | Contents |
|---|---|
| **Input – Election Parameters** | Global settings: election ID, title, description. |
| **Input – Races & Ballots** | Voting method, candidate list, ballot data. |
| **Output – Expected Results** | Predicted winners, detailed metrics, edge case handling (ties, exhausted ballots, equal-preference tallies). |

---

## Ballot Data Formatting Standards

To ensure parser reliability and readability, ballot data is formatted within **text blocks**. For small test cases, list ballots individually to preserve clarity.

### Special Characters (Edge Cases)

These characters capture voter intent and election anomalies without corrupting tabulation math:

| Character | Name | Meaning |
|---|---|---|
| `~` | Tilde | **Race-Level Abstention** — voter abstained from the entire race (e.g., wrote "Abstain" at the top). |
| `&` | Ampersand | **Candidate-Level Abstention** — voter explicitly abstained for a specific candidate. |
| `^` | Caret | **Blank / Unmarked** — candidate was left completely blank (no score or rank selected). |
| `?` | Question Mark | **Spoiled / Voided Ballot** — overvote, protest mark, or invalid formatting. |
| `%` | Percent | **Spoiled & Re-issued** — ballot was voided and a replacement was issued by the election admin. |

---

### Ranked-Choice Format (`ranks`)

For ranked elections (RCV-IRV, RCV-RR), use `>` to indicate preference order.

```
A>B>C>D>E>F
A>B
C>B>A
?
```
---
### Scored / Rated Format (`scores`)

For scored or rated elections (STAR Voting, Approval Voting), use a comma-separated list of scores corresponding to the candidate roster.

> **Note:** In STAR Voting, equal scores are counted as "Equal Preference" in the runoff — they are **not** discarded.

```
5,4,3,2,1,0
5,^,^,^,^,^    # One candidate scored; the rest left blank
&,5,3,0,0,0    # Candidate A explicitly abstained
~,~,~,~,~,~    # Race-level abstention
```

---

### Grouped Ballots

For large batches of identical ballots, group them using a colon (`:`) after the count.

```
50: A>B>C
25: B>C>A
12: C>A>B
2:  ~,~,~
```

---

## Schema Examples: Progressive Guide

### 1. Minimal Individual Ballots

```yaml
election_parameters:
  election_id: e_001
  election_title: "STAR Voting - Baseline"

race_1:
  voting_method: STAR
  candidates:
    - name: Ann
    - name: Bob
    - name: Cal
  ballots: |
    Ann,Bob,Cal
    0,3,5
    0,3,5
```

### 2. Grouped (Weighted) Ballots

```yaml
race_1:
  voting_method: STAR
  candidates:
    - name: Ann
    - name: Bob
    - name: Cal
  ballots: |
    Ann,Bob,Cal
    42: 0,3,5
    15: 5,1,0
```

### 3. Approval Voting

```yaml
race_1:
  voting_method: Approval
  candidates:
    - name: Ann
    - name: Bob
    - name: Cal
  ballots: |
    Ann,Bob,Cal
    12: 1,1,0
    8:  0,1,1
```

### 4. Multiple Races in One Election

```yaml
race_1:
  voting_method: STAR
  candidates:
    - name: Ann
    - name: Bob
  ballots: |
    Ann,Bob
    10: 5,0

race_2:
  voting_method: RCV-RR
  candidates:
    - name: Dan
    - name: Eve
    - name: Fay
  ballots: |
    Dan,Eve,Fay
    8: 1>2>3
```

### 5. Expected Results Block

```yaml
expected_results:
  race_1:
    winners:
      - Bob
    detailed_metrics:
      total_ballots_cast: 57
      scoring_round_winner: Cal
      runoff_round_winner: Bob
      runoff_equal_preference_count: 15
    edge_cases:
      tie_occurred: false
      tie_resolution_method: none
```

---

## Additional Resources

- [Better Voting Test Library (GitHub)](https://github.com/example/repo)
- [Test Cases Master Spreadsheet](https://docs.google.com/spreadsheets/d/example) — includes screenshots and explanations for each test case
- [Why YAML format?](https://docs.google.com/document/d/example)
- [Edge Case Characters: Blank `^`, Race Abstain `~`, Candidate Abstain `&`, and Score Zero](https://docs.google.com/document/d/17X4kOgXrmgbLrEyXvAJLMnLQDbV-pMcwbMZPERcnIQs/edit?tab=t.0)
- [Confusing example: space in ballot data](https://docs.google.com/document/d/1fue2xOvx9Z1IYyHOUkVlV8yPZ13hwlKn03JfHcijVDg/edit?tab=t.0)
- [Default schema elements](https://docs.google.com/document/d/1KvYgmO6moW3QDzcZCzRTP5u1poW_poJF5Z9nae6WqmQ/edit?tab=t.0)