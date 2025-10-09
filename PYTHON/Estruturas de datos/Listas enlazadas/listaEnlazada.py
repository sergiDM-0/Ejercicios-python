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

    
lista = lista()
dato = input("ingrese una palabra: ")

while dato != "":
    lista.insertar(dato)
    dato = input("ingrese una palabra: ")

buscado = input("ingresse la palabra a buscar: ")
posicion = lista.buscar(buscado)

if (posicion is not None):
    dato = lista.eliminar(posicion.info)
    print(f"elemento eliminado: {dato}")
else:
    print("no se encontro el elemento a eliminar ")

lista.barrido()