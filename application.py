from genome_toolkit.algorithms import (
    count_kmer,
    find_most_frequent_kmers,
)
from genome_toolkit.sequence import DNA

dna = DNA(
    identifier="example_dna",
    description="Part 4.3 demonstration sequence",
    sequence="aattttaaaac",
)

seq = dna.sequence
kmer = "AA"
k_len = 3


print(f"Identifier: {dna.identifier}")
print(f"Description: {dna.description}")
print(f"Validated sequence: {dna.sequence}")
print(f"Sequence length: {len(dna)}")
print(f"First nucleotide: {dna[0]}")
print(f"First four nucleotides: {dna[:4]}")
print(f"Nucleotides: {' '.join(dna)}")

print("\nDNA as JSON:")
print(dna.model_dump_json(indent=2))


print(f"\nSequence: {seq}")
print(f"k-mer: {kmer}")
print(f"Repeats found: {count_kmer(seq, kmer)}")
print(f"Most frequent k-mer: {find_most_frequent_kmers(seq, k_len)}")
