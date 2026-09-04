"""Lightweight records returned by sequence loaders."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SequenceRecord:
    """Parsed sequence data before biological validation."""

    identifier: str
    sequence: str
    description: str | None = None
