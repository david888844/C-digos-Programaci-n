# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:39:53 2021

@author: David Alzate
"""

# 23 Programación Estructurada ejercicio 112

def f_presentacion():
    print("Programa que permite cargar dos valores por teclado.")
    print("Efectua la suma de los valores")
    print("Muestra el resultado de la suma")
    print("*******************************")


def f_carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


def f_finalizacion():
    print("*******************************")    
    print("Gracias por utilizar este programa")


# programa principal

f_presentacion()
f_carga_suma()
f_finalizacion()
    

