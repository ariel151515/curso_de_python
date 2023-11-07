import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("pedos.csv")
sns.lineplot(x="fecha", y = "pedos", data=df)

# Para identificar el punto mas alto
plt.plot("01-10",123,"o")

plt.show()

