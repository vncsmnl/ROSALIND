## Rosalind: Bioinformatics Stronghold
## Problem: Speeding Up Motif Finding
## Vinícius Manoel

with open("rosalind_kmp.txt") as f:
    s = ""
    for line in f:
        if line[0] != ">":
            s += line.strip()

p = [0] * len(s)
j = 0

for i in range(1, len(s)):
    while j > 0 and s[i] != s[j]:
        j = p[j - 1]
    if s[i] == s[j]:
        j += 1
    p[i] = j

with open("rosalind_kmp_out.txt", "w") as f:
    f.write(" ".join(str(x) for x in p))
