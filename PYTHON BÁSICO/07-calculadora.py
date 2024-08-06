#calculadora whaile

while True:
    
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador [+-/*]: ')

    numeros_validos = None

    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Oops! Número(s) inválido(s)... Tente novamente')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Oops! Operador inválido... Tente novamente')
        continue


    if operador == '+':
       calculo_mais = num_1 + num_2
       print(f'A multiplicação é {calculo_mais}')
    
    elif operador == '-':
        calculo_menos = num_1 - num_2
        print(f'A subtração é {calculo_menos}')

    elif operador == '*':
        calculo_vezes = num_1 * num_2
        print(f'A subtração é {calculo_vezes}')
    
    else:
        calculo_divisão = num_1 / num_2
        print(f'A subtração é {calculo_divisão}')



    sair = input('Deseja sair? [S] Sim ou [N] Não: ').upper()
    if sair == 'S':
      print('Fechando o programa...')
      break
    elif sair == 'N':
        continue
    else:
        print('Opção inválida...')