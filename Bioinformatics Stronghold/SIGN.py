## Rosalind: Bioinformatics Stronghold
## Problem: Enumerating Oriented Gene Orderings
## Vinícius Manoel

with open("rosalind_sign.txt") as f:
    n = int(f.readline().strip())

perms = []
stack = [([], set())]

while stack:
    perm, used = stack.pop()
    if len(perm) == n:
        perms.append(perm)
        continue
    for x in range(1, n + 1):
        if x not in used:
            stack.append((perm + [x], used | {x}))

result = []

for p in perms:
    for mask in range(1 << n):
        signed = []
        i = 0
        while i < n:
            if mask & (1 << i):
                signed.append(-p[i])
            else:
                signed.append(p[i])
            i += 1
        result.append(signed)

with open("rosalind_sign_output.txt", "w") as f:
    f.write(f"{len(result)}\n")
    for r in result:
        f.write(" ".join(map(str, r)) + "\n")
