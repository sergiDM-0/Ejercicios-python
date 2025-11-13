
import random
import time
import matplotlib.pyplot as plt

#metodo de ordenamiento burbuja mejorado
def burbuja_mejorado(lista):
    i = 0
    control = True

    while (i <= len(lista)-2) and control:
        control = False
        for j in range(0, len(lista)-i-1):
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control = True
        i += 1
    return lista


#tamaño de la lista
array = []
size = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500
,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,
3100,3200,3300,3400,3500,3600,3700,3800,3900,4000]
execution_times_burbuja_mejorado = []

#generar lista aleatoria
for i2 in size:
  array = [random.randint(0,100) for _ in range(i2)]

  # Crear una copia de la lista original para preservar el estado desordenado
  array_desordenada = array.copy()

  #iniciar tiempo de ejecucion
  start_time2 = time.perf_counter()
  Lista_ordenada_burbuja_mejorado = burbuja_mejorado(array)
  end_time2 = time.perf_counter()

  #fin tiempo de ejecucion
  print(f"tiempo inicial : {start_time2}")
  print(f"tiempo final: {end_time2}")
  #imprimir lista desordenada
  print("lista desordenada:",array_desordenada,"")
  #imprimir lista ordenada
  print(f"lista ordenada: {Lista_ordenada_burbuja_mejorado}")
  #imprimit los tiempos finales de cada una de las listas
  tiempo_transcurrido = end_time2 - start_time2
  execution_times_burbuja_mejorado.append(tiempo_transcurrido)
  print(f"Tiempo para la lista de tamaño {i2}: {tiempo_transcurrido} segundos")
  print("\n")




#Imprimimos el resumen completos de resultados
print("-------------------------------------------")
print("/    Resumen de Tiempos de Ejecución       /")
print("-------------------------------------------")
for tam, tiempo in zip(size, execution_times_burbuja_mejorado):
    print(f"Tamaño: {tam}  ->  Tiempo: {tiempo} segundos")
print("------------------ -------------------------\n")


# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(size, execution_times_burbuja_mejorado, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Ordenamiento Burbuja Mejorado')
plt.grid(True, alpha=0.3)

# Configurar el eje X para mostrar todos los valores
plt.xticks(size, rotation=45)
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()

endtime2= end_time2
lastsize2 = i2