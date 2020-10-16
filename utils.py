import numpy as np

codon_dict = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}

def rna_to_aa(rna):
    codons = [rna[i:i+3] for i in range(0, len(rna), 3)]
    trans = [codon_dict.get(w.upper(),w) for w in codons]
    return ''.join(trans[:-1])

def codons_to_aa(codons):
    trans = [codon_dict.get(w.upper(),w) for w in codons]
    return ''.join(trans[:-1])

def dna_to_rna(dna):
    dna_array = np.array(list(dna))

    x = np.argwhere(dna_array == "T")
    dna_array[x] = "U"

    return "".join(dna_array)

def read_fasta(filename):
    inp_fasta = open(filename, "r")
    fasta_data = []

    # Append FASTA lines into one identified sequence
    for line in inp_fasta:
        if line[:1] == '>':
            fasta_data.append(line[1:-1])
            last = False
            continue
        if last:
            fasta_data[last] = fasta_data[last] + line.rstrip()
        else:
            fasta_data.append(line.rstrip())
            last = len(fasta_data) - 1
    return fasta_data