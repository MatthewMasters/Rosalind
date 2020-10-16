# Transition/Transversion Ratio
# Original problem: http://rosalind.info/problems/tran/
# Solution by Matthew Masters

import numpy as np
from utils import read_fasta

fasta_data = read_fasta("../datasets/rosalind_tran.txt")

seqA = list(fasta_data[1])
seqB = list(fasta_data[3])
transition_count = 0
transversion_count = 0

for i,nucleotide in enumerate(seqA):
    if nucleotide != seqB[i]:
        if nucleotide == "A" or nucleotide == "G":
            if seqB[i] == "C" or seqB[i] == "T":
                transversion_count += 1
            else:
                transition_count += 1
        else:
            if seqB[i] == "C" or seqB[i] == "T":
                transition_count += 1
            else:
                transversion_count += 1

print(transition_count/transversion_count)