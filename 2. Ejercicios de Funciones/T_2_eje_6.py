import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros del modelo 
tiempo_incremental = 0.01  
tiempo_base = 0.05       

# Definir la función
def tiempo_respuesta(solicitudes):
    return tiempo_incremental * solicitudes + tiempo_base

# Generar datos 
solicitudes = np.arange(1, 101, 5)  

# Calcular tiempos de respuesta
tiempos_respuesta = tiempo_respuesta(solicitudes)

# Graficar
plt.plot(solicitudes, tiempos_respuesta)
plt.xlabel("Número de solicitudes simultáneas")
plt.ylabel("Tiempo de respuesta promedio (segundos)")
plt.title("Tiempo de respuesta vs. Número de solicitudes")
plt.grid(True)
plt.show()

# Mostrar datos en tabla 
data = {'Solicitudes': solicitudes, 'Tiempo (seg)': tiempos_respuesta}
df = pd.DataFrame(data)
print(df)