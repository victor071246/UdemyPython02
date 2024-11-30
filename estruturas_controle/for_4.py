# for i in range(1, 10):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim!')

# Crie uma função que vai sortear um dado com números entre 1 e 6
# Em seguida crie um For que percorra de 1 a 6 com o range
# Exclua os números ímpares
# Se o número for par e for igual ao valor sorteado pela função dado, imprima a string 'ACERTOU' e depois chamar o break
# Se não acertar, chame o else... print('Não acertou o número!

from random import randint

def sortear_dado():
    return randint(1, 6)

for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortear_dado() == i:
        print('ACERTOU', i)
        break
else:
    print('Não acertou o número')