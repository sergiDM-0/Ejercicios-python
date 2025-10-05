
import random
import time
import matplotlib.pyplot as plt
import csv


def burbuja_mejorado(lista):
    """Método de ordenamiento burbuja mejorado."""
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



array = []
size = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000
,16000,17000,18000,19000,20000,21000,22000,23000,24000,25000,26000,27000,28000,29000,30000]
execution_times = []

for i in size:
  array = [random.randint(0,1000000) for _ in range(i)]

  start_time = time.time()
  print("")
  print("lista desordenada:",array,"\n")
  print(f"lista ordenada: {burbuja_mejorado(array)}")
  end_time = time.time()
  execution_times.append(end_time - start_time)

print("--------------------------------\n")
print("start time", start_time)
print("end time", end_time)
print(f"Tiempos de ejecución:{execution_times[0]}")


# Guardar resultados en CSV para lectura eficiente
with open('resultados_burbuja_mejorada.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['size', 'execution_time_seconds'])
    for s, t in zip(size, execution_times):
        writer.writerow([s, t])

# Tiempo final de la última ejecución
print(f"Tiempo final: {execution_times[-1]}")

# Guardar la lista ordenada final en un CSV aparte, en columnas (envolviendo filas)
num_columns = 10  # cambia este valor para ajustar cuántos números por fila
with open('datos_ordenados_burbuja_mejorada.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # writer.writerow([f'col_{i+1}' for i in range(num_columns)])  # opcional: encabezados
    for i in range(0, len(array), num_columns):
        writer.writerow(array[i:i+num_columns])

# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(size, execution_times, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Ordenamiento Burbuja Mejorado')
plt.grid(True, alpha=0.3)

# Configurar el eje X para mostrar todos los valores
plt.xticks(size, rotation=45)
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()
