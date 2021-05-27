# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:40:02 2021

@author: David Alzate
"""

def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li


def imprimir_mayor10(li):
    print("Elementos de la lista mayores a 10")
    for x in range(len(li)):
        if li[x]>10:
            print(li[x])


# bloque principal del programa

lista=carga_lista()
imprimir_mayor10(lista)