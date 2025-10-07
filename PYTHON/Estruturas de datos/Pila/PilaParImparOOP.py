class nodoPila(object):
    """Clase nodo pila."""
    def __init__(self, info=None, apuntador=None):
        self.info = info
        self.apuntador = apuntador

class Pila(object):
    """Clase Pila."""

#pdatos.apilar(10)

    def __init__(self):
        """Crea una pila vacía."""
        self.cima = None
        self.tamano = 0

    def apilar(self, dato):
        """Apila el dato sobre la cima de la pila."""
        nodo = nodoPila(dato) 
        nodo.apuntador = self.cima
        self.cima = nodo
        self.tamano += 1

    def desapilar(self):
        """Desapila el elemento en la cima de la pila y lo devuelve."""
        if self.cima is not None:
            x = self.cima.info
            self.cima = self.cima.apuntador
            self.tamano -= 1
            return x
        return None 

    def pila_vacia(self):
        """Devuelve true si la pila esta vacia."""
        return self.cima is None

    def en_cima(self):
        """Devuelve el valor almacenado en la cima de la pila."""
        if self.cima is not None:
            return self.cima.info
        else:
            return None

    def tamanio(self):
        """Devuelve el numero de elementos en la pila."""
        return self.tamano

    def barrido(self):
        """Muestra el contenido de una pila sin perder datos."""
        paux = Pila()
        
        while (not self.pila_vacia()):
            dato = self.desapilar()
            print(dato)
            paux.apilar(dato)

        while (not paux.pila_vacia()):
            dato = paux.desapilar()
            self.apilar(dato)
        return paux

# crea la tres pilas 
pdatos = Pila()
ppar = Pila()
pimpar = Pila()

# Pedimos al usuario que ingrese números
print("Ingrese números enteros. Ingrese 0 para terminar.")
dato = int(input("Ingrese un número: "))


while dato != 0:
    pdatos.apilar(dato)
    dato = int(input("Ingrese un número: "))

#guarda la pila inicial
print("stack inicial es: ")
pdatos.barrido()

# Vaciamos la pila principal (pdatos) y separamos sus números en la pila de pares (ppar)
# y la de impares (pimpar)

while (not pdatos.pila_vacia()):
    
    #Guardamos una referencia al nodo que está en la cima.
    nodo_anterior = pdatos.cima
    
    #para comprobar la cima
    print(f"la cima es {pdatos.en_cima()} : {pdatos.cima}")

    #Desapilamos el valor. Esto actualiza pdatos.cima para que apunte
    #al siguiente nodo.
    dato = pdatos.desapilar()

    #para comprobar la cima
    print(f"la cima es {pdatos.en_cima()} : {pdatos.cima}")

    
    #nodo_anterior.apuntador' es el puntero al siguiente nodo en la lista.
    print(f"Se desapiló el valor: {dato}\n")
    
    #se muestra el puntero del nodo anterior
    print(f"  -> El puntero de su nodo apuntaba a: {nodo_anterior.apuntador}\n")

    #si es none es el fondo de la pila
    if nodo_anterior.apuntador is None:
        print("Era el fondo de la pila\n")

    if dato % 2 == 0:
        ppar.apilar(dato)
    else:
        pimpar.apilar(dato)
    
print(f"el tamaño de la pila de pares es: {ppar.tamanio()}")
print(f"el tamaño de la pila de impares es: {pimpar.tamanio()}")

while (not ppar.pila_vacia()):
    dato = ppar.desapilar()
    print(f"el numero par es: {dato}")

while (not pimpar.pila_vacia()):
    dato = pimpar.desapilar()
    print(f"el numero impar es: {dato}")


#empty stacks
print("stack final es: ")
print(f"el tamaño de la pila de pares es: {ppar.tamanio()}")
print(f"el tamaño de la pila de impares es: {pimpar.tamanio()}")

