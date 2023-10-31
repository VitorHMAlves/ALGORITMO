d = {}

for _ in range(5):
    sobrenome = input("Digite seu sobrenome: ")
    idade = int(input("Entre com sua idade: "))
    d[sobrenome] = idade

maior_sobrenome = ''
maior_idade = 0

for chave, valor in d.items():
    if valor > maior_idade:
        maior_idade = valor
        maior_sobrenome = chave

print(f'O sobrenome com maior idade é {maior_sobrenome} e com {maior_idade} anos.')