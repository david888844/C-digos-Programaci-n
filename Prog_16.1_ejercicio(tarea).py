# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:14:46 2021

@author: David Alzate
"""

# Calcular el promedio de notas, y cuales notas son ganadas y perdidas

n1= float(input("Ingrese la nota 1: "))
n2= float(input("Ingrese la nota 2: "))
n3= float(input("Ingrese la nota 3: "))
n4= float(input("Ingrese la nota 4: "))
n5= float(input("Ingrese la nota 5: "))
prom_nota=(n1+n2+n3+n4+n5)/5
if(prom_nota>=3.0):
    print("Su promedio fue: ",prom_nota,"Ganó la materia")
else:
    print("Su promedio fue:  ",prom_nota,"Perdió la materia")