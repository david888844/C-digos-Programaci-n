# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:07:34 2021

@author: David Alzate
"""

# Factura de pago


# Entrada de datos
ve_nomArt = ""
ve_canArt = 0
ve_valUnitArt = 0.0
vps_netPag = 0.0
vps_totPag = 0.0
vps_ivaPag = 0.0

    # Definición  de variables 
    ve_nomArt = input("Articulos:  ")
    ve_canArt = int((input)("Cantidad:  "))
    ve_valUnitArt = float((input)("Valor Unitario:   "))

    #Proceso
    vps_netPag=ve_canArt * ve_valUnitArt
    vps_ivaPag=vps_netPag * cons_porIva
    vps_totPag=vps_netPag + vps_ivaPag

    # Salidas
    print("Neto:", vps_netPag)
    print("Iva:", vps_ivaPag)
    print("Total:", vps_totPag)

 
