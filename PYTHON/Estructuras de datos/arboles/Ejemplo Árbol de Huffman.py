# -*- coding: utf-8 -*-
"""
Ejemplo 1: Árbol de Huffman (págs. 145-149)
Demuestra la construcción de un árbol de Huffman para compresión de datos.
"""

import heapq # Para la cola de prioridad (montículo)
from Utilidad_de_Visualizacion import plot_tree # Importamos la función de ploteo

class nodoHuffman(object):
    """Clase nodo para el árbol de Huffman. Incluye la frecuencia."""
    def __init__(self, info, frecuencia):
        self.info = info
        self.frecuencia = frecuencia
        self.izq = None
        self.der = None

    def __lt__(self, other):
        """Permite a heapq comparar nodos por frecuencia."""
        return self.frecuencia < other.frecuencia

    def __eq__(self, other):
        """Permite a heapq comparar nodos por frecuencia."""
        return self.frecuencia == other.frecuencia
    
    # --- INICIO DE LA CORRECCIÓN ---
    def __hash__(self):
        """
        Hace que el nodo sea 'hasheable' para el diccionario de netgraph.
        Al definir __eq__, Python elimina __hash__ por defecto. 
        Lo restauramos usando el id único del objeto.
        """
        return id(self)
    # --- FIN DE LA CORRECCIÓN ---
    
    def __str__(self):
        # Muestra 'char: freq' si es hoja, o solo 'freq' si es nodo interno
        if self.info is not None:
            return f"{self.info}\n({self.frecuencia:.2f})"
        return f" \n({self.frecuencia:.2f})"

def generar_arbol_huffman(tabla_frecuencias):
    """Construye un árbol de Huffman a partir de una tabla de frecuencias."""
    bosque = []
    for info, frecuencia in tabla_frecuencias.items():
        heapq.heappush(bosque, nodoHuffman(info, frecuencia))

    while len(bosque) > 1:
        nodo_izq = heapq.heappop(bosque)
        nodo_der = heapq.heappop(bosque)

        frecuencia_padre = nodo_izq.frecuencia + nodo_der.frecuencia
        nodo_padre = nodoHuffman(None, frecuencia_padre)
        nodo_padre.izq = nodo_izq
        nodo_padre.der = nodo_der

        heapq.heappush(bosque, nodo_padre)

    return bosque[0] if bosque else None

def _generar_diccionario_huffman(raiz, diccionario, codigo_actual=""):
    """Función auxiliar recursiva para generar los códigos."""
    if raiz is None:
        return
    if raiz.info is not None:
        diccionario[raiz.info] = codigo_actual
        return
    _generar_diccionario_huffman(raiz.izq, diccionario, codigo_actual + "0")
    _generar_diccionario_huffman(raiz.der, diccionario, codigo_actual + "1")

def get_diccionario_huffman(raiz_huffman):
    """Genera un diccionario de códigos (ej: {'A': '01'}) desde un árbol."""
    diccionario = {}
    _generar_diccionario_huffman(raiz_huffman, diccionario)
    return diccionario

def main_huffman():
    """Ejecución principal del ejemplo de Huffman."""
    print("-" * 40)
    print("EJECUCIÓN: ÁRBOL DE HUFFMAN (pág. 145)")
    print("-" * 40)
    
    tabla_frec = {
        'I': 0.28, 'N': 0.16, 'T': 0.08, 'E': 0.16,
        'L': 0.08, 'G': 0.08, 'C': 0.08, 'A': 0.08
    }

    raiz_huffman = generar_arbol_huffman(tabla_frec)

    diccionario = get_diccionario_huffman(raiz_huffman)
    
    print("Tabla de códigos de Huffman generada:")
    for char, code in sorted(diccionario.items()):
        print(f"  Caracter: '{char}' -> Código: {code}")

    # Graficar el árbol
    plot_tree(raiz_huffman, "Árbol de Huffman (pág. 149)")

if __name__ == "__main__":
    # Para ejecutar este archivo:
    # 1. Asegúrate de tener tda_cola.py y visualizador_arbol.py en la misma carpeta.
    # 2. Ejecuta: python ejemplo_huffman.py
    main_huffman()