# =======================================================
# VISUALIZACIÓN DE DATOS INSTITUCIONALES - UNIVERSIDAD ECCI
# Basado en la Unidad Temática 5: Visualización de datos
# =======================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# -----------------------------
# 1️⃣ Crear datos institucionales simulados
# -----------------------------
np.random.seed(42)
# Este bloque crea datos ficticios de estudiantes para simular información institucional
# 1. "Programa": para cada uno de los 200 registros, se asigna aleatoriamente un programa entre cuatro opciones.
# 2. "Promedio": se generan 200 números aleatorios siguiendo una distribución normal (media 3.5, desviación 0.4), simulando promedios académicos.
# 3. "Asistencia": se generan 200 valores enteros aleatorios entre 60 y 99, representando porcentaje de asistencia.

data = {
    "Programa": np.random.choice(["Ingeniería Industrial", "Administración", "Mecatrónica", "Derecho",'contabilidad','economía','ingeniería de sistemas','ingeniería electrónica'], 200),
    "Promedio": np.random.normal(0.0, 5.0, 200),
    "Asistencia": np.random.randint(20, 100, 200)
}

# Se crea un DataFrame de pandas a partir del diccionario 'data', formando una tabla con tres columnas y 200 filas.
df = pd.DataFrame(data)

# -----------------------------
# Crear carpeta para guardar resultados
# -----------------------------
carpeta_resultados = "resultados graficas de dispersion"
if not os.path.exists(carpeta_resultados):
    os.makedirs(carpeta_resultados)
    print(f"✅ Carpeta '{carpeta_resultados}' creada correctamente.")

# -----------------------------
# 2️⃣ Histograma: distribución de promedios
# -----------------------------
plt.figure(figsize=(5,5))
sns.histplot(df["Promedio"], bins=10, color="pink", kde=True)
plt.title("Distribución de promedios académicos")
plt.xlabel("Promedio")
plt.ylabel("Frecuencia")
plt.tight_layout()
ruta_histograma = os.path.join(carpeta_resultados, "histograma_promedios.png")
plt.savefig(ruta_histograma)
plt.show()

# -----------------------------
# 3️⃣ Scatter Plot: relación asistencia vs. promedio
# -----------------------------
plt.figure(figsize=(5,5))
sns.scatterplot(data=df, x="Asistencia", y="Promedio", hue="Programa", palette="Set2")
plt.title("Relación entre asistencia y promedio académico")
plt.xlabel("Asistencia (%)")
plt.ylabel("Promedio")
plt.legend(title="Programa", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
ruta_dispersion = os.path.join(carpeta_resultados, "dispersión_asistencia_promedio.png")
plt.savefig(ruta_dispersion)
plt.show()

# -----------------------------
# 4️⃣ Box Plot: comparación de promedios por programa
# -----------------------------
plt.figure(figsize=(6,5))
sns.boxplot(data=df, x="Programa", y="Promedio", palette="pastel")
plt.title("Distribución de promedios por programa")
plt.xlabel("Programa Académico")
plt.ylabel("Promedio")
plt.xticks(rotation=50)
plt.tight_layout()
ruta_boxplot = os.path.join(carpeta_resultados, "boxplot_promedios_programa.png")
plt.savefig(ruta_boxplot)
plt.show()

# -----------------------------
# 5️⃣ Exportar a PDF (opcional)
# -----------------------------

from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Informe de Visualización de Datos - ECCI", ln=True, align="C")
pdf.set_font("Arial", "", 10)
pdf.multi_cell(0, 10, """
Este informe incluye tres tipos de visualizaciones creadas con Python:
1. Histograma: distribución de promedios académicos.
2. Gráfico de dispersión: relación entre asistencia y rendimiento.
3. Box Plot: comparación de promedios por programa académico.
""")

imagenes = [
    os.path.join(carpeta_resultados, "histograma_promedios.png"),
    os.path.join(carpeta_resultados, "dispersión_asistencia_promedio.png"),
    os.path.join(carpeta_resultados, "boxplot_promedios_programa.png")
]

# Agregar imágenes de 4 en 4 por página
imagenes_por_pagina = 4
ancho_pagina = 210  # A4 width in mm
margen = 10
ancho_imagen = (ancho_pagina - 3 * margen) / 2  # 2 columnas
alto_imagen = 80  # Altura aproximada para mantener proporción

for i, img in enumerate(imagenes):
    # Si es el primer elemento o múltiplo de 4, crear nueva página
    if i % imagenes_por_pagina == 0:
        pdf.add_page()
    
    # Calcular posición en la cuadrícula 2x2
    fila = (i % imagenes_por_pagina) // 2
    columna = (i % imagenes_por_pagina) % 2
    
    # Calcular coordenadas x e y
    x = margen + columna * (ancho_imagen + margen)
    y = 20 + fila * (alto_imagen + margen)
    
    pdf.image(img, x=x, y=y, w=ancho_imagen)
 



ruta_pdf = os.path.join(carpeta_resultados, "Visualizacion_Datos_ECCI.pdf")
pdf.output(ruta_pdf)
print("✅ Informe PDF generado correctamente.")
print(f"✅ Todos los archivos guardados en la carpeta: '{carpeta_resultados}'")
