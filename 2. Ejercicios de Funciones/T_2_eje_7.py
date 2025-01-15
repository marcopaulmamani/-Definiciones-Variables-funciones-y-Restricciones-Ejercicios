import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros del modelo 
ingreso_promedio = 10  
ingresos_adicionales = 500 

# Definir la función
def ingresos_plataforma(suscriptores):
    return ingreso_promedio * suscriptores + ingresos_adicionales

# Generar datos 
suscriptores = np.arange(0, 1001, 100)

# Calcular ingresos
ingresos = ingresos_plataforma(suscriptores)

# Graficar
plt.plot(suscriptores, ingresos)
plt.xlabel("Número de suscriptores")
plt.ylabel("Ingresos")
plt.title("Ingresos de la plataforma vs. Número de suscriptores")
plt.grid(True)
plt.show()

# Mostrar datos en tabla 
data = {'Suscriptores': suscriptores, 'Ingresos': ingresos}
df = pd.DataFrame(data)
print(df)