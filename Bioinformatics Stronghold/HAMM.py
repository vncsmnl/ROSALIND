## Rosalind: Bioinformatics Stronghold
## Problem: Counting Point Mutations
## Vinícius Manoel

s = input("First DNA string: ").strip()
t = input("Second DNA string: ").strip()

distance = sum(1 for a, b in zip(s, t) if a != b)

print(distance)
