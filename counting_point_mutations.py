# Counting Point Mutations
# Original problem: http://rosalind.info/problems/hamm/
# Solution by Matthew Masters

import numpy as np

seqA = list("GAGCCTACTAACGGGAT")
seqB = list("CATCGTAATGACGGCCT")
count = 0

for i,nucleotide in enumerate(seqA):
    if nucleotide != seqB[i]: count+=1

print(count)