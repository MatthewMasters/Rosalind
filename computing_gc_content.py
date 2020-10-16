# Computing GC Content
# Original problem: http://rosalind.info/problems/gc/
# Solution by Matthew Masters

import numpy as np
from utils import read_fasta

dataset = "../datasets/rosalind_gc.txt"

fasta_data = read_fasta(dataset)

# GC-content anaylsis
gc_content = []
seq = fasta_data[1::2]
for each_seq in seq:
    sequence = np.array(list(each_seq))
    g_content = np.count_nonzero(sequence == 'G')
    c_content = np.count_nonzero(sequence == 'C')
    gc_content.append(float((g_content+c_content)/len(each_seq))*100)

highest_gc = np.argmax(gc_content)
print(fasta_data[highest_gc*2])
print("%.6f" % gc_content[highest_gc])