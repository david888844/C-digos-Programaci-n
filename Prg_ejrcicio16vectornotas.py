# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:37:08 2021

@author: David Alzate
"""

# Práctica 1 con Arreglos-Vectores

# Almacenar en un vector las 5 notas del parcial

# Declarar el vector 
listaNotas=[]
sumaNotas=0.0

# Asignar valores a la lista con un ciclo 
for posLista in range (5):
    # Leer desde el teclado la nota
    notaEst=float(input("Digite Nota:  "))
    sumaNotas=sumaNotas+notaEst
    # Almacenamos la escalar en arreglo
    listaNotas.append(notaEst)

# Imprimir el arreglo 
print(listaNotas)
print("La suma de las notas es:  ", sumaNotas)

    

