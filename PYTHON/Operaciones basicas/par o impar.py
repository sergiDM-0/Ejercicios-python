
def parimp(*numeros):

    # Procesar múltiples números
    for numero in numeros:
        # Convertir a entero si es string
        numero = int(numero)
        
        # Verificar si es par o impar
        if numero % 2 == 0:
            print(f"El número {numero} es par")
        else:
            print(f"El número {numero} es impar")

num = input("Ingrese los números que desea verificar: ")
num = num.split()
parimp(*num)  # El * desempaqueta la lista en argumentos separados 
