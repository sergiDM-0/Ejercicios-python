import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Datos simulados
np.random.seed(42)
data = {
    "Programa": np.random.choice(["Ingeniería Industrial", "Administración", "Mecatrónica", "Derecho"], 200),
    "Promedio": np.random.normal(3.5, 0.4, 200),
    "Asistencia": np.random.randint(60, 100, 200)
}
df = pd.DataFrame(data)

# Histograma
sns.histplot(df["Promedio"], bins=15, color="royalblue", kde=True)
plt.title("Distribución de promedios académicos")
plt.show()

# Scatter Plot
sns.scatterplot(data=df, x="Asistencia", y="Promedio", hue="Programa", palette="Set2")
plt.title("Relación entre asistencia y promedio académico")
plt.show()

# Box Plot
sns.boxplot(data=df, x="Programa", y="Promedio", palette="pastel")
plt.title("Distribución de promedios por programa")
plt.show()