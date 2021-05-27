# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:56:02 2021

@author: David Alzate
"""

def f_calcular_sueldo(nombre,costohora,cantidadhoras):
    sueldo=costohora*cantidadhoras
    print(nombre,"trabajo",cantidadhoras,"y cobra un sueldo de",sueldo)


# bloque principal

f_calcular_sueldo("juan",10,120)
f_calcular_sueldo(costohora=12,cantidadhoras=40,nombre="ana")
f_calcular_sueldo(cantidadhoras=90,nombre="luis",costohora=7)
