import pandas as pd
import matplotlib.pyplot as plt
import json
import os

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

    # Registros con campos vacíos
    vacios = df[df.isnull().any(axis=1)]
    if not vacios.empty:
        errores.append(f"Hay {len(vacios)} registros con campos vacíos.")

    # Notas fuera de rango
    if "Nota" in df.columns:
        fuera_rango = df[(df["Nota"] < 0) | (df["Nota"] > 5)]
        if not fuera_rango.empty:
            errores.append(f"{len(fuera_rango)} notas están fuera del rango permitido (0 a 5).")
    else:
        errores.append("No se encontró la columna 'Nota'.")

    # Programas válidos
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

# =============== 4️⃣ Analizar indicadores con gráficos ===============
def graficar_indicadores(reporte):
    """
    Crea gráficos de barras y pastel con los indicadores de desempeño.
    """
    print("\n📈 Analizando indicadores de desempeño...")

    # --- Gráfico de barras ---
    plt.figure(figsize=(8, 5))
    reporte["Promedio_Nota"].plot(kind="bar", color="skyblue")
    plt.title("Promedio de Notas por Programa")
    plt.xlabel("Programa de Formación")
    plt.ylabel("Nota promedio")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("Promedio_Notas.png")
    plt.show()

    # --- Gráfico de Tasa de Aprobación ---
    plt.figure(figsize=(8, 5))
    reporte["Tasa_Aprobación"].plot(kind="bar", color="seagreen")
    plt.title("Tasa de Aprobación por Programa")
    plt.xlabel("Programa de Formación")
    plt.ylabel("Porcentaje de aprobación (%)")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("Tasa_Aprobacion.png")
    plt.show()

    # --- Gráfico general en pastel ---
    plt.figure(figsize=(6, 6))
    plt.pie(
        reporte["Total"],
        labels=reporte.index,
        autopct="%1.1f%%",
        colors=["#74b9ff", "#55efc4", "#ffeaa7", "#fab1a0"]
    )
    plt.title("Distribución de Estudiantes por Programa")
    plt.tight_layout()
    plt.savefig("Distribucion_Programas.png")
    plt.show()

    print("✅ Gráficos generados: 'Promedio_Notas.png', 'Tasa_Aprobacion.png', 'Distribucion_Programas.png'")

# =============== 5️⃣ Programa principal ===============
def main():
    print("=== 🏫 Sistema de Automatización Académica ===\n")
    archivo = input("Ingrese el nombre del archivo CSV (por ejemplo: registros.csv): ")

    df = cargar_datos(archivo)
    if df.empty:
        return

    validar_datos(df)
    reporte = generar_reporte(df)
    if not reporte.empty:
        graficar_indicadores(reporte)

    # Guardar configuración del último archivo usado
    with open("config.json", "w") as f:
        json.dump({"último_archivo": archivo}, f)
    print("\n💾 Configuración guardada en 'config.json'.")

    print("\n🏁 Proceso completado con éxito.")

# =============== Ejecutar programa ===============
if __name__ == "__main__":
    main()
