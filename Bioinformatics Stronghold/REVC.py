## Rosalind: Bioinformatics Stronghold
## Problem: Complementing a Strand of DNA
## Vinícius Manoel


def reverse_complement(s: str) -> str:
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in reversed(s))


s = input("DNA string: ").strip()
print(f"Reverse complement: {reverse_complement(s)}")
