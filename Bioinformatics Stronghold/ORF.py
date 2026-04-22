## Rosalind: Bioinformatics Stronghold
## Problem: Open Reading Frames
## Vinícius Manoel

with open("rosalind_orf.txt") as f:
    dna = "".join(line.strip() for line in f if not line.startswith(">"))

codon_table = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": "*",
    "TAG": "*",
    "TGT": "C",
    "TGC": "C",
    "TGA": "*",
    "TGG": "W",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}

comp = str.maketrans("ATCG", "TAGC")
revcomp = dna.translate(comp)[::-1]

seqs = [dna, revcomp]
proteins = set()

for s in seqs:
    for frame in range(3):
        for i in range(frame, len(s) - 2, 3):
            if s[i : i + 3] == "ATG":
                prot = ""
                for j in range(i, len(s) - 2, 3):
                    aa = codon_table[s[j : j + 3]]
                    if aa == "*":
                        proteins.add(prot)
                        break
                    prot += aa

print("\n".join(proteins))
