## Rosalind: Bioinformatics Stronghold
## Problem: Partial Permutations
## Vinícius Manoel

with open("rosalind_pper.txt") as f:
    n, k = map(int, f.readline().split())

ans = 1
for i in range(k):
    ans *= n - i

print(ans % 1_000_000)
