# -*- coding: utf-8 -*-
"""
Ejemplo 3: Árbol AVL (págs. 149-154)
Implementación de un Árbol Binario de Búsqueda Auto-Balanceado (AVL).
"""

from TDA_Arbol_Binario_de_Busqueda__ABB_ import nodoArbol # Importamos la clase base
from Utilidad_de_Visualizacion import plot_tree # Importamos la función de ploteo

class nodoAVL(nodoArbol):
    """
    Clase nodo para Árbol AVL. Hereda de nodoArbol y añade 'altura'.
    (pág. 150, Fig. 20)
    """
    def __init__(self, info):
        super().__init__(info)
        self.altura = 0 # La altura de un nodo hoja nuevo es 0

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

        if (alt_izq - alt_der) == 2: 
            # Desbalanceo a la izquierda
            if (obtener_altura(raiz.izq.izq) >= obtener_altura(raiz.izq.der)):
                raiz = rotar_simple(raiz, True) # Rotación simple derecha
            else:
                raiz = rotar_doble(raiz, True) # Rotación doble derecha
        elif (alt_der - alt_izq) == 2:
            # Desbalanceo a la derecha
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
    
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz

def remplazar_avl(raiz):
    """Función 'remplazar' adaptada para AVL que rebalancea."""
    aux = None
    if (raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar_avl(raiz.der)
        raiz = balancear(raiz)
        actualizar_altura(raiz)
    return raiz, aux

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
                raiz.izq, aux = remplazar_avl(raiz.izq) 
                raiz.info = aux.info
    
    if raiz is not None:
      raiz = balancear(raiz)
      actualizar_altura(raiz)
    return raiz, x

def main_avl():
    """Ejecución principal del ejemplo de AVL."""
    print("\n" + "-" * 40)
    print("EJECUCIÓN: ÁRBOL AVL (pág. 149)")
    print("-" * 40)
    
    raiz_avl = None
    
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

if __name__ == "__main__":
    # Para ejecutar este archivo:
    # 1. Asegúrate de tener tda_abb.py, tda_cola.py y visualizador_arbol.py
    #    en la misma carpeta.
    # 2. Ejecuta: python ejemplo_avl.py
    main_avl()