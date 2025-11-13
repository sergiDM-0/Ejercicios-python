class lista(object):
    """Define la estructura de una lista simplemente enlazada."""

    def __init__(self):
        """Crea una lista vacía."""
        self.inicio = None
        self.tamanio = 0

class nodoLista(object):
    """Define la estructura de un nodo para la lista.
    Cada nodo puede contener una sublista anidada."""
    def __init__(self):
        self.info = None
        self.sig = None
        self.sublista = lista()

def lista_vacia(lista):
    """Devuelve true si la lista esta vacia."""
    return lista.inicio is None

def tamanio(lista):
    """Devuelve el numero de elementos en la lista."""
    return lista.tamanio

def barrido(lista):
    """Realiza un barrido de la lista mostrando sus valores."""
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig

def criterio(dato, campo=None):
    """Extrae un valor de un objeto para ser usado en comparaciones.
    Si se especifica un 'campo', devuelve el valor de ese atributo.
    De lo contrario, devuelve el objeto completo."""
    dic = {}
    if (hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    else:
        return dic[campo]

def insertar(lista, dato, campo=None):
    """Inserta un dato de forma ordenada en la lista."""
    nodo = nodoLista()
    nodo.info = dato
    if (lista.inicio is None) or (criterio(lista.inicio.info, campo) > criterio(dato, campo)):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while(act is not None and criterio(act.info, campo) < criterio(dato, campo)):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1

def buscar(lista, buscado, campo=None):
    """Devuelve el nodo completo del elemento buscado."""
    aux = lista.inicio
    while(aux is not None and criterio(aux.info, campo) != criterio(buscado, campo)):
        aux = aux.sig
    return aux

def eliminar(lista, clave, campo=None):
    """Elimina un elemento de la lista y devuelve su valor."""
    dato = None
    if(criterio(lista.inicio.info, campo) == criterio(clave, campo)):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    else:
        anterior = lista.inicio
        actual = lista.inicio.sig
        while(actual is not None and criterio(actual.info, campo) != criterio(clave, campo)):
            anterior = anterior.sig
            actual = actual.sig
        if (actual is not None):
            dato = actual.info
            anterior.sig = actual.sig
            lista.tamanio -= 1
    return dato


  # codigo del libro funcion hash

# funcion hash de bernstein

def bernstein(cadena):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in cadena:
        h = h * 33 + ord(caracter)
    return h


def crear_tabla(tamanio):
    """Crea una tabla hash vacía."""
    tabla = [None] * tamanio
    return tabla


def cantidad_elementos(tabla):
    """Devuelve la cantidad de elementos en la tabla."""
    return sum(tamanio(lista) for lista in tabla if lista is not None)


def funcion_hash(dato, tamanio_tabla):
    """Determina la posición del dato en la tabla."""
    # hash por división para este caso
    return len(str(dato).strip()) % tamanio_tabla


def agregar(tabla, dato):
    """Agrega un elemento a la tabla encadenada."""
    posicion = funcion_hash(dato, len(tabla))
    if (tabla[posicion] is None):
        tabla[posicion] = lista()
    insertar(tabla[posicion], dato)


def agregar(tabla, dato):
    """Agrega un elemento a la tabla cerrada."""
    posicion = funcion_hash(dato, len(tabla))
    if (tabla[posicion] is None):
        tabla[posicion] = dato
    else:
        print('se produjo una colisión')
        # ejecutar función de sondeo para reubicar elemento


def buscar(tabla, buscado):
    """Determina si un elemento existe en la tabla y determina su posición."""
    pos = None
    posicion = funcion_hash(buscado, len(tabla))
    if (tabla[posicion] is not None):
        pos = buscar(tabla[posicion], buscado)
    return pos


def buscar(tabla, buscado):
    """Determina si un elemento existe en la tabla y determina su posición."""
    pos = None
    posicion = funcion_hash(buscado, len(tabla))
    if (tabla[posicion] is not None):
        if (buscado == tabla[posicion]):
            pos = posicion
        else:
            print('aplicar función de sondeo')
            # para determinar si está en otra posición
    return pos


def quitar(tabla, dato):
    """Quita un elemento de la tabla encadenada si existe."""
    dato = None
    posicion = funcion_hash(dato, len(tabla))
    if (tabla[posicion] is not None):
        dato = eliminar(tabla[posicion], dato)
        if (lista_vacia(tabla[posicion])):
            tabla[posicion] = None
    return dato


def quitar(tabla, dato):
    """Quita un elemento de la tabla cerrada si existe."""
    dato = None
    posicion = funcion_hash(dato, len(tabla))
    if (tabla[posicion] is not None):
        if (dato == tabla[posicion]):
            dato = tabla[posicion]
            tabla[posicion] = None
        else:
            print('aplicar función de sondeo')
            # para determinar si está en otra posición y quitarlo
    return dato



#implementacion de la tabla hash de bernstein

tabla = crear_tabla(3)

nombre = input('ingrese nombre ')

while (nombre != ''):
    agregar(tabla, nombre)
    nombre = input('ingrese nombre ')

buscado = input('ingrese el nombre a buscar ')
posicion = buscar(tabla, buscado)
if (posicion is not None):
    print('elemento encontrado', posicion)
else:
    print('no se encontro el elemento buscado')

