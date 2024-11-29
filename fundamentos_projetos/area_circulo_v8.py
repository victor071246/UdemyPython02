# -*- coding: utf-8 -*-
# import math
from math import pi

def area_circulo(raio):
    print('Área do círculo', pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area_circulo(raio)