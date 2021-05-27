# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:32:37 2021

@author: David Alzate
"""

# área = pi*r^2

# circuferencia = 2*pi*r

from math import pi

r = float(input("Escriba el valor del radio: "))

area = pi * r ** 2

print("El área del círculo es igual a {:.2f}".format(area))

circuferencia = 2 * pi * r

print("La circuferencia del círculo es igual a {:.2f}".format(circuferencia))