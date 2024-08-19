def par_impar():
    if numero % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Ímpar'
    return resultado

numero = int(input('Digite um número: '))
resultado = par_impar()

print(f'O número {numero} é: {resultado}')