# Finding a Protein Motif
# Original problem: http://rosalind.info/problems/mprt/
# Solution by Matthew Masters

import numpy as np
import urllib.request
from utils import read_fasta

uniprot_ids = open("../datasets/rosalind_mprt.txt", "r")
base_url = "http://www.uniprot.org/uniprot/"

for id in uniprot_ids:
    id = id.rstrip()
    with urllib.request.urlopen(base_url + id + ".fasta") as fasta:
        # Load FASTA data
        fasta_data = []
        for line in fasta:
            line = line.decode('UTF-8')
            if line[:1].rstrip() == '>':
                fasta_data.append(id.rstrip())
                last = False
                continue
            if last:
                fasta_data[last] = fasta_data[last] + line.rstrip()
            else:
                fasta_data.append(line.rstrip())
                last = len(fasta_data) - 1

        # Perform N-glycosylation Motif Query
        seq = np.array(list(fasta_data[1]))
        x = np.argwhere(seq=="N")
        y = np.argwhere(x>len(seq)-3)
        x = np.delete(x, y)

        ind = 0
        for loc in x:
            if seq[loc+1] == 'P':
                x = np.delete(x, ind)
            else:
                ind += 1
        ind = 0
        for loc in x:
            if seq[loc+2] != 'S' and seq[loc+2] != 'T':
                x = np.delete(x, ind)
            else:
                ind += 1

        # Formatting for output
        np.add(x,1,x)
        if x.size != 0:
            print(id)
            print(' '.join(x.astype(str)))
