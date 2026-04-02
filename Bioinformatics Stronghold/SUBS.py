## Rosalind: Bioinformatics Stronghold
## Problem: Finding a Motif in DNA
## Vinícius Manoel

s, t = input("DNA string: ").strip(), input("Motif: ").strip()

for i in range(len(s) - len(t) + 1):
    if s[i : i + len(t)] == t:
        print(i + 1, end=" ")
