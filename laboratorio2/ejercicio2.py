import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv("C:\\Users\\jorge\\Documents\\GitHub\\Programacion-Computo-2\\laboratorio2\\mcu_box_office.csv")


# Clasificar las películas según su calificación en rangos
df['clasificacion'] = pd.cut(df['tomato_meter'], bins=[70, 80, 100], labels=['7-8', '9-10'])


# Contar cuántas películas caen en cada categoría

clasificacion_contada = df['clasificacion'].value_counts()

colores = ['#1e8449', '#f1c40f']

plt.figure(figsize=(8, 8))
plt.pie(clasificacion_contada, labels=clasificacion_contada.index, autopct='%1.1f%%', startangle=140, colors=colores)
plt.title('Peliculas de  marvel con calificacion en rottem tomatoes    ')
plt.show()