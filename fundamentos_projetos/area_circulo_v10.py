from math import pi
import sys

def area_circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':
    raio = sys.argv[1]  
    area_calculada = area_circulo(raio)
    print('àrea do círculo: ', area_calculada)