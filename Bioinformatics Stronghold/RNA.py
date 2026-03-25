## Rosalind: Bioinformatics Stronghold
## Problem: Transcribing DNA into RNA
## Vinícius Manoel


dna = input("DNA string: ").strip()
rna = dna.replace("T", "U")
print(f"RNA string: {rna}")
