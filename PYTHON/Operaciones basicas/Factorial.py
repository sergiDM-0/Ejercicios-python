def Factorial(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return n * Factorial(n-1)

print(f"El factorial de 5 es: {Factorial(5)}")
        