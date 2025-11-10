import pandas as pd

# Nombre del archivo CSV
archivo_csv = input("Ingrese el nombre del archivo CSV (incluya '.csv' si es necesario): ")

def cargar_y_validar_datos(archivo):
    """Carga los datos y realiza las validaciones."""
    print(f"--- Cargando datos de '{archivo}' ---")
    try:
        df = pd.read_csv(archivo)
        print("Datos cargados exitosamente:")
        print(df.head()) # Muestra las primeras filas
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró.")
        print("Por favor, asegúrese de que el archivo está en la misma carpeta que el script.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

    print("\n--- 1. Validación: Campos Vacíos ---")
    campos_vacios = df.isnull().sum()
    if campos_vacios.sum() > 0:
        print("Se encontraron campos vacíos:")
        print(campos_vacios[campos_vacios > 0])
    else:
        print("No se encontraron campos vacíos.")

    print("\n--- 2. Validación: Notas fuera de rango (0-5) ---")
    # Asegurarnos de que 'Nota' sea numérica, los errores se convierten en NaT (No numérico)
    df['Nota'] = pd.to_numeric(df['Nota'], errors='coerce')
    
    notas_invalidas = df[(df['Nota'] < 0) | (df['Nota'] > 5)]
    
    if not notas_invalidas.empty:
        print("Se encontraron notas fuera del rango válido (0 a 5):")
        print(notas_invalidas)
    else:
        print("Todas las notas registradas están dentro del rango válido.")
        
    return df

def analizar_datos(df):
    """Realiza los cálculos de promedios y conteos."""
    if df is None:
        print("No se pueden analizar los datos debido a errores de carga.")
        return

    # --- Limpieza para cálculos ---
    # Para calcular el promedio, solo usamos notas válidas (ni vacías, ni fuera de rango)
    df_limpio = df.dropna(subset=['Nota']) # Elimina filas donde 'Nota' es NaN
    df_limpio = df_limpio[(df_limpio['Nota'] >= 0) & (df_limpio['Nota'] <= 5)]
    
    if df_limpio.empty:
        print("\nNo hay datos válidos para calcular el promedio.")
    else:
        print("\n--- 3. Cálculo: Promedio de notas por programa (sobre notas válidas) ---")
        promedio_programa = df_limpio.groupby('Programa')['Nota'].mean()
        print(promedio_programa.to_string(float_format="%.2f")) # Formateado a 2 decimales

    # --- Conteo de Aprobados/Reprobados ---
    # Usamos el dataframe original (df) para el conteo de 'Estado',
    # ya que el estado puede estar definido incluso si la nota falta.
    print("\n--- 4. Conteo: Estudiantes por 'Estado' y 'Programa' ---")
    if 'Estado' in df.columns:
        conteo_estado = df.groupby('Programa')['Estado'].value_counts().unstack().fillna(0)
        print(conteo_estado)
    else:
        print("La columna 'Estado' no se encontró en el CSV.")

def main():
    """Función principal del script de análisis."""
    datos = cargar_y_validar_datos(archivo_csv)
    analizar_datos(datos)

if __name__ == "__main__":
    main()