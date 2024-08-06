#faça um programa que peça ao usuário que peça o primeiro nome do usuário.
#Então, primeiro o nome do usuário.
#Se o nome tiver quatro letras ou menos, escreva Seu nome é curto.
#Se o nome tiver entre 5 e 6 letras, escreva seu nome normal e se o nome tiver mais do que seis letras,
#digite Seu nome é muito grande.

try:
    nome = input('Escreva seu primeiro nome: ')

    comprimento = len(nome) #ler cuprimento do nome

    if 1 == comprimento <= 4:
        print('Seu nome é curto')

    elif 5 <= comprimento <=6:
        print('Seu nome é normal')

    else:
        print('Seu nome é muito grande!')
except:
    print('Escreva um nome válido!')