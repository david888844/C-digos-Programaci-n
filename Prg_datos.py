# Ejercicio que almacena en listas -proceso en funciones-
# Declarar las librerias a usar para la solucion

import matplotlib.pyplot as plt

# General las listas con los datos inicializados
nombreProducto=["Aguardiente", "Ron", "Vino", "Cerveza", "Tequila"]
existenciaProducto=[75, 20, 100, 200, 40]

# Funciones que resuelve el problema 
def f_calc_tot_existencias():
    sumaExistencias=0
    for posLis in range (4):
        sumaExistencias=sumaExistencias+existenciaProducto[posLis]
    print("Total Existencias",sumaExistencias)


def f_calc_tot_existencias_2():
    sumaExistencias=0
    for posLis in range (4):
        sumaExistencias=sumaExistencias+existenciaProducto[posLis]
    return(sumaExistencias)
        
# Funcion que calcula el promedio de las existencias
def f_calc_prom_existencias():
    promExistencias=0.0
    promExistencias = f_calc_tot_existencias_2()/len(existenciaProducto)
    return(promExistencias)
    

# Llamado a las funciones que realizan calculos
f_calc_tot_existencias()
print("Total Existencias:",f_calc_tot_existencias_2())
print("Promedio Existencias:",f_calc_prom_existencias())



# Graficar la Informacion
fig, ax = plt.subplots()
# Definir el titulo del grafico
ax.set_title("GRAFICO EXISTENCIAL DE PRODUCTOS")
ax.set_xlabel("Productos")
ax.set_ylabel("Existencias")

# Crear el Grafico
plt.bar(nombreProducto,existenciaProducto)

# Publico el Grafico
plt.show()
