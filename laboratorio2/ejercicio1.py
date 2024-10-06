import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV usando la ruta completa
df = pd.read_csv("C:\\Users\\jorge\\Documents\\GitHub\\Programacion-Computo-2\\laboratorio2\\valorant_agent.csv")

# Contar las ocurrencias de cada rol
role_counts = df['role'].value_counts()

colors = ['skyblue', 'salmon', 'lightgreen', 'gold', 'violet']


# Crear la gráfica de barras
plt.figure(figsize=(10, 6)) 
bars = role_counts.plot(kind='bar', color=colors[:len(role_counts)], width=0.3)
# Añadir título y etiquetas
plt.title('Roles de agentes de Valorant')
plt.xlabel('Roles')
plt.ylabel('Agentes con rol de:')
plt.xticks(rotation=45) 

# Ajustar el eje y para que se adapte a los datos y aumente de 2 en 2
plt.yticks(range(0, 11, 2))

# Ajustar el diseño y mostrar la gráfica
plt.tight_layout() 

plt.show()
