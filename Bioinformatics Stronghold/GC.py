## Rosalind: Bioinformatics Stronghold
## Problem: Computing GC Content
## Vinícius Manoel

with open("rosalind_gc.txt", "r") as infile:
    data = infile.read().strip()

lines = data.splitlines()

seqs = {}
current = ""

for line in lines:
    if line.startswith(">"):
        current = line[1:]
        seqs[current] = ""
    else:
        seqs[current] += line.strip()

max_id = ""
max_gc = 0

for k in seqs:
    s = seqs[k]
    gc = (s.count("G") + s.count("C")) / len(s) * 100
    if gc > max_gc:
        max_gc = gc
        max_id = k

print(max_id)
print(f"{max_gc:.6f}")
