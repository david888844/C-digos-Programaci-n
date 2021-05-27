# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:59:55 2021

@author: David Alzate
"""

def f_cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def f_imprimir(f_lista):
    for x in range(len(f_lista)):
        print(f_lista[x], end=",")


# bloque principal

f_lista=f_cargar()
f_imprimir(f_lista)