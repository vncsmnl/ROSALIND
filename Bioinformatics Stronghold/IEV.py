## Rosalind: Bioinformatics Stronghold
## Problem: Calculating Expected Offspring
## Vinícius Manoel

with open("rosalind_iev.txt", "r") as file:
    line = file.readline().strip()

a, b, c, d, e, f = map(int, line.split())

print(2 * (a + b + c + 0.75 * d + 0.5 * e))
