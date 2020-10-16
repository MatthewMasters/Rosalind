# Mendel's First Law
# Original problem: http://rosalind.info/problems/iprb/
# Solution by Matthew Masters

import numpy as np

k, m, n = 23, 29, 17

population = k + m + n
homD_homD_mates = k * (k-1)/2
homD_het_mates = k * m
homD_homR_mates = k * n
het_het_mates = (m*(m-1)/2)*0.75
het_homR_mates = m * n * 0.5

total = (k*(k-1)/2) + (m*(m-1)/2) + (n*(n-1)/2) + k*m + k*n + m*n
mates = homD_homD_mates + homD_het_mates + homD_homR_mates + het_het_mates + het_homR_mates
print(mates/total)