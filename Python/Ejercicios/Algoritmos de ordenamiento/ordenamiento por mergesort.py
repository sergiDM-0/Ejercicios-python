import time
import random
import matplotlib.pyplot as plt


def mergesort(lista):
    if len(lista) <= 1:
        return lista
    else:
        medio = len(lista) // 2
        izquierda = lista[:medio]  # Más eficiente que el bucle
        derecha = lista[medio:]    # Más eficiente que el bucle
        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)
        resultado = merge(izquierda, derecha)
        return resultado

def merge(izquierda, derecha):
    #mezclar las dos listas
    lista_mezclada = []
    while (len(izquierda) > 0 and len(derecha) > 0):
        if izquierda[0] <= derecha[0]:
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    
    # Agregar los elementos restantes (fuera del bucle while)
    if len(izquierda) > 0:
        lista_mezclada.extend(izquierda)
    if len(derecha) > 0:
        lista_mezclada.extend(derecha)
    
    return lista_mezclada

def busqueda_binaria(lista_ordenada, elemento):
    """
    Realiza búsqueda binaria en una lista ordenada
    Retorna el índice del elemento si se encuentra, -1 si no se encuentra
    """
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista_ordenada[medio] == elemento:
            return medio
        elif lista_ordenada[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1  # Elemento no encontrado


#tamaño de la lista
array = []
size = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,
1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,
3100,3200,3300,3400,3500,3600,3700,3800,3900,4000]
execution_times_mergesort = []
execution_times_busqueda = []


#generar lista aleatoria
for i in size:
  array = [random.randint(0,100) for _ in range(i)]

  # Crear una copia de la lista original para preservar el estado desordenado
  array_desordenada = array.copy()

  # ========== PRUEBA DE MERGESORT ==========
  #iniciar tiempo de ejecucion para mergesort
  start_time_merge = time.perf_counter()
  Lista_ordenada_mergesort = mergesort(array)
  end_time_merge = time.perf_counter()

  #fin tiempo de ejecucion para mergesort
  tiempo_mergesort = end_time_merge - start_time_merge
  execution_times_mergesort.append(tiempo_mergesort)
  
  # ========== PRUEBA DE BÚSQUEDA BINARIA ==========
  # Seleccionar un elemento aleatorio para buscar
  elemento_buscar = random.choice(Lista_ordenada_mergesort)
  
  #iniciar tiempo de ejecucion para búsqueda binaria
  start_time_busqueda = time.perf_counter()
  indice_encontrado = busqueda_binaria(Lista_ordenada_mergesort, elemento_buscar)
  end_time_busqueda = time.perf_counter()

  #fin tiempo de ejecucion para búsqueda binaria
  tiempo_busqueda = end_time_busqueda - start_time_busqueda
  execution_times_busqueda.append(tiempo_busqueda)

  # Mostrar resultados
  print(f"=== Tamaño de lista: {i} ===")
  print(f"Tiempo Mergesort: {tiempo_mergesort:.6f} segundos")
  print(f"Tiempo Búsqueda Binaria: {tiempo_busqueda:.6f} segundos")
  print(f"Elemento buscado: {elemento_buscar}, Índice encontrado: {indice_encontrado}")
  print(f"Lista ordenada (primeros 10): {Lista_ordenada_mergesort[:10]}")
  print("-" * 50)
  
  


#Imprimimos el resumen completos de resultados 
print("=" * 60)
print("           RESUMEN DE TIEMPOS DE EJECUCIÓN")
print("=" * 60)
print(f"{'Tamaño':<10} {'Mergesort (s)':<15} {'Búsqueda Binaria (s)':<20}")
print("-" * 60)
for tam, tiempo_merge, tiempo_busq in zip(size, execution_times_mergesort, execution_times_busqueda):
    print(f"{tam:<10} {tiempo_merge:<15.6f} {tiempo_busq:<20.6f}")
print("=" * 60)

# Crear las gráficas
plt.figure(figsize=(15, 10))

# Subplot 1: Mergesort
plt.subplot(2, 1, 1)
plt.plot(size, execution_times_mergesort, 'bo-', linewidth=2, markersize=6)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Ordenamiento Mergesort')
plt.grid(True, alpha=0.3)
plt.xticks(size[::5], rotation=45)  # Mostrar cada 5to elemento para legibilidad

# Subplot 2: Búsqueda Binaria
plt.subplot(2, 1, 2)
plt.plot(size, execution_times_busqueda, 'ro-', linewidth=2, markersize=6)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Búsqueda Binaria')
plt.grid(True, alpha=0.3)
plt.xticks(size[::5], rotation=45)  # Mostrar cada 5to elemento para legibilidad

plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()

# Gráfica comparativa
plt.figure(figsize=(12, 8))
plt.plot(size, execution_times_mergesort, 'bo-', linewidth=2, markersize=6, label='Mergesort')
plt.plot(size, execution_times_busqueda, 'ro-', linewidth=2, markersize=6, label='Búsqueda Binaria')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de Rendimiento: Mergesort vs Búsqueda Binaria')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(size[::5], rotation=45)
plt.tight_layout()
plt.show()
