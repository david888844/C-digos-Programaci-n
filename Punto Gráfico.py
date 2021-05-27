
import matplotlib.pyplot as plt
import numpy as np

# Datos 
x=np.linspace(2, 4, 8)
y1=np.exp(x)
y2=np.log(x)

# Gráfica
plt.plot(x, y1, label="$e^x$")
plt.plot(x, y2, label="$ln$")
plt.title("Gráfico Funciones")
plt.xlabel("Log")
plt.ylabel("Exp")



# Escala 
plt.yscale("Log")

# Mostrar Gráfico
plt.show()

