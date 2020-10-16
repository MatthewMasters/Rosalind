# RNA Splicing
# Original problem: http://rosalind.info/problems/splc/
# Solution by Matthew Masters

import numpy as np
from utils import rna_to_aa, dna_to_rna, read_fasta

dataset = "../datasets/rosalind_splc.txt"

fasta_data = read_fasta(dataset)

dna_data = fasta_data[1]

for intron in fasta_data[3::2]:
    loc1 = dna_data.find(intron)
    loc2 = loc1 + len(intron)
    dna_data = dna_data[:loc1] + dna_data[loc2:]

rna = dna_to_rna(dna_data)
print(rna_to_aa(rna))