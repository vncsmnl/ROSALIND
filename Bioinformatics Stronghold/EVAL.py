## Rosalind: Bioinformatics Stronghold
## Problem: Expected Number of Restriction Sites
## Vinícius Manoel

with open("rosalind_eval.txt") as f:
    lines = f.read().split()

n = int(lines[0])
s = lines[1]
A = list(map(float, lines[2:]))

gc = s.count("G") + s.count("C")
at = len(s) - gc
positions = n - len(s) + 1

ans = []

for p in A:
    prob = (p / 2) ** gc * ((1 - p) / 2) ** at
    ans.append(positions * prob)

print(*["{:.3f}".format(x) for x in ans])
