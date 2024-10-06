import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV usando la ruta completa
df = pd.read_csv("C:\\Users\\jorge\\Documents\\GitHub\\Programacion-Computo-2\\laboratorio2\\valorant_agent.csv")

# Contar las ocurrencias de cada rol
role_counts = df['role'].value_counts()

colors = ['skyblue', 'salmon', 'lightgreen', 'gold', 'violet']


# Crear la gráfica de barras
plt.figure(figsize=(10, 6))  # Ajusta el tamaño de la figura
bars = role_counts.plot(kind='bar', color=colors[:len(role_counts)])

# Añadir título y etiquetas
plt.title('Roles de agentes de Valorant')
plt.xlabel('Rol')
plt.ylabel('Agentes con rol de:')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x

# Calcular y mostrar el porcentaje en cada barra
total_count = role_counts.sum()
for bar in bars.patches:
    height = bar.get_height()
    percentage = (height / total_count) * 100  # Calcular el porcentaje
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{percentage:.1f}%', ha='center', va='bottom')

# Ajustar el diseño y mostrar la gráfica
plt.tight_layout()  # Ajustar el diseño
plt.show()
