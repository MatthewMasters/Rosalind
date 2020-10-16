# Counting DNA Nucleotides
# Original problem: http://rosalind.info/problems/dna/
# Solution by Matthew Masters

import numpy as np

dna_data = "GATGACACCTTAGACCATCGGGTGCATATCCTGTGCAGAGAGGTTAACGTAAGATTTCACCGCCGTAACACGTGGACATTTTTAAGCTGGAAGCTATTGTCCAGAGTGCTTGATTGGGACGTTACTCTCTCTAAGACCCCAAGCTAAAGCTGGACACGTAGTGAGCATAAAGCAGTGACCAGGAGACGAAGATCCCCCTTACGGCTGTATCGCAAACACTCCCTGACCGAGGGAACTTGCGATAGTGTGTCGCCAAATACTTCTCAGCCAACCACTCAGCTCAGAACATTTCATTTTGCGGTGGATAATGTTCCGCTTGTCTCAGGGAATCTGGCAGGAATGCTGTGGACGATTGGATCGTATCCTGCACATTCCTTTTCACTCGCCAAATTAATTGGTTCCTCGAGTCAAGATCTGATTTGACAAATCCATACATACGAAGTTAACGCACAGTCCTTGCGAGCTTTGCGGCCGCTGCCGAGGTGAATGCGACTGGCAGTCTCCGATTTATGCTAGCTCCCCAGAGAAGCAACCAGAATCTGTGAACGGACAACTTCAGAAAATCAGCAATTACGTATTCATTCACCCATAGACCGTTGGCTCCGGCATCTAGCCACTACATTTTAGTTGAACCCGTGATTATAAGGTTTTACAGCCGGCTTAGAGCGAGGGAGAGATGCGGTAAATGAGTGCCGTCGAATAAATACGGGACACATAGAATCAGCCCCTTCCTACAATCTGGTGGTATGCCCCTACACCATTGGCAGGTGTGCATACATTATTAGCGTTGACACCGGTATCTCTCACACACATGTCGTTCAACATTGAATAAAGGAGCAGCAAGTTAATAACCTTCGTGGCGAAGAAGTCCCGCTGTCCGCAAGGGTCAGTCGCAGCCTTTTTATTTTAAATTAGGGACGCTGATAATCTGAGCTGGTAT"
nucleotides = ['A', 'C', 'G', 'T']
output = []

for i,nucleotide in enumerate(nucleotides):
    output.append(dna_data.count(nucleotide))

print(output)