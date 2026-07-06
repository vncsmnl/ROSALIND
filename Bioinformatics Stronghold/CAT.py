## Rosalind: Bioinformatics Stronghold
## Problem: Catalan Numbers and RNA Secondary Structures
## Vinícius Manoel

MOD = 1000000

with open("rosalind_cat.txt") as f:
    s = "".join(line.strip() for line in f if not line.startswith(">"))

dp = {}

for i in range(len(s) + 1):
    dp[(i, i - 1)] = 1

for length in range(2, len(s) + 1, 2):
    for left in range(len(s) - length + 1):
        right = left + length - 1
        total = 0

        for mid in range(left + 1, right + 1, 2):
            if (
                (s[left] == "A" and s[mid] == "U")
                or (s[left] == "U" and s[mid] == "A")
                or (s[left] == "C" and s[mid] == "G")
                or (s[left] == "G" and s[mid] == "C")
            ):
                total += dp[(left + 1, mid - 1)] * dp[(mid + 1, right)]

        dp[(left, right)] = total % MOD

print(dp[(0, len(s) - 1)])
