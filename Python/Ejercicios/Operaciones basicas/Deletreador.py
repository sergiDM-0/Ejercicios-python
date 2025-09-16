

nombres = ["ana", "carlos", "santiago", "pedro"]

"""
i = 0

while i < len(nombres):
    palabra = nombres[1]
    print(f"Palabra en posición {i+1}: {palabra}")

    j = 0
    while j < len(palabra):
        print(f"Letra {j+1}: {palabra[j]}")
        j = j + 1

    i += 1

i = 0
for nombre in nombres:
    print(f"palabra: {nombre}")
    n=0
    for letra in nombre:
        print(f"Letra {n+1}: {letra}")
        n += 1


for i in range (len(nombres)):
    palabra = nombres[i]
    print(f"Palabra {i+1}: {palabra}")
    

    for i in range(len(palabra)):
        print(f"Letra {i+1}: {palabra[i]}")
        
"""

def deletrear_lista(lista_de_palabras):

    for i in range(len(lista_de_palabras)):
        palabra = lista_de_palabras[i]
        print(f"Palabra {i+1}: {palabra}")


        for j in range(len(palabra)):
            print(f"Letra {j+1}: {palabra[j]}")
            

pala = input("Ingrese las palabras que desea deletrear: ")
sa = pala.split()

deletrear_lista(sa)
            
            


