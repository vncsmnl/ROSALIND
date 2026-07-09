## Rosalind: Bioinformatics Stronghold
## Problem: Finding a Shared Spliced Motif
## Vinícius Manoel


with open("rosalind_lcsq.txt") as f:
    s = []
    seq = ""
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            if seq:
                s.append(seq)
                seq = ""
        else:
            seq += line
    s.append(seq)

a, b = s

dp = [[""] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[i + 1][j + 1] = dp[i][j] + a[i]
        elif len(dp[i][j + 1]) >= len(dp[i + 1][j]):
            dp[i + 1][j + 1] = dp[i][j + 1]
        else:
            dp[i + 1][j + 1] = dp[i + 1][j]

with open("rosalind_lcsq_output.txt", "w") as f:
    f.write(dp[-1][-1])
