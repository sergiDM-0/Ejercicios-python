



#nodo arbol AVL
class nodoArbol(object):
    """Clase nodo árbol."""

    def __init__(self, info):
        """Crea un nodo con la información cargada."""
        self.izq = None
        self.der = None
        self.info = info
        self.altura = 0


def altura(raiz):
    """Devuelve la altura de un nodo."""
    if(raiz is None):
        return -1
    else:
        return raiz.altura


def actualizaraltura(raiz):
    """Actualiza la altura de un nodo."""
    if(raiz is not None):
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1


def rotar_simple(raiz, control):
    """Realiza una rotación simple de nodos a la derecha o a la izquierda."""
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz

    actualizaraltura(raiz)
    actualizaraltura(aux)
    raiz = aux
    return raiz

def rotar_doble(raiz, control):
    """Realiza una rotación doble de nodos a la derecha o a la izquierda."""
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz

def balancear(raiz):
    """Determina que rotación hay que hacer para balancear el árbol."""
    if(raiz is not None):
        if(altura(raiz.izq) - altura(raiz.der) == 2):
            if(altura(raiz.izq.izq) >= altura(raiz.izq.der)):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif(altura(raiz.der) - altura(raiz.izq) == 2):
            if(altura(raiz.der.der) >= altura(raiz.der.izq)):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return raiz

def insertar_nodo(raiz, dato, pos):
    """Inserta un dato al árbol."""
    if(raiz is None):
        raiz = nodoArbol(dato, pos)
    elif(dato < raiz.info):
        raiz.izq = insertar_nodo(raiz.izq, dato, pos)
    else:
        raiz.der = insertar_nodo(raiz.der, dato, pos)
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz

def eliminar_nodo(raiz, clave):
    """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
    x = None
    if(raiz is not None):
        if(clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif(clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info, raiz.nrr = aux.info, aux.nrr
        raiz = balancear(raiz)
        actualizaraltura(raiz)
    return raiz, x


raiz = None
i = 0
pais = input('ingrese nombre del pais a cargar: ')
while(pais != '' and i < 21):
    raiz = insertar_nodo(raiz, pais)
    i += 1
    pais = input('ingrese nombre del pais a cargar: ')

inorden(raiz)
pais = input('ingrese nombre del pais a eliminar: ')
raiz, dato = eliminar_nodo(raiz, pais)
if(dato is not None):
    print('País eliminado:', dato)

pos = buscar(raiz, 'Tailandia')
if(pos is not None):
    raiz, dato = eliminar_nodo(raiz, 'Tailandia')
    dato = 'Tailandia'
    raiz = insertar_nodo(raiz, dato)

inorden(raiz)
raiz = None
i = 0
pais = input('ingrese nombre del pais a cargar: ')
while(pais != '' and i < 21):
    raiz = insertar_nodo(raiz, pais)
    i += 1
    pais = input('ingrese nombre del pais a cargar: ')

inorden(raiz)
pais = input('ingrese nombre del pais a eliminar: ')
raiz, dato = eliminar_nodo(raiz, pais)
if(dato is not None):
    print('País eliminado:', dato)

pos = buscar(raiz, 'Tailandia')
if(pos is not None):
    raiz, dato = eliminar_nodo(raiz, 'Tailandia')
    dato = 'Tailandia'
    raiz = insertar_nodo(raiz, dato)

inorden(raiz)
