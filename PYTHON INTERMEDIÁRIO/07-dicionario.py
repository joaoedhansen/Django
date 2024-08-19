pessoa = {
    'Nome': 'João Eduardo',
    'Sobrenome': 'Nunes Hansen',
    'Idade': '19',
    'Endereços': [
        {'Rua:' 'Roca Sales' 'Número:' '163' 'Bairro:' 'Rondônia'},
        {'Rua:' 'Pedro Adams' 'Número:' '2421' 'Bairro:' 'Ouro Branco'},
    ],
}

# print(pessoa['Nome'])
# print(pessoa['Sobrenome'])

for informacoes in pessoa:
    print(informacoes, pessoa[informacoes])