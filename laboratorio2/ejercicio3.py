import pandas as pd
import matplotlib.pyplot as plt

# Datos de Aston Villa
jornadas = list(range(1, 26))  # Simulando 25 jornadas en la temporada
goles_anotados = [4, 3, 2, 1, 3, 0, 2, 1, 3, 2, 2, 3, 1, 2, 3, 4, 0, 1, 2, 3, 1, 2, 3, 1, 2]  # Ejemplo de goles anotados
goles_concedidos = [1, 2, 1, 3, 0, 1, 2, 2, 1, 3, 2, 1, 3, 0, 2, 2, 4, 3, 1, 1, 2, 3, 0, 2, 1]  # Ejemplo de goles concedidos

# Crear la gráfica de líneas
plt.figure(figsize=(10, 6))

# Goles anotados por Aston Villa
plt.plot(jornadas, goles_anotados, marker='o', linestyle='-', color='blue', label='Goles Anotados')



# Etiquetas y leyendas
plt.xlabel('Jornadas')
plt.ylabel('Goles')
plt.title('Evolución de Goles Anotados  por Aston Villa')
plt.xticks(jornadas)
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()
