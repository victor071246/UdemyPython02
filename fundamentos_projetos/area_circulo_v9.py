# -*- coding: utf-8 -*-
# import math
from math import pi

def area_circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area_calculada = area_circulo(raio)
    print('àrea do círculo: ', area_calculada)