# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:52:58 2021

@author: David Alzate
"""

def f_carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


def f_separacion():
    print("*******************************")    


# programa principal

for x in range(5):
    f_carga_suma()
    f_separacion()