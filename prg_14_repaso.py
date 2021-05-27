# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:37:31 2021

@author: David Alzate
"""

"""
Programas que lee el nombre y la nota definitiva de 3 materias 
(basic, fortran y pascal) de N estudiantes.
Condición de salida nombre = ***

"""

# Area de declaración de variables
var_e_nom = "***"
var_e_bas = 0.0
var_e_for = 0.0
var_e_pas = 0.0

var_p_s_conEst = 0

var_p_s_medEst = 0.0

# Leer nombre
var_e_nom = input("Digite nombre del estudiante :")

# Ciclo While
while (var_e_nom != "***"):
# Inicio del ciclo
    var_e_bas = float(input("Definitiva Basic :  "))
    var_e_for = float(input("Definitiva Fortran : "))
    var_e_pas = float(input("Definitiva Pascal  :"))
    
# Proceso que calcula la media del estudiante 
    var_p_s_medEst = (var_e_bas+var_e_for+var_e_pas)/3
    print("La  media de :",var_e_nom,"es",var_p_s_medEst)
    var_e_nom = input("Digite nombre del estudiante :  ")
    var_p_s_conEst  =  var_p_s_conEst+1
#Fin del ciclo
print("Cantidad de Estudiantes : ",var_p_s_conEst)
print("ADIOS. . . . ")



