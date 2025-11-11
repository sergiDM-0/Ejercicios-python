import time

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n--- GESTIÓN DE PROYECTOS ACADÉMICOS ---")
    print("1. Registrar proyecto")
    print("2. Buscar proyecto por nombre")
    print("3. Mostrar lista de proyectos")
    print("4. Modificar estado del proyecto")
    print("5. Eliminar proyecto por nombre")
    print("6. Salir")
    return input("Seleccione una opción: ")

def buscar_proyecto(nombre_buscar, lista_proyectos):
    """Busca un proyecto por nombre y devuelve el diccionario si lo encuentra."""
    for proyecto in lista_proyectos:
        if proyecto['nombre'].lower() == nombre_buscar.lower():
            return proyecto
    return None

def registrar_proyecto(lista_proyectos):
    """Registra un nuevo proyecto en la lista."""
    print("\n--- Registro de Nuevo Proyecto ---")
    nombre = input("Nombre del proyecto: ")
    
    # Evitar duplicados
    if buscar_proyecto(nombre, lista_proyectos):
        print("Error: Ya existe un proyecto con ese nombre.")
        return

    investigador = input("Investigador principal: ")
    area = input("Área de conocimiento: ")
    
    # Validación simple de estado
    estado = ""
    while estado not in ['en curso', 'finalizado']:
        estado = input("Estado (en curso / finalizado): ").lower()
        if estado not in ['en curso', 'finalizado']:
            print("Estado no válido. Use 'en curso' o 'finalizado'.")
            
    nuevo_proyecto = {
        "nombre": nombre,
        "investigador": investigador,
        "area": area,
        "estado": estado
    }
    
    lista_proyectos.append(nuevo_proyecto)
    print(f"¡Proyecto '{nombre}' registrado con éxito!")

def buscar_proyecto_menu(lista_proyectos):
    """Opción de menú para buscar y mostrar un proyecto."""
    nombre_buscar = input("Ingrese el nombre del proyecto a buscar: ")
    proyecto = buscar_proyecto(nombre_buscar, lista_proyectos)
    
    if proyecto:
        print("\n--- Proyecto Encontrado ---")
        print(f"  Nombre: {proyecto['nombre']}")
        print(f"  Investigador: {proyecto['investigador']}")
        print(f"  Área: {proyecto['area']}")
        print(f"  Estado: {proyecto['estado']}")
    else:
        print(f"No se encontró ningún proyecto con el nombre '{nombre_buscar}'.")

def mostrar_proyectos(lista_proyectos):
    """Muestra todos los proyectos registrados."""
    if not lista_proyectos:
        print("\nNo hay proyectos registrados.")
        return
        
    print("\n--- LISTA DE TODOS LOS PROYECTOS ---")
    for i, proyecto in enumerate(lista_proyectos):
        print(f"\n  Proyecto {i + 1}:")
        print(f"    Nombre: {proyecto['nombre']}")
        print(f"    Investigador: {proyecto['investigador']}")
        print(f"    Área: {proyecto['area']}")
        print(f"    Estado: {proyecto['estado']}")
    print("---------------------------------")

def modificar_estado(lista_proyectos):
    """Modifica el estado de un proyecto existente."""
    nombre_buscar = input("Ingrese el nombre del proyecto a modificar: ")
    proyecto = buscar_proyecto(nombre_buscar, lista_proyectos)
    
    if not proyecto:
        print(f"No se encontró ningún proyecto con el nombre '{nombre_buscar}'.")
        return

    print(f"El estado actual de '{proyecto['nombre']}' es: {proyecto['estado']}")
    nuevo_estado = ""
    while nuevo_estado not in ['en curso', 'finalizado']:
        nuevo_estado = input("Ingrese el nuevo estado (en curso / finalizado): ").lower()
        if nuevo_estado not in ['en curso', 'finalizado']:
            print("Estado no válido.")
        elif nuevo_estado == proyecto['estado']:
            print(f"El proyecto ya se encuentra en estado '{nuevo_estado}'.")
            return

    proyecto['estado'] = nuevo_estado
    print(f"Estado del proyecto '{proyecto['nombre']}' actualizado a '{nuevo_estado}'.")

def eliminar_proyecto(lista_proyectos):
    """Elimina un proyecto de la lista por nombre."""
    nombre_buscar = input("Ingrese el nombre del proyecto a eliminar: ")
    proyecto = buscar_proyecto(nombre_buscar, lista_proyectos)
    
    if not proyecto:
        print(f"No se encontró ningún proyecto con el nombre '{nombre_buscar}'.")
        return

    # Confirmación
    confirmar = input(f"¿Está seguro de que desea eliminar el proyecto '{proyecto['nombre']}'? (s/n): ").lower()
    
    if confirmar == 's':
        lista_proyectos.remove(proyecto)
        print(f"Proyecto '{proyecto['nombre']}' eliminado.")
    else:
        print("Eliminación cancelada.")

def main():
    """Función principal del programa."""
    proyectos = [] # Lista de diccionarios
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            registrar_proyecto(proyectos)
        elif opcion == '2':
            buscar_proyecto_menu(proyectos)
        elif opcion == '3':
            mostrar_proyectos(proyectos)
        elif opcion == '4':
            modificar_estado(proyectos)
        elif opcion == '5':
            eliminar_proyecto(proyectos)
        elif opcion == '6':
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()