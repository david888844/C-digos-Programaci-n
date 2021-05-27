# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:29:15 2021

@author: David Alzate
"""

def largo(cadena):
    return len(cadena)


# bloque principal

nombre1=input("Ingrese primer nombre:")
nombre2=input("Ingrese segundo nombre:")
la1=largo(nombre1)
la2=largo(nombre2)
if la1==la2:
    print("Los nombres:",nombre1,nombre2,"tienen la misma cantidad de caracteres")
else:
    if la1>la2:
        print(nombre1,"es mas largo")
    else:
        print(nombre2,"es mas largo")