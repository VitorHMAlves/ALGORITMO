nota1 = float(input("Valor da nota 1: "))
nota2 = float(input("valor da nota 2: "))
nota3 = float(input("valor da nota 3: "))
media = (nota1 + nota2 + nota3) / 3

if media < 3:
    resultado = "Reprovado"
else:
    if media < 7:
        resultado = "Exame"
    else:
        resultado = "Aprovado"

print(f"Média {media:5.2f} -{ resultado}!")
