# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:54:29 2021

@author: David Alzate
"""

# Programa que lee N números enteros y calcula su promedio con
#un número menor a cero

# Declarar variables 

num = 0 # Variable que almacena los números que digita el usuario
suma = 0 # Variable que almacena la suma de los números positivos 
med = 0 # Variable que almacena la media
canEle = 0 # Variable que almacena la cantidad de números digitados

num = int(input(" Número :")) # Lectura del primer número 

while (num > 0):  # Inicio delo ciclo
    suma = suma + num 
    num = int(input(" Número : ")) # Lectura de los otros números 
    canEle = canEle + 1
    
# Termina el ciclo
if canEle != 0: 
    med = suma/canEle # Calcular la media 
    print("La media es: ", med) # Imprimir la media
else:
    print  ("No hay número para calculaer la media")
    




