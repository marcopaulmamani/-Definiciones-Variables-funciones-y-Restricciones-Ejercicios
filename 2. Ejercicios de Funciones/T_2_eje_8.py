import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros del modelo
energia_por_operacion = 0.005 
energia_base = 10            

# Definir la función
def energia_consumida(operaciones):
    return energia_por_operacion * operaciones + energia_base

# Generar datos 
operaciones = np.arange(0, 10001, 500)  

# Calcular energía consumida
energia = energia_consumida(operaciones)

# Graficar
plt.plot(operaciones, energia)
plt.xlabel("Número de operaciones")
plt.ylabel("Energía consumida (julios)")
plt.title("Energía consumida vs. Número de operaciones")
plt.grid(True)
plt.show()

# Mostrar datos en tabla 
data = {'Operaciones': operaciones, 'Energía (julios)': energia}
df = pd.DataFrame(data)
print(df)