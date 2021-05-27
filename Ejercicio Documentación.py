# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:27:04 2021

@author: David Alzate
"""

print("ingrese 3 numeros enteros diferenetes; ") #Se da entender la información que el usuario se necesita.
e = int(input("elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor")) #Primera variable donde 1 es para elegir mayor o menor y 2 para elegir menor a mayor.
a = int(input("ingrese el numero a:")) #Segunda variable dice que ingrese un número a.
b = int(input("ingrese el numero b: ")) #Tercera variable dice que ingrese un número b.
c = int(input("ingrese el numero c: ")) #Cuarta variable dice que ingrese un número c.

if (e == 1): #La primera condición dice que e es igual a 1.
    if (a > b): #Si a es mayor a b para que la condición se ejecuta.
        if (a > c): # Si a es mayor a c para que la condición se ejecuta.
            if(b > c): #Si b es mayor a c para que la condición se ejecuta.
               print(a, b, c) #Si las condiciones anteriores cumple entonces deberá imprimir los valores de la variable (a,b,c).
            else: #Si las condiciones no se cumple 
               print(a, c, b) #El programa deberia imprimir los valores de la variable (a,c,b).
    if (c > a): #Si c es mayor a a.
        if (c > b): #Si c es mayor a b.
            if(b > a):#Si b es mayor a a.
               print(c, b, a) # Si las condiciones anteriores se cumple entonces deberá imprimir los valores de la variable (c,b,a).
            else: #Las condicones no se cumplen.
               print(c, a, b) #El programa deberia imprimir los valores de la variable (a,c,b).
    if (b > a): #Si b es mayor a a.
        if (b > c): #Si b es mayor a c.
            if(a > c): #Si a es mayor a c.
               print(b, a, c) ##Si las condiciones anteriores cumple entonces deberá imprimir los valores de la variable (b,a,c).
            else: #Las condicones no se cumplen
               print(b, c, a) #Si las condiciones anteriores cumple entonces deberá imprimir los valores de la variable (b,a,c).


if (e == 2): #La segunda condición e es igual a 2.
    if (a < b): #Si a es menor a b.
        if (a < c): #Si a es menor a c.
            if(b < c): #Si b es menor a c.
               print(a, b, c) #Si las condiciones anteriores cumple entonces deberá imprimir los valores de la variable (a,b,c).
            else: #Las condiciones no se cumplen.
               print(a, c, b) ##Si las condiciones anteriores cumple entonces deberá imprimir los valores de la variable (a,b,c).
    if (c < a): #Si c es menor a a.
        if (c < b): #Si c es menor a b.
            if(b < a): #Si b es menor a a.
               print(c, b, a) ##Si las condiciones anteriores cumple entonces deberá imprimir los valores de la variable (c,b,a).
            else: #Si las condiciones no se cumplen.
               print(c, a, b) ##Si las condiciones anteriores cumple entonces deberá imprimir los valores de la variable (c,b,a).
    if (b < a): #Si b es menor a a.
        if (b < c): #Si b es menor a c.
            if(a < c): #Si a es menor a c.
               print(b, a, c) #Si las condiciones anteriores cumple entonces deberá imprimir los valores de la variable (b,a,c).
            else: #Si las condiciones no se cumplen
               print(b, c, a) #Si las condiciones anteriores cumple entonces deberá imprimir los valores de la variable (b,a,c).

if (a == b): #La tercera condicón a es igual a b.
    print("b y a son iguales") #Si la condicón se cumple se deberá imprimir el programa b y a son iguales.
    if (a == c): #La cuarta condición a es igual a c.
        print("a y c son iguales") ##Si la condicón se cumple se deberá imprimir el programa a y c son iguales.
        if(b == c): #La quinta condición b es igual a c.
           print(" b y c con iguales") #Si la condicón se cumple se deberá imprimir el programa b y c son iguales.
           if(a == b == c): #La sexta condición a es igual a,b es igual a c.
              print("todos son iguales") # #Si la condicón se cumple se deberá imprimir el programa "Todos son iguales".