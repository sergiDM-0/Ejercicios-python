# -*- coding: utf-8 -*-
"""
Módulo de Visualización Gráfica
Utiliza 'netgraph' y 'matplotlib' para dibujar cualquier árbol binario
que tenga nodos con atributos .info, .izq, y .der.
"""

import matplotlib.pyplot as plt
from netgraph import Graph

# ---------------------------------------------------------------------------
# ALGORITMO DE LAYOUT N-ARIO (KNUTH / HIJO-IZQ, HERMANO-DER) - v2
# ---------------------------------------------------------------------------

def _process_knuth_nodes(nodo, x_start, y, pos, edges, labels, level_height=2.0, sibling_spacing=2.5):
    """
    Función recursiva mejorada que procesa un nodo y todos sus hermanos
    y devuelve la próxima coordenada 'x' libre en este nivel.
    """
    current_x = x_start
    temp_nodo = nodo # Iterador para la lista de hermanos
    
    while temp_nodo:
        # 1. Posiciona el nodo actual
        pos[temp_nodo] = (current_x, y)
        labels[temp_nodo] = str(temp_nodo.info)
        
        # 2. Procesa a los HIJOS de este nodo (en el nivel inferior)
        child_x_next = current_x # El primer hijo se alinea con el padre por defecto
        if temp_nodo.izq:
            edges.append((temp_nodo, temp_nodo.izq))
            # Esta llamada recursiva procesará al primer hijo Y a todos sus hermanos.
            # Nos devolverá la próxima 'x' libre en el nivel HIJO.
            child_x_next = _process_knuth_nodes(
                temp_nodo.izq, 
                x_start=current_x, # Inicia en la 'x' del padre
                y=y - level_height, 
                pos=pos, edges=edges, labels=labels, 
                level_height=level_height, 
                sibling_spacing=sibling_spacing
            )
        
        # 3. Avanza al SIGUIENTE HERMANO (en el mismo nivel)
        
        # El próximo hermano debe estar a la derecha de:
        # a) El nodo actual (current_x)
        # b) El subárbol de hijos completo del nodo actual (child_x_next)
        # Le sumamos el spacing para que no se peguen.
        next_sibling_x = max(current_x + sibling_spacing, child_x_next + sibling_spacing - 1.0) # Ajuste para que no quede tan lejos
        
        if temp_nodo.der:
            edges.append((temp_nodo, temp_nodo.der))
        
        # Actualiza el 'x' para el siguiente bucle (hermano)
        current_x = next_sibling_x 
        temp_nodo = temp_nodo.der # Mueve el iterador al siguiente hermano
    
    # Devuelve la próxima 'x' libre en ESTE nivel
    return current_x

def _get_knuth_layout_pos(raiz, x=0, y=0, pos=None, edges=None, labels=None, level_height=2.0, sibling_spacing=2.5):
    """Wrapper para inicializar el layout Knuth."""
    if pos is None: pos = {}
    if edges is None: edges = []
    if labels is None: labels = {}
    
    _process_knuth_nodes(
        raiz, x_start=x, y=y, 
        pos=pos, edges=edges, labels=labels, 
        level_height=level_height, 
        sibling_spacing=sibling_spacing
    )
    
    return edges, labels, pos


# ---------------------------------------------------------------------------
# ALGORITMO DE LAYOUT BINARIO (ESTÁNDAR)
# ---------------------------------------------------------------------------
def _get_binary_layout_pos(nodo, x=0, y=0, pos=None, edges=None, labels=None, level_height=1.0):
    """
    Calcula posiciones para un layout de Árbol Binario estándar.
    - .izq = hijo izquierdo
    - .der = hijo derecho
    """
    if pos is None: pos = {}
    if edges is None: edges = []
    if labels is None: labels = {}
    
    pos[nodo] = (x, y)
    labels[nodo] = str(nodo.info)

    ancho_nivel = 2**(abs(y) + 2) # Aumentado para más espacio

    if nodo.izq:
        edges.append((nodo, nodo.izq))
        _get_binary_layout_pos(nodo.izq, x - ancho_nivel / 4, y - level_height, 
                               pos, edges, labels, level_height)
    
    if nodo.der:
        edges.append((nodo, nodo.der))
        _get_binary_layout_pos(nodo.der, x + ancho_nivel / 4, y - level_height, 
                               pos, edges, labels, level_height)
    return edges, labels, pos

# ---------------------------------------------------------------------------
# FUNCIÓN PRINCIPAL DE PLOTEO
# ---------------------------------------------------------------------------
def plot_tree(raiz, title="Visualización del Árbol", layout='binary'):
    """
    Dibuja un árbol binario usando netgraph y matplotlib.
    El 'raiz' debe ser un objeto nodo con .info, .izq, y .der.
    
    Parámetros:
    - raiz: El nodo raíz del árbol a dibujar.
    - title: El título del gráfico.
    - layout: 'binary' (default) o 'knuth' (para árboles n-arios).
    """
    if raiz is None:
        print(f"Árbol '{title}' está vacío. No hay nada que graficar.")
        return

    # Elige el algoritmo de layout correcto
    if layout == 'binary':
        edges, labels, pos = _get_binary_layout_pos(raiz)
    elif layout == 'knuth':
        edges, labels, pos = _get_knuth_layout_pos(raiz)
    else:
        raise ValueError(f"Layout desconocido: '{layout}'. Use 'binary' o 'knuth'.")

    # Aumenta el tamaño de la figura para que no se amontone
    plt.figure(figsize=(20, 10)) 
    ax = plt.subplot(111)
    ax.set_title(title, fontsize=16, fontweight='bold')
    
    g = Graph(edges,
              node_layout=pos,
              node_labels=labels,
              # Ajuste para que las etiquetas no se superpongan tanto
              node_label_fontdict=dict(size=9, weight='bold'),
              node_label_offset=(0, 0.05), # Desplaza la etiqueta un poco hacia arriba
              node_size=6, # Nodos un poco más pequeños
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