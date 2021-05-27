# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:18:06 2021

@author: David Alzate
"""

def mostrar_perimetro(lado):
    per=lado*4
    print("El perimetro es",per)


def mostrar_superficie(lado):
    sup=lado*lado
    print("La superficie es",sup)


def cargar_dato():
    la=int(input("Ingrese el valor del lado de un cuadrado:"))
    respuesta=input("Quiere calcular el perimetro o la superficie[ingresar texto: perimetro/superficie]?")
    if respuesta=="perimetro":
        mostrar_perimetro(la)
    if respuesta=="superficie":
        mostrar_superficie(la)


# programa principal

cargar_dato()