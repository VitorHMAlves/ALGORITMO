while True:
    x = float(input(f"Entre com a base:"))
    if x > 0:
        break
    print("O valor digitado é inválido!!!")
while True:
    y = float(input(f"Entre com a altura:"))
    if y > 0:
        break
    print("O valor digitado é inválido!!!")
area = (x * y) / 2
print(f" A área do triângulo é {area:5.2f}")
