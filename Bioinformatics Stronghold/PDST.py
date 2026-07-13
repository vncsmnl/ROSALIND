## Rosalind: Bioinformatics Stronghold
## Problem: Creating a Distance Matrix
## Vinícius Manoel

with open("rosalind_pdst.txt") as f:
    lines = f.read().splitlines()

seqs = []
s = ""

for line in lines:
    if line.startswith(">"):
        if s:
            seqs.append(s)
            s = ""
    else:
        s += line

if s:
    seqs.append(s)

m = len(seqs[0])

with open("rosalind_pdst_out.txt", "w") as f:
    for a in seqs:
        row = []
        for b in seqs:
            diff = 0
            for i in range(m):
                if a[i] != b[i]:
                    diff += 1
            row.append(f"{diff / m:.5f}")
        f.write(" ".join(row) + "\n")
