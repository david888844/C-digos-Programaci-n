# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:37:00 2021

@author: David Alzate
"""

# Calcular la velocidad

#  Valores a determinar d y t

tf=int(input('¿cuanto tiempo?: '))
d=float(input('¿distancia recorrida?: '))

v=d/tf
vkmh=(v/1000)*60*60

print('Velocidad del vehiculo(Km/h)')
print(vkmh)
