## Rosalind: Bioinformatics Stronghold
## Problem: Mortal Fibonacci Rabbits
## Vinícius Manoel

n, m = map(int, input("Enter n and m: ").split())

ages = [1] + [0] * (m - 1)

for i in range(n - 1):
    ages = [sum(ages[1:])] + ages[:-1]

print(sum(ages))
