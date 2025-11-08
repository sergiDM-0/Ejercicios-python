# =======================================================
# SISTEMA INSTITUCIONAL DE GESTIÓN DE DATOS
# Consolidación de archivos + Cálculo de promedios + Reportes Excel y PDF
# =======================================================

import pandas as pd
from fpdf import FPDF
import os

# ----------------------------
# 1️⃣ CONSOLIDAR ARCHIVOS CON BUCLE
# ----------------------------
def consolidar_archivos(directorio):
    """Lee todos los archivos CSV o Excel de un directorio y los combina en un solo DataFrame."""
    archivos = [f for f in os.listdir(directorio) if f.endswith(('.csv', '.xlsx', '.xls'))]
    if not archivos:
        raise FileNotFoundError(f"No se encontraron archivos CSV o Excel en {directorio}")

    print(f"→ Archivos encontrados en '{directorio}': {archivos}")
    datos_consolidados = pd.DataFrame()

    # 🔁 Bucle que recorre todos los archivos
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        print(f"   - Leyendo: {archivo}")
        if archivo.endswith(".csv"):
            df = pd.read_csv(ruta)
        else:
            df = pd.read_excel(ruta)
        df["archivo_origen"] = archivo
        datos_consolidados = pd.concat([datos_consolidados, df], ignore_index=True)
    
    print(f"✅ Consolidación completada ({len(datos_consolidados)} registros).")
    return datos_consolidados

# ----------------------------
# 2️⃣ CALCULAR PROMEDIOS POR ESTUDIANTE
# ----------------------------
def calcular_promedios(df):
    if "nota" not in df.columns:
        raise ValueError("El archivo debe tener una columna llamada 'nota'.")
    if "asistencia" not in df.columns:
        raise ValueError("El archivo debe tener una columna llamada 'asistencia'.")
    if "programa" not in df.columns or "nombre" not in df.columns or "estado" not in df.columns:
        raise ValueError("El archivo debe tener las columnas 'nombre', 'programa' y 'estado'.")

    print("→ Calculando promedios por estudiante...")
    df_promedio = (
        df.groupby(["nombre", "programa", "estado"], as_index=False)
          .agg({"nota": "mean", "asistencia": "mean"})
    )
    df_promedio["nota"] = df_promedio["nota"].round(2)
    df_promedio["asistencia"] = df_promedio["asistencia"].round(2)
    return df_promedio

# ----------------------------
# 3️⃣ LIMPIAR DATOS
# ----------------------------
def limpiar_datos(df):
    df = df.dropna(subset=["nota", "asistencia"])
    df = df[(df["asistencia"] >= 0) & (df["asistencia"] <= 100)]
    return df

# ----------------------------
# 4️⃣ CALCULAR INDICADORES
# ----------------------------
def calcular_indicadores(df):
    total = len(df)
    aprobados = (df["estado"] == "Aprobado").sum()
    retirados = (df["estado"] == "Retirado").sum()
    eficiencia = (aprobados / total) * 100 if total else 0
    retencion = ((total - retirados) / total) * 100 if total else 0
    return {
        "eficiencia (%)": round(eficiencia, 2),
        "tasa_aprobacion (%)": round((aprobados / total) * 100, 2),
        "retencion (%)": round(retencion, 2)
    }

# ----------------------------
# 5️⃣ FUNCIONES AUXILIARES
# ----------------------------
def filtrar_por_estado(df, estado):
    return df[df["estado"] == estado]

def programas_mayor_matricula(df):
    """Devuelve un DataFrame con columnas 'programa' y 'cantidad' sin riesgo de KeyError."""
    if "programa" not in df.columns:
        return pd.DataFrame(columns=["programa", "cantidad"])
    
    conteo = df["programa"].value_counts().reset_index()
    conteo.columns = ["programa", "cantidad"]  # fuerza nombres correctos
    return conteo

# ----------------------------
# 6️⃣ REPORTE EN CONSOLA
# ----------------------------
def generar_reporte(df):
    indicadores = calcular_indicadores(df)
    print("\n===== REPORTE INSTITUCIONAL =====")
    print("Indicadores:")
    for k, v in indicadores.items():
        print(f" - {k}: {v}")
    print("\nProgramas con mayor matrícula:")
    print(programas_mayor_matricula(df))
    print("=================================")
    return indicadores

# ----------------------------
# 7️⃣ EXPORTAR A EXCEL (4 hojas)
# ----------------------------
def exportar_excel(df, indicadores, ruta_salida="reporte_institucional.xlsx"):
    print(f"→ Generando reporte Excel: {ruta_salida}")
    resumen = pd.DataFrame(list(indicadores.items()), columns=["Indicador", "Valor"])
    programas = programas_mayor_matricula(df)
    aprobados = filtrar_por_estado(df, "Aprobado")[["nombre", "programa", "nota", "asistencia"]]
    
    with pd.ExcelWriter(ruta_salida, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Datos Consolidados")
        resumen.to_excel(writer, index=False, sheet_name="Indicadores")
        programas.to_excel(writer, index=False, sheet_name="Programas")
        aprobados.to_excel(writer, index=False, sheet_name="Aprobados")
    
    print(f"✅ Reporte Excel creado con éxito: {ruta_salida}")

# ----------------------------
# 8️⃣ EXPORTAR A PDF (con tabla)
# ----------------------------
def exportar_pdf(df, indicadores, ruta_salida="reporte_institucional.pdf"):
    pdf = FPDF()
    pdf.add_page()
    
    # --- Encabezado ---
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "REPORTE INSTITUCIONAL CONSOLIDADO", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.ln(8)
    
    # --- Indicadores ---
    pdf.cell(200, 10, "Indicadores Clave:", ln=True)
    for k, v in indicadores.items():
        pdf.cell(200, 10, f"  - {k}: {v}", ln=True)
    pdf.ln(6)
    
    # --- Programas con mayor matrícula ---
    pdf.cell(200, 10, "Programas con mayor matrícula:", ln=True)
    programas = programas_mayor_matricula(df)
    for _, row in programas.iterrows():
        pdf.cell(200, 10, f"  - {row['programa']}: {row['cantidad']} estudiantes", ln=True)
    pdf.ln(8)
    
    # --- Tabla de aprobados ---
    aprobados = filtrar_por_estado(df, "Aprobado")
    if not aprobados.empty:
        pdf.set_font("Arial", "B", 13)
        pdf.cell(200, 10, "Estudiantes Aprobados", ln=True)
        pdf.set_font("Arial", "B", 11)
        
        pdf.cell(50, 8, "Nombre", 1, 0, "C")
        pdf.cell(60, 8, "Programa", 1, 0, "C")
        pdf.cell(30, 8, "Nota", 1, 0, "C")
        pdf.cell(40, 8, "Asistencia (%)", 1, 1, "C")
        
        pdf.set_font("Arial", "", 10)
        for _, fila in aprobados.iterrows():
            pdf.cell(50, 8, str(fila["nombre"]), 1, 0, "C")
            pdf.cell(60, 8, str(fila["programa"]), 1, 0, "C")
            pdf.cell(30, 8, str(fila["nota"]), 1, 0, "C")
            pdf.cell(40, 8, str(fila["asistencia"]), 1, 1, "C")
    
    pdf.output(ruta_salida)
    print(f"✅ Reporte PDF generado: {ruta_salida}")

# ----------------------------
# 9️⃣ PROCESO COMPLETO
# ----------------------------
def ejecutar_proceso_consolidado(directorio):
    print(f"\n→ Iniciando consolidación desde: {directorio}")
    df = consolidar_archivos(directorio)
    
    print("→ Calculando promedios...")
    df_promedio = calcular_promedios(df)
    
    print("→ Limpiando datos...")
    df_limpio = limpiar_datos(df_promedio)
    
    print("→ Calculando indicadores y generando reporte...")
    indicadores = generar_reporte(df_limpio)
    
    print("\n→ Exportando resultados...")
    exportar_excel(df_limpio, indicadores)
    exportar_pdf(df_limpio, indicadores)
    
    print("\n→ Estudiantes aprobados:")
    print(filtrar_por_estado(df_limpio, "Aprobado")[["nombre", "programa", "nota", "asistencia"]])

# ----------------------------
# EJECUCIÓN PRINCIPAL
# ----------------------------
if __name__ == "__main__":
    carpeta = "data"  # 📂 Carpeta con archivos CSV o Excel
    ejecutar_proceso_consolidado(carpeta)

