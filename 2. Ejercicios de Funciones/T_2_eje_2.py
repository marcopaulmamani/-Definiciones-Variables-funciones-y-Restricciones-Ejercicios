import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Definir los parámetros
ganancia_prediccion = 50  
ingresos_fijos = 1000 

# Definir la función
def ganancia_mensual(predicciones):
    return ganancia_prediccion * predicciones + ingresos_fijos

# Generar datos (número de predicciones)
predicciones = np.arange(0, 501, 25)
# Calcular ganancias
ganancias = ganancia_mensual(predicciones)

# Graficar
plt.plot(predicciones, ganancias)
plt.xlabel("Número de predicciones")
plt.ylabel("Ganancia mensual")
plt.title("Relación entre predicciones y ganancia mensual")
plt.grid(True)
plt.show()

# Mostrar datos en tabla (opcional)
data = {'Predicciones': predicciones, 'Ganancia': ganancias}
df = pd.DataFrame(data)
print(df)