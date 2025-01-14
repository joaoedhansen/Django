import copy

#original
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#aumento de 10%
novos_produtos = copy.deepcopy(produtos)
for produto in novos_produtos:
    produto['preco'] *= 1.1 

    #2 casas decimais
    produto['preco'] = round(produto['preco'], 2)

#do maior ao menor nome
produtos_ordenados_por_nomes = copy.deepcopy(novos_produtos)
produtos_ordenados_por_nomes = sorted(produtos_ordenados_por_nomes, key=lambda produto: produto['nome'], reverse=True)

#do menor ao maior preço
produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preco = sorted(produtos_ordenados_por_preco, key=lambda produto: produto['preco'])

print('Original')
print(*produtos, sep='\n')
print('\n')

print('Aumento de 10%')
print(*novos_produtos, sep='\n')
print('\n')

print('Do maior ao menor nome')
print(*produtos_ordenados_por_nomes, sep='\n')
print('\n')

print('Do menor ao maior preço')
print(*produtos_ordenados_por_preco, sep='\n')
print('\n')


