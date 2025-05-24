import matplotlib.pyplot as plt
import random
import time
from quicksort_utils import randomized_quick_sort, deterministic_quick_sort

# Функція для вимірювання часу

def measure_average_time(sort_func, arr, runs=5):
    total_time = 0.0
    for _ in range(runs):
        data = arr.copy()
        start = time.perf_counter()
        sort_func(data)
        total_time += time.perf_counter() - start
    return total_time / runs

# Розміри масивів
sizes = [10_000, 50_000, 100_000, 500_000]
rand_times = []
det_times = []

for size in sizes:
    array = [random.randint(0, 10**6) for _ in range(size)]

    rand_time = measure_average_time(randomized_quick_sort, array)
    det_time = measure_average_time(deterministic_quick_sort, array)

    rand_times.append(rand_time)
    det_times.append(det_time)

    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {det_time:.4f} секунд\n")

# Побудова графіка
plt.plot(sizes, rand_times, label="Рандомізований QuickSort")
plt.plot(sizes, det_times, label="Детермінований QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
