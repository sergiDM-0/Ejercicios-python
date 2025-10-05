def analizar_nombres (lista_nombres):

    for nombres in lista_nombres:
    # Solo si el nombre tiene más de 3 letras, hacemos lo de adentro.
        if len(nombres) > 2:
            print (f"El nombre de perro es: {nombres}")

            for delnombres in nombres:
                print(delnombres)



nombres_de_perros = ["toby","tony","romeo","dog","dr"]

"""
analizar_nombres(nombres_de_perros)



for i in range(10,0,-2):
    print(i)


u=0

while u < 10:
    print(u)
    u += 1

"""

"""

perros = ["toby","tony","romeo","dog","dr"]

i = 0
while i <len(perros):
  perro = perros[i]
  print(f"El perro es: {perro}")
  

  j = 0
  while j < len(perro):
    print(perro[j])
    j += 1
  
  i += 1

"""

"""

frutas = ["manzana", "pera", "uva"]

for n in range(len(frutas)):

  palabra = frutas[n]
  print(f"La fruta es: {palabra}")

  for u in range(len(palabra)):
    letra = palabra[u]
    print(letra)


"""

def deletrear_lista(lista_de_palabras):
  """
  Esta función recibe una lista de palabras y deletrea cada una,
  una letra a la vez, usando bucles for in range.
  """
  print("\n--- Iniciando el deletreo ---")

  # Bucle externo: recorre los índices de la lista de palabras
  for i in range(len(lista_de_palabras)):
    palabra = lista_de_palabras[i]
    print(f"\nPalabra: '{palabra}'")

    # Bucle interno: recorre los índices de la palabra actual
    for j in range(len(palabra)):
      letra = palabra[j]
      print(letra)

# --- Parte principal del programa ---

# 1. Pedir al usuario que ingrese las palabras
entrada_usuario = input("Ingresa las palabras que quieras deletrear, separadas por espacios: ")

# 2. Convertir la entrada del usuario en una lista de strings
# El método .split() divide el texto por los espacios en blanco
lista_usuario = entrada_usuario.split()

# 3. Llamar a la función con la lista creada a partir de la entrada del usuario
# Se verifica que el usuario haya escrito algo antes de llamar a la función
if lista_usuario:
  deletrear_lista(lista_usuario)
else:
  print("No ingresaste ninguna palabra para deletrear.")


