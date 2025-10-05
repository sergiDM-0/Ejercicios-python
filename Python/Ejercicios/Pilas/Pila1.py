class NodoPila(object):
    """Clase que crea un nodo para la pila."""
    def __init__(self, info):
        # Cada nodo guarda la información (el dato)
        self.info = info
        # y una referencia al siguiente nodo
        self.sig = None

class Pila(object):
    """
    Clase que define la estructura y todas las operaciones de una Pila.
    """

    def __init__(self):
        """Crea una pila vacía."""
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato):
        """Apila un dato sobre la cima de la pila."""
        # Creamos un nodo y le pasamos el dato a guardar
        nodo = NodoPila(dato)
        # El nuevo nodo apunta a la cima anterior
        nodo.sig = self.cima
        # La cima de la pila ahora es el nuevo nodo
        self.cima = nodo
        # Incrementamos el tamaño
        self.tamanio += 1

    def desapilar(self):
        """Desapila el elemento en la cima, lo elimina y lo devuelve."""
        # Guardamos la información del nodo que está en la cima
        x = self.cima.info
        # La cima ahora es el nodo al que apuntaba la cima anterior
        self.cima = self.cima.sig
        # Decrementamos el tamaño
        self.tamanio -= 1
        return x

    def pila_vacia(self):
        """Devuelve True si la pila está vacía."""
        return self.cima is None

    def en_cima(self):
        """Devuelve el valor almacenado en la cima sin quitarlo."""
        if not self.pila_vacia():
            return self.cima.info
        else:
            return None

    def get_tamanio(self):
        """Devuelve el número de elementos en la pila."""
        return self.tamanio

    def barrido(self):
        """Muestra el contenido de la pila sin perder los datos."""
        paux = Pila()
        print("Contenido de la pila (desde la cima):")
        # Vaciamos la pila original y mostramos cada elemento
        while not self.pila_vacia():
            dato = self.desapilar()
            print(dato)
            paux.apilar(dato)
        # Restauramos la pila original a partir de la pila auxiliar
        while not paux.pila_vacia():
            dato = paux.desapilar()
            self.apilar(dato)

# ---------------------------------------------------------------------------
# SECCIÓN 2: BLOQUE PRINCIPAL DE EJECUCIÓN
# ---------------------------------------------------------------------------


print("--- DEMOSTRACIÓN DE TODOS LOS MÉTODOS DE LA PILA ---")

# El método __init__ se usa aquí al crear el objeto
pila_demo = Pila()
print("1. Se ha creado una pila vacía usando el método __init__.")

# Método: pila_vacia() en una pila vacía
print(f"\n2. ¿La pila está vacía? -> pila_vacia(): {pila_demo.pila_vacia()}")

# Método: get_tamanio() en una pila vacía
print(f"3. ¿Cuál es su tamaño? -> get_tamanio(): {pila_demo.get_tamanio()}")

# Método: apilar()
print("\n4. Apilando los elementos 10, 20 y 30 -> apilar():")
pila_demo.apilar(10)
pila_demo.apilar(20)
pila_demo.apilar(30)

# Método: pila_vacia() en una pila con datos
print(f"\n5. ¿La pila sigue vacía? -> pila_vacia(): {pila_demo.pila_vacia()}")

# Método: get_tamanio() en una pila con datos
print(f"6. ¿Cuál es su tamaño ahora? -> get_tamanio(): {pila_demo.get_tamanio()}")

# Método: en_cima()
print(f"7. ¿Qué elemento está en la cima? -> en_cima(): {pila_demo.en_cima()}")
print(f"   (El tamaño no cambia: {pila_demo.get_tamanio()})")

# Método: barrido()
print("\n8. Mostrando todos los elementos -> barrido():")
pila_demo.barrido()
print("   (La pila original no se ha modificado después del barrido)")

# Método: desapilar()
print("\n9. Desapilando un elemento -> desapilar():")
elemento_quitado = pila_demo.desapilar()
print(f"   < Se desapiló y devolvió el elemento: {elemento_quitado}")

# Verificamos los cambios
print(f"10. ¿Cuál es la nueva cima? -> en_cima(): {pila_demo.en_cima()}")
print(f"11. ¿Cuál es el nuevo tamaño? -> get_tamanio(): {pila_demo.get_tamanio()}")
print("\n--- Fin de la demostración ---")

"""

# Creamos las tres pilas que necesitamos
pdatos = Pila()
ppar = Pila()
pimpar = Pila()

# Pedimos al usuario que ingrese números
print("Ingrese números enteros. Ingrese 0 para terminar.")
dato = int(input("Ingrese un número: "))

while dato != 0:
    pdatos.apilar(dato)
    dato = int(input("Ingrese un número: "))

# Vaciamos la pila principal (pdatos) y separamos sus números en la pila de pares (ppar)
# y la de impares (pimpar)
while not pdatos.pila_vacia():
    dato = pdatos.desapilar()
    if dato % 2 == 0:
        ppar.apilar(dato)
    else:
        pimpar.apilar(dato)

# Mostramos los resultados finales vaciando las pilas de pares e impares
print("\n--- Resultados ---")
print("Números Pares (mostrados desde el último ingresado):")
while not ppar.pila_vacia():
    print(ppar.desapilar())

print("\nNúmeros Impares (mostrados desde el último ingresado):")
while not pimpar.pila_vacia():
    print(pimpar.desapilar())
"""