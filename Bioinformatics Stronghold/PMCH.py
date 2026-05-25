## Rosalind: Bioinformatics Stronghold
## Problem: Perfect Matchings and RNA Secondary Structures
## Vinícius Manoel

with open("rosalind_pmch.txt") as f:
    s = f.read().strip()

a = s.count("A")
c = s.count("C")

ans = 1

for i in range(2, a + 1):
    ans *= i

for i in range(2, c + 1):
    ans *= i

print(ans)
