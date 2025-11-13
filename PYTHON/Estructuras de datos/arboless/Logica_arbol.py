"""
TDA Base (Capítulo 10)

Contiene las clases y funciones corregidas para:
1. TDA Cola (necesario para el barrido por nivel)
2. TDA Árbol Binario de Búsqueda (ABB)
"""

# ----------------------------------------
# CLASE COLA (TDA Cola)
# ----------------------------------------

class nodoCola(object):
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
        nodo = nodoCola(dato)
        if self.frente is None:
            self.frente = nodo
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

# ----------------------------------------
# CLASE ÁRBOL (TDA ABB)
# ----------------------------------------

class nodoArbol(object):
    """Clase nodo árbol."""
    def __init__(self, info):
        """Crea un nodo con la información cargada."""
        self.izq = None
        self.der = None
        self.info = info
    
    def __str__(self):
        """Define cómo se debe 'imprimir' el nodo."""
        return str(self.info)

# ----------------------------------------
# FUNCIONES DEL TDA ABB
# ----------------------------------------

#Agrega el elemento al árbol
def insertar_nodo(raiz, dato):
    """Inserta un dato al árbol."""
    if (raiz is None):
        raiz = nodoArbol(dato)
    elif (dato < raiz.info):
        raiz.izq = insertar_nodo(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

#Devuelve verdadero (true) si el árbol no contiene elementos
def arbolvacio(raiz):
    """Devuelve True si el árbol está vacío."""
    return raiz is None


#Determina el nodo que reemplazará al que se va a eliminar, esta es una fun-
#ción interna que solo es utilizada por la función eliminar;
def remplazar(raiz):
    """Determina el nodo que reemplazará al que se elimina."""
    aux = None
    if (raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux


#Elimina y devuelve del árbol si encuentra un elemento que coincida
#con la clave dada –el primero que encuentre–, si devuelve None significa que no se encontró la
#clave en el árbol, y por ende no se elimina ningún elemento
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


#Devuelve un puntero que apunta al nodo que contiene un elemento que
#coincida con la clave –el primero que encuentra–, si devuelve None significa que no se encontró
#la clave en el árbol
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

#Realiza un recorrido de orden previo del árbol mostrando la información de los
#elementos almacenados en el árbol
def preorden(raiz):
    """Realiza el barrido preorden del árbol."""
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

#Realiza un recorrido en orden del árbol mostrando la información de los ele-
#mentos almacenados en el árbol;
def inorden(raiz):
    """Realiza el barrido inorden del árbol."""
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

#Realiza un recorrido de orden posterior del árbol mostrando la información
#de los elementos almacenados en el árbol.
def postorden(raiz):
    """Realiza el barrido postorden del árbol."""
    if(raiz is not None):
        postorden(raiz.izq)
        postorden(raiz.der)
        print(raiz.info)

#Realiza un recorrido del árbol por nivel mostrando la información de los ele-
#mentos almacenados.
def por_nivel(raiz):
    """Realiza el barrido por niveles del árbol."""
    if raiz is None:
        print("Árbol vacío")
        return
        
    # CORRECCIÓN: Se debe crear un objeto Cola y llamar a sus métodos
    pendientes = Cola()
    pendientes.arribo(raiz)
    
    while (not pendientes.cola_vacia()):
        nodo = pendientes.atencion()
        print(nodo.info)
        
        if (nodo.izq is not None):
            pendientes.arribo(nodo.izq)
        if (nodo.der is not None):
            pendientes.arribo(nodo.der)