
#clase de lista y nodo lista con sublista

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

    if lista.inicio is None:
        return None

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

def crear_tabla(tamanio):
    """Crea una tabla hash vacía."""
    tabla = [None] * tamanio
    return tabla

def cantidad_elementos(tabla):
    """Devuelve la cantidad de elementos en la tabla."""
    return sum(tamanio(lista) for lista in tabla if lista is not None)

def agregar(tabla, dato):
    """Agrega un elemento a la tabla encadenada."""
    h = funcion_hash(str(dato), len(tabla))
    posicion = funcion_hash(dato, len(tabla))
    print(f"\nElemento: '{dato}' | Hash completo: {h} | Posición en tabla: {posicion}")

    if tabla[posicion] is None:
        tabla[posicion] = lista()
        print(f"[+] '{dato}' insertado en posición {posicion}")
    else:
        print(f"[⚠️ ] Colisión detectada en posición {posicion} con '{dato}'")

    insertar(tabla[posicion], dato)

def buscar_tabla(tabla, buscado):
    """Busca un elemento dentro de la tabla encadenada."""
    h = funcion_hash(str(buscado), len(tabla))
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

def quitar(tabla, dato):
    """Quita un elemento de la tabla encadenada si existe."""
    posicion = funcion_hash(dato, len(tabla))
    elemento_eliminado = None

    if tabla[posicion] is not None:
        # Llama a la función 'eliminar' de la lista enlazada
        elemento_eliminado = eliminar(tabla[posicion], dato)

        # Si la lista en esa posición queda vacía, la eliminamos para limpiar
        if lista_vacia(tabla[posicion]):
            tabla[posicion] = None

    return elemento_eliminado

def funcion_hash(dato, tamanio_tabla):
    """
    Usa la función hash de CUADRADO MEDIO (Mid-Square) 
    combinado con la división.
    """
    
    # 1. Obtener la clave numérica 'k' de 32 bits (usando MurmurHash3)
    #    (Tu código ya convierte 'dato' a str, lo cual es perfecto)
    k = hash_MurmurHash3_32(str(dato))
    
    # 2. Elevar 'k' al cuadrado.
    #    En Python, k (32 bits) * k (32 bits) = k_squared (64 bits)
    k_squared = k * k
    
    # 3. Extraer los 32 bits intermedios (de 64).
    #    Esto se hace desplazando 16 bits a la derecha y 
    #    quedándonos con los 32 bits siguientes.
    #    (Se desplaza (64-32)/2 = 16)
    k_middle = (k_squared >> 16) & 0xFFFFFFFF # 0xFFFFFFFF es la máscara para 32 bits
    
    # 4. Aplicar el método de la división (módulo) al NUEVO hash.
    #    Como discutimos, este paso es inevitable para un tamaño 'm' 
    #    arbitrario, pero ahora lo aplicamos a un número
    #    completamente diferente ('k_middle' en lugar de 'k').
    posicion = k_middle % tamanio_tabla
    
    return posicion

def  hash_MurmurHash3_32(cadena, seed=0):
    """
    Calcula el hash MurmurHash3 de 32 bits de una CADENA (str)
    y lo devuelve como entero.
    """
    # Convertir la cadena a bytes (UTF-8)
    try:
        data = cadena.encode('utf-8')
    except Exception:
        # Fallback por si acaso (aunque str.encode no suele fallar)
        data = bytes(cadena, 'utf-8')

    c1 = 0xcc9e2d51
    c2 = 0x1b873593
    r1 = 15
    r2 = 13
    m = 5
    n = 0xe6546b64

    # Longitud y número de bloques
    length = len(data)
    nblocks = length // 4
    h = seed # Iniciar hash con la semilla

    # --- Procesar bloques de 4 bytes ---
    for i in range(0, nblocks):
        idx = i * 4
        # Leer 4 bytes (little-endian)
        k = (data[idx] & 0xFF) | \
            ((data[idx + 1] & 0xFF) << 8) | \
            ((data[idx + 2] & 0xFF) << 16) | \
            ((data[idx + 3] & 0xFF) << 24)

        # --- Mezcla del bloque ---
        # (Se usa & 0xFFFFFFFF para simular aritmética de 32 bits sin signo)
        k = (k * c1) & 0xFFFFFFFF
        k = ((k << r1) | (k >> (32 - r1))) & 0xFFFFFFFF # ROL32
        k = (k * c2) & 0xFFFFFFFF

        h = h ^ k
        h = ((h << r2) | (h >> (32 - r2))) & 0xFFFFFFFF # ROL32
        h = (h * m + n) & 0xFFFFFFFF

    # --- Procesar la cola (bytes restantes) ---
    tail_index = nblocks * 4
    k = 0
    tail_size = length & 3 # length % 4

    if tail_size == 3:
        k ^= (data[tail_index + 2] & 0xFF) << 16
    if tail_size >= 2: # Cae aquí si es 2 o 3
        k ^= (data[tail_index + 1] & 0xFF) << 8
    if tail_size >= 1: # Cae aquí si es 1, 2 o 3
        k ^= (data[tail_index] & 0xFF)
        
        # --- Mezcla de la cola ---
        k = (k * c1) & 0xFFFFFFFF
        k = ((k << r1) | (k >> (32 - r1))) & 0xFFFFFFFF # ROL32
        k = (k * c2) & 0xFFFFFFFF
        h = h ^ k

    # --- Etapa final (Avalancha/Fmix) ---
    h ^= length
    h = (h ^ (h >> 16)) & 0xFFFFFFFF
    h = (h * 0x85ebca6b) & 0xFFFFFFFF
    h = (h ^ (h >> 13)) & 0xFFFFFFFF
    h = (h * 0xc2b2ae35) & 0xFFFFFFFF
    h = (h ^ (h >> 16)) & 0xFFFFFFFF

    return h



print("=== TABLA HASH CON FUNCIÓN FNV-1a ===")

tamanio_tabla = int(input("Ingrese el tamaño de la tabla hash (>=1): "))
#asignar el tamaño de la tabla
tabla = crear_tabla(tamanio_tabla)

print("\nIngrese valores (deje vacío para terminar):")
#inicializador de los valores de la tabla
valor = input("Valor: ")

while valor != "":
    #mientras el valor no sea vacio, agregar el valor a la tabla
    agregar(tabla, valor)
    valor = input("Valor: ")

print("\n--- Contenido final de la tabla ---")
#imprime la cantidad de elementos en la tabla
print("Cantidad de elementos en la tabla: ", cantidad_elementos(tabla))

#imprime la tabla
#usa la funcion enumerate para imprimir la posicion de la tabla y el slot de la tabla
for i, slot in enumerate(tabla):
    print(f"Posición {i}:", end=" ")
    if slot is not None:
        barrido(slot)
    else:
        print("Vacía")

print("\n--- Búsqueda en la tabla ---")
#obtener el valor a buscar
buscado = input("Ingrese un valor a buscar: ")

#Usar la función que busca en la TABLA COMPLETA
resultado_busqueda = buscar_tabla(tabla, buscado)

if resultado_busqueda is not None:
    # Si se encontró, PREGUNTAR si se quiere eliminar
    respuesta = input("¿Desea quitar el elemento? (s/n): ").lower()
    
    if respuesta == "s":
        # Si la respuesta es sí, INTENTAR quitarlo
        valor_quitado = quitar(tabla, buscado)
        if valor_quitado is not None:
            print(f"✅ Elemento '{valor_quitado}' eliminado exitosamente.")
    else:
        # Si la respuesta es no, no lo elimina
        print("No se elimino el valor buscado.")
        
else:
    # Si no se encontró el valor imprimir 
    print("❌ Elemento no encontrado, no se puede eliminar.")

# Imprimir el estado final de la tabla para mostrar cambios si hay 
print("\n--- Contenido final de la tabla ---")
print("Cantidad de elementos en la tabla:", cantidad_elementos(tabla))
for i, slot in enumerate(tabla):
    print(f"Posición {i}:", end=" ")
    if slot is not None:
        barrido(slot)
    else:
        print("Vacía")