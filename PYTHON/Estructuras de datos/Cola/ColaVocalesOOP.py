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

letra = input("ingrese un caracter (enter para salir) :  ")
while (letra != ''):
  cdatos.arribo(letra)
  letra = input("ingrese un caracter (enter para salir) : ")

#imprime una copia de la cola inicial
print("cola  inicial es: ")
cdatos.barrido1()

print("______"*20)

#haciend uso del metodo mover_al_final 
moveralfinal = input("ingrese (y) or (n) para move el primer dato en la cola al final:   " )
if moveralfinal == "y":
  cdatos.mover_al_final()
  print("la cola con modificaciones es: ")
  cdatos.barrido2()
  print("")
else:
  print("la cola sin modificaciones es: ")
  cdatos.barrido2()
  print("")
print("______"*20)


print(f"el tamaño total inicial de la cola es {cdatos.obtener_tamanio()}")
print(f"Cola vacia?: {cdatos.cola_vacia()}\n")

while (not cdatos.cola_vacia()):

  #Guardamos una referencia al nodo que está en la frente.
  nodo_en_frente = cdatos.frente

  #comprobar el primer dato en la cola y el apuntador
  print(f"el primer dato en la cola es: {cdatos.en_frente()}")
  print(f"el apuntador primer dato en la cola es: {cdatos.frente.apuntador}")

  
  #Atendemes un dato para que cambie el primer dato en -1
  letra = cdatos.atencion()
  print(f"el dato atendido es ({nodo_en_frente.info}) con apuntador : {nodo_en_frente.apuntador}")

  

  #si es none es el fondo de la cola
  if nodo_en_frente.apuntador is None:
    print("Era el fondo de la cola\n")

  if letra.upper() in ["A",'E','I','O','U']:
    cvocales.arribo(letra)

print("Datos cola Vocales")
while (not cvocales.cola_vacia()):
  dato = cvocales.atencion()
  print(dato,"\n")

print(f"el tamaño total de la cola es: {cvocales.obtener_tamanio()}")
print(f"el tamaño total de la cola de vocales es: {cvocales.obtener_tamanio()}")