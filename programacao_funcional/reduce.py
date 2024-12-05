from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]
so_idades = map(lambda p: p['idade'], pessoas)
menores = filter(lambda p: p['idade'] < 18, pessoas)

soma_idades = reduce(lambda idades, idade: idades + idade, menores, 0)
print(soma_idades)