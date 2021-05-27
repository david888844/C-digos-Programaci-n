# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:37:31 2021

@author: David Alzate
"""

# Leer una tabla, imprime 1 al 20 y suma los resultados 

# Declarar variables:

tabla = 0
multiplicador = 1
resultado = 0
sumaResultado = 0
conRepCiclo = 1

# Leer el número de la tabla para la cual vamos a realizar las operaciones 
tabla = int(input("Tabla: "))
# Leer el multiplicador
multiplicador = int(input("Multiplicador:  ", ))

# Inicio del Ciclo
for conRepCiclo in range (multiplicador):
    resultado = tabla * conRepCiclo
    sumaResultado = sumaResultado + resultado
    print(tabla," * ", conRepCiclo, "=", resultado)
    #Incrementar la variable que controla el ciclo
    print(" En que vuelta va Juan Diego : ", sumaResultado)
# Se imprime la suma por fuera del ciclo 
print("La suma de los resultados es : ", sumaResultado)
