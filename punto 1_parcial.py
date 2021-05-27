# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:09:30 2021

@author: David Alzate
"""

import math

def CalculaValores(Lado):
    raiz_82202113066=math.sqrt(3)
    #calculo de la raiz de 3
    area_82202113066=(pow(Lado,2)*raiz_82202113066)/4
    # calculo del area
    perimetro_82202113066=(Lado*3)
    # calculo del perimetro
    print("El area es :" ,area_82202113066,"El perimetro es:",perimetro_82202113066)
    # mostrado de informacion

print("Teniendo en cuenta que un triangulo equilatero todos sus lados son iguales")
# mensaje de enunciado
Lado_82202113066=int(input("Para hallar el area y perimetro . Ingrese el valor de uno de los dalos del triangulo : "))
# ingreso del valor del el lado
CalculaValores(Lado_82202113066)
# llamado de la funcion y enviado de lado como parametro