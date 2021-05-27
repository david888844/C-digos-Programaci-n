# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:41:11 2021

@author: David Alzate
"""

print("Convertidor de temperaturas.")

GC = float(input("Ingrese la temperatura en grados Celsius: "))

GF = (GC * 9/5) +32

GK = GC + 273.15

print("{} grados Celsius son {} grados Farenheit".format(GC,GF))
print("{} gradois Celsius son {} grados Kelvin".format (GC, GK))