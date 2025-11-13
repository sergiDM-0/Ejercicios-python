"""
Ejemplo de uso del TDA Árbol Binario de Búsqueda (ABB)
(Págs. 138-144)
"""

# Importamos las herramientas del TDA base
from Logica_arbol import *

# Importamos la herramienta de visualización que ya teníamos
try:
    from utilidad_de_visualizacion import plot_tree
except ImportError:
    print("ADVERTENCIA: No se encontró 'utilidad_de_visualizacion.py'.")
    print("El script funcionará, pero no podrá generar gráficos.")


def main_abb():
    """Función principal para demostrar el TDA ABB."""
    
    print("-" * 40)
    print("EJECUCIÓN: ÁRBOL BINARIO DE BÚSQUEDA (Fig. 2)")
    print("-" * 40)

    raiz = None
    
    # Esta lista de datos genera el árbol de la Figura 2 (pág. 138)
    datos = [17, 7, 29, 5, 11, 22, 45, 25, 31]
    
    print(f"Insertando los datos: {datos}")
    for dato in datos:
        raiz = insertar_nodo(raiz, dato)

    print("\nÁrbol generado. Mostrando gráfico...")
    plot_tree(raiz, "Árbol Binario de Búsqueda (Fig. 2, p. 138)", layout='binary')
    
    print("\n--- Barrido Inorden (Muestra ordenado) ---")
    inorden(raiz)
    
    print("\n--- Barrido Preorden (Raíz, Izq, Der) ---")
    preorden(raiz)
    
    print("\n--- Barrido Postorden (Izq, Der, Raíz) ---")
    postorden(raiz)
    
    print("\n--- Barrido por Nivel (Usa TDA Cola) ---")
    por_nivel(raiz)
    
    print("\n--- Búsqueda ---")
    clave_buscada = 22
    nodo_encontrado = buscar(raiz, clave_buscada)
    if nodo_encontrado:
        print(f"Nodo {clave_buscada} encontrado. Info: {nodo_encontrado.info}")
    else:
        print(f"Nodo {clave_buscada} NO encontrado.")

    print("\n--- Eliminación (Nodo con dos hijos) ---")
    clave_a_eliminar = 29
    print(f"Eliminando el nodo: {clave_a_eliminar}...")
    raiz, x = eliminar_nodo(raiz, clave_a_eliminar)
    if x is not None:
        print(f"Se eliminó el valor {x}.")
    
    print("Mostrando árbol después de eliminar...")
    plot_tree(raiz, f"Árbol después de eliminar el {clave_a_eliminar}", layout='binary')

    print("\n--- Barrido Inorden (después de eliminar) ---")
    inorden(raiz)

if __name__ == "__main__":
    # Para ejecutar este archivo:
    # 1. Asegúrate de tener 'tda_arboles_base.py' y 'visualizador_arbol.py'
    #    en la misma carpeta.
    # 2. Ejecuta: python ejemplo_abb_simple.py
    main_abb()