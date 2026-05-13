# Better Voting Test Library: Pydantic Schema Validation

This project provides a standardized, strongly-typed schema for defining election test cases to support Better Voting methods.

## Why StrictYAML & Pydantic?

Pure CSV files containing ballot data inherently lack crucial context. Ambiguities inevitably arise regarding the specific voting method used, the number of available seats, the candidate roster, and the expected format of the ballots. 

### The Ambiguity of Zeros and Blanks
Historically, election data files have relied on zeros (`0`) or empty spaces to represent anything that isn't a standard, valid vote. However, this creates dangerous ambiguity between developers, management, and election stakeholders. If a tabulation engine receives a `0` or a blank space, what does it actually mean?

* Did the voter intentionally leave the candidate blank (which mathematically behaves as zero)?
* Was the ballot spoiled or voided entirely?
* Did the voter explicitly write "Abstain" next to a candidate, or across the entire race?

While a blank space, an explicit abstention, and a voided ballot might all result in "zero points" or "zero stars" for a specific candidate during the calculation phase, they represent fundamentally different scenarios when determining the election's metadata. 

Without explicitly differentiating these voter intents, it is impossible to:
1. Accurately calculate quorums.
2. Define exact majority thresholds (e.g., determining whether explicit abstentions should be included in, or excluded from, the total valid ballot count).
3. Generate accurate statistical reports regarding voter behavior and spoiled ballots.

Resolving this ambiguity—and ensuring that edge cases are explicitly preserved from the ballot box to the final report—was a primary driver for creating this schema library. 

### The "Missing Schema" Problem: Context-Blind Data
Passing around a CSV is like passing around an untyped data payload without a header—the system is forced to guess how to parse it. This is incredibly dangerous for something as precise as election tabulation.

Consider a system that receives the following simple CSV input:
```
A,B,C,D,E
1,1,0, ,0
```
Notice the empty space for Candidate D. What is the meaning of that space? Did the voter skip it? Did the scanner fail to read it? Is it a typo that will crash the parser?

Without a strongly defined schema, the tabulation engine has no idea how to interpret this ballot. Depending on the missing context, this exact same string of data could be perfectly valid or entirely corrupt:

* **Ranked Voting Method:** **Invalid input.** The system should be expecting preference syntax (e.g., `A>B>C`), not an array of scores.
* **Plurality Election:** **Invalid data.** The voter has selected two candidates (an overvote), meaning the ballot should be voided or flagged.
* **Approval Voting:** **Valid.** The voter simply approved of candidates A and B. The parser might just assume the blank space means "unapproved."
* **STAR Voting (Single Winner):** **Valid.** The voter gave candidates A and B a score of 1 star, and the rest 0 stars (assuming the engine is hard-coded to treat spaces as zeros).
* **Bloc STAR Voting (3 seats, min. 3 selections required):** **Invalid.** The voter only provided scores for two candidates, violating the minimum selection rule.

When election data is decoupled from election rules, tabulation engines are forced to make assumptions about both the math and the data types. By bundling the Global Election Parameters (the voting method, the number of seats, and specific constraints) directly with the ballot data using StrictYAML, this library ensures that a `1,1,0, ,0` ballot is instantly validated, explicitly understood, or correctly rejected based on the actual rules of that specific race.

## Purpose & Scope

**What this library DOES:**

* **Strict Input Validation:** Parses and validates the logic, structure, and consistency of election data using StrictYAML and Pydantic.
* **Schema Enforcement:** Ensures that Global Election Parameters (ID, title, format definition, quorum rules) and specific Race/Ballot structures strictly adhere to defined formats.
* **Edge Case Preservation:** Captures complex ballot statuses using standardized special characters to ensure tabulation engines have the exact denominator needed to calculate majorities, statistics, and quorums correctly.
* **Error Handling Verification:** Confirms that malformed inputs trigger the appropriate schema validation errors.

**What this library DOES NOT DO:**

* **Calculate Winners:** This library is not an election calculation engine.
* **Dictate Results:** Expected outcomes (like round-by-round results or final winners) included in the test cases are strictly for reference data to verify engine accuracy.

## Ballot Data Formatting Standards

To ensure parser reliability and maintain readability, the schema expects ballot data to be explicitly formatted within text blocks. For test cases with a small number of ballots, list ballots individually to preserve clarity. 

### Edge Cases & Special Characters
To capture voter intent, out-of-band communication, and election anomalies without corrupting the tabulation math, the schema utilizes specific characters. These ensure that tabulation engines process missing data and spoiled ballots correctly.

* `~` **(Tilde): Race-Level Abstention.** The voter abstained from the entire race (e.g., wrote "Abstain" at the top).
* `&` **(Ampersand): Candidate-Level Abstention.** The voter explicitly abstained for a specific candidate.
* `^` **(Caret): Blank / Unmarked.** The candidate was left completely blank (no score/rank selected).
* `?` **(Question Mark): Spoiled / Voided Ballot.** A wasted or protest vote (e.g., overvotes, writing "Void" across the ballot, or marking multiple scores incorrectly).
* `%` **(Percent): Spoiled & Re-issued.** The voter made a mistake, the ballot was voided, and a new ballot was issued by the election admin.

### Ranked-Choice Scenarios (Ranks Format)
For ranked elections, such as RCV-IRV or RCV-RR, use the `>` separator to indicate preference order.

A>B>C>D>E>F
A>B
C>B>A
?

### Scored Scenarios (Scores Format)
For scored or rated elections, such as STAR Voting or Approval voting, use a comma-separated list of scores corresponding to the candidate roster. Note that for STAR Voting, equal scores are counted as an "Equal Preference" in the runoff, not discarded.
```5,4,3,2,1,0
5,^,^,^,^,^
&,5,3,0,0,0
~,~,~,~,~,~
```
### Grouped Ballots
For large batches of identical ballots, group them by placing a colon (`:`) immediately after the ballot count, followed by a space and the ballot data.
```
50: A>B>C
25: B>C>A
12: ~,~,~
```
# Better Voting Test Library using Pydantic Schema Validation

This project provides a standardized schema for defining election test cases to support Better Voting methods.

### CSV Files Carry No Embedded Schema

Passing around a CSV is like passing around an untyped data payload without a header—the system has to guess how to parse it, which is incredibly dangerous for something as precise as election tabulation.

Consider a system that receives the following simple CSV input:

```csv
A,B,C,D,E
1,1,0, ,0
```

Notice the empty space for Candidate D. What is the meaning of that space? Did the voter skip it? Did the scanner fail to read it? Is it a typo that will crash the parser?

Without a strongly defined schema, the tabulation engine has no idea how to interpret this ballot. Depending on the missing context, this exact same string of data could be perfectly valid or entirely corrupt:

*   **Is it a Ranked Voting method?** Invalid input. The system should be expecting preference syntax (e.g., `A>B>C`), not an array of scores.
*   **Is it a Plurality election?** Invalid data. The voter has selected two candidates (an overvote), and the ballot should be voided or flagged.
*   **Is it Approval Voting?** Valid. The voter simply approved of candidates A and B, and the parser might just assume the blank space means "unapproved."
*   **Is it a single-winner STAR Voting election?** Valid. The voter gave candidates A and B a score of 1 star, and the rest 0 stars (assuming the engine is hard-coded to treat spaces as zeros).
*   **Is it a Bloc STAR Voting election (3 seats, min. 3 selections required)?** Invalid. The voter only provided scores for two candidates, violating the minimum selection rule.

When election data is decoupled from election rules, tabulation engines are forced to make assumptions about both the math and the data types. By bundling the Global Election Parameters (the voting method, the number of seats, and specific constraints) directly with the ballot data using StrictYAML, this library ensures that a `1,1,0, ,0` ballot is instantly validated, explicitly understood, or correctly rejected based on the actual rules of that specific race.

## Why StrictYAML & Pydantic?

A pure CSV file with ballot data often lacks crucial context. Ambiguities inevitably arise regarding the specific voting method used, the number of seats available, the candidate roster, and the expected format of the ballots. 

### The Ambiguity of Zeros and Blanks
Historically, election data files have relied on zeros (`0`) or empty spaces to represent anything that isn't a direct, valid vote. However, this creates dangerous ambiguity when communicating between developers, management, and stakeholders. If a tabulation engine receives a `0` or a blank space, what does it actually mean?

* Did the voter intentionally leave the candidate blank (which mathematically behaves as zero)?
* Was the ballot spoiled or voided entirely?
* Did the voter explicitly write "Abstain" next to a candidate, or across the entire race?

While a blank space, an explicit abstention, and a voided ballot might all result in "zero points" or "zero stars" for a specific candidate during the calculation phase, they represent completely different scenarios when determining the election's metadata. 

Without explicitly differentiating these voter intents, it is impossible to:
1. Accurately calculate quorums.
2. Define exact majority thresholds (e.g., determining whether explicit abstentions should be included in or excluded from the total valid ballot count).
3. Generate accurate statistical reports regarding voter behavior and spoiled ballots.

Resolving this ambiguity—and ensuring that edge cases are explicitly preserved from the ballot box to the final report—was a primary driver for creating this schema library. By bundling election parameters, explicit edge-case rulesets, and ballot information into a predefined StrictYAML format, this schema enables robust data validations and consistency checks that simple flat files cannot support.

## Purpose & Scope

**What this library DOES:**

* **Strict Input Validation:** Parses and validates the logic, structure, and consistency of election data using StrictYAML and Pydantic.
* **Schema Enforcement:** Ensures that Global Election Parameters (ID, title, format definition, quorum rules) and specific Race/Ballot structures strictly adhere to the defined format.
* **Edge Case Preservation:** Captures complex ballot statuses using standardized special characters to ensure tabulation engines have the exact denominator needed to correctly calculate majorities, statistics, and quorums.
* **Error Handling Verification:** Confirms that malformed inputs trigger the correct schema validation errors.

**What this library DOES NOT DO:**

* **Calculate Winners:** This library is not an election calculation engine.
* **Dictate Results:** You will see expected outcomes (like round-by-round results or final winners) included in the test cases. These are included strictly as reference data to verify engine accuracy.

## Ballot Data Formatting Standards

To ensure parser reliability and maintain readability, the schema expects ballot data to be explicitly formatted within text blocks. For test cases with a small number of ballots, ballots are listed individually to preserve clarity. 

### Edge Cases & Special Characters
To capture voter intent, out-of-band communication, and election anomalies without corrupting the tabulation math, the schema utilizes specific characters. These ensure that tabulation engines process missing data and spoiled ballots correctly.

* `~` **(Tilde): Race-Level Abstention.** The voter abstained from the entire race (e.g., wrote "Abstain" at the top).
* `&` **(Ampersand): Candidate-Level Abstention.** The voter explicitly abstained for a specific candidate.
* `^` **(Caret): Blank / Unmarked.** The candidate was left completely blank (no score/rank selected).
* `?` **(Question Mark): Spoiled / Voided Ballot.** A wasted or protest vote (e.g., overvotes, writing "Void" across the ballot, or marking multiple scores incorrectly).
* `%` **(Percent): Spoiled & Re-issued.** The voter made a mistake, the ballot was voided, and a new ballot was issued by the election admin.

### Scored Scenarios (Scores Format)
For scored or rated elections, such as STAR Voting or Approval voting, use a comma-separated list of scores corresponding to the candidate roster. Note that for STAR Voting, equal scores are counted as an "Equal Preference" in the runoff, not discarded.

```text
5,4,3,2,1,0
5,^,^,^,^,^
&,5,3,0,0,0
~,~,~,~,~,~
```

### Grouped Ballots
For batches of identical ballots, group them by placing a colon (`:`) immediately after the ballot count, followed by a space and the ballot data.

```text
5: A>B>C
3: B>C>A
2: ~,~,~
```

# Better Voting Test Library using Pydantic Schema Validation - old

This project provides a standardized schema for defining election test cases to support Better Voting methods.

## Why StrictYAML & Pydantic?

A pure CSV file with ballot data often lacks crucial context. Ambiguities inevitably arise regarding the specific voting method used, the number of seats available, the candidate roster, and the expected format of the ballots. 

**The Critical Gap: Edge Cases and Election Rules**
Beyond basic context, flat data files fail to capture the complex, real-world edge cases that dictate an election's actual outcome. Simple formats make it exceedingly difficult to accurately communicate nuances such as:

* **Abstentions:** Differentiating between a race-level abstention (skipping the race entirely) versus a candidate-level abstention[cite: 1].
* **Special Ballot Designations:** Handling "None of the Above" (NOTA) options, voided or spoiled ballots, and tracking the true total of ballots issued (including re-issues)[cite: 1].
* **Threshold Definitions:** Establishing the precise rules for quorums and majority thresholds based on ballot status (e.g., clearly defining if a "simple majority" requires 50%+1 of *all* ballots cast, or only of the *valid* ballots minus abstentions).

By bundling election parameters, explicit edge-case rulesets, and ballot information into a predefined StrictYAML format, this schema enables robust data validations, consistency checks, and plausibility checks. These test cases are written as simple text files that can be easily edited by hand and utilized universally across different voting tabulation engines.

## Purpose & Scope

**What this library DOES:**

* **Strict Input Validation:** Parses and validates the logic, structure, and consistency of election data using StrictYAML and Pydantic.
* **Schema Enforcement:** Ensures that Global Election Parameters (ID, title, format definition, quorum rules) and specific Race/Ballot structures strictly adhere to the defined format.
* **Edge Case Preservation:** Captures complex ballot statuses using standardized special characters to ensure tabulation engines have the exact denominator needed to correctly calculate majorities, statistics, and quorums[cite: 1].
* **Error Handling Verification:** Confirms that malformed inputs trigger the correct schema validation errors.

**What this library DOES NOT DO:**

* **Calculate Winners:** This library is not an election calculation engine.
* **Dictate Results:** You will see expected outcomes (like round-by-round results or final winners) included in the test cases. These are included strictly as reference data to verify engine accuracy.

## Ballot Data Formatting Standards

To ensure parser reliability and maintain readability, the schema expects ballot data to be explicitly formatted within text blocks. For test cases with a small number of ballots, ballots are listed individually to preserve clarity. 

### Edge Cases & Special Characters
To accurately capture voter intent, out-of-band communication, and election anomalies without corrupting the tabulation math, the schema utilizes specific characters. These ensure that tabulation engines process missing data and spoiled ballots correctly[cite: 1].

* `~` **(Tilde): Race-Level Abstention.** The voter abstained from the entire race (e.g., wrote "Abstain" at the top)[cite: 1].
* `&` **(Ampersand): Candidate-Level Abstention.** The voter explicitly abstained for a specific candidate[cite: 1].
* `^` **(Caret): Blank / Unmarked.** The candidate was left completely blank (no score/rank selected)[cite: 1].
* `?` **(Question Mark): Spoiled / Voided Ballot.** A wasted or protest vote (e.g., overvotes, writing "Void" across the ballot, or marking multiple scores incorrectly)[cite: 1].
* `%` **(Percent): Spoiled & Re-issued.** The voter made a mistake, the ballot was voided, and a new ballot was issued by the election admin[cite: 1].

### Ranked-Choice Scenarios (Ranks Format)
For ranked elections, such as RCV-IRV or RCV-RR, use the `>` separator to indicate preference order.

```text
A>B>C>D>E>F
A>B
C>B>A
?       # Spoiled ballot
```

### Scored Scenarios (Scores Format)
For scored or rated elections, such as STAR Voting or Approval voting, use a comma-separated list of scores corresponding to the candidate roster. Note that for STAR Voting, equal scores are counted as an "Equal Preference" in the runoff, not discarded.

```text
5,4,3,2,1,0
5,^,^,^,^,^  # One candidate scored, the rest left blank
&,5,3,0,0,0  # Candidate A explicitly abstained
~,~,~,~,~,~  # Race-level abstention
```

### Grouped Ballots
For large batches of identical ballots, group them by placing a colon (`:`) immediately after the ballot count, followed by a space and the ballot data.

```text
50: A>B>C
25: B>C>A
12: C>A>B
2:  ~,~,~
```


old:

This project provides a standardized schema for defining election test cases to support [Better Voting methods](https://bettervoting.com/).

## Why StrictYAML?

A pure CSV file with ballot data often lacks crucial context. Ambiguities arise regarding:
* The specific voting method used
* The number of seats available
* The candidate roster
* The expected format of the ballots

By bundling election parameters and ballot information into a predefined StrictYAML format, this schema enables robust data validations, consistency checks, and plausibility checks. These test cases are written as simple text files that can be easily edited by hand and utilized universally across different voting tabulation engines.

## Purpose & Scope 
### What this library DOES:

**Strict Input Validation**: Parses and validates the logic, structure, and consistency of election data using StrictYAML and Pydantic.

**Schema Enforcement**: Ensures that Global Election Parameters (ID, title, format definition) and specific Race/Ballot structures strictly adhere to the defined format.

**Error Handling Verification**: Confirms that malformed inputs trigger the correct schema validation errors.

### What this library DOES NOT DO:

Calculate Winners: This library is not an election calculation engine.

A Note on "Expected Results" in Test Cases:
You will see expected outcomes (like round-by-round results or final winners) included in the test cases. These are included strictly as **reference data**. 

The purpose of the test case is to guarantee that the input payload associated with those results is perfectly formatted and ready to be handed off to external engines written in different programming languages (Better Voting, STARVote https://github.com/larryhastings/starvote, give more examples here) which actually perform the math and generates the reports.

The core objective of this library is to ensure the structural integrity and internal consistency of YAML ballot data before it reaches downstream tabulation systems. It acts as a defensive validation layer to catch incorrect formatting and invalid configurations.

**Primary Focus**:
This testing suite is purpose-built to thoroughly flesh out and support the testing environments for:
* STAR Voting (Single-Winner)
* STAR Multi-Winner (Block STAR, STAR-PR)
* Approval Voting
* RCV-RR

The library rigorously tests both **positive test cases** (ensuring valid configurations process cleanly and output expected winners) and **negative test cases** (ensuring purposefully flawed data throws the exact, expected error messages) for these core methods.

* **Positive Test Cases:** Used for audits, certifications, and IT reviews. These validate election results, winners, and reports.
* **Negative Test Cases:** Used to verify that the validation program raises the expected error messages (e.g., inconsistent configuration settings, internal consistency check failures, or format compatibility issues).

## Validation Architecture: StrictYAML vs. Pydantic

When building the test suite for our voting tabulation library, we require a robust way to ingest test cases (written in YAML) and convert them into mathematically reliable Python objects. 

Because we rely on multi-line text for ballot data (especially crucial for cleanly representing STAR Voting Scoring arrays), standard YAML parsers are prone to type-coercion errors (e.g., the "Norway Problem"). To solve this, we enforce **StrictYAML** as our baseline parser. 

However, parsing is only half the battle. We also need complex cross-field validation. We utilize **StrictYAML + Pydantic**. 

StrictYAML provides the perfect human-authored interface for maintaining clean multi-line parameters and ballot inputs. StrictYAML securely handles the "string-to-dictionary" parse to avoid type coercion, and hands the resulting dictionary over to **Pydantic** for deep validation. Pydantic acts as an industrial-grade gatekeeper, ensuring that no malformed test case ever reaches the tabulation logic, and easily serializing validated cases into strict JSON baselines for secondary systems.

---

## Schema Structure

Each testcase file (`testcase.yaml`) consists of three main sections:
1. **Input – Election Parameters:** Global settings like election ID, title, and description.
2. **Input – Races & Ballots:** Specific race parameters (voting method, candidate list) and the ballot data itself.
3. **Output – Expected Results:** Predicted winners, detailed reports, and edge case handling (e.g., handling ties, "No preference" vote counts).

### Format Examples & Progression

Below is a progressive guide to understanding the schema.

#### 1. The Baseline: Minimal Individual Ballots
For a small number of voters, ballots are listed individually. 

```text
election_parameters:
  election_id: e_001
  election_title: STAR Voting - Baseline 
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

#### 2. Scaling Up: Grouped (Weighted) Ballots
When dealing with many voters, group identical ballots using a colon (`:`) after the group count to indicate the weight.

```text
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

#### 3. Method Flexibility: Approval Voting
By simply changing the `voting_method` to Approval, the exact same structure is used to represent binary choices.

```text
race_1:
  voting_method: Approval
  candidates: 
    - name: Ann
    - name: Bob
    - name: Cal
  ballots: |
    Ann,Bob,Cal
    12: 1,1,0
    8: 0,1,1
```

#### 4. Structural Complexity: Multiple Races
A single election file can contain multiple races with different voting methods.

```text
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

#### 5. Defining Expected Results (The Assertions)
A test case is only as reliable as its output assertions. This block should strictly define:
* **Predicted Winners:** The final elected candidate(s).
* **Detailed Reports:** Intermediate metrics such as scoring matrices or approval totals.
* **Edge Case Handling:** Explicit tracking of specific mechanics, such as tie resolutions, exhausted ballots, or "Equal Preference" tallies.

```text
expected_results:
  race_1:
    status: completed
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

## Testing Architecture: The "Test Case Bundle" Approach

To ensure absolute consistency across multiple data formats, this project utilizes a **Test Case Bundle** architecture. Tests are grouped by the specific voting scenario they evaluate.



### Execution Strategy & Baselines
Our testing strategy follows a strict order of operations to prevent "refactoring churn":

1. **YAML First:** The `testcase.yaml` is written and locked in as the absolute source of truth.
2. **Parser Validation:** The Python runner strictly validates the YAML. For bundles in the `negative/` directory, the runner asserts that the parser throws an exception matching the exact string found in `expected_error.txt`.
3. **Baseline Generation (Snapshot Testing):** Once the YAML parsing is flawless, the runner translates the data structures into our target formats (JSON, TOML) and writes them to the bundle directory alongside the YAML file.

---

### Additional Links & Resources
* **GitHub Link:** [YAML Better Voting Test Library](https://github.com/masiarek/YAML)
* **Test Cases Spreadsheet:** [Google Sheets Link](https://docs.google.com/spreadsheets/d/1EXQsABY2qEu8kKQJGQdyQHn-C89hbCnNqZoGxKXZJNE/edit?gid=0#gid=0) - includes screenshots and additional explanations to each test case
* **Why YAML format:** [Google Docs Link](https://docs.google.com/document/d/171HVrwNQGzqnBsdOfU-6e9QEVcMS-Joh8b61whg1z1o/edit?tab=t.0)
* **Blank-space (^), Abstain race (~), Abstain candidate (&) and Score Zero**:   https://docs.google.com/document/d/17X4kOgXrmgbLrEyXvAJLMnLQDbV-pMcwbMZPERcnIQs/edit?tab=t.0
