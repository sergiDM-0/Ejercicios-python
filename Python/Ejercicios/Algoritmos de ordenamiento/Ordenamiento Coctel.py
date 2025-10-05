
import random
import time
import matplotlib.pyplot as plt


#metodo de ordenamiento cóctel o burbuja bidireccional
def coctel(lista):
    izquierda = 0
    derecha = len(lista) - 1
    control = True
    while (izquierda < derecha) and control:
        control = False
        for i in range(izquierda, derecha):
            if(lista[i] > lista[i+1]):
                control = True
                lista[i], lista[i+1] = lista[i+1], lista[i]
        derecha -= 1
        for j in range(derecha, izquierda, -1):
            if(lista[j] < lista[j-1]):
                control = True
                lista[j], lista[j-1] = lista[j-1], lista[j]
        izquierda += 1
    return lista


#tamaño de la lista
array = []
size = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500
,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000
,3100,3200,3300,3400,3500,3600,3700,3800,3900,4000]
execution_times_coctel = []


#generar lista aleatoria
for i3 in size:
  array = [random.randint(0,100) for _ in range(i3)]

  # Crear una copia de la lista original para preservar el estado desordenado
  array_desordenada = array.copy()

  #iniciar tiempo de ejecucion
  start_time3 = time.perf_counter()
  Lista_ordenada_coctel = coctel(array)
  end_time3 = time.perf_counter()

  #fin tiempo de ejecucion
  print(f"tiempo inicial : {start_time3}")
  print(f"tiempo final: {end_time3}")
  #imprimir lista desordenada
  print("lista desordenada:",array_desordenada,"")
  #imprimir lista ordenada
  print(f"lista ordenada: {Lista_ordenada_coctel}")
  #imprimit los tiempos finales de cada una de las listas
  tiempo_transcurrido = end_time3 - start_time3
  execution_times_coctel.append(tiempo_transcurrido)
  print(f"Tiempo para la lista de tamaño {i3}: {tiempo_transcurrido} segundos")
  print("\n")




#Imprimimos el resumen completos de resultados
print("-------------------------------------------")
print("/    Resumen de Tiempos de Ejecución       /")
print("-------------------------------------------")
for tam, tiempo in zip(size, execution_times_coctel):
    print(f"Tamaño: {tam}  ->  Tiempo: {tiempo} segundos")
print("------------------ -------------------------\n")


# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(size, execution_times_coctel, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Ordenamiento Coctel')
plt.grid(True, alpha=0.3)

# Configurar el eje X para mostrar todos los valores
plt.xticks(size, rotation=45)
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()

endtime3 = end_time3
lastsize3 = i3