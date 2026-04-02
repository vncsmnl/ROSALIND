## Rosalind: Bioinformatics Stronghold
## Problem: Mendel's First Law
## Vinícius Manoel

k, m, n = map(
    int, input("Enter the number of organisms of each genotype (k m n): ").split()
)

total = k + m + n

# Probability of recessive offspring (aa)

# aa × aa
p_nn = (n / total) * ((n - 1) / (total - 1))

# Aa × aa and aa × Aa (each gives 50% aa)
p_mn = (m / total) * (n / (total - 1)) * 0.5
p_nm = (n / total) * (m / (total - 1)) * 0.5

# Aa × Aa (25% aa)
p_mm = (m / total) * ((m - 1) / (total - 1)) * 0.25

p_recessive = p_nn + p_mn + p_nm + p_mm

# dominant = 1 - recessive
result = 1 - p_recessive

print(round(result, 5))
