# Enumerating Gene Orders
# Original problem: http://rosalind.info/problems/perm/
# Solution by Matthew Masters

import numpy as np

input = 6
array = [i+1 for i in range(input)]

def permutation(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [array]

    permutations = []
    for i in range(len(array)):
        x = array[i]
        rem = array[:i] + array[i + 1:]
        for p in permutation(rem):
            permutations.append([x] + p)
    return permutations

results = permutation(array)
print(len(results))
for p in results:
    print(' '.join(np.array(p, dtype=str)))