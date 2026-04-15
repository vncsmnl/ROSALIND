## Rosalind: Bioinformatics Stronghold
## Problem: Finding a Shared Motif
## Vinícius Manoel

with open("rosalind_lcsm.txt") as f:
    data = f.read().strip().split(">")
seqs = ["".join(x.splitlines()[1:]) for x in data if x]

shortest = min(seqs, key=len)

best = ""
for i in range(len(shortest)):
    for j in range(i + len(best) + 1, len(shortest) + 1):
        sub = shortest[i:j]
        if all(sub in s for s in seqs):
            best = sub

print(best)
