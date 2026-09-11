from pathlib import Path

from genome_toolkit.algorithms import (
    count_kmer,
    find_most_frequent_kmers,
)
from genome_toolkit.load import fasta
from genome_toolkit.sequence import DNA

SAMPLES_DIR = Path(__file__).resolve().parent / "samples"
FASTA_SAMPLE = SAMPLES_DIR / "sample.fasta"

# Insepct the FASTA File headers:
fasta_headers = fasta.get_headers(FASTA_SAMPLE)

for position, header in enumerate(fasta_headers):
    print(f"{position}: {header}")

# Load a sequence from FASTA by identifier
fasta_record_1 = fasta.get_sequence(
    FASTA_SAMPLE,
    identifier="M57671.1",
)

dna = DNA.model_validate(
    fasta_record_1,
    from_attributes=True,
)

count_kmers_run_1 = count_kmer(dna, "CCG")
count_kmers_run_2 = count_kmer(dna, "TTCC")

print(f"\nSequence: {dna.sequence}")

print(f"\nExperiment #1:\n{count_kmers_run_1.model_dump_json(indent=2)}")
print(f"\nExperiment #2:\n{count_kmers_run_2.model_dump_json(indent=2)}")

kmer_freq_run_1 = find_most_frequent_kmers(dna, k_len=4)
kmer_freq_run_2 = find_most_frequent_kmers(dna, k_len=5)

print(f"\nExperiment #3:{kmer_freq_run_1.model_dump_json(indent=2)}")
print(f"\nExperiment #4:{kmer_freq_run_2.model_dump_json(indent=2)}")

print("\nExperiment #5:")

for klen in range(1, 9):
    kmers_found = find_most_frequent_kmers(dna, klen)
    print(f"k-len: {klen}, kmers found: {kmers_found.output.kmers}")
