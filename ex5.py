import timeit
import numpy as np
import random
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

def linear_func(x, a, b):
    return a * x + b

def log_func(x, a, b):
    return a * np.log2(x) + b

sizes = [1000, 2000, 4000, 8000, 16000, 32000]
repeat = 1000
iterations = 100

linear_times = []
binary_times = []

for size in sizes:
    arr = sorted(np.random.randint(1, size+1, size))
    total_time_linear = 0
    total_time_binary = 0

    for _ in range(repeat):
        target = random.choice(arr)
        start_time = timeit.timeit(lambda: linear_search(arr, target), number=iterations)
        total_time_linear += start_time
        start_time = timeit.timeit(lambda: binary_search(arr, target), number=iterations)
        total_time_binary += start_time

    avg_time_linear = total_time_linear / repeat
    avg_time_binary = total_time_binary / repeat

    linear_times.append(avg_time_linear)
    binary_times.append(avg_time_binary)

popt_linear, _ = curve_fit(linear_func, sizes, linear_times)
popt_binary, _ = curve_fit(log_func, sizes, binary_times)

x_values = np.linspace(min(sizes), max(sizes), 1000)

y_values_linear = linear_func(x_values, *popt_linear)
y_values_binary = log_func(x_values, *popt_binary)

plt.figure(figsize=(10, 6))
plt.scatter(sizes, linear_times, label='Linear search times')
plt.plot(x_values, y_values_linear, label='Fitted linear function')
plt.scatter(sizes, binary_times, label='Binary search times')
plt.plot(x_values, y_values_binary, label='Fitted logarithmic function')
plt.legend()
plt.show()

# Linear_func: Is a linear function, it takes in x, a and b as parameters and returns a * x + b
# Log_func: Is a logarithmic function, it takes in x, a and b as parameters and returns a * np.log2(x) + b
# The linear search times is as expected, but the binary search time is O(1) which is the best case scenario
# our guess for the binary search is that the average time of a binary search is O(log n) so we would assume that
# this binary search would also have that time complexity.
