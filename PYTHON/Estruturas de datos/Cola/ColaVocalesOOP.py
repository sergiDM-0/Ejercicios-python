class nodo_cola(object):
    """Clase nodo cola."""
    def __init__(self, info=None, apuntador=None):
        self.info = info
        self.apuntador = apuntador

class Cola(object):
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
      

    def tamanio(self):
      "devuelve el numero de elementos en la cola"
      return self.tamanio

    def mover_al_final(self):
      "mueve el elemento del frente de la cola al final de la cola"
      dato = self.atencion()
      self.arribo(dato)
      return dato 

    def barrido1(self):
      "muestra el contenido de una cola sin perder datos (n^2)"

      caux = self.cola()
      while (not self.cola_vacia()):
        dato = self.atencion()
        print(dato)
        self.arribo(dato)

      while (not caux.cola_vacia()):
        dato = self.atencion()
        self.arribo(dato)
      return caux

    def barrido2(self):
      "muestra el contenido de una cola sin perder datos O(n)"
      i = 0
      while (i < self.tamanio()):
        dato = self.mover_al_final()
        print(dato)
        i += 1


cdatos = Cola()
cvocales = Cola()

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





