largura = float(input('Digite a largura da parede: '))
comprimento = float(input('Digite o comprimento parede: '))
tipo = int(input('Para Lata digite 1, para Galão digite 2 e para Litro digite 3: '))
porta = 1.68

tinta = (largura * comprimento) * 4 - porta
if tipo == 1:
    vf1 = tinta / 48
    print(f'Você vai precisar de {vf1:0.0f} Lata(s) ')
elif tipo == 2:
    vf2 = tinta / 10.8
    print(f'Você vai precisar de {vf2:0.0f} Galão(oes)')
elif tipo == 3:
    vf3 = tinta / 3
    print(f'Você vai precisar de {vf3:0.0f} Litro(s) ')
