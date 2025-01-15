import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros del modelo 
factor_ajuste = 1.2  
desplazamiento = 5   

# Definir la función
def medicion_calibrada(medicion_cruda):
    return factor_ajuste * medicion_cruda + desplazamiento

# Generar datos 
mediciones_crudas = np.arange(0, 51, 5)  

# Calcular mediciones calibradas
mediciones_calibradas = medicion_calibrada(mediciones_crudas)

# Graficar
plt.plot(mediciones_crudas, mediciones_calibradas)
plt.xlabel("Medición en crudo")
plt.ylabel("Medición calibrada")
plt.title("Medición calibrada vs. Medición en crudo")
plt.grid(True)
plt.show()

# Mostrar datos en tabla 
data = {'Crudo': mediciones_crudas, 'Calibrado': mediciones_calibradas}
df = pd.DataFrame(data)
print(df)