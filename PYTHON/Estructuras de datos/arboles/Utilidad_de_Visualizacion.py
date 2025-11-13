# -*- coding: utf-8 -*-
"""
Módulo de Visualización Gráfica
Utiliza 'netgraph' y 'matplotlib' para dibujar cualquier árbol binario
que tenga nodos con atributos .info, .izq, y .der.
"""

import matplotlib.pyplot as plt
from netgraph import Graph

def _get_edges_labels_pos(nodo, x=0, y=0, pos=None, edges=None, labels=None, level_height=1.0):
    """Función auxiliar recursiva para construir la estructura del gráfico."""
    if pos is None:
        pos = {}
    if edges is None:
        edges = []
    if labels is None:
        labels = {}

    pos[nodo] = (x, y)
    labels[nodo] = str(nodo.info) # Usa el __str__ del nodo

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
    El 'raiz' debe ser un objeto nodo con .info, .izq, y .der.
    """
    if raiz is None:
        print(f"Árbol '{title}' está vacío. No hay nada que graficar.")
        return

    edges, labels, pos = _get_edges_labels_pos(raiz)
    
    plt.figure(figsize=(16, 8))
    ax = plt.subplot(111)
    ax.set_title(title, fontsize=16, fontweight='bold')
    
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
    
    ax.set_xticks([])
    ax.set_yticks([])
    plt.box(False)
    plt.show()