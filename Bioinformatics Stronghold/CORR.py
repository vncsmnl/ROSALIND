## Rosalind: Bioinformatics Stronghold
## Problem: Error Correction in Reads
## Vinícius Manoel

with open("rosalind_corr.txt") as f:
    lines = f.read().splitlines()

reads = []
seq = ""

for line in lines:
    if line.startswith(">"):
        if seq:
            reads.append(seq)
            seq = ""
    else:
        seq += line
if seq:
    reads.append(seq)

comp = {"A": "T", "T": "A", "C": "G", "G": "C"}

rc = {}
for r in reads:
    rc[r] = "".join(comp[c] for c in r[::-1])

count = {}
for r in reads:
    count[r] = count.get(r, 0) + 1

good = set()
for r in reads:
    if count[r] + count.get(rc[r], 0) >= 2:
        good.add(r)
        good.add(rc[r])

with open("rosalind_corr_out.txt", "w") as f:
    for r in reads:
        if r not in good:
            for g in good:
                if sum(a != b for a, b in zip(r, g)) == 1:
                    f.write(r + "->" + g + "\n")
                    break
