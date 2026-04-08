## Rosalind: Bioinformatics Stronghold
## Problem: Consensus and Profile
## Vinícius Manoel

from collections import Counter

with open("rosalind_cons.txt") as f:
    seqs = ["".join(s.splitlines()[1:]) for s in f.read().strip().split(">") if s]

cols = zip(*seqs)

profile = {n: [] for n in "ACGT"}
consensus = ""

for col in cols:
    count = Counter(col)
    for n in "ACGT":
        profile[n].append(count[n])
    consensus += max("ACGT", key=lambda x: count.get(x, 0))

print(consensus)
for n in "ACGT":
    print(f"{n}: {' '.join(map(str, profile[n]))}")
