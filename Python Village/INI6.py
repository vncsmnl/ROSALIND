## Rosalind: Python Village
## Problem: Dictionaries
## Vinícius Manoel


def count_word(s):
    words = s.split(" ")

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Print
    for key, value in word_counts.items():
        print(f"{key} {value}")


# Sample Dataset
with open("rosalind_ini6.txt", "r") as infile:
    dataset = infile.read().strip()
count_word(dataset)
