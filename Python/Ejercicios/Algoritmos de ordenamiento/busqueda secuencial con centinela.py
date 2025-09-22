import random
import time
import matplotlib.pyplot as plt


#metodo de busqueda secuencial con centinela
def Busqueda_secuencial_con_centinela(lista, buscado):
    """Método de búsqueda secuencial con centinela."""
    posicion = -1
    for i in range(0, len(lista)):
        if(lista[i] == buscado):
            posicion = i
            break
    return posicion

#numero a buscar
buscado = 1



#tamaño de la lista
array = []
size = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500
,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,
3100,3200,3300,3400,3500,3600,3700,3800,3900,4000]
execution_times = []

#generar lista aleatoria
for i in size:
  array = [random.randint(0,100) for _ in range(i)]

  #iniciar tiempo de ejecucion
  start_time = time.perf_counter()
  Busqueda_secuencial_con_centinela_Lista = Busqueda_secuencial_con_centinela(array,buscado)
  end_time = time.perf_counter()

  #fin tiempo de ejecucion
  print(f"tiempo inicial : {start_time}")
  print(f"tiempo final: {end_time}")
  #imprimir lista 
  print("lista :",array,"")
  #imprimir numero encontrado
  print(f"posicion en la lista del numero {buscado}: {Busqueda_secuencial_con_centinela_Lista}")
  #imprimit los tiempos finales de cada una de las listas 
  tiempo_transcurrido = end_time - start_time
  execution_times.append(tiempo_transcurrido)
  print(f"Tiempo para la busqueda en la lista de tamaño {i}: {tiempo_transcurrido} segundos")
  print("\n")
  



#Imprimimos el resumen completos de resultados 
print("-------------------------------------------")
print("/    Resumen de Tiempos de Ejecución       /")
print("-------------------------------------------")
for tam,bus, tiempo in zip(size,buscado, execution_times):
    print(f"Tamaño: {tam}  ->  Tiempo: {tiempo} segundos")
print("------------------ -------------------------\n")


# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(size, execution_times, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del Algoritmo de Busqueda Secuencial con Centinela')
plt.grid(True, alpha=0.3)

# Configurar el eje X para mostrar todos los valores
plt.xticks(size, rotation=45)
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.show()

