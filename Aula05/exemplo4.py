dia = int(input("Digite o no. do dia: "))
match dia:
    case 1:
        nome = "domingo"
    case 2:
        nome = "segunda"
    case 3:
        nome = "terça"
    case 4:
        nome = "quarta"
    case 5:
        nome = "quinta"
    case 6:
        nome = "sexta"
    case 7:
        nome = "sabado"
    case _:
        nome = f"valor {dia} inválido"
print(nome)
