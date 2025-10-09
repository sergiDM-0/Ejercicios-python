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

"""
# --- Código de ejemplo ---
estaciones = lista()

dato = input('Ingrese nombre de la estación: ')
insertar(estaciones, dato)

# Se busca la estación recién creada para agregarle datos a su sublista
estacion = buscar(estaciones, dato)
if(estacion is not None):
    estado_clima = input('Cargar estado del clima: ')
    insertar(estacion.sublista, estado_clima)

# Se busca una estación para mostrar los datos de su sublista
buscado = input('Ingrese nombre de la estación a listar: ')
pos = buscar(estaciones, buscado)
if(pos is not None):
    barrido(pos.sublista)
"""

# ========================================================================================
# EXTENSIÓN: Múltiples estaciones con múltiples estados de clima
# ========================================================================================

# Crear lista de estaciones
estaciones_clima = lista()

# Cargar primera estación
dato = input('Ingrese nombre de la estación: ')
insertar(estaciones_clima, dato)

# Agregar estados del clima a la primera estación
estacion = buscar(estaciones_clima, dato)
if(estacion is not None):
    estado_clima = input('Cargar estado del clima: ')
    insertar(estacion.sublista, estado_clima)
    estado_clima = input('Cargar estado del clima: ')
    insertar(estacion.sublista, estado_clima)

# Cargar segunda estación
dato = input('Ingrese nombre de la estación: ')
insertar(estaciones_clima, dato)

# Agregar estados del clima a la segunda estación
estacion = buscar(estaciones_clima, dato)
if(estacion is not None):
    estado_clima = input('Cargar estado del clima: ')
    insertar(estacion.sublista, estado_clima)
    estado_clima = input('Cargar estado del clima: ')
    insertar(estacion.sublista, estado_clima)

# Cargar tercera estación
dato = input('Ingrese nombre de la estación: ')
insertar(estaciones_clima, dato)

# Agregar estados del clima a la tercera estación
estacion = buscar(estaciones_clima, dato)
if(estacion is not None):
    estado_clima = input('Cargar estado del clima: ')
    insertar(estacion.sublista, estado_clima)

# Mostrar punteros de la lista principal
print('\n--- PUNTEROS LISTA PRINCIPAL ---')
print(f'estaciones_clima.inicio: {estaciones_clima.inicio}')
print(f'estaciones_clima.tamanio: {estaciones_clima.tamanio}')

# Mostrar punteros de cada nodo y sus sublistas
aux = estaciones_clima.inicio
while(aux is not None):
    print(f'\nNodo estacion: {aux}')
    print(f'  info: {aux.info}')
    print(f'  sig: {aux.sig}')
    print(f'  sublista.inicio: {aux.sublista.inicio}')
    
    # Mostrar punteros de la sublista
    aux2 = aux.sublista.inicio
    while(aux2 is not None):
        print(f'    Nodo clima: {aux2}')
        print(f'      info: {aux2.info}')
        print(f'      sig: {aux2.sig}')
        aux2 = aux2.sig
    
    aux = aux.sig

# Listar todas las estaciones con sus climas
print('\n--- LISTAR ESTACIONES Y CLIMAS ---')
aux = estaciones_clima.inicio
while(aux is not None):
    print(f'\nEstacion: {aux.info}')
    barrido(aux.sublista)
    aux = aux.sig