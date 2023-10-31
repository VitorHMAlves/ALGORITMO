d = {}

for _ in range(5):
    nome = input("Digite seu nome: ")
    idade = int(input("Entre com sua idade: "))
    d[nome] = idade

# Calcula média das idades
idades = list(d.values())
media_idade = sum(idades) / len(idades)
print(f'A média das idades é {media_idade}')

# Percorre o dicionário e encontra mostrando
# O sobrenome com idade maior que a idade média
for chave, valor in nome.items():
    if valor > media_idade:
        print(f'Nome: {chave}')
