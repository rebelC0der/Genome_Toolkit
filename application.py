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
    identifier="GAMMA_OPERON_SEQ3",
)

# Load a sequence from FASTA by index
fasta_record_2 = fasta.get_sequence(
    FASTA_SAMPLE,
    index=2,
)

dna = DNA.model_validate(
    fasta_record_1,
    from_attributes=True,
)

seq = dna.sequence
kmer = "AA"
k_len = 3


print(f"\nSequence: {seq}")
print(f"k-mer: {kmer}")
print(f"Repeats found: {count_kmer(seq, kmer)}")
print(f"Most frequent k-mer: {find_most_frequent_kmers(seq, k_len)}")
