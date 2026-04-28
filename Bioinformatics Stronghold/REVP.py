## Rosalind: Bioinformatics Stronghold
## Problem: Locating Restriction Sites
## Vinícius Manoel

with open("rosalind_revp.txt") as f:
    s = "".join(line.strip() for line in f if not line.startswith(">"))

comp = str.maketrans("ACGT", "TGCA")

for i in range(len(s)):
    for l in range(4, 13):
        sub = s[i : i + l]
        if len(sub) == l and sub == sub.translate(comp)[::-1]:
            print(i + 1, l)
