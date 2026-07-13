## Rosalind: Bioinformatics Stronghold
## Problem: Reversal Distance
## Vinícius Manoel


with open("rosalind_rear.txt") as f:
    lines = [x.strip() for x in f if x.strip()]

ans = []

goal = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for k in range(0, len(lines), 2):
    a = list(map(int, lines[k].split()))
    b = list(map(int, lines[k + 1].split()))

    pos = {}
    for i in range(10):
        pos[b[i]] = i + 1

    start = tuple(pos[x] for x in a)

    if start == goal:
        ans.append("0")
        continue

    d1 = {start: 0}
    d2 = {goal: 0}

    q1 = [start]
    q2 = [goal]

    h1 = 0
    h2 = 0

    found = False

    while not found:
        if len(q1) - h1 <= len(q2) - h2:
            level = d1[q1[h1]]

            while h1 < len(q1) and d1[q1[h1]] == level and not found:
                cur = q1[h1]
                h1 += 1

                for left in range(10):
                    for right in range(left + 1, 10):
                        nxt = (
                            cur[:left] + cur[left : right + 1][::-1] + cur[right + 1 :]
                        )

                        if nxt in d1:
                            continue

                        d1[nxt] = level + 1

                        if nxt in d2:
                            ans.append(str(d1[nxt] + d2[nxt]))
                            found = True
                            break

                        q1.append(nxt)
                    if found:
                        break

        else:
            level = d2[q2[h2]]

            while h2 < len(q2) and d2[q2[h2]] == level and not found:
                cur = q2[h2]
                h2 += 1

                for left in range(10):
                    for right in range(left + 1, 10):
                        nxt = (
                            cur[:left] + cur[left : right + 1][::-1] + cur[right + 1 :]
                        )

                        if nxt in d2:
                            continue

                        d2[nxt] = level + 1

                        if nxt in d1:
                            ans.append(str(d1[nxt] + d2[nxt]))
                            found = True
                            break

                        q2.append(nxt)
                    if found:
                        break

print(" ".join(ans))
