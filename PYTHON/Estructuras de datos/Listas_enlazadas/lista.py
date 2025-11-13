class nodoLista(object):
    """Clase nodo lista."""

    info, puntero = None, None


class lista(object):
    """Clase lista simplemente elazada."""

    def __init__(self):
        """Crea una lista vacia."""
        self.inicio = None
        self.tamanio = 0

    def insertar(self, dato):
        "inserta un dato pasad en la lista"
        nodo = nodoLista()
        nodo.info = dato
        if (self.inicio is None) or (self.inicio.info > dato):
            nodo.puntero = self.inicio
            self.inicio = nodo
        else:
            ant = self.inicio
            act = self.inicio.puntero
            while (act is not None and act.info < dato):
                ant = ant.puntero
                act = act.puntero

            nodo.puntero = act
            ant.puntero = nodo
        self.tamanio += 1

    def lista_vacia(self):
        """Devuelve true si la lista esta vacia."""
        return self.inicio is None

    def eliminar(self, clave):
        """Elimina un elemento de la lista y lo devuelve si lo encuentra."""
        dato = None
        if(self.inicio is not None and self.inicio.info == clave):
            dato = self.inicio.info
            self.inicio = self.inicio.puntero
            self.tamanio -= 1
        elif self.inicio is not None:
            anterior = self.inicio
            actual = self.inicio.puntero
            while(actual is not None and actual.info != clave):
                anterior = actual
                actual = actual.puntero
            if (actual is not None):
                dato = actual.info
                anterior.puntero = actual.puntero
                self.tamanio -= 1
        return dato

    def tamanio(self):
        """Devuelve el numero de elementos en la lista."""
        return self.tamanio

    def buscar(self, buscado):
        """Devuelve la direccion del elemento buscado."""
        aux = self.inicio
        while(aux is not None and aux.info != buscado):
            aux = aux.puntero
        return aux

    def barrido(self):
        """Realiza un barrido de la lista mostrando sus valores."""
        aux = self.inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.puntero


#ejemplo lista 

# Crear lista
mi_lista = lista()

# Insertar primer dato
dato = input("ingrese una palabra: ")

while(dato != ''):
    mi_lista.insertar(dato)
    dato = input("ingrese una palabra: ")

# Mostrar punteros de la lista
print('\n--- PUNTEROS DE LA LISTA ---')
print(f'mi_lista.inicio: {mi_lista.inicio}')
print(f'mi_lista.tamanio: {mi_lista.tamanio}')

# Mostrar punteros de cada nodo
aux = mi_lista.inicio
while(aux is not None):
    print(f'\nNodo: {aux}')
    print(f'  info: {aux.info}')
    print(f'  puntero: {aux.puntero}')
    aux = aux.puntero

# Verificar si la lista está vacía
print(f'\n¿Lista vacia? {mi_lista.lista_vacia()}')

# Buscar un elemento
buscado = input("\ningrese la palabra a buscar y elimina la palabra buscada: ")
posicion = mi_lista.buscar(buscado)

if (posicion is not None):
    print(f'\nElemento encontrado:')
    print(f'  Nodo: {posicion}')
    print(f'  info: {posicion.info}')
    print(f'  puntero: {posicion.puntero}')

    # Eliminar el elemento encontrado
    dato = mi_lista.eliminar(posicion.info)
    print(f'\nelemento eliminado: {dato}')
else:
    print("\nno se encontro el elemento a eliminar")

# Mostrar lista actualizada con punteros
print('\n--- PUNTEROS DESPUÉS DE ELIMINAR ---')
print(f'mi_lista.inicio: {mi_lista.inicio}')
print(f'mi_lista.tamanio: {mi_lista.tamanio}')

aux = mi_lista.inicio
while(aux is not None):
    print(f'\nNodo: {aux}')
    print(f'  info: {aux.info}')
    print(f'  puntero: {aux.puntero}')
    aux = aux.puntero

# Barrido final de la lista
print('\n--- BARRIDO FINAL ---')
mi_lista.barrido()