## Rosalind: Bioinformatics Stronghold
## Problem: Ordering Strings of Varying Length Lexicographically
## Vinícius Manoel

with open("rosalind_lexv.txt") as f:
    alphabet = f.readline().split()
    n = int(f.readline())

answer = []
stack = [""]

while stack:
    s = stack.pop()

    if s:
        answer.append(s)

    if len(s) < n:
        for c in reversed(alphabet):
            stack.append(s + c)

with open("rosalind_lexv_output.txt", "w") as f:
    f.write("\n".join(answer))
