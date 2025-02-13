# YAML Better Voting Test Library

GitHub Repository: https://github.com/masiarek/YAML

Library contains both positive (happy path) and negative test cases (should fail):

- **Positive** Test Cases are cases used for audits, certifications, IT reviews.
  These are well formated YAML files and contain validated Election Results - winner(s), reports, etc.
- **Negative** Test Cases are used to check that the validation programs raises expected error messages if the YAML file
  is using
  inconsistent configuration settings (internal consistency checks).

Additional Links:

- https://bettervoting.com/
- Open source code: https://github.com/Equal-Vote/star-server
- Why YAML format: https://docs.google.com/document/d/171HVrwNQGzqnBsdOfU-6e9QEVcMS-Joh8b61whg1z1o/edit?tab=t.0

Python code in this library is addressing the step "Validate" - consitency checks and plausibilty checks.
![img.png](img.png)