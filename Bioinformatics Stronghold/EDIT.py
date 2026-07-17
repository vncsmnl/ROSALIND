## Rosalind: Bioinformatics Stronghold
## Problem: Edit Distance
## Vinícius Manoel

with open("rosalind_edit.txt") as f:
    lines = f.read().splitlines()

seqs = []
cur = ""

for line in lines:
    if line.startswith(">"):
        if cur:
            seqs.append(cur)
            cur = ""
    else:
        cur += line

seqs.append(cur)

s = seqs[0]
t = seqs[1]

n = len(s)
m = len(t)

dp = []

for i in range(n + 1):
    row = []
    for j in range(m + 1):
        row.append(0)
    dp.append(row)

for i in range(n + 1):
    dp[i][0] = i

for j in range(m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            a = dp[i - 1][j] + 1
            b = dp[i][j - 1] + 1
            c = dp[i - 1][j - 1] + 1

            if a < b:
                if a < c:
                    dp[i][j] = a
                else:
                    dp[i][j] = c
            else:
                if b < c:
                    dp[i][j] = b
                else:
                    dp[i][j] = c

print(dp[n][m])
