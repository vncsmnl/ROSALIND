## Rosalind: Bioinformatics Stronghold
## Problem: Introduction to Random Strings
## Vinícius Manoel

from math import log10

with open("rosalind_prob.txt") as f:
    s = f.readline().strip()
    a = list(map(float, f.readline().split()))

gc = s.count("G") + s.count("C")
at = len(s) - gc

print(*[round(gc * log10(x / 2) + at * log10((1 - x) / 2), 3) for x in a])
