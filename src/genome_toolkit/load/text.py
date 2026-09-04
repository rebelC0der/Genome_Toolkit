"""Loader for plain-text sequence files."""

from pathlib import Path

from .records import SequenceRecord


def get_sequence(filepath: str | Path) -> SequenceRecord:
    """Load one sequence and remove all whitespace.

    Args:
        filepath: Path to a plain-text file containing one sequence.

    Returns:
        A neutral sequence record containing the parsed sequence.

    Raises:
        ValueError: If the file contains no sequence data.
    """
    path = Path(filepath)

    with path.open("r", encoding="utf-8") as file:
        sequence = "".join("".join(line.split()) for line in file)

    if not sequence:
        raise ValueError(f"'{path}' does not contain sequence data.")

    return SequenceRecord(
        identifier=path.stem,
        sequence=sequence,
    )
