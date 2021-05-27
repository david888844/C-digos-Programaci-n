# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:35:21 2021

@author: David Alzate
"""

#Ingeresar calificaciones del primer y segundo bimestre

print("Introduce la primera calificacion:")
calif1=input()
calif2=input ()
calif3=input ()
calif4=input ()
calif5=input ()
calif6=input ()
calif_promedio=input ("Para pasar debe ser:  > 3.0")

calif1_n= int (calif1)
calif2_n= int (calif2)
calif3_n= int (calif3)
calif4_n= int (calif4)
calif5_n= int (calif5)
calif6_n= int (calif6)

suma= calif1_n+calif2_n+calif3_n+calif4_n+calif5_n+calif6_n
promedio= suma/6

print("El promedio de las calificaciones es : %d"%promedio)
input()
