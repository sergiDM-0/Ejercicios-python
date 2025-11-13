# clase cola
class Cola(object):
    """Clase Cola."""

    def __init__(self):
        """Crea una cola vacía."""
        self.frente, self.final = None, None
        self.tamanio = 0 

class nodo_cola(object):

    """Clase nodo cola."""
    def __init__(self, info=None, apuntador=None):
        self.info = info
        self.apuntador = apuntador

# funciones de la clase cola
def arribo(self,dato):
      "agrega el dato al final de la cola"
      nodo = nodo_cola(dato)

      if self.frente is None:
        self.frente = nodo
        self.final = nodo
      else:
        self.final.apuntador = nodo
        self.final = nodo
      self.tamanio += 1

def atencion(self):
      "atiende el elemento en frente de la cola y lo devuelve"
      dato = self.frente.info
      self.frente = self.frente.apuntador

      if self.frente is None:
        self.final = None
      self.tamanio -= 1
      return dato

def cola_vacia(self):
    "devuelve true si la cola esta vacia"
    return self.frente is None


#clase arbol
class nodoArbol(object):
    """Clase nodo árbol."""

    def __init__(self, info):
        """Crea un nodo con la información cargada."""
        self.izq = None
        self.der = None
        self.info = info


# funciones de la clase arbol
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


def por_nivel(raiz):
    """Realiza el barrido por niveles del árbol."""
    pendientes = Cola()
    arribo(pendientes, raiz)
    while (not cola_vacia(pendientes)):
        nodo = atencion(pendientes)
        print(nodo.info)
        if (nodo.izq is not None):
            arribo(pendientes, nodo.izq)
        if (nodo.der is not None):
            arribo(pendientes, nodo.der)


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


def por_nivel(raiz):
    """Realiza el barrido por niveles del árbol."""
    pendientes = Cola()
    arribo(pendientes, raiz)
    while (not cola_vacia(pendientes)):
        nodo = atencion(pendientes)
        print(nodo.info)
        if (nodo.izq is not None):
            arribo(pendientes, nodo.izq)
        if (nodo.der is not None):
            arribo(pendientes, nodo.der)


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

