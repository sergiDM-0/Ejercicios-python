
import time
import random
import matplotlib.pyplot as plt
import numpy as np

#metodo de ordenamiento burbuja
def burbuja(lista):
  for i in range (0,len(lista)-1):
    for j in range (0,len(lista)-i-1):
      if(lista[j]>lista[j+1]):
        lista[j],lista[j+1]=lista[j+1],lista[j]

  return lista

#tamaño de la lista
array = []
size = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500
,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,
3100,3200,3300,3400,3500,3600,3700,3800,3900,4000]
execution_times_burbuja = []



#generar lista aleatoria
for i1 in size:
  array = [random.randint(0,100) for _ in range(i1)]

  # Crear una copia de la lista original para preservar el estado desordenado
  array_desordenada = array.copy()

  #iniciar tiempo de ejecucion
  start_time1 = time.perf_counter()
  Lista_ordenada_burbuja = burbuja(array)
  end_time1 = time.perf_counter()

  #fin tiempo de ejecucion
  print(f"tiempo inicial : {start_time1}")
  print(f"tiempo final: {end_time1}")
  #imprimir lista desordenada
  print("lista desordenada:",array_desordenada,"")
  #imprimir lista ordenada
  print(f"lista ordenada: {Lista_ordenada_burbuja}")
  #imprimit los tiempos finales de cada una de las listas
  tiempo_transcurrido = end_time1 - start_time1
  execution_times_burbuja.append(tiempo_transcurrido)
  print(f"Tiempo para la lista de tamaño {i1}: {tiempo_transcurrido} segundos")
  print("\n")


#Imprimimos el resumen completos de resultados
print("-------------------------------------------")
print("/    Resumen de Tiempos de Ejecución       /")
print("-------------------------------------------")
for tam, tiempo in zip(size, execution_times_burbuja):
    print(f"Tamaño: {tam}  ->  Tiempo: {tiempo} segundos")
print("------------------ -------------------------\n")


# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(size, execution_times_burbuja, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Ordenamiento Burbuja')
plt.grid(True, alpha=0.3)

# Configurar el eje X para mostrar todos los valores
plt.xticks(size, rotation=45)
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()



# Guardar los últimos tiempos y tamaño
endtime1 = end_time1
lastsize1 = i1