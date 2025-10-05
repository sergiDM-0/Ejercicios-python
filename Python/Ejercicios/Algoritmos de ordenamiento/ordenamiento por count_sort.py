
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
size = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500
,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,
3100,3200,3300,3400,3500,3600,3700,3800,3900,4000]
execution_times_countsort = []

#generar lista aleatoria
for i8 in size:
  array = [random.randint(0,100) for _ in range(i8)]

  # Crear una copia de la lista original para preservar el estado desordenado
  array_desordenada = array.copy()

  #iniciar tiempo de ejecucion
  start_time8 = time.perf_counter()
  Lista_ordenada_count_sort = count_sort(array, max(array))
  end_time8 = time.perf_counter()

  #fin tiempo de ejecucion
  print(f"tiempo inicial : {start_time8}")
  print(f"tiempo final: {end_time8}")
  #imprimir lista desordenada
  print("lista desordenada:",array_desordenada,"")
  #imprimir lista ordenada
  print(f"lista ordenada: {Lista_ordenada_count_sort}")
  #imprimit los tiempos finales de cada una de las listas
  tiempo_transcurrido = end_time8 - start_time8
  execution_times_countsort.append(tiempo_transcurrido)
  print(f"Tiempo para la lista de tamaño {i8}: {tiempo_transcurrido} segundos")
  print("\n")


print(execution_times_countsort)

#Imprimimos el resumen completos de resultados
print("-------------------------------------------")
print("/    Resumen de Tiempos de Ejecución       /")
print("-------------------------------------------")
for tam, tiempo in zip(size, execution_times_countsort):
    print(f"Tamaño: {tam}  ->  Tiempo: {tiempo} segundos")
print("------------------ -------------------------\n")


# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(size, execution_times_countsort, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Ordenamiento Count Sort')
plt.grid(True, alpha=0.3)

# Configurar el eje X para mostrar todos los valores
plt.xticks(size, rotation=45)
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()

endtime8 = end_time8
lastsize8 = i8