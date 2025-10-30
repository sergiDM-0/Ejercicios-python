class lista(object):
    """Define la estructura de una lista simplemente enlazada."""

    def __init__(self):
        """Crea una lista vacía."""
        self.inicio = None
        self.tamanio = 0


class nodoLista(object):
    """Define la estructura de un nodo para la lista."""
    def __init__(self):
        self.info = None
        self.sig = None
        self.sublista = None


def lista_vacia(lista):
    """Devuelve True si la lista está vacía."""
    return lista.inicio is None


def tamanio(lista):
    """Devuelve el número de elementos en la lista."""
    return lista.tamanio


def barrido(lista):
    """Realiza un barrido de la lista mostrando sus valores."""
    aux = lista.inicio
    while aux is not None:
        print(aux.info, end=" -> ")
        aux = aux.sig
    print("None")


def criterio(dato, campo=None):
    """Extrae un valor de un objeto para comparaciones."""
    dic = {}
    if hasattr(dato, '__dict__'):
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
        while (act is not None and criterio(act.info, campo) < criterio(dato, campo)):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1


def buscar(lista, buscado, campo=None):
    """Devuelve el nodo completo del elemento buscado."""
    aux = lista.inicio
    while aux is not None and criterio(aux.info, campo) != criterio(buscado, campo):
        aux = aux.sig
    return aux


def eliminar(lista, clave, campo=None):
    """Elimina un elemento de la lista y devuelve su valor."""
    dato = None
    if (criterio(lista.inicio.info, campo) == criterio(clave, campo)):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    else:
        anterior = lista.inicio
        actual = lista.inicio.sig
        while (actual is not None and criterio(actual.info, campo) != criterio(clave, campo)):
            anterior = anterior.sig
            actual = actual.sig
        if actual is not None:
            dato = actual.info
            anterior.sig = actual.sig
            lista.tamanio -= 1
    return dato


# funcion hash 

def fnv1a_32(key: str) -> int:
    """
    Calcula el hash FNV-1a de 32 bits para una clave.
    Ideal para dispersión en tablas hash.
    """
    # Constantes mágicas para la versión de 32 bits
    FNV_PRIME_32 = 0x01000193
    FNV_OFFSET_BASIS_32 = 0x811c9dc5
    
    hash_val = FNV_OFFSET_BASIS_32
    
    # Procesa cada byte de la clave codificada
    for byte in key.encode('utf-8'):
        hash_val ^= byte
        hash_val *= FNV_PRIME_32
        # Mantiene el valor dentro de los 32 bits
        hash_val &= 0xffffffff 
        
    return hash_val



def crear_tabla(tamanio):
    """Crea una tabla hash vacía."""
    tabla = [None] * tamanio
    return tabla


def cantidad_elementos(tabla):
    """Devuelve la cantidad de elementos en la tabla."""
    return sum(tamanio(lista) for lista in tabla if lista is not None)


def funcion_hash(dato, tamanio_tabla):
    """Usa la función hash de Bernstein para calcular la posición."""
    h = fnv1a_32(str(dato))
    return h % tamanio_tabla


def agregar(tabla, dato):
    """Agrega un elemento a la tabla encadenada."""
    h = fnv1a_32(str(dato))
    posicion = funcion_hash(dato, len(tabla))
    print(f"\nElemento: '{dato}' | Hash completo: {h} | Posición en tabla: {posicion}")

    if tabla[posicion] is None:
        tabla[posicion] = lista()
        print(f"[+] '{dato}' insertado en posición {posicion}")
    else:
        print(f"[⚠️] Colisión detectada en posición {posicion} con '{dato}'")

    insertar(tabla[posicion], dato)


def buscar_tabla(tabla, buscado):
    """Busca un elemento dentro de la tabla encadenada."""
    h = fnv1a_32(str(buscado))
    posicion = funcion_hash(buscado, len(tabla))
    print(f"\nBuscando '{buscado}' | Hash completo: {h} | Posición esperada: {posicion}")
    if tabla[posicion] is not None:
        nodo = buscar(tabla[posicion], buscado)
        if nodo is not None:
            print(f"✅ '{buscado}' encontrado en posición {posicion}")
            return nodo
        else:
            print(f"❌ '{buscado}' no está en la sublista de la posición {posicion}")
    else:
        print(f"❌ No hay lista en la posición {posicion}")
    return None




#implementacion de la tabla hash de fnv1a-1a
# se hace uso implicitamente de la funcion de fnv1a-1a en las funciones agregar y buscar_tabla no se llama directamente la funcion de fnv1a-1a

if __name__ == "__main__":
    print("=== TABLA HASH CON FUNCIÓN DE fnv1a_32 ===")
    tamanio_tabla = int(input("Ingrese el tamaño de la tabla hash: "))
    tabla = crear_tabla(tamanio_tabla)

    print("\nIngrese valores (deje vacío para terminar):")
    valor = input("Valor: ")

    while valor != "":
        agregar(tabla, valor)
        valor = input("Valor: ")

    print("\n--- Contenido final de la tabla ---")
    for i, slot in enumerate(tabla):
        print(f"Posición {i}:", end=" ")
        if slot is not None:
            barrido(slot)
        else:
            print("Vacía")

    print("\n--- Búsqueda en la tabla ---")
    buscado = input("Ingrese un valor a buscar: ")
    buscar_tabla(tabla, buscado)
