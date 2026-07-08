## Rosalind: Bioinformatics Stronghold
## Problem: Complementing a Strand of DNA
## Vinícius Manoel

complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
s = input("DNA string: ").strip()

print("Reverse complement:", "".join(complement[base] for base in s[::-1]))
