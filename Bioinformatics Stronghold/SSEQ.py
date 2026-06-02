## Rosalind: Bioinformatics Stronghold
## Problem: Finding a Spliced Motif
## Vinícius Manoel

with open("rosalind_sseq.txt") as f:
    sequences = []
    current = []

    for line in f:
        line = line.strip()

        if line.startswith(">"):
            if current:
                sequences.append("".join(current))
                current = []
        else:
            current.append(line)

    sequences.append("".join(current))

s, t = sequences

i = 0
ans = []

for c in t:
    i = s.index(c, i)
    ans.append(i + 1)
    i += 1

print(*ans)
