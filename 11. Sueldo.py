# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:43:18 2021

@author: David Alzate
"""

s=int(input("ingresa sueldo\n"))
if(s>2000):
 d=100+(s-1000)*0.03
 monto=s-d
else:
 if(s>1000 and s<=2000):
  d=100+(s-1000)*0.05
  monto=s-d
 else:
  d=s*0.1
  monto=s-d  
print( "El sueldo percibido es " +
str(monto) + "  y su descuento fue " + str(d))
                   