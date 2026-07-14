## Rosalind: Bioinformatics Stronghold
## Problem: Matching Random Motifs
## Vinícius Manoel

with open("rosalind_rstr.txt") as f:
    n, x = f.readline().split()
    n = int(n)
    x = float(x)
    s = f.readline().strip()

p = 1.0
for c in s:
    if c in "GC":
        p *= x / 2
    else:
        p *= (1 - x) / 2

print(1 - (1 - p) ** n)
