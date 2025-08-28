def analizar_nombres (lista_nombres):

    for nombres in lista_nombres:
    # Solo si el nombre tiene más de 3 letras, hacemos lo de adentro.
        if len(nombres) > 2:
            print (f"El nombre de perro es: {nombres}")

            for delnombres in nombres:
                print(delnombres)



nombres_de_perros = ["toby","tony","romeo","dog","dr"]


analizar_nombres(nombres_de_perros)


def sumar(a, b):
  """Esta función suma dos números y devuelve el resultado."""
  resultado = a + b
  return resultado


s = sumar(5, 3)
print(s)
print(f"El resultado de la suma es: {s}\n")
                                                                    