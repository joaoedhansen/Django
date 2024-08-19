def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicar = multiplicacao(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(multiplicar)