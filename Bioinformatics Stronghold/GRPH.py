## Rosalind: Bioinformatics Stronghold
## Problem: Overlap Graphs
## Vinícius Manoel

with open("rosalind_grph.txt") as f:
    fasta = f.read()

seqs = {}
label = ""

for line in fasta.splitlines():
    if line.startswith(">"):
        label = line[1:]
        seqs[label] = ""
    else:
        seqs[label] += line.strip()

k = 3

for a, sa in seqs.items():
    for b, sb in seqs.items():
        if a != b and sa.endswith(sb[:3]):
            print(a, b)
