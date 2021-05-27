# Lectura de archivos tipo excel 
# Importar librerías
import matplotlib.pyplot as plt
import pandas as pd 

df_archivoExcel = pd.read_excel('Futbol_Partidos.xlsx')#,index_col="Producto")
#archivoExcel = pd.read_excel('Futbol_Partidos.xlsx')
n_goles_local= df_archivoExcel['goles_local']
n_goles_visita= df_archivoExcel['goles_visita']
equipo =df_archivoExcel['local']

#  Función desarrollada por el programador
# 1. Calcular Cantidad de goles de los equipos locales y graficar
def goles_local1():
    Tgoles_local = df_archivoExcel['goles_local'].sum()#  Función propia del lenguaje
    return Tgoles_local
# 2. Calcular Cantidad de goles de los equipos visitantes y graficar
def goles_visita2():
    Tgoles_visita = df_archivoExcel['goles_visita'].sum()#  Función propia del lenguaje
    return Tgoles_visita
# 3. Calcular Cantidad total de goles de todos los partidos y graficar
def tot_goles3():
    def gol_loc():
        tot_gol1=df_archivoExcel['goles_local'].sum()
        return tot_gol1
        def gol_vis():
            tot_gol2=df_archivoExcel['goles_visita'].sum()
            return tot_gol2
            tot_gol=gol_loc()+gol_vis()
            return tot_gol

# 4. Calcular Cantidad de goles de los equipos locales por campeonato y graficar 
   
df=pd.DataFrame(df_archivoExcel)
def goles_local_torneo():
    goles_local_torneo = df.groupby(['torneo'])[['goles_local']].sum()
    return goles_local_torneo

# 5 Calcular Cantidad de goles de los equipos visitantes por campeonato y graficar
def goles_visitantes_torneo():
    goles_visitantes_torneo= df.groupby(['torneo'])[['goles_visita']].sum()
    return goles_visitantes_torneo

# 6 Calcular la cantidad total de goles por campeonato y graficar 
def goles_totales_torneo():
    unificado = df.groupby(['torneo'])[['goles_visita','goles_local']].sum()
    goles_totales_torneo = unificado[['goles_visita','goles_local']].astype(int).sum(axis=1)
    return goles_totales_torneo

#7. Gráfico de barras de cantidad de partidos por selección



print("1. El total de goles de los locales es",(goles_local1()))
print("2. El total de goles de los visitantes es",(goles_visita2()))
print("3. El total de goles marcados en todos los partidos es ",(tot_goles3()))
print("4. El total de goles marcados por equipos locales en torneos son ")
print(goles_local_torneo())
print("5. El total de goles marcados por equipos visitantes en torneos son ")
print(goles_visitantes_torneo())
print('6. El total de goles por campeonato son')
print(goles_totales_torneo())


# Punto 1
fig, df = plt.subplots()
df.set_title("Goles local")
df.set_ylabel("Goles local")
df.set_xlabel(" # de Goles")
#crear el gráfico

plt.barh(df_archivoExcel['local'],df_archivoExcel['goles_local'] )
plt.show()

#Punto 2

fig, df = plt.subplots()
df.set_title("Goles visitante")
df.set_ylabel("Goles visitante")
df.set_xlabel(" # de Goles")

plt.barh(df_archivoExcel['visitante'],df_archivoExcel['goles_visita'])
plt.show()

#Punto 3

fig, df = plt.subplots()
df.set_title("Cantidad de goles de todos los partidos")
df.set_ylabel("Equipo")
df.set_xlabel(" # de Goles")

# tamaño de letra 
plt.bar(['visitantes' , 'local'], [goles_visita2(),goles_local1()] )
plt.rc('xtick', labelsize=12) 
plt.rc('ytick', labelsize=9)
plt.show()

# Punto 4
fig, df = plt.subplots()
df.set_title("Goles locales por torneo")
df.set_ylabel("torneo")
df.set_xlabel(" # de Goles")
#crear el gráfico

plt.barh(df_archivoExcel['torneo'],df_archivoExcel['goles_local'])
plt.show()

# Punto 5
fig, df = plt.subplots()
df.set_title("Goles visitantes por torneo")
df.set_ylabel("torneo")
df.set_xlabel(" # de Goles")
#crear el gráfico

plt.barh(df_archivoExcel['torneo'],df_archivoExcel['goles_visita'])
plt.show()

# punto 6
unificado = pd.DataFrame(df.groupby(['torneo'])[['goles_visita','goles_local']].sum())
unificado.add('asdasd')
goles_totales_torneo = pd.DataFrame(unificado[['goles_visita','goles_local']].astype(int).sum(axis=1))


fig, df = plt.subplots()
df.set_title("Cantidad total de goles por campeonato")
df.set_ylabel("Torneo")
df.set_xlabel(" # de Goles")
#crear el gráfico

plt.barh(goles_totales_torneo[0][0],goles_totales_torneo)

plt.show()

