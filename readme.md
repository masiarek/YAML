# "YAML Better Voting" Test Library

## Purpose & Scope
The core objective of this library is to ensure the structural integrity and internal consistency of YAML ballot data before it reaches downstream tabulation systems. It acts as a defensive validation layer to catch incorrect formatting and invalid configurations.

**Primary Focus**:
This testing suite is purpose-built to thoroughly flesh out and support the testing environments for:

* STAR Voting (Single-Winner)
* STAR Multi-Winner (Block STAR, STAR-PR)
* Approval Voting
* RCV-RR

The library rigorously tests both positive test cases (ensuring valid configurations process cleanly) and negative test cases (ensuring purposefully flawed data throws the exact, expected error messages) for these core methods.

**Secondary Focus**:
While the schema is capable of parsing and validating standard RCV-IRV and Plurality ballots, support for these methods is entirely secondary. They are covered in passing by the broader validation logic, but they are not the main priority or focus of this repository.

Python code validates "YAML files" - the YAML Better Voting **Test Library**: consistency checks and plausibility checks
before uploading into: https://bettervoting.com/. Open source code: https://github.com/Equal-Vote/star-server

Test cases: https://docs.google.com/spreadsheets/d/1EXQsABY2qEu8kKQJGQdyQHn-C89hbCnNqZoGxKXZJNE/edit?gid=0#gid=0

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
