# -*- coding: utf-8 -*-
"""
Algoritmo de Ordenamiento Coctel (Cocktail Shaker Sort)
======================================================

Es una variante del burbuja. En lugar de ir siempre en una dirección, va de 
izquierda a derecha (llevando el más grande al final) y luego de derecha a 
izquierda (llevando el más pequeño al inicio). Es como sacudir una coctelera. 🍸

Complejidad: O(n²)
Categoría: Básico
"""

import time
import random
import matplotlib.pyplot as plt

def coctel(lista):
    """
    Método de ordenamiento cóctel o burbuja bidireccional.
    
    Args:
        lista: Lista de números a ordenar
        
    Returns:
        Lista ordenada
    """
    izquierda = 0
    derecha = len(lista) - 1
    control = True
    
    while (izquierda < derecha) and control:
        control = False
        
        # Pasar de izquierda a derecha
        for i in range(izquierda, derecha):
            if lista[i] > lista[i+1]:
                control = True
                lista[i], lista[i+1] = lista[i+1], lista[i]
        derecha -= 1
        
        # Pasar de derecha a izquierda
        for j in range(derecha, izquierda, -1):
            if lista[j] < lista[j-1]:
                control = True
                lista[j], lista[j-1] = lista[j-1], lista[j]
        izquierda += 1
    
    return lista

def ejecutar_pruebas_coctel():
    """
    Ejecuta las pruebas de rendimiento del algoritmo coctel.
    """
    # Tamaños de lista para probar
    size = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500,
            1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000,
            3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000]
    
    execution_times = []
    
    print("🔄 Ejecutando pruebas de rendimiento - Algoritmo Coctel")
    print("=" * 60)
    
    # Generar listas aleatorias y medir tiempos
    for i in size:
        array = [random.randint(0, 100) for _ in range(i)]
        array_desordenada = array.copy()
        
        # Medir tiempo de ejecución
        start_time = time.perf_counter()
        lista_ordenada = coctel(array)
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
    plt.plot(size, execution_times, 'mo-', linewidth=2, markersize=8)
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Rendimiento del Algoritmo de Ordenamiento Coctel')
    plt.grid(True, alpha=0.3)
    plt.xticks(size, rotation=45)
    plt.tight_layout()
    plt.show()
    
    return execution_times, size

if __name__ == "__main__":
    # Ejecutar pruebas
    tiempos, tamanos = ejecutar_pruebas_coctel()
    
    # Mostrar estadísticas finales
    print(f"\n🏆 ESTADÍSTICAS FINALES:")
    print(f"   • Tiempo mínimo: {min(tiempos):.6f} segundos")
    print(f"   • Tiempo máximo: {max(tiempos):.6f} segundos")
    print(f"   • Tiempo promedio: {sum(tiempos)/len(tiempos):.6f} segundos")
    print(f"   • Tamaño máximo probado: {max(tamanos)} elementos")