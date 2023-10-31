lista1 = []
lista2 = []
for i in range(1, 6):
    lista1.append(int(input(f"Digite o {i}° número da lista 1.: ")))
for i in range(1, 6):
    lista2.append(int(input(f"Digite o {i}° número da lista 2.: ")))

# cria um conjunto da união entre duas listas
conjunto_uniao = set(lista1).union(set(lista2))

# exibe o resultado
print(f"conjunto da união entre as duas listas:")
print(conjunto_uniao)
