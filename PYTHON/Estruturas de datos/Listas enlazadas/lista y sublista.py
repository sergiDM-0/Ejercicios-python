class lista(object):
    """Define la estructura de una lista simplemente enlazada."""

    def __init__(self):
        """Crea una lista vacía."""
        self.inicio = None
        self.tamanio = 0

class nodoLista(object):
    """Define la estructura de un nodo para la lista.
    Cada nodo puede contener una sublista anidada."""

    info, sig = None, None
    sublista = lista()

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



#implementacion

estaciones = lista()

while True:
    dato = input('Ingrese nombre de la estación (enter para salir): ')
    if dato == "":
        break
    # Verifica si ya existe la estación, si no la inserta
    nodo_estacion = buscar(estaciones, dato)
    if nodo_estacion is None:
        insertar(estaciones, dato)
        nodo_estacion = buscar(estaciones, dato)
    # Asegura que la sublista exista
    if not hasattr(nodo_estacion, "sublista"):
        nodo_estacion.sublista = lista()
    while True:
        estado_clima = input(f'Cargar estado del clima para "{dato}" (enter para salir de esta estación): ')
        if estado_clima == "":
            break
        insertar(nodo_estacion.sublista, estado_clima)
    print(f'\nDatos de la estación "{dato}":')
    barrido(nodo_estacion.sublista)

# Se busca una estación para mostrar los datos de su sublista
while True:
    buscado = input('Ingrese nombre de la estación a listar (enter para salir): ')
    if buscado == "":
        break
    pos = buscar(estaciones, buscado)
    if(pos is not None):
        print(f'Climas registrados en "{buscado}":')
        barrido(pos.sublista)
    else:
        print(f'No se encontró la estación "{buscado}".')