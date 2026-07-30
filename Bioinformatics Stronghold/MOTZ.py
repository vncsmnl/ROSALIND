## Rosalind: Bioinformatics Stronghold
## Problem: Motzkin Numbers and RNA Secondary Structures
## Vinícius Manoel

with open("rosalind_motz.txt") as f:
    s = "".join(line.strip() for line in f if not line.startswith(">"))

MOD = 10**6
n = len(s)

pair = {("A", "U"), ("U", "A"), ("C", "G"), ("G", "C")}

dp = {}

for i in range(n + 1):
    dp[(i, i)] = 1

for i in range(n):
    dp[(i, i + 1)] = 1

for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length

        ans = dp[(l + 1, r)]

        for k in range(l + 1, r):
            if (s[l], s[k]) in pair:
                ans += dp[(l + 1, k)] * dp[(k + 1, r)]
                ans %= MOD

        dp[(l, r)] = ans

print(dp[(0, n)] % MOD)
