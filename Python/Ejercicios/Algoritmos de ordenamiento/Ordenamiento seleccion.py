
import time
import random
import matplotlib.pyplot as plt

#metodo de ordenamiento seleccion
def seleccion(lista):
    """Método de ordenamiento selección."""
    for i in range(0, len(lista)-1):
        minimo = i
        for j in range(i+1, len(lista)):
            if(lista[j] < lista[minimo]):
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

array = []
size = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500
,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,
3100,3200,3300,3400,3500,3600,3700,3800,3900,4000]
execution_times_seleccion = []
#generar lista aleatoria
for i4 in size:
  array = [random.randint(0,100) for _ in range(i4)]

  # Crear una copia de la lista original para preservar el estado desordenado
  array_desordenada = array.copy()

  #iniciar tiempo de ejecucion
  start_time4 = time.perf_counter()
  Lista_ordenada_seleccion = seleccion(array)
  end_time4 = time.perf_counter()

  #fin tiempo de ejecucion
  print(f"tiempo inicial : {start_time4}")
  print(f"tiempo final: {end_time4}")
  #imprimir lista desordenada
  print("lista desordenada:",array_desordenada,"")
  #imprimir lista ordenada
  print(f"lista ordenada: {Lista_ordenada_seleccion}")
  #imprimit los tiempos finales de cada una de las listas
  tiempo_transcurrido = end_time4 - start_time4
  execution_times_seleccion.append(tiempo_transcurrido)
  print(f"Tiempo para la lista de tamaño {i4}: {tiempo_transcurrido} segundos")
  print("\n")




#Imprimimos el resumen completos de resultados
print("-------------------------------------------")
print("/    Resumen de Tiempos de Ejecución       /")
print("-------------------------------------------")
for tam, tiempo in zip(size, execution_times_seleccion):
    print(f"Tamaño: {tam}  ->  Tiempo: {tiempo} segundos")
print("------------------ -------------------------\n")


# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(size, execution_times_seleccion, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Ordenamiento Seleccion')
plt.grid(True, alpha=0.3)

# Configurar el eje X para mostrar todos los valores
plt.xticks(size, rotation=45)
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()

endtime4 = end_time4
lastsize4 = i4