## Rosalind: Bioinformatics Stronghold
## Problem: Enumerating k-mers Lexicographically
## Vinícius Manoel

from itertools import product

with open("rosalind_lexf.txt") as f:
    alphabet = f.readline().split()
    n = int(f.readline())

with open("rosalind_lexf_output.txt", "w") as outfile:
    for s in product(alphabet, repeat=n):
        outfile.write("".join(s) + "\n")
