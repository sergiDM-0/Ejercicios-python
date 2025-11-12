"""
analysis_institucional.py
Script de ejemplo para integrar, limpiar y analizar datos académicos
Genera estadísticas descriptivas, identifica asignaturas con mayor variabilidad,
calcula porcentaje de estudiantes en riesgo (promedio < 3.0) y exporta resultados.

Requisitos:
pip install pandas numpy openpyxl
Ejecutar:
python analysis_institucional.py
"""
from pathlib import Path
import pandas as pd
import numpy as np

BASE = Path(__file__).resolve().parent
OUTPUT_DIR = BASE / "resultados"
OUTPUT_DIR.mkdir(exist_ok=True)  # Crear carpeta de resultados si no existe
ENROLLMENT = BASE / "matricula.csv"
GRADES = BASE / "calificaciones.xlsx"
SUBJECTS = BASE / "asignaturas.json"


def cargar_fuentes():
    df_enroll = pd.read_csv(ENROLLMENT, dtype=str)  # CSV matrícula
    df_grades = pd.read_excel(GRADES, dtype={'student_id': str, 'asignatura_id': str})  # Excel calificaciones
    df_subj = pd.read_json(SUBJECTS)  # JSON asignaturas
    return df_enroll, df_grades, df_subj


def limpiar_datos(df_enroll, df_grades):
    antes = len(df_enroll)
    df_enroll = df_enroll.drop_duplicates(subset=['student_id'], keep='first').reset_index(drop=True)
    despues = len(df_enroll)
    print(f"Duplicados matricula: {antes-despues} eliminados. ({antes} -> {despues})")

    df_enroll['student_id'] = df_enroll['student_id'].astype(str).str.strip()
    df_enroll['nombre'] = df_enroll['nombre'].str.title().str.strip()
    df_enroll['programa'] = df_enroll['programa'].str.title().str.strip()
    df_enroll['jornada'] = df_enroll['jornada'].str.title().str.strip()

    df_grades['student_id'] = df_grades['student_id'].astype(str).str.strip()
    df_grades['asignatura_id'] = df_grades['asignatura_id'].astype(str).str.strip()

    df_grades['asignatura'] = df_grades['asignatura'].str.title().str.strip()
    df_grades['nota'] = pd.to_numeric(df_grades['nota'], errors='coerce')

    imputes = df_grades.groupby('asignatura_id')['nota'].transform('mean')
    df_grades['nota_imputada'] = df_grades['nota'].fillna(imputes).fillna(0)
    df_grades['nota_imputada'] = df_grades['nota_imputada'].clip(0, 5)

    return df_enroll, df_grades


def integrar(df_enroll, df_grades, df_subj):
    df = df_grades.merge(df_enroll, on='student_id', how='left')
    df = df.merge(df_subj, on='asignatura_id', how='left', suffixes=('', '_subj'))

    if 'asignatura_subj' in df.columns:
        df['asignatura'] = df['asignatura_subj']
    df = df.drop(columns=[c for c in df.columns if c.endswith('_subj')], errors='ignore')

    return df


def calcular_estadisticas(df):
    resultados = {}

    if 'asignatura' not in df.columns:
        raise KeyError("No se encontró la columna 'asignatura' después de integrar los datos.")

    grp_prog = df.groupby('programa')['nota_imputada']
    resumen_prog = grp_prog.agg(['mean', 'median', 'std', 'min', 'max', 'count']).rename(columns={
        'mean':'promedio','median':'mediana','std':'desviacion','min':'minimo','max':'maximo','count':'n_registros'
    })
    resultados['por_programa'] = resumen_prog.round(3)

    grp_asig = df.groupby('asignatura')['nota_imputada']
    resumen_asig = grp_asig.agg(['mean','std','count']).rename(columns={
        'mean':'promedio',
        'std':'desviacion',
        'count':'n_registros'
    })

    resumen_asig['desviacion'] = resumen_asig['desviacion'].fillna(0)
    resultados['por_asignatura'] = resumen_asig.round(3)

    resultados['asignaturas_mayor_variabilidad'] = resumen_asig.sort_values('desviacion', ascending=False).head(5)

    prom_est = df.groupby('student_id').agg(promedio_est=('nota_imputada','mean')).reset_index()
    total_est = prom_est['student_id'].nunique()
    en_riesgo = prom_est[prom_est['promedio_est'] < 3.0]['student_id'].nunique()
    resultados['porcentaje_en_riesgo'] = round((en_riesgo / total_est) * 100, 2) if total_est > 0 else 0
    resultados['por_estudiante'] = prom_est.round(3)

    return resultados


def analizar_segmentos(df):
    return df.groupby(['jornada','programa']).agg(
        promedio=('nota_imputada','mean'),
        n=('student_id','nunique')
    ).reset_index()


def exportar_resultados(resultados, df_integrado):
    resultados['por_programa'].to_excel(OUTPUT_DIR / 'resumen_por_programa.xlsx')
    resultados['por_asignatura'].to_excel(OUTPUT_DIR / 'resumen_por_asignatura.xlsx')
    resultados['asignaturas_mayor_variabilidad'].to_excel(OUTPUT_DIR / 'asignaturas_alta_variabilidad.xlsx')
    resultados['por_estudiante'].to_csv(OUTPUT_DIR / 'promedio_por_estudiante.csv', index=False)
    df_integrado.to_csv(OUTPUT_DIR / 'datos_integrados.csv', index=False)

    with open(OUTPUT_DIR / 'porcentaje_en_riesgo.txt', 'w') as f:
        f.write(str(resultados['porcentaje_en_riesgo']))

    print("Resultados exportados en:", OUTPUT_DIR)


def main():
    print("Cargando fuentes...")
    df_enroll, df_grades, df_subj = cargar_fuentes()
    print("Limpiando datos...")
    df_enroll, df_grades_clean = limpiar_datos(df_enroll, df_grades)
    print("Integrando datos...")
    df_integrado = integrar(df_enroll, df_grades_clean, df_subj)
    print("Calculando estadísticas...")
    resultados = calcular_estadisticas(df_integrado)

    print("\nPorcentaje estudiantes en riesgo (<3.0):", resultados['porcentaje_en_riesgo'], "%")
    print("\nResumen por programa:\n", resultados['por_programa'])
    print("\nTop asignaturas por variabilidad:\n", resultados['asignaturas_mayor_variabilidad'])

    segmentos = analizar_segmentos(df_integrado)
    print("\nSegmentación por jornada y programa:\n", segmentos)

    exportar_resultados(resultados, df_integrado)
    print("\n✅ Análisis completado correctamente ✅")


if __name__ == '__main__':
    main()
