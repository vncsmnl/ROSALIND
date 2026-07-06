## Rosalind: Bioinformatics Stronghold
## Problem: Completing a Tree
## Vinícius Manoel

with open("rosalind_tree.txt") as f:
    lines = f.read().splitlines()

n = int(lines[0])

g = [[] for _ in range(n + 1)]

for line in lines[1:]:
    a, b = map(int, line.split())
    g[a].append(b)
    g[b].append(a)

seen = [False] * (n + 1)
components = 0

for i in range(1, n + 1):
    if not seen[i]:
        components += 1
        stack = [i]
        seen[i] = True

        while stack:
            v = stack.pop()
            for u in g[v]:
                if not seen[u]:
                    seen[u] = True
                    stack.append(u)

print(components - 1)
