import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros
costo_m2 = 1500
costos_fijos = 50000

# Definir la función
def precio_vivienda(area):
    return costo_m2 * area + costos_fijos

# Generar datos (áreas construidas)
areas = np.arange(50, 251, 10)  # Áreas de 50 a 250 m², en incrementos de 10

# Calcular precios
precios = precio_vivienda(areas)

# Graficar
plt.plot(areas, precios)
plt.xlabel("Área construida (m²)")
plt.ylabel("Precio de la vivienda")
plt.title("Relación entre área y precio de vivienda")
plt.grid(True)
plt.show()

# Mostrar los datos en una tabla (opcional)
data = {'Area (m²)': areas, 'Precio': precios}
df = pd.DataFrame(data)
print(df)