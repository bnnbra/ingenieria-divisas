def euro_a_dolar(euros):
    tasa = 1.10
    return euros * tasa

def euro_a_libra(euros):
    tasa = 0.85
    return euros * tasa

print(f"100€ son {euro_a_dolar(100)}$")
print(f"100€ son {euro_a_libra(100)}£")
