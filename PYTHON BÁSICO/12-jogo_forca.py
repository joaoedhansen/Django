import os

def input_limite(mensagem, limite):
    while True:
        digitado = input(mensagem)
        
        if len(digitado) <= limite:
            return digitado
        print(f'Oops! Digite no máximo {limite} caracteres.')


palavra_secreta = 'cristian'
letras_acertadas = ''   
tentativas = 0

while True:
    letra_digitada = input_limite('Digite uma letra: ', 1)
    
    tentativas += 1

    #se letra_digitada estiver em palavra_secreta
    if letra_digitada in palavra_secreta:
        #adicionar letra_digitada em letras_acertadas
        letras_acertadas += letra_digitada

    palavra_formada = '' #para sair na horizontal

    #para letra_secreta em palavra_secreta
    for letra_secreta in palavra_secreta:
        #se letra_secreta estiver em letras_acertadas
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls') 
        print('Você acertou!')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Tentativas: {tentativas}')      
        letras_acertadas = ''   
        tentativas = 0