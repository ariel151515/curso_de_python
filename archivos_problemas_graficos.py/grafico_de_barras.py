import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("colla_ingresos.csv")
sns.barplot(x="fuente", y = "ingresos", data=df)

#obteniendo el total de ingresos
total_ingresos = df['ingresos'].sum()

#mostrando el total de ingresos
print(f"El total de ingresos es de: {total_ingresos}")

#mostrando el grafico
plt.show()
