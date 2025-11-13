# -*- coding: utf-8 -*-
"""
Archivo Base: TDA Árbol Binario de Búsqueda (ABB)
Contiene la clase nodoArbol y las funciones básicas de un ABB
descritas en el Capítulo 10 (págs. 140-144).
"""

from TDA_cola import Cola # Necesario para el barrido por nivel

# --- Clase Árbol ---
class nodoArbol(object):
    """Clase nodo árbol."""

    def __init__(self, info):
        """Crea un nodo con la información cargada."""
        self.izq = None
        self.der = None
        self.info = info

    def __str__(self):
        """Facilita la visualización en netgraph."""
        return str(self.info)

# --- Funciones de la Clase Árbol ---

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

# --- Barridos ---

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