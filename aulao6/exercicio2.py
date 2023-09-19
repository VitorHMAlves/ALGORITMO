x = float(input("Digite o valor da compra: R$"))

if x <= 1000.00:
    desconto1 = (x * 0.10)
    vf1 = x - desconto1
    print(f"O valor do desconto é de 10%, R${desconto1}, e o valor final do produto é de R${vf1}")
elif x <= 5000.00:
    desconto2 = (x * 0.20)
    vf2 = x - desconto2
    print(f"O valor do desconto é de 20%, R${desconto2}, e o valor final do produto é de R${vf2}")
elif x > 5000.00:
    desconto3 = (x * 0.30)
    vf3 = x - desconto3
    print(f"O valor do desconto é de 30%, R${desconto3}, e o valor final do produto é de R${vf3}")

