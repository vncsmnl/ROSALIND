## Rosalind: Bioinformatics Stronghold
## Problem: Enumerating Gene Orders
## Vinícius Manoel

from itertools import permutations

n = int(input("Enter the number of genes: "))

perms = list(permutations(range(1, n + 1)))

with open("rosalind_perm.txt", "w") as f:
    f.write(str(len(perms)) + "\n")
    for p in perms:
        f.write(" ".join(map(str, p)) + "\n")
