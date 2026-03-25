## Rosalind: Bioinformatics Stronghold
## Problem: Working with Files
## Vinícius Manoel


with open("rosalind_ini5.txt", "r") as infile:
    lines = infile.readlines()

with open("rosalind_ini5_output.txt", "w") as outfile:
    # Iterate over lines with 1-based indexing
    for i, line in enumerate(lines, start=1):
        if i % 2 == 0:  # even-numbered lines
            outfile.write(line)
