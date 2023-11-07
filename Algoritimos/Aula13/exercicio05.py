from math import pow,pi
def volume (r):
    v = (4* pi * pow(r, 3)) / 3
    return v

r = float(input("Digite o raio: "))
valor = volume(r)
print(f"O volume da esfera é{valor: .2f} m³")
