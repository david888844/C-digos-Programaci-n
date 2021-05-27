# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:33:12 2021

@author: David Alzate
"""

#  Programa que calcula la nota de un estudiante

#  Entradas
#  Pedir el nombre del estudiante y sus 3 notas de parciales

canEst=int(input("Cantidad de Estudiantes : "))
#  Inicializar la variable que controla el ciclo
conRep=0
#  Variable real para sumar las definitivas del grupo
sumDefGru=0.0
# Variable para calcular la nota promedio del grupo
notProDefGru=0.0

while(conRep < canEst):
    #  Instrucciones a repetir
    nomEst=input("Nombre Estudiante : ")
    notUnoEst= float(input("Parcial Uno: "))
    notDosEst= float(input("Parcial Dos: "))
    notTresEst= float(input("Parcial Tres: "))
    
    #  Cálculos
    notDefEst = (notUnoEst+notDosEst+notTresEst)/3
    
    # Acumulo las definitivas del grupo
    sumDefGru=sumDefGru+notDefEst

    #  Imprimir los resultados - Salidas
    print(f"1. La nota definitiva es :{notDefEst:.2f}")
    
    #Incrementar la variable que controla el ciclo
    conRep = conRep+1

# Calcular el promedio del grupo
notProDefGru = sumDefGru/canEst
    
#  Imprimir la nota promedio del grupo
print(f"2. La nota promedio del grupo es :{notProDefGru:.2f}")
