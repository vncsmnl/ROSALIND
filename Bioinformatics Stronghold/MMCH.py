## Rosalind: Bioinformatics Stronghold
## Problem: Maximum Matchings and RNA Secondary Structures
## Vinícius Manoel


with open("rosalind_mmch.txt") as f:
    s = "".join(line.strip() for line in f if not line.startswith(">"))

a = s.count("A")
u = s.count("U")
c = s.count("C")
g = s.count("G")

x = max(a, u)
y = min(a, u)

ans = 1
for i in range(x - y + 1, x + 1):
    ans *= i

x = max(c, g)
y = min(c, g)

for i in range(x - y + 1, x + 1):
    ans *= i

print(ans)
