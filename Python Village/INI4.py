## Rosalind: Bioinformatics Stronghold
## Problem: Conditions and Loops
## Vinícius Manoel


a, b = map(int, input("Numbers: ").split())

total = 0

for x in range(a, b + 1):
    if x % 2 == 1:
        total += x

print(total)
