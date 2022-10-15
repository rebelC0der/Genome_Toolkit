from genome_toolkit import genomeToolkit

gt = genomeToolkit()

seq = "AAAGAAAATTGA"
kmer = "AA"

print(f'Sequence: {seq}')
print(f'k-mer: {kmer}')
print(f'Repeats found: {gt.count_kmer(seq, kmer)}')
