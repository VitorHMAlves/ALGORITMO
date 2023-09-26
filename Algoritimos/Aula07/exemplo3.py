soma = 0
idade = int(input("Entre com a quantidade:"))
for i in range(1, idade+1):
    n = int(input(f"Entre com o {i}ª idade:"))
    soma = soma + n
media = soma / idade
print(f"A média das idades é {media:5.2f}")
