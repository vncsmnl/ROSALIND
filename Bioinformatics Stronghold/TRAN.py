## Rosalind: Bioinformatics Stronghold
## Problem: Transitions and Transversions
## Vinícius Manoel

with open("rosalind_tran.txt") as f:
    lines = f.read().splitlines()

s1 = ""
s2 = ""
cur = 0

for line in lines:
    if line.startswith(">"):
        cur += 1
    elif cur == 1:
        s1 += line
    else:
        s2 += line

transitions = 0
transversions = 0

for a, b in zip(s1, s2):
    if a != b:
        if (a, b) in [("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")]:
            transitions += 1
        else:
            transversions += 1

print(transitions / transversions)
