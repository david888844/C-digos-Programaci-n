# Métodos de ordenamientos

# Crear una lista y darle valores

listaBase=[34, 12, 45, 2, 37, 60, 34, 8]

print("lista base: ",listaBase)
# Ordenar la lista con una función de python 
listaBase.sort()
print("lista base ordenada ascendente:",listaBase)

# Ordenar la lista con una función de python 
listaBase.sort(reverse=True)
print("lista base ordenada descendente:",listaBase)

# ============================================================================

# FUNCIÓN DESARROLLADA POR EL PROGRAMADAOR 
# ORDENAMIENTO BURBUJA ASCENDENTE
print("FUNCION DESARROLLADA POR EL PROGRAMADOR")
def ordenamientoBurbujaAscendente(unalista):
    for numPasada in range(len(unalista)-1, 0, -1):
        for i in range(numPasada):
            if unalista [i]>unalista[i+1]:
                temp = unalista[i]
                unalista[i] = unalista[i+1]
                unalista[i+1] = temp
                
unaLista = [54,26,93,17,77,31,44,55,20]
print("Lista Original: ", unaLista)

ordenamientoBurbujaAscendente(unaLista)
print("Lista Ordenada ascendente: ", unaLista) 

# ==============================================================================

# FUNCIÓN DESARROLLADA POR EL PROGRAMADAOR 
# ORDENAMIENTO BURBUJA  DESCENDENTE
print("FUNCION DESARROLLADA POR EL PROGRAMADOR")
def ordenamientoBurbujaDescendente(unalista):
    for numPasada in range(len(unalista)-1, 0, -1):
        for i in range(numPasada):
            if unalista [i]<unalista[i+1]:
                temp = unalista[i]
                unalista[i] = unalista[i+1]
                unalista[i+1] = temp
                
#=====================# FIN DE LA FUNCIÓN#============================00
unaLista = [54,26,93,17,77,31,44,55,20]
print("Lista Original: ", unaLista)
ordenamientoBurbujaDescendente(unaLista)
print("Lista Ordenada descendente: ", unaLista) 

# ==================================================================


