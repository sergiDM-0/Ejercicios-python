import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
import os

# Estilo global para seaborn
sns.set(style="whitegrid", palette="muted", font_scale=1.1)

# =============== 1️⃣ Cargar datos académicos ===============
def cargar_datos(archivo):
    """
    Carga un archivo CSV con los registros académicos.
    """
    try:
        df = pd.read_csv(archivo)
        print("✅ Datos cargados correctamente.")
        return df
    except FileNotFoundError:
        print("⚠️ Archivo no encontrado. Verifica la ruta o el nombre del archivo.")
        return pd.DataFrame()
    except Exception as e:
        print("⚠️ Error al cargar el archivo:", e)
        return pd.DataFrame()

# =============== 2️⃣ Validar datos administrativos ===============
def validar_datos(df):
    """
    Revisa si hay errores comunes en los datos:
    - Campos vacíos
    - Notas fuera del rango 0 a 5
    - Programas no válidos
    """
    print("\n🔎 Validando datos administrativos...")
    errores = []

    vacios = df[df.isnull().any(axis=1)]
    if not vacios.empty:
        errores.append(f"Hay {len(vacios)} registros con campos vacíos.")

    if "Nota" in df.columns:
        fuera_rango = df[(df["Nota"] < 0) | (df["Nota"] > 5)]
        if not fuera_rango.empty:
            errores.append(f"{len(fuera_rango)} notas están fuera del rango permitido (0 a 5).")
    else:
        errores.append("No se encontró la columna 'Nota'.")

    programas_validos = ["Sistemas", "Contabilidad", "Gestión Empresarial", "Electrónica"]
    if "Programa" in df.columns:
        no_validos = df[~df["Programa"].isin(programas_validos)]
        if not no_validos.empty:
            errores.append(f"{len(no_validos)} registros pertenecen a programas no reconocidos.")
    else:
        errores.append("No se encontró la columna 'Programa'.")

    if errores:
        print("⚠️ Se detectaron inconsistencias:")
        for e in errores:
            print("   -", e)
    else:
        print("✅ Todos los datos son válidos.")

# =============== 3️⃣ Generar reporte institucional ===============
def generar_reporte(df):
    """
    Genera un resumen con promedios, aprobados y tasas de aprobación por programa.
    """
    print("\n📊 Generando reporte institucional...")

    if "Programa" not in df.columns or "Estado" not in df.columns:
        print("⚠️ No se pueden generar reportes. Faltan columnas 'Programa' o 'Estado'.")
        return pd.DataFrame()

    reporte = df.groupby("Programa").agg(
        Promedio_Nota=("Nota", "mean"),
        Aprobados=("Estado", lambda x: (x == "Aprobado").sum()),
        Reprobados=("Estado", lambda x: (x == "Reprobado").sum()),
        Total=("Estado", "count")
    )

    reporte["Tasa_Aprobación"] = (reporte["Aprobados"] / reporte["Total"]) * 100

    print("\n📘 Reporte generado:\n")
    print(reporte.round(2))
    reporte.to_excel("Reporte_Institucional.xlsx")
    print("\n✅ Reporte guardado como 'Reporte_Institucional.xlsx'")
    return reporte

# =============== 4️⃣ Análisis visual con Seaborn ===============
def graficar_indicadores(df, reporte):
    """
    Crea gráficos de desempeño con Seaborn.
    """
    print("\n📈 Creando visualizaciones con Seaborn...")

    # --- Distribución general de notas ---
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="Nota", kde=True, bins=10, color="royalblue")
    plt.title("Distribución General de Notas")
    plt.xlabel("Nota")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("Distribucion_Notas.png")
    plt.show()

    # --- Promedio de notas por programa ---
    plt.figure(figsize=(8, 5))
    sns.barplot(data=reporte.reset_index(), x="Programa", y="Promedio_Nota", palette="viridis")
    plt.title("Promedio de Notas por Programa")
    plt.xlabel("Programa de Formación")
    plt.ylabel("Nota Promedio")
    plt.tight_layout()
    plt.savefig("Promedio_Programa.png")
    plt.show()

    # --- Tasa de aprobación por programa ---
    plt.figure(figsize=(8, 5))
    sns.barplot(data=reporte.reset_index(), x="Programa", y="Tasa_Aprobación", palette="crest")
    plt.title("Tasa de Aprobación por Programa")
    plt.xlabel("Programa de Formación")
    plt.ylabel("Porcentaje de Aprobación (%)")
    plt.tight_layout()
    plt.savefig("Tasa_Aprobacion.png")
    plt.show()

    # --- Comparación de notas por programa ---
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="Programa", y="Nota", palette="Set2")
    plt.title("Distribución de Notas por Programa")
    plt.xlabel("Programa")
    plt.ylabel("Nota")
    plt.tight_layout()
    plt.savefig("Boxplot_Notas.png")
    plt.show()

    print("✅ Gráficos guardados: 'Distribucion_Notas.png', 'Promedio_Programa.png', 'Tasa_Aprobacion.png', 'Boxplot_Notas.png'")

# =============== 5️⃣ Programa principal ===============
def main():
    print("=== 🏫 Sistema de Automatización Académica (con Seaborn) ===\n")
    archivo = input("Ingrese el nombre del archivo CSV (por ejemplo: registros.csv): ")

    df = cargar_datos(archivo)
    if df.empty:
        return

    validar_datos(df)
    reporte = generar_reporte(df)
    if not reporte.empty:
        graficar_indicadores(df, reporte)

    with open("config.json", "w") as f:
        json.dump({"último_archivo": archivo}, f)
    print("\n💾 Configuración guardada en 'config.json'.")
    print("\n🏁 Proceso completado con éxito.")

# =============== Ejecutar programa ===============
if __name__ == "__main__":
    main()
