## Rosalind: Bioinformatics Stronghold
## Problem: k-Mer Composition
## Vinícius Manoel

with open("rosalind_kmer.txt") as f:
    s = "".join(line.strip() for line in f if not line.startswith(">"))

kmers = [a + b + c + d for a in "ACGT" for b in "ACGT" for c in "ACGT" for d in "ACGT"]

counts = {k: 0 for k in kmers}

for i in range(len(s) - 3):
    counts[s[i : i + 4]] += 1

with open("rosalind_kmer_output.txt", "w") as f:
    f.write(" ".join(str(counts[k]) for k in kmers))
