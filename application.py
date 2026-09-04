from pathlib import Path

from genome_toolkit.algorithms import (
    count_kmer,
    find_most_frequent_kmers,
)
from genome_toolkit.load import text
from genome_toolkit.sequence import DNA

SAMPLES_DIR = Path(__file__).resolve().parent / "samples"

record = text.get_sequence(SAMPLES_DIR / "sample.txt")

dna = DNA.model_validate(
    record,
    from_attributes=True,
)

seq = dna.sequence
kmer = "AA"
k_len = 3

print(f"\nSequence: {seq}")
print(f"k-mer: {kmer}")
print(f"Repeats found: {count_kmer(seq, kmer)}")
print(f"Most frequent k-mer: {find_most_frequent_kmers(seq, k_len)}")
