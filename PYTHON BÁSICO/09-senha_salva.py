senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input('Informe sua senha: ')

    repeticoes += 1


print(f'Você digitou a senha {repeticoes}x')