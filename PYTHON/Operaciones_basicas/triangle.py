def triangle(n):
    # Generar un triángulo con n filas
    for i in range(n):
        # Crear la línea con el patrón "*#"
        line = "*#" * (i + 1)
        print(line)

# Llamar la función
triangle(30)