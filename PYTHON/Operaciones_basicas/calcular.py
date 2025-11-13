import sys


# Establecemos el límite a 0 (sin límite) para la conversión de int a string
sys.set_int_max_str_digits(0) 

#numero_gigante = 31416 ** 10000

# Ahora el print funcionará sin problemas
#print(numero_gigante)

                                           # f string 

nombre = "ana"

year = 2025

print(f"nombre: {nombre} año: {year}")

print(f"nombre> {nombre}{year}")

                                          # 2 ejercicio 

nombre_personaje = "master"

nivel = 10

puntuacion = 3.10

print (f"*** Perfil del Jugador ***\n \
    Nombre : {nombre_personaje}, Nivel : {nivel}, Puntuacion : {puntuacion}")

                                          # 3 ejercicio
"""
Imagina que tienes una variable temperatura = 28.

¿Cómo escribirías una condición que imprima "Hace calor, ¡a la piscina!" 
si la temperatura es mayor a 25, y si no, que imprima "Hoy no hace tanto calor."?
"""

temperatura = 28 

if temperatura > 25:
    print("Hace calor, ¡a la piscina!")
else : 
    print("Hoy no hace tanto calor.")


                                        # 4 ejercicio 


"""
Imagina que estás programando un videojuego. Tienes una variable vida = 75.

Escribe una estructura de condiciones para que:

    Si la vida es igual a 100, imprima "Salud perfecta".

    Si la vida es mayor o igual a 50, imprima "Estás en buena forma".

    Si no, imprima "¡Cuidado! Salud baja".
"""

vida = 75 

if vida == 100:
    print("Salud perfecta")
elif vida >= 50:
    print("Estás en buena forma")
else:
    print("¡Cuidado! Salud baja")   


                                                # 5 ejercicio

# listas 

nombres = ['carlos','pedro','ana','sergio']
print(nombres)
print (nombres[2])

# actualizar

nombres.append('santiago')
print(nombres)

# eliminar 
nombres.pop()
print(nombres)

                                                # 6 ejercicio 


"""
Ejercicio Final: Lista de Calificaciones

Imagina que tienes una lista con las calificaciones de varios estudiantes. 
Tu misión es crear un programa que revise cada calificación y decida si el estudiante aprobó o no.

La regla para aprobar es tener una calificación de 6 o más.

Tu Misión

    Copia esta lista de calificaciones en tu código: calificaciones = [8, 5, 10, 3, 7]

    Escribe un bucle for para recorrer cada calificacion en la lista.

    Dentro del bucle, usa una condición if/else para comprobar si la calificacion es mayor o igual a 6.

        Si la calificación es 6 o más, imprime un mensaje como: Calificación: 8 -> Aprobado

        Si la calificación es menor a 6, imprime un mensaje como: Calificación: 5 -> Reprobado
"""

calificaciones = [8, 5, 10, 3, 7]


for notas in calificaciones:
    if notas >= 6:
        print(f"Calificación: {notas} -> Aprobado")
    
    else:
        print(f"Calificación: {notas} -> Reprobado")

                                                    #7 EJERCICIO

# imprimir numeros de 1 a 5
for i in range(1,6):
    print(i,end = " ")

                                                    #8 ejercicio


contador = 1
while contador <= 5:
    contador = contador + 1  # ¡Esto es clave!
    print(f"El contador es {contador}")


                                                    #9 ejercicio 


# Ciclo de afuera: Controla las FILAS
for fila in range(1, 4):
  
  # Ciclo de adentro: Controla las COLUMNAS
  for columna in range(1, 4):
    print("Coordenada:", fila, ",", columna)

  # Agregamos un separador para que se vea más claro
  print("--- Fin de la fila ---")