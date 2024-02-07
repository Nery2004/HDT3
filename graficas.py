import random
import time
import matplotlib.pyplot as plt

# Implementación de los algoritmos de ordenamiento

# Algoritmo de ordenamiento Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Algoritmo de ordenamiento Insertion Sort
def gnome_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Algoritmo de ordenamiento Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Algoritmo de ordenamiento Quick Sort
def countingSort_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return countingSort_sort(left) + middle + countingSort_sort(right)

# Algoritmo de ordenamiento Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Función para generar datos de entrada aleatorios
def generate_random_data(size):
    return [random.randint(0, size) for _ in range(size)]

# Función para medir el tiempo de ejecución de un algoritmo de ordenamiento
def measure_time(algorithm, data):
    start_time = time.time()
    algorithm(data)
    end_time = time.time()
    return end_time - start_time

# Tamaños de datos para probar
data_sizes = [100, 200, 300, 400, 500]

# Medir tiempos de ejecución para cada algoritmo
bubble_sort_times = []
insertion_sort_times = []
merge_sort_times = []
quick_sort_times = []
selection_sort_times = []

for size in data_sizes:
    data = generate_random_data(size)
    bubble_sort_times.append(measure_time(bubble_sort, data.copy()))
    insertion_sort_times.append(measure_time(gnome_sort, data.copy()))
    merge_sort_times.append(measure_time(merge_sort, data.copy()))
    quick_sort_times.append(measure_time(countingSort_sort, data.copy()))
    selection_sort_times.append(measure_time(selection_sort, data.copy()))

# Graficar los tiempos de ejecución
plt.figure(figsize=(10, 6))
plt.plot(data_sizes, bubble_sort_times, label='Bubble Sort')
plt.plot(data_sizes, insertion_sort_times, label='Insertion Sort')
plt.plot(data_sizes, merge_sort_times, label='Merge Sort')
plt.plot(data_sizes, quick_sort_times, label='Quick Sort')
plt.plot(data_sizes, selection_sort_times, label='Selection Sort')
plt.xlabel('Tamaño del conjunto de datos')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento teórico esperado de algoritmos de ordenamiento')
plt.legend()
plt.grid(True)
plt.show()
