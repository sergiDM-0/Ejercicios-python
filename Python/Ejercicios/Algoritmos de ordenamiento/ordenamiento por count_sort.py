import random
import time
import matplotlib.pyplot as plt


#metodo de ordenamiento countsort
def count_sort(lista, maximo):
    """Método de ordenamiento countsort."""
    lista_conteo = [0] * (maximo + 1)
    lista_ordenada = [None] * len(lista)

    for i in lista:
        lista_conteo[i] += 1

    total = 0
    for i in range(len(lista_conteo)):
        lista_conteo[i], total = total, total + lista_conteo[i]

    for indice in lista:
        lista_ordenada[lista_conteo[indice]] = indice
        lista_conteo[indice] += 1
    
    return lista_ordenada


#tamaño de la lista
array = []
size = [100,200]
execution_times = []

#generar lista aleatoria
for i in size:
  array = [random.randint(0,100) for _ in range(i)]

  # Crear una copia de la lista original para preservar el estado desordenado
  array_desordenada = array.copy()

  #iniciar tiempo de ejecucion
  start_time = time.perf_counter()
  Lista_ordenada_count_sort = count_sort(array)
  end_time = time.perf_counter()

  #fin tiempo de ejecucion
  print(f"tiempo inicial : {start_time}")
  print(f"tiempo final: {end_time}")
  #imprimir lista desordenada
  print("lista desordenada:",array_desordenada,"")
  #imprimir lista ordenada
  print(f"lista ordenada: {Lista_ordenada_count_sort}")
  #imprimit los tiempos finales de cada una de las listas 
  tiempo_transcurrido = end_time - start_time
  execution_times.append(tiempo_transcurrido)
  print(f"Tiempo para la lista de tamaño {i}: {tiempo_transcurrido} segundos")
  print("\n")
  
  


#Imprimimos el resumen completos de resultados
print("-------------------------------------------")
print("/    Resumen de Tiempos de Ejecución       /")
print("-------------------------------------------")
for tam, tiempo in zip(size, execution_times):
    print(f"Tamaño: {tam}  ->  Tiempo: {tiempo} segundos")
print("------------------ -------------------------\n")


# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(size, execution_times, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Ordenamiento Count Sort')
plt.grid(True, alpha=0.3)

# Configurar el eje X para mostrar todos los valores
plt.xticks(size, rotation=45)
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()
