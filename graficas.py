import cProfile
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

# Algoritmo de ordenamiento Gnome Sort
def gnome_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        if i == 0:
            i = i + 1
        if arr[i] >= arr[i-1]:
            i = i + 1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i - 1

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
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

# Algoritmo de ordenamiento Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Algoritmo de ordenamiento Counting Sort
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    sorted_arr = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    for num in reversed(arr):
        sorted_arr[count[num] - 1] = num
        count[num] -= 1

    return sorted_arr

# Algoritmo de ordenamiento Radix Sort
def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10

# Función para generar datos aleatorios
def generate_random_data(size):
    return [random.randint(0, size) for _ in range(size)]

# Función para medir el tiempo de ejecución
def measure_time(algorithm, data):
    start_time = time.time()
    algorithm(data)
    end_time = time.time()
    return end_time - start_time

# Tamaños de datos para probar
data_sizes = [100, 200, 300, 400, 500]

# Medir tiempos de ejecución para cada algoritmo
bubble_sort_times = []
gnome_sort_times = []
merge_sort_times = []
quick_sort_times = []
selection_sort_times = []
counting_sort_times = []
radix_sort_times = []

for size in data_sizes:
    data = generate_random_data(size)
    bubble_sort_times.append(measure_time(bubble_sort, data.copy()))
    gnome_sort_times.append(measure_time(gnome_sort, data.copy()))
    merge_sort_times.append(measure_time(merge_sort, data.copy()))
    quick_sort_times.append(measure_time(quick_sort, data.copy()))
    selection_sort_times.append(measure_time(selection_sort, data.copy()))
    counting_sort_times.append(measure_time(counting_sort, data.copy()))
    radix_sort_times.append(measure_time(radix_sort, data.copy()))

# Graficar los tiempos de ejecución
plt.figure(figsize=(10, 6))
plt.plot(data_sizes, bubble_sort_times, label='Bubble Sort')
plt.plot(data_sizes, gnome_sort_times, label='Gnome Sort')
plt.plot(data_sizes, merge_sort_times, label='Merge Sort')
plt.plot(data_sizes, quick_sort_times, label='Quick Sort')
plt.plot(data_sizes, selection_sort_times, label='Selection Sort')
plt.plot(data_sizes, counting_sort_times, label='Counting Sort')
plt.plot(data_sizes, radix_sort_times, label='Radix Sort')

plt.xlabel('Tamaño del conjunto de datos')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento teórico esperado de algoritmos de ordenamiento')
plt.legend()
plt.grid(True)
plt.show()