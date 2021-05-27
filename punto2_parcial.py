# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:10:20 2021

@author: David Alzate
"""

import math

def CalcularArea(a,b,c,SemiPeri):
    SmenosA=SemiPeri-a
    # calculo del semiperimetro menos a
    SmenosB=SemiPeri-b
    # calculo del semiperimetro menos b
    SmenosC=SemiPeri-c
    # calculo del semiperimetro menos c
    ValorDeRaiz_82202113066_82202114050=SmenosA*SmenosB*SmenosC*SemiPeri
    # calculo de l numero a sacar la raiz
    Area_82202113066_82202114050=math.sqrt(ValorDeRaiz_82202113066_82202114050)
    # calculo de la raiz
    print("El area es :" ,Area_82202113066_82202114050)
    # mostrado de la raiz
    
a_82202113066_82202114050=float(input("Ingrese el valor de A para el triangulo : "))
# cargado de valor a
b_82202113066_82202114050=float(input("Ingrese el valor de B para el triangulo : "))
# cargado de valor b
c_82202113066_82202114050=float(input("Ingrese el valor de C para el triangulo : "))
# cargado de valor c
SemiPeri_82202113066_82202114050=(a_82202113066_82202114050+b_82202113066_82202114050+c_82202113066_82202114050)/2
# calculo de semiperimetro
CalcularArea(a_82202113066_82202114050,b_82202113066_82202114050,c_82202113066_82202114050,SemiPeri_82202113066_82202114050)
# llamado de la funcion y envio de los parametros