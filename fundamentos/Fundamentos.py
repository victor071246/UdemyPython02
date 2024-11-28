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

#Builtins
type(1)
__builtins__.type('Fala Galera!')
__builtins__.print(10/3)
# __builtins__.help(__builtins__.dir)

#a = 7
# import math
# dir()
# dir(__builtins__)

nome = 'João da Silva'
type(nome)
__builtins__.len(nome)

dir()


#Conversão de tipos
2 + 3
'2' + '3'
# 2 + '3'
# print(2 + '3')

a = 2
b = '3'

print(type(a))
print(type(b))

print(a + int(b))
print(str(a) + b)

type(str(a))

# print(2 + int('2 legal')) da erro [quem diria :o]

# Coerção automática
10 / 2 # Gera float
type(10 / 2)
10 / 3
10 // 3
type(10 // 3) # retorna int
type(10 // 3.3) # retorna float
type(10 / 2.5) # retorna float
2 + True # retorna 3
2 + False # retorna 2
type(1 + 2) # int
type(1 + 2.5) # float


# Tipos Numéricos
dir(int)
dir(float)


a = 5
b = 2.5
a / b
a + b
a * b

type(a)
type(a - b)

b.is_integer()
5.0.is_integer()

dir(int)
int.__add__(2, 3)
2 + 3

(-2).__abs__
abs(-2)
(-3.6).__abs__()
dir(float)
abs(-3.6)

#1.1 + 2.2
from decimal import Decimal, getcontext

Decimal(1) / Decimal(7)

getcontext().prec = 4
Decimal(1) / Decimal(7)
Decimal.max(Decimal(1), Decimal(7))
dir(Decimal)

1.1 + 2.2
getcontext().prec = 10
Decimal(1.1) / Decimal(2.2)

dir(Decimal)

import decimal
dir(decimal)

#_________________#
#Tipo String
#_________________#
dir(str)
nome = 'Saulo Pedro'
nome
nome[0]
# nome[0] = 'P'

# 'marca d'água'
"Dias D'Avila" == 'Dias D\'Avila'
"Teste \" funciona!"
texto = 'Texto entre apostrófos pode ter "aspas"'
texto 

doc = """Texto com múltiplas
    ... linhas"""
doc
print('Texto com múltiplas\n\t... linhas')
print(doc)

doc2 = '''Também é possível
... com 3 aspas simples'''

nome = 'Ana Paula'
nome[0]
nome[6]
nome[-3]
nome[4]
nome[-5:]
nome[:3] # índice final não é considerado
nome[2:5]

numeros = '1234567890'
numeros
numeros[::]
numeros[::2]
numeros[1::2]
numeros[::-1]
numeros[::-2]

nome[::-1]

frase = 'Python é uma linguagem excelente'
'py' not in frase
'ing' in frase
len(frase)
'py' in frase.lower()
frase = frase.upper()
frase

frase.split()
frase.split('E')

# dir(str)
# help(str.center)

a = '123'
b = ' de Oliveira 4'
a + b
a.__add__(b)
str.__add__(a, b)

dir(str)
len(a)
a.__len__()
'1' in a
a.__contains__('1')


#_________________#
#Listas
#_________________#
lista = []
type(lista)
dir(lista)
# help(list)
len(lista)
lista.append(1)
lista.append(5)
lista.append([1, 2, 3])
lista
len(lista)

nova_lista = [ 1, 5, 'Ana', 'Bia']
nova_lista
nova_lista.remove(5)
nova_lista
nova_lista.remove()
nova_lista

lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
lista.index('Guilherme')
# lista.index(42)
lista[2]
1 in lista
'Rebeca' in lista
'Pedro' not in lista
lista[0]
lista[4]
# lista[5]
lista[-1]
lista[-5]

lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
lista[1:3]
lista[1:-1]
lista[1:]
lista[:-1]
lista[:]
lista[::2]
lista[::-1]
del lista[2]
lista
del lista[1:]
lista

#_________________#
#Tuplas
#_________________#
tupla = tuple()
tupla = ()
type(tupla)
dir(tupla)
# help(tupla)
tupla = ('um')
type(tupla) #é uma string
tupla = ('um',)
type(tupla) #agora sim é uma tupla
tupla[0]
# tupla[0] = 'novo' # não é possível
cores = ('verde', 'amarelo', 'azul', 'azul', 'azul', 'branco')
cores[0]
cores[-1]
cores[1:]

cores.index('amarelo')
cores.count('azul')
len(cores)

#_________________#
#Dicionários
#_________________#

pessoa = {'nome': 'Prof(a).Ana', 'idade':38, 'cursos': ['Inglês', 'Português']}
type(pessoa)
dir(dict)
len(pessoa)

pessoa
pessoa['nome']
pessoa['idade']
pessoa['cursos']
pessoa['cursos'][1]
# pessoa['tags'] #não é possível acessar algo que não existe
pessoa.keys()
pessoa.values()
pessoa.items()
pessoa.get('idade')
pessoa.get('tags') # não retornada nada mas não dá erro

pessoa.get('tags', []) # retorna [] caso o primeiro valor não exista, parecido com o ternário

pessoa = {'nome': 'Prof.Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
pessoa
pessoa.pop('idade')

pessoa
pessoa.update({'idade': 40, 'Sexo': 'M'})
pessoa
del pessoa['cursos']
pessoa
pessoa.clear()
pessoa

#_________________#
#Conjuntos | Set
#_________________#
a = {1, 2, 3}
type(a) #set
# a[0] #não aceita índice
a = set('cod3r')
print(a)
print('3' in a, 4 not in a)
(1, 2, 3) == {3, 2, 1 ,3} # True

# operações
c1 = {1, 2}
c2 = {2, 3}
c1.union(c2)
c1.intersection(c2)
c1.update(c2) # essa união gera impacto
c1
c2 <= c1 #("c2 é subconjunto de c1?")
c1 >= c2 #("c2 é superconjnto de c2?")

{1, 2, 3} - {2}
#caso coloque um +, dará um erro
c1 - c2
c1 -= {2}
c1

#_________________#
#Interpolação
#_________________#

from string import Template
nome, idade = 'Ana', 30.9875

# print('Nome: %s Idade: %d' % (nome, idade)) # %d para int
print('Nome: %s Idade: %.2f' % (nome, idade)) # versão mais antiga
print('Nome: {0} Idade: {1}'.format(nome, idade))
print(f'Nome: {nome} Idade: {idade}')

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))