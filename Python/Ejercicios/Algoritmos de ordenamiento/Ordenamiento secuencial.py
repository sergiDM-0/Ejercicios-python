import random
import time
import matplotlib.pyplot as plt


#metodo de ordenamiento secuencial
def secuencial(lista, buscado):
    """Método de búsqueda secuencial."""
    posicion = -1
    for i in range(0, len(lista)):
        if lista[i] == buscado:
            posicion = i
    return posicion


#tamaño de la lista
array = []
size = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500
,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000]
execution_times = []

#generar lista aleatoria
for i in size:
  array = [random.randint(0,100) for _ in range(i)]


  print("")
  print("lista desordenada:",array,"\n")

  #iniciar tiempo de ejecucion
  start_time = time.perf_counter()
  Lista_ordenada_secuencial = secuencial(array,20)
  end_time = time.perf_counter()
  #fin tiempo de ejecucion

  #imprimir lista ordenada
  print(f"lista ordenada: {Lista_ordenada_secuencial}")
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
plt.title('Rendimiento del Algoritmo de Ordenamiento Secuencial')
plt.grid(True, alpha=0.3)

# Configurar el eje X para mostrar todos los valores
plt.xticks(size, rotation=45)
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()
