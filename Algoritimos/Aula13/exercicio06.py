def conversao(h, m, s):
    segundos= (h*3600) + (m*60) + s
    return segundos
hora = int(input("digite a hora: "))
min = int(input("digite o minuto: "))
seg = int(input("digite o segundo: "))
valor = conversao(hora, min, seg)

print(f"A soma de hora:{hora}, minuto:{min} e segundo:{seg} correspondem a {valor} segundos")
