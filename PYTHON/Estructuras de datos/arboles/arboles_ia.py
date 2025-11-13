# -*- coding: utf-8 -*-
"""
Este archivo contiene la lógica completa del TDA Árbol del Capítulo 10,
incluyendo Árboles Binarios de Búsqueda (ABB), Árboles de Huffman, 
Transformada de Knuth (Árbol N-ario) y Árboles AVL.

Para ejecutar, necesitarás instalar las librerías:
pip install netgraph matplotlib
"""

import matplotlib.pyplot as plt
from netgraph import Graph # Para la visualización gráfica de los árboles
import heapq # Para la cola de prioridad de Huffman

# ---------------------------------------------------------------------------
# SECCIÓN 0: CÓDIGO BASE (TDA Cola y TDA Árbol Binario)
# Este es el código base proporcionado, con funciones adaptadas como métodos.
# ---------------------------------------------------------------------------

class nodo_cola(object):
    """Clase nodo cola."""
    def __init__(self, info=None, apuntador=None):
        self.info = info
        self.apuntador = apuntador

class Cola(object):
    """Clase Cola."""
    def __init__(self):
        """Crea una cola vacía."""
        self.frente, self.final = None, None
        self.tamanio = 0

    def arribo(self, dato):
        """Agrega el dato al final de la cola."""
        nodo = nodo_cola(dato)
        if self.frente is None:
            self.frente = nodo
            self.final = nodo
        else:
            self.final.apuntador = nodo
            self.final = nodo
        self.tamanio += 1

    def atencion(self):
        """Atiende el elemento en frente de la cola y lo devuelve."""
        if self.frente is None:
            return None
        dato = self.frente.info
        self.frente = self.frente.apuntador
        if self.frente is None:
            self.final = None
        self.tamanio -= 1
        return dato

    def cola_vacia(self):
        """Devuelve true si la cola esta vacia."""
        return self.frente is None

    def __len__(self):
        return self.tamanio

# --- TDA Árbol Binario de Búsqueda (ABB) ---

class nodoArbol(object):
    """Clase nodo árbol."""
    def __init__(self, info):
        """Crea un nodo con la información cargada."""
        self.izq = None
        self.der = None
        self.info = info
    
    def __str__(self):
        # Ayuda a que los nodos se muestren bien en los gráficos
        return str(self.info)

def insertar_nodo(raiz, dato):
    """Inserta un dato al árbol."""
    if (raiz is None):
        raiz = nodoArbol(dato)
    elif (dato < raiz.info):
        raiz.izq = insertar_nodo(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

def arbolvacio(raiz):
    """Devuelve True si el árbol está vacío."""
    return raiz is None

def remplazar(raiz):
    """Determina el nodo que reemplazará al que se elimina."""
    aux = None
    if (raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux

def eliminar_nodo(raiz, clave):
    """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
    x = None
    if (raiz is not None):
        if (clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif (clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if (raiz.izq is None):
                raiz = raiz.der
            elif (raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x

def buscar(raiz, clave):
    """Devuelve la dirección del elemento buscado."""
    pos = None
    if (raiz is not None):
        if (raiz.info == clave):
            pos = raiz
        elif (clave < raiz.info):
            pos = buscar(raiz.izq, clave)
        else:
            pos = buscar(raiz.der, clave)
    return pos

# --- Barridos (agregados desde el capítulo) ---
def inorden(raiz):
    """Realiza el barrido inorden del árbol."""
    if (raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

def preorden(raiz):
    """Realiza el barrido preorden del árbol."""
    if (raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

def postorden(raiz):
    """Realiza el barrido postorden del árbol."""
    if (raiz is not None):
        postorden(raiz.izq)
        postorden(raiz.der)
        print(raiz.info)

def por_nivel(raiz):
    """Realiza el barrido por niveles del árbol."""
    if raiz is None:
        return
    pendientes = Cola()
    pendientes.arribo(raiz)
    while (not pendientes.cola_vacia()):
        nodo = pendientes.atencion()
        print(nodo.info)
        if (nodo.izq is not None):
            pendientes.arribo(nodo.izq)
        if (nodo.der is not None):
            pendientes.arribo(nodo.der)

# ---------------------------------------------------------------------------
# SECCIÓN 1: LÓGICA DE VISUALIZACIÓN (NETGRAPH)
# ---------------------------------------------------------------------------

def _get_edges_labels_pos(nodo, x=0, y=0, pos=None, edges=None, labels=None, level_height=1.0):
    """Función auxiliar recursiva para construir la estructura del gráfico."""
    if pos is None:
        pos = {}
    if edges is None:
        edges = []
    if labels is None:
        labels = {}

    pos[nodo] = (x, y)
    labels[nodo] = str(nodo.info)

    ancho_nivel = 2**(y + 1) # Ajusta el ancho basado en la profundidad

    if nodo.izq:
        edges.append((nodo, nodo.izq))
        _get_edges_labels_pos(nodo.izq, x - ancho_nivel / 4, y - level_height, pos, edges, labels, level_height)
    
    if nodo.der:
        edges.append((nodo, nodo.der))
        _get_edges_labels_pos(nodo.der, x + ancho_nivel / 4, y - level_height, pos, edges, labels, level_height)
        
    return edges, labels, pos

def plot_tree(raiz, title="Visualización del Árbol"):
    """
    Dibuja un árbol binario usando netgraph y matplotlib.
    El 'raiz' debe ser un objeto nodoArbol (o derivado) con .info, .izq, y .der.
    """
    if raiz is None:
        print(f"Árbol '{title}' está vacío. No hay nada que graficar.")
        return

    edges, labels, pos = _get_edges_labels_pos(raiz)
    
    plt.figure(figsize=(16, 8))
    # Usamos un subplot para poder poner el título
    ax = plt.subplot(111)
    ax.set_title(title, fontsize=16, fontweight='bold')
    
    # Crear el objeto Graph
    g = Graph(edges,
              node_layout=pos,
              node_labels=labels,
              node_label_fontdict=dict(size=10, weight='bold'),
              node_size=10,
              node_color='lightblue',
              node_edge_width=1,
              edge_width=1.5,
              edge_color='gray',
              arrows=True,
              ax=ax)
    
    # Ocultar ejes
    ax.set_xticks([])
    ax.set_yticks([])
    plt.box(False)
    plt.show()

# ---------------------------------------------------------------------------
# SECCIÓN 2: ÁRBOL DE HUFFMAN (págs. 145-149)
# ---------------------------------------------------------------------------

class nodoHuffman(object):
    """Clase nodo para el árbol de Huffman. Incluye la frecuencia."""
    def __init__(self, info, frecuencia):
        self.info = info
        self.frecuencia = frecuencia
        self.izq = None
        self.der = None

    # Métodos de comparación para que heapq (cola de prioridad) funcione
    def __lt__(self, other):
        return self.frecuencia < other.frecuencia
    def __eq__(self, other):
        return self.frecuencia == other.frecuencia
    
    def __str__(self):
        # Si es una hoja, muestra 'char: freq', si es un nodo, solo 'freq'
        if self.info is not None:
            return f"{self.info}\n({self.frecuencia:.2f})"
        return f" \n({self.frecuencia:.2f})"


def generar_arbol_huffman(tabla_frecuencias):
    """Construye un árbol de Huffman a partir de una tabla de frecuencias."""
    # heapq es una implementación de cola de prioridad (montículo)
    bosque = []
    for info, frecuencia in tabla_frecuencias.items():
        # Usamos heapq para mantener el bosque ordenado por frecuencia
        heapq.heappush(bosque, nodoHuffman(info, frecuencia))

    while len(bosque) > 1:
        # 1. Sacar los dos nodos con menor frecuencia
        nodo_izq = heapq.heappop(bosque)
        nodo_der = heapq.heappop(bosque)

        # 2. Crear un nuevo nodo padre
        frecuencia_padre = nodo_izq.frecuencia + nodo_der.frecuencia
        nodo_padre = nodoHuffman(None, frecuencia_padre) # Nodo interno no tiene info
        nodo_padre.izq = nodo_izq
        nodo_padre.der = nodo_der

        # 3. Insertar el nuevo nodo en el bosque
        heapq.heappush(bosque, nodo_padre)

    # El último elemento que queda en el bosque es la raíz del árbol
    return bosque[0] if bosque else None

def _generar_diccionario_huffman(raiz, diccionario, codigo_actual=""):
    """Función auxiliar recursiva para generar los códigos."""
    if raiz is None:
        return
    
    # Si es un nodo hoja (tiene un caracter)
    if raiz.info is not None:
        diccionario[raiz.info] = codigo_actual
        return

    # Recursión: 0 para la izquierda, 1 para la derecha
    _generar_diccionario_huffman(raiz.izq, diccionario, codigo_actual + "0")
    _generar_diccionario_huffman(raiz.der, diccionario, codigo_actual + "1")

def get_diccionario_huffman(raiz_huffman):
    """Genera un diccionario de códigos (ej: {'A': '01'}) desde un árbol."""
    diccionario = {}
    _generar_diccionario_huffman(raiz_huffman, diccionario)
    return diccionario

def main_huffman():
    """Ejemplo principal para Huffman."""
    print("-" * 40)
    print("EJECUCIÓN: ÁRBOL DE HUFFMAN (pág. 145)")
    print("-" * 40)
    
    # Datos de la tabla de frecuencias de la pág. 145
    tabla_frec = {
        'I': 0.28, 'N': 0.16, 'T': 0.08, 'E': 0.16,
        'L': 0.08, 'G': 0.08, 'C': 0.08, 'A': 0.08
    }

    # 1. Generar el árbol
    raiz_huffman = generar_arbol_huffman(tabla_frec)

    # 2. Generar la tabla de códigos
    diccionario = get_diccionario_huffman(raiz_huffman)
    
    print("Tabla de códigos de Huffman generada:")
    for char, code in sorted(diccionario.items()):
        print(f"  Caracter: '{char}' -> Código: {code}")

    # 3. Graficar el árbol
    # Nota: La función de ploteo genérica funciona con nodoHuffman
    # porque también tiene .info, .izq, y .der.
    plot_tree(raiz_huffman, "Árbol de Huffman (pág. 149)")


# ---------------------------------------------------------------------------
# SECCIÓN 3: TRANSFORMADA DE KNUTH (pág. 155)
# ---------------------------------------------------------------------------

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
    
    # --- Conectar el árbol ---
    
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
    """Ejemplo principal para la Transformada de Knuth."""
    print("\n" + "-" * 40)
    print("EJECUCIÓN: TRANSFORMADA DE KNUTH (pág. 156)")
    print("-" * 40)
    
    raiz_dioses = crear_arbol_dioses_knuth()
    
    print("Árbol N-ario de Dioses Griegos (Fig. 31) transformado a Árbol Binario (Fig. 32).")
    print("El gráfico mostrará la estructura binaria (hijo-izquierdo, hermano-derecho).")
    
    plot_tree(raiz_dioses, "Árbol de Dioses Griegos (Transformada de Knuth)")

# ---------------------------------------------------------------------------
# SECCIÓN 4: ÁRBOL AVL (págs. 149-154)
# ---------------------------------------------------------------------------

class nodoAVL(nodoArbol):
    """
    Clase nodo para Árbol AVL. Hereda de nodoArbol y añade 'altura'.
    (pág. 150, Fig. 20)
    """
    def __init__(self, info):
        super().__init__(info)
        self.altura = 0 # La altura de un nodo hoja es 0

def obtener_altura(raiz):
    """Obtiene la altura de un nodo AVL. (pág. 150, Fig. 21)"""
    if raiz is None:
        return -1 # Altura de un nodo nulo es -1
    else:
        return raiz.altura

def actualizar_altura(raiz):
    """Recalcula la altura de un nodo. (pág. 150, Fig. 21)"""
    if raiz is not None:
        alt_izq = obtener_altura(raiz.izq)
        alt_der = obtener_altura(raiz.der)
        raiz.altura = max(alt_izq, alt_der) + 1

def rotar_simple(raiz, control):
    """Realiza una rotación simple (derecha o izquierda). (pág. 153, Fig. 26)"""
    if control: # Rotación simple a la derecha
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else: # Rotación simple a la izquierda
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    
    actualizar_altura(raiz) # Actualiza altura del nodo que baja
    actualizar_altura(aux)  # Actualiza altura del nodo que sube
    return aux

def rotar_doble(raiz, control):
    """Realiza una rotación doble (izq-der o der-izq). (pág. 153, Fig. 27)"""
    if control: # Rotación doble a la derecha (Izquierda-Derecha)
        raiz.izq = rotar_simple(raiz.izq, False) # Rotación simple a la izquierda
        raiz = rotar_simple(raiz, True)          # Rotación simple a la derecha
    else: # Rotación doble a la izquierda (Derecha-Izquierda)
        raiz.der = rotar_simple(raiz.der, True)  # Rotación simple a la derecha
        raiz = rotar_simple(raiz, False)         # Rotación simple a la izquierda
    return raiz

def balancear(raiz):
    """Verifica el balance del árbol y aplica rotaciones. (pág. 153, Fig. 28)"""
    if raiz is not None:
        alt_izq = obtener_altura(raiz.izq)
        alt_der = obtener_altura(raiz.der)

        # Factor de equilibrio (FE)
        # FE > 1: Desbalanceado a la izquierda
        # FE < -1: Desbalanceado a la derecha
        if (alt_izq - alt_der) == 2: 
            # Desbalanceo a la izquierda. Chequeamos el hijo izquierdo.
            if (obtener_altura(raiz.izq.izq) >= obtener_altura(raiz.izq.der)):
                raiz = rotar_simple(raiz, True) # Rotación simple derecha
            else:
                raiz = rotar_doble(raiz, True) # Rotación doble derecha
        elif (alt_der - alt_izq) == 2:
            # Desbalanceo a la derecha. Chequeamos el hijo derecho.
            if (obtener_altura(raiz.der.der) >= obtener_altura(raiz.der.izq)):
                raiz = rotar_simple(raiz, False) # Rotación simple izquierda
            else:
                raiz = rotar_doble(raiz, False) # Rotación doble izquierda
    return raiz

def insertar_nodo_avl(raiz, dato):
    """Inserta un dato en un árbol AVL. (pág. 154, Fig. 29)"""
    if (raiz is None):
        raiz = nodoAVL(dato)
    elif (dato < raiz.info):
        raiz.izq = insertar_nodo_avl(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo_avl(raiz.der, dato)
    
    # Después de insertar, balanceamos el subárbol actual
    raiz = balancear(raiz)
    # Y actualizamos su altura
    actualizar_altura(raiz)
    return raiz

def eliminar_nodo_avl(raiz, clave):
    """Elimina un nodo de un árbol AVL. (Adaptado de pág. 154, Fig. 30)"""
    x = None
    if (raiz is not None):
        if (clave < raiz.info):
            raiz.izq, x = eliminar_nodo_avl(raiz.izq, clave)
        elif (clave > raiz.info):
            raiz.der, x = eliminar_nodo_avl(raiz.der, clave)
        else:
            x = raiz.info
            if (raiz.izq is None):
                raiz = raiz.der
            elif (raiz.der is None):
                raiz = raiz.izq
            else:
                # El nodo a reemplazar es un nodoAVL, por eso usamos eliminar_nodo_avl
                raiz.izq, aux = remplazar_avl(raiz.izq) 
                raiz.info = aux.info
    
    # Después de eliminar, balanceamos y actualizamos altura
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz, x

def remplazar_avl(raiz):
    """Función 'remplazar' adaptada para AVL."""
    aux = None
    if (raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar_avl(raiz.der)
        # Al volver de la recursión, balanceamos
        raiz = balancear(raiz)
        actualizar_altura(raiz)
    return raiz, aux


def main_avl():
    """Ejemplo principal para AVL."""
    print("\n" + "-" * 40)
    print("EJECUCIÓN: ÁRBOL AVL (pág. 149)")
    print("-" * 40)
    
    raiz_avl = None
    # Insertamos datos que causarían un desbalanceo en un ABB simple
    # Ejemplo: 10, 20, 30 (requiere rotación simple izquierda)
    # Ejemplo: 10, 30, 20 (requiere rotación doble izquierda)
    
    print("Insertando datos [10, 20, 30, 5, 1, 25, 35, 40]...")
    datos_avl = [10, 20, 30, 5, 1, 25, 35, 40]
    for dato in datos_avl:
        raiz_avl = insertar_nodo_avl(raiz_avl, dato)

    print("Árbol AVL resultante (auto-balanceado):")
    plot_tree(raiz_avl, "Árbol AVL Auto-Balanceado")

    print("\nEliminando el 1 (hoja)...")
    raiz_avl, _ = eliminar_nodo_avl(raiz_avl, 1)
    print("Eliminando el 10 (nodo con dos hijos)...")
    raiz_avl, _ = eliminar_nodo_avl(raiz_avl, 10)
    print("Árbol AVL después de eliminaciones (sigue balanceado):")
    plot_tree(raiz_avl, "Árbol AVL Después de Eliminar Nodos")


# ---------------------------------------------------------------------------
# BLOQUE PRINCIPAL DE EJECUCIÓN
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    
    # Ejemplo 1: Huffman
    main_huffman()
    
    # Ejemplo 2: Knuth
    main_knuth()
    
    # Ejemplo 3: AVL
    main_avl()