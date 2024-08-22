import os

lista = []

while True:
    os.system('cls')
    print('0 - Sair')
    print('1 - Adicionar texto')
    print('2 - Adicionar número')
    
    escolha = int(input('Informe o que você deseja: '))

    if escolha == 0:
        os.system('cls')
        print('\n Encerrando o programa...')
        break

        
    elif escolha == 1:
        while True:
            add_texto = input('\n Infore o texto: ')
            lista.append(add_texto)

            continuar_1 = input('\n Deseja continuar? [S/N] ').upper()

            if continuar_1 == 'S':
                continue
            elif continuar_1 == 'N':
                break
         
    elif escolha == 2:
        while True: 
            add_numero = float(input('\n Infore o número: '))
            lista.append(add_numero)

            continuar_2 = input('\n Deseja continuar? [S/N] ').upper()

            if continuar_2 == 'S':
                continue
            elif continuar_2 == 'N':
                break

    else:
        print('\n Oops! Informe um número valido.')

print('\n', lista)
for item in lista:
    print('\n String:', item, isinstance(item, str))
    print('\n Inteiro:', item, isinstance(item, int))
    print('\n Flutuante:', item, isinstance(item, float))


