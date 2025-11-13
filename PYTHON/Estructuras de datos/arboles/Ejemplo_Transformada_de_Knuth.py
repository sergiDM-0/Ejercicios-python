# -*- coding: utf-8 -*-
"""
Ejemplo 2: Transformada de Knuth (págs. 155-156)
Demuestra la creación manual de un árbol binario que representa
un árbol N-ario (jerarquía de Dioses Griegos).
"""

from TDA_Arbol_Binario_de_Busqueda__ABB_ import nodoArbol # Importamos la clase base del nodo
from Utilidad_de_Visualizacion import plot_tree # Importamos la función de ploteo

def crear_arbol_dioses_knuth():
    """
    Crea manualmente el árbol binario de Dioses Griegos
    basado en la "transformada de Knuth" (pág. 156, Fig. 32).
    
    - .izq = primer hijo
    - .der = siguiente hermano
    """
    # Nivel 0
    cronos = nodoArbol("Cronos")
    
    # Nivel 1 (Hijos de Cronos)
    zeus = nodoArbol("Zeus")
    poseidon = nodoArbol("Poseidón")
    hades = nodoArbol("Hades")
    hera = nodoArbol("Hera")
    demeter = nodoArbol("Deméter")
    hestia = nodoArbol("Hestia")
    
    # Nivel 2 (Hijos de Zeus y Hera/Deméter)
    atenea = nodoArbol("Atenea")
    apolo = nodoArbol("Apolo")
    artemisa = nodoArbol("Artemisa")
    dionisio = nodoArbol("Dionisio")
    hermes = nodoArbol("Hermes")
    
    ares = nodoArbol("Ares")
    hefesto = nodoArbol("Hefesto")
    
    persefone = nodoArbol("Perséfone")
    
    # --- Conectar el árbol (según Fig. 32) ---
    
    # Hijos de Cronos
    cronos.izq = zeus
    zeus.der = poseidon
    poseidon.der = hades
    hades.der = hera
    hera.der = demeter
    demeter.der = hestia
    
    # Hijos de Zeus
    zeus.izq = atenea
    atenea.der = apolo
    apolo.der = artemisa
    artemisa.der = dionisio
    dionisio.der = hermes
    
    # Hijos de Hera
    hera.izq = ares
    ares.der = hefesto
    
    # Hija de Deméter
    demeter.izq = persefone
    
    return cronos

def main_knuth():
    """Ejecución principal del ejemplo de Knuth."""
    print("\n" + "-" * 40)
    print("EJECUCIÓN: TRANSFORMADA DE KNUTH (pág. 156)")
    print("-" * 40)
    
    raiz_dioses = crear_arbol_dioses_knuth()
    
    print("Árbol N-ario (Fig. 31) transformado a Árbol Binario (Fig. 32).")
    print("El gráfico muestra la estructura binaria (hijo-izquierdo, hermano-derecho).")
    
    plot_tree(raiz_dioses, "Árbol de Dioses Griegos (Transformada de Knuth - Fig. 32)")

if __name__ == "__main__":
    # Para ejecutar este archivo:
    # 1. Asegúrate de tener tda_abb.py y visualizador_arbol.py en la misma carpeta.
    # 2. Ejecuta: python ejemplo_knuth.py
    main_knuth()