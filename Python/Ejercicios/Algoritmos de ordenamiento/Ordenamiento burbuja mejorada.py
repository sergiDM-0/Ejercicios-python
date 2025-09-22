# -*- coding: utf-8 -*-
"""
Algoritmo de Ordenamiento Burbuja Mejorada
==========================================

Una versión más inteligente del burbuja tradicional. Si en una pasada completa 
por la lista no hace ningún intercambio, significa que la lista ya está ordenada 
y el algoritmo se detiene para no trabajar de más.

Complejidad: O(n²) en el peor caso, O(n) en el mejor caso
Categoría: Básico
"""

import time
import random
import matplotlib.pyplot as plt

def burbuja_mejorado(lista):
    """
    Método de ordenamiento burbuja mejorado.
    
    Args:
        lista: Lista de números a ordenar
        
    Returns:
        Lista ordenada
    """
    i = 0
    control = True
    
    while (i <= len(lista)-2) and control:
        control = False
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control = True
        i += 1
    return lista

def ejecutar_pruebas_burbuja_mejorado():
    """
    Ejecuta las pruebas de rendimiento del algoritmo burbuja mejorado.
    """
    # Tamaños de lista para probar
    size = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500,
            1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000,
            3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000]
    
    execution_times = []
    
    print("🔄 Ejecutando pruebas de rendimiento - Algoritmo Burbuja Mejorado")
    print("=" * 60)
    
    # Generar listas aleatorias y medir tiempos
    for i in size:
        array = [random.randint(0, 100) for _ in range(i)]
        array_desordenada = array.copy()
        
        # Medir tiempo de ejecución
        start_time = time.perf_counter()
        lista_ordenada = burbuja_mejorado(array)
        end_time = time.perf_counter()
        
        tiempo_transcurrido = end_time - start_time
        execution_times.append(tiempo_transcurrido)
        
        print(f"Tamaño: {i:4d} | Tiempo: {tiempo_transcurrido:.6f} segundos")
    
    # Mostrar resumen
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE RESULTADOS")
    print("=" * 60)
    for tam, tiempo in zip(size, execution_times):
        print(f"Tamaño: {tam:4d} -> Tiempo: {tiempo:.6f} segundos")
    
    # Crear gráfica
    plt.figure(figsize=(12, 8))
    plt.plot(size, execution_times, 'go-', linewidth=2, markersize=8)
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Rendimiento del Algoritmo de Ordenamiento Burbuja Mejorado')
    plt.grid(True, alpha=0.3)
    plt.xticks(size, rotation=45)
    plt.tight_layout()
    plt.show()
    
    return execution_times, size

if __name__ == "__main__":
    # Ejecutar pruebas
    tiempos, tamanos = ejecutar_pruebas_burbuja_mejorado()
    
    # Mostrar estadísticas finales
    print(f"\n🏆 ESTADÍSTICAS FINALES:")
    print(f"   • Tiempo mínimo: {min(tiempos):.6f} segundos")
    print(f"   • Tiempo máximo: {max(tiempos):.6f} segundos")
    print(f"   • Tiempo promedio: {sum(tiempos)/len(tiempos):.6f} segundos")
    print(f"   • Tamaño máximo probado: {max(tamanos)} elementos")