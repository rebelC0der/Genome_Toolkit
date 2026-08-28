from genome_toolkit.algorithms import (
    count_kmer,
    find_most_frequent_kmers,
)

seq = "AATTTTAAAAC"
kmer = "AA"
k_len = 3


print(f"Sequence: {seq}")
print(f"k-mer: {kmer}")
print(f"Repeats found: {count_kmer(seq, kmer)}")
print(f"Most frequent k-mer: {find_most_frequent_kmers(seq, k_len)}")
