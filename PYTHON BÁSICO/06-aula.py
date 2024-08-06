while True:

    senha = 12345
    digite_senha = int(input('Digite sua senha: '))

    if digite_senha != senha:
        print('Acesso negado')
        
    else:
        print('Acessado permitido')
        break