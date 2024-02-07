# 1. A profiler is a tool that measures various aspects of a program execution. It can provide
# information about the time and space complexity of a program.

# 2. Profiling measures the time and space complexity of a program while benchmarking measures the performance of a 
# program.


import cProfile

import timeit


def sub_function(n):
    # sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n - 1)


def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data


def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i ** 2 for i in range(100000000)]
cProfile.run('test_function()')
cProfile.run('third_function()')
