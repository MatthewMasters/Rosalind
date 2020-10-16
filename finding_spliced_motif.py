# Finding a Spliced Motif
# Original problem: http://rosalind.info/problems/sseq/
# Solution by Matthew Masters

import numpy as np
from utils import read_fasta

dataset = "../datasets/rosalind_sseq.txt"
fasta_data = read_fasta(dataset)

seq = fasta_data[1]
subseq = fasta_data[3]
last = 0
indices = []
for letter in subseq:
    last = seq.find(letter,last+1,len(seq))+1
    indices.append(str(last))

print (' '.join(indices))