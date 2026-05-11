# "YAML Better Voting" Test Library
# Better Voting Test Library

## Overview
This test library supports [Better Voting methods](https://bettervoting.com/) by providing a standardized schema for election test cases. 

### Why StrictYAML?
A pure CSV file with ballot data often lacks crucial context—such as the specific voting method, the number of seats, candidate names, and expected ballot formats. By bundling election parameters and ballot information into a predefined StrictYAML format, this schema enables:
- Robust data validations
- Consistency and plausibility checks
- Easy hand-editing
- Universal compatibility across different voting tabulation engines

## Schema Structure
Each test case is written as a simple text file and consists of three main sections:
1. **Input – Election Parameters:** Global settings like election ID, title, and description.
2. **Input – Races & Ballots:** Specific race parameters (voting method, candidates) and the ballot data.
3. **Output – Expected Results:** Predicted winners, detailed reports, and edge case handling (e.g., ties).

---

## Format Examples

We recommend progressing through the examples below to understand how the schema scales from a simple baseline to complex, multi-race elections.

### 1. The Baseline: Minimal Individual Ballots
For a small number of voters, ballots are listed individually. This example demonstrates the minimum required data for a single STAR voting race.

```text
election_parameters:
  election_id: e_001
  election_title: STAR Voting - Baseline 
  election_description: |
    Test Election Goal: Demonstrate a minimum set of data with three candidates and two individual ballots.
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
    

## Purpose & Scope
The core objective of this library is to ensure the structural integrity and internal consistency of YAML ballot data before it reaches downstream tabulation systems. It acts as a defensive validation layer to catch incorrect formatting and invalid configurations.

**Primary Focus**:
This testing suite is purpose-built to thoroughly flesh out and support the testing environments for:

* STAR Voting (Single-Winner)
* STAR Multi-Winner (Block STAR, STAR-PR)
* Approval Voting
* RCV-RR

The library rigorously tests both positive test cases (ensuring valid configurations process cleanly) and negative test cases (ensuring purposefully flawed data throws the exact, expected error messages) for these core methods.

Test cases: https://docs.google.com/spreadsheets/d/1EXQsABY2qEu8kKQJGQdyQHn-C89hbCnNqZoGxKXZJNE/edit?gid=0#gid=0

## Validation Architecture: StrictYAML vs. Pydantic

When building the test suite for our voting tabulation library, we require a robust way to ingest test cases (written in YAML) and convert them into mathematically reliable Python objects. 

Because we rely on multi-line text for ballot data (especially crucial for cleanly representing STAR Voting Scoring arrays), standard YAML parsers are prone to type-coercion errors (e.g., the "Norway Problem"). To solve this, we enforce **StrictYAML** as our baseline parser. 

However, parsing is only half the battle. We also need complex cross-field validation (e.g., "If `race_abstention_allowed` is true, the `input_data` format must align"). We evaluated two architectural approaches to handle this validation.

### Approach 1: Pure StrictYAML + Procedural Validation
In this approach, StrictYAML handles both parsing and basic type enforcement using its native schema definitions. Complex business logic is handled via custom Python functions after the parse is complete.

* **Workflow:** Read YAML -> `strictyaml.load()` -> Extract Dict -> Run custom `if/else` validation functions.
* **Pros:** Very lightweight; minimal dependencies.
* **Cons:** Business logic is decoupled from the data structure. It requires writing manual error-handling loops and leaves validation logic floating in external scripts.

### Approach 2: StrictYAML + Pydantic (Recommended)
This hybrid approach uses StrictYAML strictly as a secure "string-to-dictionary" parser to avoid type coercion, and hands the resulting dictionary over to **Pydantic** for deep validation and serialization.

* **Workflow:** Read YAML -> `strictyaml.load()` -> Pass Dict to Pydantic `BaseModel` -> Pydantic enforces complex rules via `@model_validator`.
* **Pros:**
    * **Encapsulation:** All cross-field validation rules live securely inside the data model itself.
    * **Strong Typing:** Generates heavily typed Python objects, providing full IDE autocomplete support.
    * **Native Serialization:** Pydantic objects can be instantly exported to highly structured, machine-friendly JSON files (`model_dump_json()`), establishing perfect regression baselines.
* **Cons:** Introduces an additional dependency (Pydantic), though the architectural benefits far outweigh the cost.

### The Decision
We utilize **Approach 2 (StrictYAML + Pydantic)**. 

StrictYAML provides the perfect human-authored interface for maintaining clean multi-line parameters and ballot inputs. Pydantic then acts as an industrial-grade gatekeeper, ensuring that no malformed test case ever reaches the tabulation logic, and easily serializing validated cases into strict JSON baselines for secondary systems.


Library contains both positive (happy path with expected winners) and negative test cases (with expected error
messages):

- **Positive** Test Cases are used for audits, certifications, IT reviews.
  These are validated Election Results - winner(s), reports, etc.
- **Negative** Test Cases are used to check that the validation programs raises expected error messages (YAML file
  with inconsistent configuration settings - internal consistency check fails - election configuration and ballot data /
  format - compatibility check).

## Voting Methods tested

### Single winner:

- STAR Voting
- Approval Voting
- Plurality Voting
- RCV IRV

### Multi-winner

- Block STAR (Basic Multi-Winner )
- STAR-PR (Proportional Multi-Winner)
- STV (Single Transferable Vote)

Additional Links:
- Why YAML format: https://docs.google.com/document/d/171HVrwNQGzqnBsdOfU-6e9QEVcMS-Joh8b61whg1z1o/edit?tab=t.0

![img.png](img.png)

# Example ballot - STAR Voting:

![img_1.png](img_1.png)

- GitGub Link - YAML Better Voting Test Library: https://github.com/masiarek/YAML
- Similar
  idea: https://github.com/fairvotereform/rcv_cruncher/tree/9bb9f8482290033ff7b31d6b091186474e7afff6/tests/contest_sets/tabulation_test

## Testing Architecture: The "Test Case Bundle" Approach

To ensure absolute consistency across multiple data formats, this project utilizes a **Test Case Bundle** architecture. Instead of organizing test files by their file extension (e.g., all JSONs in one folder, all YAMLs in another), tests are grouped by the specific voting scenario they evaluate.

This approach establishes a single source of truth and guarantees format-agnostic validation for methods like STAR Voting (Scoring), Approval, and RCV-IRV.

### Directory Structure

Each directory under `tests/cases/` represents a self-contained test case. 

```text
tests/
└── cases/
    ├── positive/
    │   ├── 01_star_basic_scoring/
    │   │   ├── testcase.yaml      # The Source of Truth (StrictYAML)
    │   │   ├── testcase.json      # Generated regression baseline
    │   │   └── testcase.toml      # Generated regression baseline
    │   └── 02_rcv_irv_tiebreaker/
    │       ├── testcase.yaml
    │       └── testcase.json
    └── negative/
        ├── err_missing_parameters/
        │   ├── testcase.yaml      # Intentionally malformed YAML
        │   └── expected_error.txt # Exact exception string expected
        └── err_invalid_scoring/
            ├── testcase.yaml
            └── expected_error.txt
The Source of Truth (testcase.yaml)
The core of every bundle is the testcase.yaml file. We enforce StrictYAML parsing to prevent unexpected type coercion. Every valid test case must contain exactly three sections:

parameters: Defines the election rules (voting method, seats, candidates).

input_data: The raw ballot data. For testing clarity, small numbers of ballots are listed individually using a CSV-style format.

expected_results: The anticipated winners, election reports, and head-to-head (vs) matrices.

Example testcase.yaml (STAR Voting Scenario):

YAML

parameters:
  voting_method: STAR
  seats: 1
  races: 1
  candidates: [A, B, C]

input_data: |
  A,B,C
  5,1,0
  3,1,5
  0,5,1

expected_results:
  winner: A
  head_to_head:
    A vs B: [2, 1]
    A vs C: [2, 1]

Execution Strategy & Baselines
Our testing strategy follows a strict order of operations to prevent "refactoring churn":

YAML First: The testcase.yaml is written and locked in as the absolute source of truth.

Parser Validation: The Python runner strictly validates the YAML. For bundles in the negative/ directory, the runner asserts that the parser throws an exception matching the exact string found in expected_error.txt.

Baseline Generation (Snapshot Testing): Once the YAML parsing is flawless, the runner translates the data structures into our target formats (JSON, TOML, XML) and writes them to the bundle directory alongside the YAML file.