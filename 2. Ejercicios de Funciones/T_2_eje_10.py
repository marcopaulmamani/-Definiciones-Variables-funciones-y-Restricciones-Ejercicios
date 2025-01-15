import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros del modelo 
costo_por_iteracion = 0.02 
costos_iniciales = 5       

# Definir la función
def costo_entrenamiento(iteraciones):
    return costo_por_iteracion * iteraciones + costos_iniciales

# Generar datos 
iteraciones = np.arange(0, 10001, 500)  

# Calcular costo total
costos = costo_entrenamiento(iteraciones)

# Graficar
plt.plot(iteraciones, costos)
plt.xlabel("Número de iteraciones")
plt.ylabel("Costo total")
plt.title("Costo de entrenamiento vs. Número de iteraciones")
plt.grid(True)
plt.show()

# Mostrar datos en tabla 
data = {'Iteraciones': iteraciones, 'Costo': costos}
df = pd.DataFrame(data)
print(df)