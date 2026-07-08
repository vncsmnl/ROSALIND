## Rosalind: Python Village
## Problem: Dictionaries
## Vinícius Manoel


with open("rosalind_ini6.txt") as infile:
    word_counts = {}

    for word in infile.read().split():
        word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.items():
        print(word, count)
