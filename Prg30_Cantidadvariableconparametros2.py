# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:15:38 2021

@author: David Alzate
"""

def sumar(v1, v2, v3):
    return v1 + v2 + v3

li=[2, 4, 5]
su=sumar(*li)
print(su)