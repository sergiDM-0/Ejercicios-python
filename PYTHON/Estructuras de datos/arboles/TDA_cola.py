# -*- coding: utf-8 -*-
"""
Archivo Base: TDA Cola
Contiene la implementación de la clase Cola y nodo_cola
basada en el código del Capítulo 10.
"""

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
            return None # No se puede atender una cola vacía
        
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
        """Permite usar len(cola)"""
        return self.tamanio