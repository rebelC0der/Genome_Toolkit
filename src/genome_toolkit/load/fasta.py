# FASTA LOADER
from pathlib import Path

from .records import SequenceRecord


def _parse_header(line: str) -> tuple[str, str | None]:
    """Split one FASTA header into identifier and optional description.

    Args:
        line: FASTA header line beginning with `>`.

    Returns:
        The sequence identifier and optional description.

    Raises:
        ValueError: If the FASTA header does not contain an identifier.
    """

    header = line[1:].strip()

    if not header:
        raise ValueError("A FASTA header must contain a sequence identifier.")

    parts = header.split(maxsplit=1)
    identifier = parts[0]
    description = parts[1] if len(parts) == 2 else None

    return identifier, description


def get_headers(
    filepath: str | Path,
) -> list[tuple[str, str | None]]:
    """Return FASTA identifiers and descriptions in file order.

    Args:
        filepath: Path to the FASTA file.

    Returns:
        Identifier and optional-description tuples in file order.

    Raises:
        ValueError: If sequence data appears before the first header,
            or the file contains no FASTA records.
    """

    path = Path(filepath)

    # Prepare an empty list for discovered headers.
    headers: list[tuple[str, str | None]] = []

    with path.open("r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()

            if not line:
                continue

            # If this is a header, parse and save it.
            if line.startswith(">"):
                headers.append(_parse_header(line))

            elif not headers:
                raise ValueError(f"'{path}' does not begin with a FASTA header.")

    if not headers:
        raise ValueError(f"'{path}' does not contain FASTA records.")

    return headers


def get_sequence(
    filepath: str | Path,
    *,
    identifier: str | None = None,
    index: int | None = None,
) -> SequenceRecord:
    """Return one FASTA record by identifier or zero-based index.

    Args:
        filepath: Path to the FASTA file.
        identifier: Identifier of the record to load.
        index: Zero-based position of the record to load.

    Returns:
        The selected FASTA record as a neutral `SequenceRecord`.

    Raises:
        ValueError: If both or neither selector is provided, an identifier
            is empty, an index is negative, sequence data appears before the
            first header, the requested record cannot be found, or the
            selected record contains no sequence data.
    """

    # Require exactly one selector: identifier OR index.
    if (identifier is None) == (index is None):
        raise ValueError("Provide exactly one of 'identifier' or 'index'.")

    # Validate the identifier if one was provided.
    if identifier is not None:
        identifier = identifier.strip()

        if not identifier:
            raise ValueError("'identifier' must not be empty.")

    # Validate the zero-based index if one was provided.
    if index is not None and index < 0:
        raise ValueError("'index' must be non-negative.")

    path = Path(filepath)
    current_index = 0
    seen_header = False

    selected_identifier: str | None = None
    selected_description: str | None = None
    sequence_parts: list[str] = []

    with path.open("r", encoding="utf-8") as file:
        # Read the file one line at a time.
        for raw_line in file:
            line = raw_line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if selected_identifier is not None:
                    break

                seen_header = True

                current_identifier, current_description = _parse_header(line)
                matches = current_identifier == identifier or current_index == index

                if matches:
                    selected_identifier = current_identifier
                    selected_description = current_description

                current_index += 1

                continue

            if not seen_header:
                raise ValueError(f"'{path}' does not begin with a FASTA header.")

            if selected_identifier is not None:
                sequence_parts.append("".join(line.split()))

    if selected_identifier is None:
        target = identifier if identifier is not None else f"index {index}"

        raise ValueError(f"No sequence found matching '{target}' in '{path}'.")

    sequence = "".join(sequence_parts)

    if not sequence:
        raise ValueError(
            f"Sequence '{selected_identifier}' in '{path}' "
            "does not contain sequence data."
        )

    return SequenceRecord(
        identifier=selected_identifier,
        description=selected_description,
        sequence=sequence,
    )
