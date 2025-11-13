import random
import time
n=100

aleatorios = [random.randint(1,100) for i in range(n)]
print(aleatorios)
print("--------------------------------")
inicio = time.time()
print (inicio)
aleatorios.sort()
print(aleatorios)
print("--------------------------------")
fin = time.time()
print (fin)
print(fin - inicio)


#aleatorios.reverse()
#print(aleatorios)



"""
aleatorios.sort(reverse=True)
print(aleatorios)

aleatorios.sort(key=lambda x: x%2)
print(aleatorios)

aleatorios.sort(key=lambda x: x%2, reverse=True)
print(aleatorios)
"""