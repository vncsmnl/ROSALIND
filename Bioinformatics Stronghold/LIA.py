## Rosalind: Bioinformatics Stronghold
## Problem: Independent Alleles
## Vinícius Manoel

from math import comb

with open("rosalind_lia.txt") as f:
    k, N = map(int, f.read().split())

p = 0.25
n = 1 << k

print(sum(comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(N, n + 1)))
