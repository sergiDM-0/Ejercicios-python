class nodoCola(object):
  "clase nodo cola"
  info,sig = None,None


class cola(object):
  "clase cola"
  def __init__(self):
    self.frente,self.final = None,None
    self.tamanio = 0

  def arribo(self,cola,dato):
    "arriba el dato al final de la cola"
    nodo = nodoCola()
    nodo.info = dato
    if cola.frente is None:
      cola.frente = nodo
    else:
      cola.final.sig = nodo

    cola.final = nodo
    cola.tamanio += 1

  def atencion(self):
    "atiende al elemento en frente de la cola y lo devuelve"
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
      cola.final = None
    cola.tamanio -= 1
    return dato

  def cola_vacia(self):
    "devuelve true si la cola esta vacia"
    return self.frente is None

  def en_frente(self):
    "devuelve el valor almacenado en el frente de la cola"
    return self.frente.info

  def tamanio(self):
    "devuelve el numero de elementos de la cola"
    return self.tamanio

  def mover_al_final(self):
    "mueve el elemento del frente de la cola al final"
    dato = self.atencion()
    self.arribo(self, dato)
    return dato

  def barrido(self):
    "muestra el contenido de una cola sin perder datos0"

    caux = self()
    while(not self.cola_vacia(self)):
      dato = self.atencion(self)
      print(dato)
      self.arribo(caux,dato)

    while(not self.cola_vacia(caux)):