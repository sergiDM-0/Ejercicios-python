import time
import random
import matplotlib.pyplot as plt

#metodo de ordenamiento burbuja
def burbuja(lista):
  for i in range (0,len(lista)-1):
    for j in range (0,len(lista)-i-1):
      if(lista[j]>lista[j+1]):
        lista[j],lista[j+1]=lista[j+1],lista[j]

  return lista

#tamaño de la lista
array = []
size = [100,200,300,400,500,600,700,800,900,1000]
execution_times = []

#generar lista aleatoria
for i in size:
  array = [random.randint(0,1000000) for _ in range(i)]


  print("")
  print("lista desordenada:",array,"\n")

  #iniciar tiempo de ejecucion
  start_time = time.perf_counter()
  burbuja(array)
  end_time = time.perf_counter()
  #fin tiempo de ejecucion

  print(f"lista ordenada: {burbuja(array)}")
  execution_times.append(end_time - start_time)

#imprimir resultados
print("--------------------------------\n")
print("start time", start_time)
print("end time", end_time)
print(f"Tiempos de ejecución:{execution_times}")
print(f"Tiempo final (última iteración): {end_time - start_time}")

# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(size, execution_times, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Ordenamiento Burbuja')
plt.grid(True, alpha=0.3)

# Configurar el eje X para mostrar todos los valores
plt.xticks(size, rotation=45)
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()
