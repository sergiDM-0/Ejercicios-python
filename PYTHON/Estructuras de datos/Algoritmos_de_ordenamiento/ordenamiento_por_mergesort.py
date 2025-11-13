
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
    while (len(izquierda) > 0 and (len(derecha) > 0)):
        if (izquierda[0] <= derecha[0]):
            lista_mezclada.append(izquierda.pop(0))

        else:
            lista_mezclada.append(derecha.pop(0))
    if len(izquierda) > 0:
            lista_mezclada += izquierda
    if len(derecha) > 0:
            lista_mezclada += derecha
    return lista_mezclada


#tamaño de la lista
array = []
size = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500
,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,
3100,3200,3300,3400,3500,3600,3700,3800,3900,4000]
execution_times_mergesort = []


#generar lista aleatoria
for i7 in size:
  array = [random.randint(0,100) for _ in range(i7)]

  # Crear una copia de la lista original para preservar el estado desordenado
  array_desordenada = array.copy()

  #iniciar tiempo de ejecucion
  start_time7 = time.perf_counter()
  Lista_ordenada_mergesort = mergesort(array)
  end_time7 = time.perf_counter()

  #fin tiempo de ejecucion
  print(f"tiempo inicial : {start_time7}")
  print(f"tiempo final: {end_time7}")
  #imprimir lista desordenada
  print("lista desordenada:",array_desordenada,"")
  #imprimir lista ordenada
  print(f"lista ordenada: {Lista_ordenada_mergesort}")
  #imprimit los tiempos finales de cada una de las listas
  tiempo_transcurrido = end_time7 - start_time7
  execution_times_mergesort.append(tiempo_transcurrido)
  print(f"Tiempo para la lista de tamaño {i7}: {tiempo_transcurrido} segundos")
  print("\n")




#Imprimimos el resumen completos de resultados
print("-------------------------------------------")
print("/    Resumen de Tiempos de Ejecución       /")
print("-------------------------------------------")
for tam, tiempo in zip(size, execution_times_mergesort):
    print(f"Tamaño: {tam}  ->  Tiempo: {tiempo} segundos")
print("------------------ -------------------------\n")


# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(size, execution_times_mergesort, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Ordenamiento Mergesort')
plt.grid(True, alpha=0.3)

# Configurar el eje X para mostrar todos los valores
plt.xticks(size, rotation=45)
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()


endtime7 = end_time7
lastsize7 = i7