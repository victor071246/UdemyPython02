from math import pi
import sys

def area_circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("É necessário informar o raio do círculo.")
        print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))
    else:
        raio = sys.argv[1]  
        area_calculada = area_circulo(raio)
        print('àrea do círculo: ', area_calculada)