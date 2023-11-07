def multiplicar(x, y):
    multi = x * y
    return multi
def ehprimo(n):
    for i in range (1, n):
        if n % i == 0:
            return False
    return True
