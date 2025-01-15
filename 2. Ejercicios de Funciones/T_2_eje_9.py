import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros del modelo 
proporcion_interaccion = 0.1  
likes_base = 5                

# Definir la función
def numero_likes(seguidores):
    return proporcion_interaccion * seguidores + likes_base

# Generar datos 
seguidores = np.arange(0, 10001, 500)  

# Calcular número de likes
likes = numero_likes(seguidores)

# Graficar
plt.plot(seguidores, likes)
plt.xlabel("Número de seguidores")
plt.ylabel("Número de likes")
plt.title("Número de likes vs. Número de seguidores")
plt.grid(True)
plt.show()

# Mostrar datos en tabla 
data = {'Seguidores': seguidores, 'Likes': likes}
df = pd.DataFrame(data)
print(df)