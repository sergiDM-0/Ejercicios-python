import pandas as pd
import matplotlib.pyplot as plt
import os

# =============== 1️⃣ Cargar datos académicos ===============
def cargar_datos(archivo):
    """
    Carga registros académicos desde un archivo CSV o Excel (.xlsx).
    """
    try:
        if archivo.endswith(".csv"):
            df = pd.read_csv(archivo)
        elif archivo.endswith(".xlsx"):
            df = pd.read_excel(archivo)
        else:
            print("⚠️ Formato no compatible. Usa un archivo .csv o .xlsx")
            return pd.DataFrame()

        print("✅ Datos cargados correctamente desde:", archivo)
        return df
    except FileNotFoundError:
        print("⚠️ Archivo no encontrado. Verifica la ruta o el nombre.")
        return pd.DataFrame()
    except Exception as e:
        print("⚠️ Error al cargar el archivo:", e)
        return pd.DataFrame()

# =============== 2️⃣ Validar datos administrativos ===============
def validar_datos(df):
    """
    Revisa errores comunes en los datos:
    - Campos vacíos
    - Notas fuera de rango (0-5)
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
    Crea un resumen de desempeño por programa.
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
    Crea gráficos con Matplotlib para visualizar indicadores institucionales.
    """
    print("\n📈 Analizando indicadores de desempeño...")

    # --- Gráfico de Promedio de Notas ---
    plt.figure(figsize=(8, 5))
    reporte["Promedio_Nota"].plot(kind="bar", color="cornflowerblue")
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
    plt.ylabel("Porcentaje de Aprobación (%)")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("Tasa_Aprobacion.png")
    plt.show()

    # --- Gráfico de Distribución de Estudiantes ---
    plt.figure(figsize=(6, 6))
    plt.pie(
        reporte["Total"],
        labels=reporte.index,
        autopct="%1.1f%%",
        colors=["#74b9ff", "#55efc4", "#ffeaa7", "#fab1a0"]
    )
    plt.title("Distribución de Estudiantes por Programa")
    plt.tight_layout()
    plt.savefig("Distribucion_Estudiantes.png")
    plt.show()

# =============== 5️⃣ Ejecución principal ===============
if __name__ == "__main__":
    archivo = input("📂 Ingresa el nombre del archivo (.csv o .xlsx): ").strip()

    if os.path.exists(archivo):
        datos = cargar_datos(archivo)
        if not datos.empty:
            validar_datos(datos)
            reporte = generar_reporte(datos)
            if not reporte.empty:
                graficar_indicadores(reporte)
    else:
        print("⚠️ El archivo no existe en la ruta indicada.")

