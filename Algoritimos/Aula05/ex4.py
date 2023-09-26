x = float(input('Primeiro lado: '))
y = float(input('Segundo  lado: '))
z = float(input('Terceiro lado: '))


if (x+y > z) and (x+z > y) and (y+z > x):
    # É um triângulo
    if x == y == z:
        print('É um triângulo Equilátero')
    elif (x == y) or (x == z) or (y == z):
        print('É um triângulo Isósceles')
    else:
        print('É um triângulo Escaleno')
else:
    #  não é um triângulo
    print('os lados não formam um triângulo')
