# Primeiros Exemplos

print('primeiro programa')

1 + 2 + 3
4 + 5 + 6

print(1 + 2 + 3)
print(4 + 5 + 6)

help(print)

# Tipos Básicos

print(True)
print(False)
print(1.2 + 1)
print(' Aqui eu falo minha língua!')
print(" Também funciona")
print(' Você é ' + 3 * 'muito ' + 'legal')
# print(3 + 'a') -> ambiguidade
print([1, 2, 3])
print({'nome': 'pedro', 'idade': 22})

#Variáveis
a = 10
b = 5.2

print(a + b)

a = 'Agora sou uma string'
print(a)
a
b

#Comentários


"""
A ideia é calcular o quanto
vai sobrar no 
final do mês!
"""


print('Fim')
print('Fim de verdade') # comentário aqui também vale

#Fim

#Operadores aritméticos
print(2 + 3)
print( 4 - 7)
print(2 * 5.3)
print(9.4 / 3)
print(9.4 // 3)
print(2 ** 8)
print( 10 % 3)

a = 12
b = a
print(a + b)

#Minhas variáveis
salario = 3450.45
despesas = 2456.2

# Resposta do desafio
percentual_comprometido = despesas / salario * 100
print(percentual_comprometido)

#Operadores Relacionais
3 > 4
4 >= 3
1 < 2
3 <= 1
3 != 2
3 == 3
2 == '2'

#Operadores de Atribuição
a = 3
a = a + 7
print(a)

# a = 5
a += 5 # a + 5
print(a)

a -= 3
print(a)

a *= 2
print(a)


a /= 4
print(a)

a %= 4
print(a)

a **= 8
print(a)

a //= 256
print(a)

# Operadores Lógicos
True or False
7 != 3 and 2 > 3

#Tabela verdade do AND
True and True # True
True and False #False
False and True #True
False and False #False

# Tabela verdade do OR
True or True #True
True or False #True
False or True #True
False or False #False

# Tabela verdade do XOR
True != True #False
True != False #True
False != True #True
False != False #False

# Operador de Negação (unário)
not True #False
not False #True

not 0 #True
not 1 #False
not not -1 #True
not not True #True

# Cuidado!
True & False
False | True
True ^ False

# AND Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 10
3 & 2


# OR Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 10
3 | 2

# XOR Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 01
3 ^ 2

# Um pouco de realidade
saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo > 0 and salario
despesas_controladas = despesas >= 0.2 * salario
meta =  saldo_positivo and despesas_controladas

# Desafio Operadores Lógicos

# Os Trabalhos
trabalho_terca = True
trabalho_quinta = False

"""
- Confirmando os 2 trabalhos: TV 50' + Sorvete
- Confirmando apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_quinta != trabalho_quinta #xor
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Saudável={}".format(tv_50, tv_32, sorvete, mais_saudavel))

# "{1}, {2} = {0}".format(1, False, 'resultado')

#Operadores Unários
a = 3
# a++ inválido
a += 1
# a-- inválido
a = -a

not 0
not 1
not -2
not False
not not True

#Operadores Ternários

esta_chovendo = True
'Hoje estou com as roupas' + ('secas.', 'molhadas.')[esta_chovendo]

'Hoje estou com as roupas ' + ('molhadas.' if esta_chovendo else 'secas')

#Mais Operadores | (Operador de Membro) |
lista = [1, 2, 3, 'Ana', 'Carla']
2 in lista
'Ana' not in lista

# | Operador de Identidade |
x = 3
y = x
z = 3
x is y
y is z
x is not z

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

lista_a is lista_b
lista_b is lista_c
lista_a is not lista_c