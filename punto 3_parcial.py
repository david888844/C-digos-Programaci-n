# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:07:53 2021

@author: David Alzate
"""

empleados=int(input("Ingrese la cantidad de empleados con los que desea trabajar : "))
# solicitud de los empleados
x=0
AcumulorHoras=0
AcumulorHorasExtras=0
AcumulorSalariosEmpleados=0
AcumulorPagoHorasExtras=0
# acumuladores para los datos generales
AHS1=0
AHES1=0
ASES1=0
ACHES1=0
# acumuladores para los datos generales de la seccion 1
AHS2=0
AHES2=0
ASES2=0
ACHES2=0
# acumuladores para los datos generales de la seccion 2
AHS3=0
AHES3=0
ASES3=0
ACHES3=0
# acumuladores para los datos generales de la seccion 3
AHSGM=0
AHESGM=0
ASESGM=0
ACHESGM=0
# acumuladores para los datos generales para el genermo masculino
AHSGF=0
AHESGF=0
ASESGF=0
ACHESGF=0
# acumuladores para los datos generales para el genermo femenino
while(x<empleados):
    HorasExtras=0
    ValorHorasExtras=0
    #inicializacion de variables
    nombre=input("Ingrese el nombre del empleado : ")
    # cargado de nombre
    HorasTra=int(input("Ingrese la cantidad de horas trabajadas : "))
    # cargado de las horas trabajadas
    ValorHorasTra=int(input("Ingrese el valor a pagar por hora trabajada : "))
    # cargado del precio por hora trabajda
    Genero=input("Ingrese el geneo del empleado M o F: ")
    # cargado del genero
    GeneroCon=Genero.lower()
    # convercion del genero a misnuscula
    Seccion=int(input("Ingrese la Sección donde trabaja 1 , 2 o 3 : "))
    # cargado de la seccion
    if(HorasTra<=35):
        SalarioEmpleado=HorasTra*ValorHorasTra
        # calculo del salario sin horas extra
    else:
        SalarioEmpleado = ( 35 * ValorHorasTra ) + ( HorasTra -35) * 1.5 * ValorHorasTra
        # calculo del salario con horas extra
        HorasExtras=HorasTra-35
        # calculo de horas extra
        ValorHorasExtras= ( HorasTra -35) * 1.5 * ValorHorasTra
        # calculo del valor de las horas extra
    Salud=SalarioEmpleado*0.125
    # calculo del valor de la salud
    ICBF=SalarioEmpleado*0.04
    # calculo del ICBF
    RTF=0;
    if(SalarioEmpleado>=2000000 and SalarioEmpleado<=3000000):
        RTF=SalarioEmpleado*0.05
    elif(SalarioEmpleado<=4000000):
        RTF=SalarioEmpleado*0.07
    elif(SalarioEmpleado<=5000000):
        RTF=SalarioEmpleado*0.09
    else:
        RTF=SalarioEmpleado*0.11
    # calculo de la rentencion en la fuente
    DescuentoTotal=Salud+ICBF+RTF
    # calculo del descuento total
    SalarioFinal=(SalarioEmpleado-DescuentoTotal)
    # calculo del salario final
    print(" Nombre :" ,nombre)
    print(" Genero :" ,Genero)
    print(" Sección :" ,Seccion)
    print(" Salario Final :" ,SalarioFinal)
    # mostrado de informacion induvidual por empleado
    AcumulorHoras=AcumulorHoras+HorasTra
    AcumulorHorasExtras=AcumulorHorasExtras+HorasExtras
    AcumulorSalariosEmpleados=AcumulorSalariosEmpleados+SalarioEmpleado
    AcumulorPagoHorasExtras=AcumulorPagoHorasExtras+ValorHorasExtras
    # mostacumuladores totales
        
    if(Seccion==1):
        AHS1=AHS1+HorasTra
        AHES1=AHES1+HorasExtras
        ASES1=ASES1+SalarioEmpleado
        ACHES1=ACHES1+ValorHorasExtras
    elif(Seccion==2):
        AHS2=AHS2+HorasTra
        AHES2=AHES2+HorasExtras
        ASES2=ASES2+SalarioEmpleado
        ACHES2=ACHES2+ValorHorasExtras
    elif(Seccion==3):
        AHS3=AHS3+HorasTra
        AHES3=AHES3+HorasExtras
        ASES3=ASES2+SalarioEmpleado
        ACHES3=ACHES3+ValorHorasExtras
    # acumuladores por seccion
    
    if(Genero == "m"):
        AHSGM=AHSGM+HorasTra
        AHESGM=AHESGM+HorasExtras
        ASESGM=ASESGM+SalarioEmpleado
        ACHESGM=ACHESGM+ValorHorasExtras
    elif(Genero == "f"):
        AHSGF=AHSGF+HorasTra
        AHESGF=AHESGF+HorasExtras
        ASESGF=ASESGF+SalarioEmpleado
        ACHESGF=ACHESGF+ValorHorasExtras
        # acumuladores por genero
    x=x+1
print("Total de empleados :",empleados,",",
      "Total de Horas :",AcumulorHoras,",",
      "Total de Horas Extra :",AcumulorHorasExtras,",",
      "Total de Salarios :", AcumulorSalariosEmpleados,",",
      "Total de pagos por horas extras" , AcumulorPagoHorasExtras)
    # mostrado de acumuladores generales
print("Sección 1:")
print("Total de Horas :",AHS1,",",
      "Total de Horas Extra :",AHES1,",",
      "Total de Salarios :", ASES1,",",
      "Total de pagos por horas extras" , ACHES1)
    # mostrado de acumuladores de empleados de la seccion 1
print("Sección 2:")
print("Total de Horas :",AHS2,",",",",
      "Total de Horas Extra :",AHES2,",",",",
      "Total de Salarios :", ASES3,",",",",
      "Total de pagos por horas extras" , ACHES2)
    # mostrado de acumuladores de empleados de la seccion 2
print("Sección 3:")
print("Total de Horas :",AHS3,",",
      "Total de Horas Extra :",AHES3,",",
      "Total de Salarios :", ASES2,",",
      "Total de pagos por horas extras" , ACHES3)
    # mostrado de acumuladores de empleados de la seccion 3
print("Genero Maculino:")
print("Total de Horas :",AHSGM,",",
      "Total de Horas Extra :",AHESGM,",",
      "Total de Salarios :", ASESGM, ",",
      "Total de pagos por horas extras" , ACHESGM)
    # mostrado de acumuladores de empleados de genero masculino
print("Genero Femenino:")
print("Total de Horas :",AHSGF,",",
      "Total de Horas Extra :",AHESGF,",",
      "Total de Salarios :", ASESGF, ",",
      "Total de pagos por horas extras" , ACHESGF)
    # mostrado de acumuladores de empleados de genero femenino