# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:29:29 2021

@author: David Alzate
"""

# Valor compras con IVA y descuento del 5%

def Calcular ():
    precio = float(input("Ingrese el precio de su producto:"))
    iva = precio * 0.19
    print("El valor del IVA del producto es: ", iva)
    ptotal = precio + iva
    print("El precio total es de: $", ptotal)

Calcular()    
    

def Calcular ():
    precio = float(input("Ingrese el precio del producto: "))
    descuento = precio * 0.05
    precio_final = precio - descuento

    print(f"El precio final a pagar es de ${precio_final:.2f}")

Calcular()
