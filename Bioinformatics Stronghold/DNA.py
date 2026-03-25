## Rosalind: Bioinformatics Stronghold
## Problem: Counting DNA Nucleotides
## Vinícius Manoel

s = input("DNA string: ").strip()

A = s.count("A")
C = s.count("C")
G = s.count("G")
T = s.count("T")

print(f"The counts of nucleotides in the DNA string are: {A} {C} {G} {T}")
