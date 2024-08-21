pessoa = {
    'nome': 'João',
    'sobrenome': 'Nunes'
    }

a, b = pessoa.values()
print(a, b, '\n')


dados_pessoa = {
    'idade': 19,
    'altura': 1.75
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

#empacotamento
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='Joana', qlq=123)