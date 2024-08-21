produtos = [
    {'produto': 'p1', "preco": 10},
    {'produto': 'p2', "preco": 20},
    {'produto': 'p3', "preco": 30},
]
print(*produtos, sep='\n')
print('\n')

atualiza_produto = [ #atualizar lista produtos
    {**produto, 'preco': produto['preco'] * 1.05} #aumento de 0,5%
    if produto['preco'] > 20 else {**produto} #apenas aumenrae se o preco foi + 20
    for produto in produtos
]

print(*atualiza_produto, sep='\n')