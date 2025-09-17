import time
import random
import matplotlib.pyplot as plt


def mergesort(lista):

    if len(lista) <= 1:
        return lista
    else:
        medio = len(lista) // 2
        izquierda = []
        for i in range(0, medio):
            izquierda.append(lista[i])
        derecha = []
        for i in range(medio, len(lista)):
            derecha.append(lista[i])
        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)
        if(izquierda[medio-1] <= derecha[0]):
            izquierda += derecha
            return izquierda
        resultado = merge(izquierda, derecha)
        return resultado

def merge(izquierda,derecha):
    #mezclar las dos listas
    lista_mezclada = []
    while (len(izquierda) > 0 and len(derecha) > 0):
        if izquierda[0] <= derecha[0]:
            lista_mezclada.append(izquierda.pop(0))
            
        else:
            lista_mezclada.append(derecha.pop(0))
        if len(izquierda) > 0:
            lista_mezclada.extend(izquierda)
        if len(derecha) > 0:
            lista_mezclada.extend(derecha)
    return lista_mezclada

#tamaño de la lista
array = []
size = [100,200]
execution_times = []

#generar lista aleatoria
for i in size:
  array = [random.randint(0,1000000) for _ in range(i)]
  
  print("")
  print("lista desordenada:",array,"\n")

  #inicio tiempo de ejecucion
  start_time = time.perf_counter()
  Lista_ordenada_mergesort = mergesort(array)
  end_time = time.perf_counter()
  #fin tiempo de ejecucion

  #imprimir lista ordenada
  print(f"lista ordenada: {Lista_ordenada_mergesort}")
  execution_times.append(end_time - start_time)


#imprimir resultados
print("--------------------------------\n")
print("start time", start_time ,"segundos")
print("end time", end_time ,"segundos")
print(f"Tiempos de ejecución:{execution_times} segundos")
print(f"Tiempo final: {end_time - start_time} segundos")
print(f"Tiempo total sumado: {sum(execution_times)} segundos")


# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(size, execution_times, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Ordenamiento Mergesort')
plt.grid(True, alpha=0.3)

# Configurar el eje X para mostrar todos los valores
plt.xticks(size, rotation=45)
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()