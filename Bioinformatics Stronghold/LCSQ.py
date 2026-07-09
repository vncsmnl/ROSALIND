## Rosalind: Bioinformatics Stronghold
## Problem: Finding a Shared Spliced Motif
## Vinícius Manoel


with open("rosalind_lcsq.txt") as f:
    lines = f.read().splitlines()

seqs = []
cur = ""

for line in lines:
    if line[0] == ">":
        if cur:
            seqs.append(cur)
            cur = ""
    else:
        cur += line

seqs.append(cur)

s = seqs[0]
t = seqs[1]

dp = [[""] * (len(t) + 1) for _ in range(len(s) + 1)]

for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + s[i]
        elif len(dp[i][j + 1]) >= len(dp[i + 1][j]):
            dp[i + 1][j + 1] = dp[i][j + 1]
        else:
            dp[i + 1][j + 1] = dp[i + 1][j]

with open("rosalind_lcsq_output.txt", "w") as f:
    f.write(dp[-1][-1])
