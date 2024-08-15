#Lista de mercado

import os

lista_compras = [] #lista de compras vazia para poder editar

while True:
    try:
        print('-' * 20)
        print('| Lista de compras |')
        print('-' * 20)
        print('1 - Incluir')
        print('2 - Visualizar')
        print('3 - Apagar')
        print('0 - Sair')
        print('-' * 20)

        opcao_escolhida = int(input('\nDigite a opção desejada:  '))

        if opcao_escolhida == 0: #sair do programa
                os.system('cls')

                print('\n Fechando o programa...')
                break
            
        while True:

            if opcao_escolhida == 1: #adicionar item
                os.system('cls')
                incluir_compra = input('\nPara incluir, escreva aqui:  ')
                lista_compras.append(incluir_compra) #adicionar compra na lista

                menu = input('\nPossui mais alguma compra: [S/N] ').upper() #voltar ao menu
                if menu == 'S':
                    continue

                else:
                    print('\nVoltando ao menu...')
                    break

            elif opcao_escolhida == 2: #visualizar lista
                os.system('cls')

                for id, item in enumerate(lista_compras): 
                    print(id, item)
                
                menu = input('\n Para voltar ao menu, digite [S] ').upper() #voltar ao menu
                if menu == 'S':
                        break
                
                else:
                    print('Oops, tente novamente!')
                        
            elif opcao_escolhida == 3: #realizar exclusão de um item da lista
                os.system('cls')

                informe_id = int(input('\n informe o número do item que deseja excluir: '))
                lista_compras.pop(informe_id) #remover item da lista

                menu = input('\n Possui mais alguma exclusão? [S/N] ').upper() #voltar ao menu
                if menu == 'S':
                    continue

                else:
                    print('\n Voltando ao menu...')
                    break
            
            else: 
                 print('Oops! Escolha uma opção valida.')
                 break
    except ValueError:
        print('\n Oops! Digite um valor valido.')