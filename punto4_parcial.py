# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:10:18 2021

@author: David Alzate
"""

Numeroterminos_82202113066_82202114050 = int(input("Cuantos terminos desea : "))
# numero de terminos que va a conetener la serie
NumeroDeLaSerie_82202113066_82202114050=int(input("termino que desee saber que este e el rango de terminos anteriores: "))
# numero de la serie a mostrar por separado
LimiteInferiror_82202113066_82202114050=int(input("Ingrese el limite Inferiror "))
# limite inferior de los numeros a sumar de la serie
LimiteSuperior_82202113066_82202114050=int(input("Ingrese el limite superior "))
# limite superiror de los numeros a sumar de la serie

n1=0
# declaracion primer variable
n2 =1
# declaracion segunda variable
Acumulador = 0
# acumulador de numeros que llevamos en la serie
Arreglo_82202113066_82202114050=[];
# declaracion del arreglo para llenarlo con la serie

AcumuladorTerminos_82202113066_82202114050=0;
# declaracion deñ acumulador

if Numeroterminos_82202113066_82202114050 <= 0:
    # comparacion si el numero de terminos que solicite si sea un numero valido
   print("Ingrese un numero positivo")
elif Numeroterminos_82202113066_82202114050 == 1:
    # mostrar 0 en caso de que pida solo 1 termino
   print(n1)
else:
   print("Secuencia:")
   while Acumulador < Numeroterminos_82202113066_82202114050:
       # while para llevar la cantidad de numeros que pidio y los que ha dado demomento la serie segun aumente x
       print(n1)
       Arreglo_82202113066_82202114050.append(n1)
       # llenado del arreglo para luego buscarlo por la posicion que el usuario haya ingresado que desee saber
       nMasn = n1 + n2
       # sumado delas variables
       
       n1 = n2
       # obtencion del valor de la variable 1 con el valor que haya quedado en la 2
       n2 = nMasn
       # obtencion del valor de la suma de las variables para la variable 2
       Acumulador =Acumulador+1
       # acumulado de numeros que lleva la serie
       
x=LimiteInferiror_82202113066_82202114050
# declaracion de variable con limite inferiror como valor
while(x<=LimiteSuperior_82202113066_82202114050):
    # generacion de ciclo con los numeros correspondientes entre el limite inferiror y el limite superior
    AcumuladorTerminos_82202113066_82202114050=AcumuladorTerminos_82202113066_82202114050+Arreglo_82202113066_82202114050[x]
    # acumulado de valores de la serie en las posisiciones respectivas entre los valores que van desde el limite inferiro y el superior siendo estos las posiciones a sumar
    x=x+1
    # aumento de 1 en 1 que son las posicionesentre los limites

 
print("Numero de la serie :", Arreglo_82202113066_82202114050[NumeroDeLaSerie_82202113066_82202114050])
# mostrado del numero escogido por el usuario en la serie
print("Acumulado : ",AcumuladorTerminos_82202113066_82202114050)
# mostrado del acumulado entre el limite inferior y el limite superior