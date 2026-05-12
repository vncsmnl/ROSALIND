## Rosalind: Bioinformatics Stronghold
## Problem: Genome Assembly as Shortest Superstring
## Vinícius Manoel

reads = []
with open("rosalind_long.txt", "r") as file:
    seq = []
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if seq:
                reads.append("".join(seq))
                seq = []
        else:
            seq.append(line)
    if seq:
        reads.append("".join(seq))

# Assemble genome
genome = reads.pop(0)

while reads:
    for i, read in enumerate(reads):
        length = len(read)
        merged = False

        for j in range(length, length // 2, -1):
            # suffix-prefix match
            if genome.endswith(read[:j]):
                genome += read[j:]
                reads.pop(i)
                merged = True
                break

            # prefix-suffix match
            if genome.startswith(read[-j:]):
                genome = read[:-j] + genome
                reads.pop(i)
                merged = True
                break

        if merged:
            break

# Write output
with open("rosalind_long_output.txt", "w") as file:
    file.write(genome)
