"""Base models for biological sequences."""

from collections.abc import Iterator

from pydantic import BaseModel, ConfigDict, Field


class Sequence(BaseModel):
    """Base model shared by biological sequence types."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        str_strip_whitespace=True,
    )

    identifier: str = Field(min_length=1)
    description: str | None = None
    sequence: str = Field(min_length=1)

    def __len__(self) -> int:
        """Return the number of symbols in the sequence."""
        return len(self.sequence)

    def __getitem__(self, index: int | slice) -> str:
        """Return one symbol or a sequence slice."""
        return self.sequence[index]

    def __iter__(self) -> Iterator[str]:
        """Iterate over sequence symbols."""
        return iter(self.sequence)
