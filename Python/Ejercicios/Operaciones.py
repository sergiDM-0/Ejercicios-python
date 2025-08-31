# una por una
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b
    
"""
print(suma(10,20))
print(resta(10,20))
print(multiplicacion(10,20))
print(division(10,20))
"""



# dos a la vez
def DosOPalaVez(a,b):
    return a + b, a - b, a * b, a / b


print('0.todas las operaciones\n',"1. Suma\n","2. Resta\n","3. Multiplicación\n","4. División\n")



op = int(input("Ingrese la operación que desea realizar: "))
    

a,b = int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))
if op == 0:
    print(DosOPalaVez(a,b))

if op == 1:
    print(suma(a,b))
elif op == 2:
    print(resta(a,b))
elif op == 3:
    print(multiplicacion(a,b))
elif op == 4:
    print(division(a,b))

