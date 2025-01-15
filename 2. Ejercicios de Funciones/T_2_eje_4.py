import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros del modelo 
costo_por_gb = 2  
tarifas_fijas = 10  

# Definir la función
def costo_almacenamiento(datos_gb):
    return costo_por_gb * datos_gb + tarifas_fijas

# Generar datos 
datos_gb = np.arange(0, 101, 10) 

# Calcular costos
costos = costo_almacenamiento(datos_gb)

# Graficar
plt.plot(datos_gb, costos)
plt.xlabel("Cantidad de datos (GB)")
plt.ylabel("Costo total")
plt.title("Costo de almacenamiento vs. Cantidad de datos")
plt.grid(True)
plt.show()

# Mostrar datos en tabla 
data = {'Datos (GB)': datos_gb, 'Costo': costos}
df = pd.DataFrame(data)
print(df)