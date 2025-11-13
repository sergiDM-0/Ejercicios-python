"""
Módulo de Visualización Gráfica (Versión Final)
Utiliza 'netgraph' y 'matplotlib' para dibujar cualquier árbol binario.

Compatible con:
- Árboles ABB estándar (layout='binary')
- Árboles N-arios/Knuth (layout='knuth')
- Árboles de Huffman (con etiquetas __str__ personalizadas)
- Árboles AVL (layout='binary')
"""

import matplotlib.pyplot as plt
from netgraph import Graph

"""
Módulo de Visualización Gráfica (Versión Final Corregida v4)
Utiliza 'netgraph' y 'matplotlib' para dibujar cualquier árbol binario.

Novedades:
- Corregido error crítico en '_get_binary_layout_pos' que causaba
  que los nodos se superpusieran.
- El layout binario ahora calcula la altura del árbol
  primero para asignar coordenadas X que no colisionan.
"""

import matplotlib.pyplot as plt
from netgraph import Graph

# ---------------------------------------------------------------------------
# ALGORITMO DE LAYOUT N-ARIO (KNUTH / HIJO-IZQ, HERMANO-DER)
# (Esta parte ya estaba bien)
# ---------------------------------------------------------------------------

def _process_knuth_nodes(nodo, x_start, y, pos, edges, labels, level_height=2.0, sibling_spacing=2.5):
    """
    Función recursiva que procesa un nodo y todos sus hermanos
    y devuelve la próxima coordenada 'x' libre en este nivel.
    """
    current_x = x_start
    temp_nodo = nodo
    
    while temp_nodo:
        pos[temp_nodo] = (current_x, y)
        labels[temp_nodo] = str(temp_nodo)
        
        child_x_next = current_x 
        if temp_nodo.izq:
            edges.append((temp_nodo, temp_nodo.izq))
            child_x_next = _process_knuth_nodes(
                temp_nodo.izq, 
                x_start=current_x,
                y=y - level_height, 
                pos=pos, edges=edges, labels=labels, 
                level_height=level_height, 
                sibling_spacing=sibling_spacing
            )
        
        next_sibling_x = max(current_x + sibling_spacing, child_x_next + sibling_spacing - 1.0) 
        
        if temp_nodo.der:
            edges.append((temp_nodo, temp_nodo.der))
        
        current_x = next_sibling_x 
        temp_nodo = temp_nodo.der 
    
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
# ALGORITMO DE LAYOUT BINARIO (ESTÁNDAR) - CORREGIDO
# ---------------------------------------------------------------------------

def _get_tree_height(nodo):
    """Función auxiliar para calcular la altura de un árbol."""
    if nodo is None:
        return -1
    return 1 + max(_get_tree_height(nodo.izq), _get_tree_height(nodo.der))

def _assign_binary_pos(nodo, x, y, pos, edges, labels, level_height, x_offset_map):
    """
    Función recursiva que asigna posiciones usando un offset precalculado.
    """
    if nodo is None:
        return

    pos[nodo] = (x, y)
    labels[nodo] = str(nodo)
    
    current_level = abs(int(y / level_height))
    if current_level + 1 in x_offset_map:
        offset = x_offset_map[current_level + 1]
    else:
        offset = 0 # No hay más niveles

    if nodo.izq:
        edges.append((nodo, nodo.izq))
        _assign_binary_pos(nodo.izq, x - offset, y - level_height, 
                           pos, edges, labels, level_height, x_offset_map)
    
    if nodo.der:
        edges.append((nodo, nodo.der))
        _assign_binary_pos(nodo.der, x + offset, y - level_height, 
                           pos, edges, labels, level_height, x_offset_map)

def _get_binary_layout_pos(raiz, level_height=1.0):
    """
    Calcula posiciones para un layout de Árbol Binario estándar.
    Versión corregida que evita colisiones.
    """
    pos = {}
    edges = []
    labels = {}
    
    # 1. Calcular la altura máxima
    max_height = _get_tree_height(raiz)
    
    # 2. Calcular el offset 'x' para cada nivel
    # El offset en el nivel N será 2^(altura_max - N)
    x_offset_map = {}
    for i in range(max_height + 1):
        x_offset_map[i] = 2**(max_height - i)
    
    # 3. Asignar posiciones recursivamente
    _assign_binary_pos(raiz, x=0, y=0, pos=pos, edges=edges, labels=labels, 
                       level_height=level_height, x_offset_map=x_offset_map)
    
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

    # Ajusta el tamaño de la figura dinámicamente
    min_y = min(y for (x, y) in pos.values()) if pos else 0
    height = max(10, abs(min_y) * 2.5) 
    
    min_x = min(x for (x, y) in pos.values()) if pos else 0
    max_x = max(x for (x, y) in pos.values()) if pos else 0
    width = max(15, abs(max_x - min_x) * 0.5)

    plt.figure(figsize=(width, height)) 
    ax = plt.subplot(111)
    ax.set_title(title, fontsize=16, fontweight='bold')
    
    g = Graph(edges,
              node_layout=pos,
              node_labels=labels,
              node_label_fontdict=dict(size=9, weight='bold', linespacing=0.95),
              node_label_offset=(0, 0), 
              node_size=20,
              node_color='lightcoral',
              node_edge_width=1,
              edge_width=1.5,
              edge_color='black',
              arrows=True,
              ax=ax)
    
    # Ocultar ejes
    ax.set_xticks([])
    ax.set_yticks([])
    plt.box(False)
    plt.show()