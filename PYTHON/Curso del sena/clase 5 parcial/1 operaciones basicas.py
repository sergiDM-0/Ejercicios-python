from typing import Any

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n--- GESTIÓN DE NOMBRES ---")
    print("1 Agregar nombre")
    print("2 Mostrar lista")
    print("3 Buscar nombre")
    print("4 Eliminar nombre por posición")
    print("5 Salir")
    return input("Seleccione una opción: ")

def inicializar_lista():
    """Solicita al usuario el número inicial de nombres y los registra."""
    #crea una lista vacia de nombres 

    nombres = []
    while True: # bucle while para que el usuario ingrese un numero positivo o cero
        try:
            cantidad = int(input("¿Cuántos nombres desea registrar inicialmente? "))
            if cantidad < 0:
                print("Por favor, ingrese un número positivo o cero.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    #por cada iteracion, suma un mumero y solicita un nombre para agregar a la lista
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre {i + 1}: ")
        nombres.append(nombre)
    
    print("Lista inicial registrada.")

    #metodo para mostrar la lista de nombres 
    mostrar_lista(nombres)
    return nombres

def agregar_nombre(lista):
    """Agrega un nombre a la lista."""
    nombre = input("Ingrese el nombre que desea agregar: ")
    lista.append(nombre)
    print(f"'{nombre}' ha sido agregado.")
    mostrar_lista(lista)

def mostrar_lista(lista):
    """Muestra la lista de nombres."""
    if not lista:
        print("La lista está vacía.")
    else:
        print("\n--- LISTA ACTUAL ---")
        for i, nombre in enumerate(lista):
            print(f"  {i}: {nombre}")
        print("--------------------")

def buscar_nombre(lista):
    """Busca un nombre en la lista."""
    nombre_buscar = input("Ingrese el nombre que desea buscar: ")
    if nombre_buscar in lista:
        print(f"Sí, '{nombre_buscar}' se encuentra en la lista.")
    else:
        print(f"No, '{nombre_buscar}' no se encuentra en la lista.")

def eliminar_nombre(lista):
    """Elimina un nombre por su posición (índice)."""
    mostrar_lista(lista)
    if not lista:
        print("No hay nombres que eliminar.")
        return

    try:
        posicion = int(input("Ingrese la posición (número) del nombre a eliminar: "))
        
        #si la posicion es mayor o igual a 0 y menor a la longitud de la lista, elimina el nombre de la lista
        if 0 <= posicion < len(lista):
            nombre_eliminado = lista.pop(posicion)
            print(f"Se ha eliminado '{nombre_eliminado}' de la posición {posicion}.")
            #hace uso del metodo mostrar lista
            mostrar_lista(lista) #muestra la lista actualizada
        else:
            print("Posición fuera de rango. No se eliminó ningún nombre.")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número de posición.") #si el usuario ingresa un valor no valido, imprime un mensaje de error

def main():
    """Función principal del programa."""
    nombres = inicializar_lista()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            agregar_nombre(nombres)
        elif opcion == '2':
            mostrar_lista(nombres)
        elif opcion == '3':
            buscar_nombre(nombres)
        elif opcion == '4':
            eliminar_nombre(nombres)
        elif opcion == '5':
            print("Saliendo del programa...")
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()