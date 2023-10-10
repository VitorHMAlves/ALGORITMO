lista=[]

for i in range(5):
    lista.append(int(input(f"Digite o número {i + 1}: ")))

'''
maior= sorted(lista, reverse=True)[0]
pos = lista.index(maior)

'''
maior = lista[0]
pos = 0

for i in range(0, len(lista)):
    if lista[i] >= maior:
        maior = lista[i]
        pos = i


print(f"O maior elemento é {maior} no endereço {pos}.")