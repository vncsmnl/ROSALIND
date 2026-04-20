## Rosalind: Bioinformatics Stronghold
## Problem: Finding a Protein Motif
## Vinícius Manoel

import re
import requests

with open("rosalind_mprt.txt") as f:
    ids = [line.strip() for line in f]

for uid in ids:
    base = uid.split("_")[0]
    url = f"https://www.uniprot.org/uniprot/{base}.fasta"

    fasta = requests.get(url).text
    seq = "".join(fasta.split("\n")[1:])

    # N{P}[ST]{P} → regex: N[^P][ST][^P]
    matches = [m.start() + 1 for m in re.finditer(r"(?=(N[^P][ST][^P]))", seq)]

    if matches:
        print(uid)
        print(*matches)
