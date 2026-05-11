from pydantic import BaseModel, Field


class TestElectionParameters(BaseModel):
    """
    Core configuration and metadata for a single voting system validation scenario.
    """

    election_id: str = Field(
        ...,
        description="Unique alphanumeric identifier for the test case (e.g., 'BV10')."
    )

    election_title: str = Field(
        ...,
        description="Same as Better Voting field 'Election Title'."
    )

    short_description: str = Field(
        ...,
        description="A single-sentence summary stating the explicit purpose and expected outcome of this test case."
    )

    long_description: str = Field(
        ...,
        description="A comprehensive narrative explaining the scenario, edge case details, expected tabulation behavior (e.g., scoring vs. automatic runoff phases), and links to external reference results."
    )