"""DNA-specific sequence validation."""

from pydantic import field_validator

from .base import Sequence

DNA_ALPHABET = frozenset("ACGTN")


class DNA(Sequence):
    """DNA sequence validated against the A, C, G, T, and N alphabet."""

    @field_validator("sequence")
    @classmethod
    def validate_nucleotides(cls, value: str) -> str:
        """Normalize DNA to uppercase and reject unsupported symbols."""
        normalized = value.upper()
        invalid = set(normalized) - DNA_ALPHABET

        if invalid:
            symbols = ", ".join(sorted(invalid))
            raise ValueError(
                f"Sequence contains invalid DNA symbols: {symbols}. "
                "Allowed symbols are A, C, G, T, and N."
            )

        return normalized
