## Rosalind: Bioinformatics Stronghold
## Problem: Inferring mRNA from Protein
## Vinícius Manoel

from functools import reduce

with open("rosalind_mrna.txt") as f:
    protein = f.read().strip()

codons = {
    "F": 2,
    "L": 6,
    "I": 3,
    "M": 1,
    "V": 4,
    "S": 6,
    "P": 4,
    "T": 4,
    "A": 4,
    "Y": 2,
    "H": 2,
    "Q": 2,
    "N": 2,
    "K": 2,
    "D": 2,
    "E": 2,
    "C": 2,
    "W": 1,
    "R": 6,
    "G": 4,
}

mod = 1_000_000

result = reduce(
    lambda acc, aa: (acc * codons[aa]) % mod,
    protein,
    3,  # 3 stop codons
)

print(result)
