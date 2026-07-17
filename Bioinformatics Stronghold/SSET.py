## Rosalind: Bioinformatics Stronghold
## Problem: Counting Subsets
## Vinícius Manoel

with open("rosalind_sset.txt") as f:
    n = int(f.read())

print(pow(2, n, 1000000))
