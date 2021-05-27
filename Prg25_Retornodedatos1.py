# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:25:00 2021

@author: David Alzate
"""

def retornar_superficie(lado):
    sup=lado*lado
    return sup


# bloque principal del programa

va=int(input("Ingrese el valor del lado del cuafrado:"))
superficie=retornar_superficie(va)
print("La superficie del cuadrado es",superficie)