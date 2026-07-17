## Rosalind: Bioinformatics Stronghold
## Problem: Introduction to Alternative Splicing
## Vinícius Manoel

with open("rosalind_aspc.txt") as f:
    n, m = map(int, f.read().split())

MOD = 1000000

c = [0] * (n + 1)
c[0] = 1

for i in range(1, n + 1):
    for j in range(i, 0, -1):
        c[j] = (c[j] + c[j - 1]) % MOD

print(sum(c[m:]) % MOD)
