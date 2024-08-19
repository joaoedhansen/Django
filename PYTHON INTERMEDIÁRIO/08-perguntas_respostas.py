perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': [0, 2, 4, 3, 6],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': [5, 20, 30, 25, 15],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': [5, 20, 25, 30, 15],
        'Resposta': '5',
    },
]

qtd_acertos = 0

for pergunta in perguntas: #pergunta em perguntas
    print('\n Pergunta:', pergunta['Pergunta'])

    opcoes = pergunta['Opções']
    for lista, opcao in enumerate(opcoes): #pergunta em perguntas com numereção (lista e enumerate)
        print(f'{lista})', opcao)

    escolha = input('\n Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    quantidade_opcoes = len(opcoes)

    if escolha.isdigit(): #verificar se é um digito
        escolha_int = int(escolha) #se for digito, converte para inteiro

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < quantidade_opcoes:
            if opcoes[escolha_int] == int(pergunta['Resposta']):
                acertou = True

    if acertou:
        qtd_acertos += 1
        print('\n Acertou')
    else:
        print('\n Errou')
    
    print(f'\n Você acertou {qtd_acertos} de {len(perguntas)} perguntas.')