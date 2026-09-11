"""Shared models for structured algorithm results."""

from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field

from genome_toolkit import __version__
from genome_toolkit.sequence import Sequence


class ResultModel(BaseModel):
    """Base configuration shared by algorithm result models."""

    model_config = ConfigDict(extra="forbid")


class ToolkitMetadata(ResultModel):
    """Describe when and how an algorithm result was produced."""

    toolkit_version: str = __version__
    algorithm: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))


class SequenceMetadata(ResultModel):
    """Compact information about an analyzed biological sequence."""

    identifier: str
    description: str | None = None
    length: int


def sequence_metadata(
    sequence: Sequence,
) -> SequenceMetadata:
    """Extract compact metadata from a validated sequence.

    Args:
        sequence: Validated biological sequence used by an algorithm.

    Returns:
        Compact metadata describing the analyzed sequence.
    """
    return SequenceMetadata(
        identifier=sequence.identifier,
        description=sequence.description,
        length=len(sequence),
    )


class SequenceInputs(ResultModel):
    """Inputs for an algorithm operating on one biological sequence."""

    sequence: SequenceMetadata


class AlgorithmResult(ResultModel):
    """Base structure shared by Genome Toolkit algorithm results."""

    metadata: ToolkitMetadata
