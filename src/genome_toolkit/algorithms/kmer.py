from genome_toolkit.sequence import Sequence

from .base import (
    AlgorithmResult,
    ResultModel,
    SequenceInputs,
    ToolkitMetadata,
    sequence_metadata,
)


class KmerCountParameters(ResultModel):
    """Parameters passed to `count_kmer()`."""

    kmer: str


class KmerCountOutput(ResultModel):
    """Values computed by `count_kmer()`."""

    count: int


class KmerCountResult(AlgorithmResult):
    """Structured result returned by `count_kmer()`."""

    inputs: SequenceInputs

    parameters: KmerCountParameters

    output: KmerCountOutput


def count_kmer(sequence: Sequence, kmer: str) -> KmerCountResult:
    """
    Counts the number of times a specific k-mer appears in a given sequence,
    including overlapping k-mers.

    Parameters:
        sequence: Validated biological sequence to search.
        kmer (str): The specific k-mer to search for in the sequence.

    Returns:
        KmerCountResult: Structured result containing input metadata, parameters, and count.
    """
    kmer_count = 0

    for position in range(len(sequence) - (len(kmer) - 1)):
        if sequence[position : position + len(kmer)] == kmer:
            kmer_count += 1

    return KmerCountResult(
        metadata=ToolkitMetadata(
            algorithm=count_kmer.__name__,
        ),
        inputs=SequenceInputs(
            sequence=sequence_metadata(sequence),
        ),
        parameters=KmerCountParameters(
            kmer=kmer,
        ),
        output=KmerCountOutput(
            count=kmer_count,
        ),
    )


class FrequentKmersParameters(ResultModel):
    """Parameters passed to `find_most_frequent_kmers()`."""

    k_len: int


class FrequentKmersOutput(ResultModel):
    """Values computed by `find_most_frequent_kmers()`."""

    kmers: list[str]

    frequency: int


class FrequentKmersResult(AlgorithmResult):
    """Structured result returned by `find_most_frequent_kmers()`."""

    inputs: SequenceInputs

    parameters: FrequentKmersParameters

    output: FrequentKmersOutput


def find_most_frequent_kmers(
    sequence: Sequence,
    k_len: int,
) -> FrequentKmersResult:
    """Find the most frequent k-mers of a requested length.

    Args:
        sequence: Validated biological sequence to analyze.
        k_len: Length of the k-mers to count.

    Returns:
        FrequentKmersResult: Structured result containing the most frequent k-mers and their
        shared frequency.
    """
    kmer_frequencies: dict[str, int] = {}

    for i in range(len(sequence) - k_len + 1):
        kmer = sequence[i : i + k_len]
        if kmer in kmer_frequencies:
            kmer_frequencies[kmer] += 1
        else:
            kmer_frequencies[kmer] = 1

    highest_frequency = max(kmer_frequencies.values())

    frequent_kmers = [
        kmer
        for kmer, frequency in kmer_frequencies.items()
        if frequency == highest_frequency
    ]

    return FrequentKmersResult(
        metadata=ToolkitMetadata(
            algorithm=find_most_frequent_kmers.__name__,
        ),
        inputs=SequenceInputs(
            sequence=sequence_metadata(sequence),
        ),
        parameters=FrequentKmersParameters(
            k_len=k_len,
        ),
        output=FrequentKmersOutput(
            kmers=frequent_kmers,
            frequency=highest_frequency,
        ),
    )
