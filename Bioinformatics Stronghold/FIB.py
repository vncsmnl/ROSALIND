## Rosalind: Bioinformatics Stronghold
## Problem: Rabbits and Recurrence Relations
## Vinícius Manoel


n, k = map(int, input("Enter n and k: ").split())

a = 1  # F1
b = 1  # F2

for i in range(3, n + 1):
    c = b + k * a
    a = b
    b = c

print(f"The {n}th term of the sequence is: {b}")
