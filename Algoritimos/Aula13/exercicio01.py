def numpar(numero):
    if (numero % 2) == 0 :
        return True
    else:
        return False

x = int(input("Digite o número inteiro: "))
if numpar(x):
    print("O número é par!!")
else:
    print("O número é impar!!")