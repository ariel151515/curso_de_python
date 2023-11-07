import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv("torta.csv")

# Crear el gráfico de torta
plt.figure(figsize=(6, 6))  # Opcional: establecer el tamaño de la figura
colors = plt.cm.Paired(range(len(df)))
plt.pie(df['gasto'], labels=df['categoria'], autopct='%1.1f%%', startangle=90, colors=colors)
plt.title("Gráfico de Torta de Gastos")

# Mostrar el gráfico
plt.show()
