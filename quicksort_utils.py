import random
import time


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def measure_time(sort_func, arr, repeats=5):
    total_time = 0
    for _ in range(repeats):
        arr_copy = arr[:]
        start = time.perf_counter()
        sort_func(arr_copy)
        total_time += time.perf_counter() - start
    return total_time / repeats
