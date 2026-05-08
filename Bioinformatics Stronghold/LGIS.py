## Rosalind: Bioinformatics Stronghold
## Problem: Longest Increasing Subsequence
## Vinícius Manoel

from bisect import bisect_left

with open("rosalind_lgis.txt") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))

# LIS
tails = []
tails_idx = []
prev = [-1] * n

for i, x in enumerate(a):
    j = bisect_left(tails, x)

    if j == len(tails):
        tails.append(x)
        tails_idx.append(i)
    else:
        tails[j] = x
        tails_idx[j] = i

    if j:
        prev[i] = tails_idx[j - 1]

i = tails_idx[-1]
lis = []

while i != -1:
    lis.append(a[i])
    i = prev[i]

lis.reverse()

# LDS
tails = []
tails_idx = []
prev = [-1] * n

for i, x in enumerate(a):
    x = -x
    j = bisect_left(tails, x)

    if j == len(tails):
        tails.append(x)
        tails_idx.append(i)
    else:
        tails[j] = x
        tails_idx[j] = i

    if j:
        prev[i] = tails_idx[j - 1]

i = tails_idx[-1]
lds = []

while i != -1:
    lds.append(a[i])
    i = prev[i]

lds.reverse()

with open("rosalind_lgis_output.txt", "w") as output:
    output.write(" ".join(map(str, lis)) + "\n")
    output.write(" ".join(map(str, lds)) + "\n")
