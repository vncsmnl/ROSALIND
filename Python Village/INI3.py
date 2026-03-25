## Rosalind: Bioinformatics Stronghold
## Problem: Strings and Lists
## Vinícius Manoel

s = input("String: ").strip()
a, b, c, d = map(int, input("Indices: ").split())

part1 = s[a : b + 1]
part2 = s[c : d + 1]

# Print
print(part1, part2)
