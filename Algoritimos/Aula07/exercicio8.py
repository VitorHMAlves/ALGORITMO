k = int(input(f"Digite o número inteiro:"))
primo = True
n = 0
for i in range(1, k+1):
    if k % i == 0:
        n = n + 1
if n > 2:
    primo = False
if primo:
    print(f"O número {k} é primo!!")
else:
    print(f"O númro {k} não é primo !!!")