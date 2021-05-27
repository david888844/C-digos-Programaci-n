# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:33:36 2021

@author: David Alzate
"""

# Variables escalares

varEscNum1=10
print (varEscNum1)
varEscNum2=20
print (varEscNum2)
varEscNum100=20
print (varEscNum100)

sumaVariables=varEscNum1+varEscNum2+varEscNum100

# Variables vectoriales - N Datos del mismo tipo de datos
# Aplicación de estrucutra de datos

print("ARREGLO VECTORIAL")
varVectorNum=[10, 20, 30, 12, 35, 10]
print(varVectorNum)

# Funciones de una lista

# Adicionar al final de la lista
varVectorNum.append(2000)
print(varVectorNum)

# Adicionar datos por teclado a la lista

VarVectorNumTecUno=[]
# Adicionar datos por teclado a la lista
for pos in range(3):
    datoTeclado=int(input("Digite Valor: ")) # Escalar
    VarVectorNumTecUno.append(datoTeclado)
print(VarVectorNumTecUno)
varVectorNum.append(3000)
print(varVectorNum)

# Borrar los elementos de la lista
# VarVectorNumTecUno.clear()

# Crear una lista con sus datos
varVectorNumDos=[2, 4, 6, 8, 10]
print(VarVectorNumTecUno)
print(varVectorNumDos)

# Unir dos listas
VarVectorNumTecUno.extend(varVectorNumDos)
print(VarVectorNumTecUno)

# Conocer el tamaño  de la lista

tamVect=len(VarVectorNumTecUno)
print(tamVect)

# Contar las repeticiones de un dato
VarVectorNumTecUno.count((12))

     