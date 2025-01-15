import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros del modelo
tiempo_por_unidad = 0.002 
tiempo_configuracion = 0.1 

# Definir la función
def tiempo_procesamiento(tamaño_datos):
    return tiempo_por_unidad * tamaño_datos + tiempo_configuracion

# Generar datos 
tamaños_datos = np.arange(100, 10001, 500)  

# Calcular tiempos de procesamiento
tiempos = tiempo_procesamiento(tamaños_datos)

# Graficar
plt.plot(tamaños_datos, tiempos)
plt.xlabel("Tamaño de los datos")
plt.ylabel("Tiempo de procesamiento (segundos)")
plt.title("Tiempo de procesamiento vs. Tamaño de datos")
plt.grid(True)
plt.show()

# Mostrar datos en tabla
data = {'Tamaño de datos': tamaños_datos, 'Tiempo (seg)': tiempos}
df = pd.DataFrame(data)
print(df)