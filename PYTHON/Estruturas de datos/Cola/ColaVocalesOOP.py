class nodo_cola(object):
    """Clase nodo cola."""
    def __init__(self, info=None, apuntador=None):
        self.info = info
        self.apuntador = apuntador

class cola(object):
    """Clase Cola."""

    def __init__(self):
        """Crea una cola vacía."""
        self.frente, self.final = None, None
        self.tamanio = 0


    def arribo(self,dato):
      "agrega el dato al final de la cola"
      nodo = nodo_cola(dato)

      if self.frente is None:
        self.frente = nodo
        self.final = nodo
      else:
        self.final.apuntador = nodo
        self.final = nodo
      self.tamanio += 1

    def atencion(self):
      "atiende el elemento en frente de la cola y lo devuelve"
      dato = self.frente.info
      self.frente = self.frente.apuntador

      if self.frente is None:
        self.final = None
      self.tamanio -= 1
      return dato

    def cola_vacia(self):
      "devuelve true si la cola esta vacia"
      return self.frente is None

    def en_frente(self):
      "devuelve el valor almacenado en el frente de la cola"
      return self.frente.info


    def obtener_tamanio(self):
      "devuelve el numero de elementos en la cola"
      return self.tamanio

    def mover_al_final(self):
      "mueve el elemento del frente de la cola al final de la cola"
      dato = self.atencion()
      self.arribo(dato)
      return dato

    def barrido1(self):
      "muestra el contenido de una cola sin perder datos (n^2)"
      caux = cola()
      while (not self.cola_vacia()):
        dato = self.atencion()
        print(dato)
        caux.arribo(dato)

      while (not caux.cola_vacia()):
        dato = caux.atencion()
        self.arribo(dato)

    def barrido2(self):
      "muestra el contenido de una cola sin perder datos O(n)"
      i = 0
      while (i < self.tamanio):
        dato = self.mover_al_final()
        print(dato)
        i += 1

"""
cdatos = cola()
cvocales = cola()

letra = input("ingrese un caracter (enter para salir) :  ")
while (letra != ''):
  cdatos.arribo(letra)
  letra = input("ingrese un caracter (enter para salir) : ")

while (not cdatos.cola_vacia()):
  letra = cdatos.atencion()
  if letra.upper() in ["A",'E','I','O','U']:
    cvocales.arribo(letra)

print("Datos cola Vocales")
while (not cvocales.cola_vacia()):
  dato = cvocales.atencion()
  print(dato)
"""

cdatos = cola()
cvocales = cola()

#agrar los datos de la cola primero al final de la cola 

letra = input("Ingrese un caracter (Enter para salir): ")
while (letra != ''):
  cdatos.arribo(letra)
  letra = input("Ingrese un caracter (Enter para salir): ")

print("\n---------------------------------------\n")

#mostar el tamaño de la cola inicial 
print(f"La cola de datos tiene {cdatos.obtener_tamanio()} elementos.")

#primer dato que saldra de la cola 
print(f"El elemento que está en el frente es: {cdatos.en_frente()}")

print("\n---------------------------------------\n")

#imprimir la cola inicial 
print(" Mostrando contenido con el método de barrido eficiente:")
cdatos.barrido2()
print(f"Tamaño de la cola inicial: {cdatos.obtener_tamanio()}.")

print("\n---------------------------------------\n")

#cambiar el primer dato de la cola al final de la cola 
print("Moviendo el elemento del frente al final...")
elemento_movido = cdatos.mover_al_final()
print(f"Se movió el elemento {elemento_movido} al final de la cola.")
#nuevo siguiente en salir de la cola
print(f"Ahora, el nuevo elemento en el frente es: {cdatos.en_frente()}\n")
print(f"la cola de datos ahora es ")
cdatos.barrido2()
print("\n---------------------------------------\n")


print("Separando las vocales de la cola principal...")
while not cdatos.cola_vacia():
  # Se saca un elemento con atencion()
  letra = cdatos.atencion()
  if letra.upper() in ["A",'E','I','O','U']:
    #agrega la vocal a la cola de vocales 
    cvocales.arribo(letra)

print(f"La cola de vocales ahora tiene {cvocales.obtener_tamanio()} elementos.")

print("\n---------------------------------------\n")

#mostrar la cola de vocales
print("Mostrando el contenido de la cola de vocales: ")
cvocales.barrido1()

print("\n---------------------------------------\n")


#empty stacks
print("stack final es: ")
print(f"el tamaño de la cola de vocales es: {cvocales.obtener_tamanio()}")


