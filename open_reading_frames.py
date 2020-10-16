# Open Reading Frames
# Original problem: http://rosalind.info/problems/orf/
# Solution by Matthew Masters

import numpy as np
from utils import codons_to_aa, dna_to_rna

dna_data = "TGCCGACATAAGGGCTGGTAATCCGTCCCAGAGTTCATCTTTTTAAGCACAGCGGAGTTTCCATCTAGGGTGCGACCTATTGTCACTCGTAACTTTAACTCGGTTTGGGCTTAAGAGAGTCAGACCTTGGCCTACAGAGTAGAAGTCCACCGGGATGAAGGTTGCCGGCACTAGCCAACCGTTGGGTGCTTTTAAACCTGGAAGCACTGCCGTGTGACAACGACGTCTCTAGCCTGTTTTCGATACTACATGTCAATAGGCGTAATTCATTGCCAGCTCGACTAGATGCACCCGATTGAGGAATCCCAATTTGTGGCTGTTAAACGGATGTCATCCGGCACTCTGGAATATCACCTCTTTGATGTTAACATGGGATCTAGGGACGGATAATCGTTAAAAGCCACGCAGCCGAATGCCTAACCAGGCGGGACATTACTCGTTGTAGCTACAACGAGTAATGTCCCGCCTGGTTAGGCATTACGTTCACTCAGCGCCTTAGCCTCTTATGGGCTTTCCGCGGGTTTGGCAGAGGTACCATAGGTGTTTCAGATGCACAGTTCGGTACTACTTCCTGAGCGTATGTACGTAGGGTGCTCCGCTTCACTGAGATTACTAGATTAACTTACGTGCCAGGTCCAACTCCAGGATAGAAAATCTACACTCCACGATGGGGACGCCGCTGTTTATCAGGTATTCCCCATCTAACCGCTCTGATCAGGCCATTTGAGTTATTACGCCTACCGGGGAGAGTGCGACTTTGACGCAATAACTGGCACGCTCACAGCTATAGTAAGACACATAGACGCCATACATTGGGTAATTCCCTCCATGGAGTGGGGTTCCACATGACCCCGGTCTATACGAGACTGATTCGAATGGATTTATGAGTG"
start_codon = "AUG"
stop_codons = ["UAG", "UGA", "UAA"]
nucleotides = ['A', 'C', 'G', 'U']

rna_data = dna_to_rna(dna_data)

rna_data2 = rna_data[::-1]
rna_array = np.array(list(rna_data2))
complement_array = np.copy(rna_array)

for i,nucleotide in enumerate(nucleotides):
    x = np.argwhere(rna_array==nucleotide)
    complement_array[x] = nucleotides[::-1][i]

data = [rna_data, "".join(complement_array)]
possible_frames = []
for rna_strand in data:
    for reading_frame in range(3):
        framed_strand = rna_strand[reading_frame:]
        codons = [framed_strand[i:i + 3] for i in range(0, len(framed_strand), 3)]
        codons = np.array(codons)
        start_codon_pos = np.where(codons=='AUG')[0]

        for start in start_codon_pos:
            coding_region = []
            end=False
            for codon in codons[start:]:
                if codon in stop_codons:
                    end=True
                    break
                else:
                    coding_region.append(codon)

            if end==True:
                trans = codons_to_aa(codons=coding_region)
                possible_frames.append(trans)

# Exclude Duplicates
possible_frames = np.unique(possible_frames)
for frame in possible_frames:
    print(frame)