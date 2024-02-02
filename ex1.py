import timeit
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
# 1. The purpose of this code is to calculate the nth Fibonacci number.
# 2. Yes, this is an example of a divide-and-conquer algorithm because it dividing
# it into a simpler problem.
# 3. The time complexity of this code is O(2^n) because 
# each function call branches into two new recursive calls 
# leading into exponential number of calls as n increases.

def func_memo(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0 or n == 1:
        return n
    else:
        result = func_memo(n-1, memo) + func_memo(n-2, memo)
        memo[n] = result
        return result

#5 The time complexity of this code is O(n) because the memoization

original_times = [timeit.timeit(lambda: func(i), number=1) for i in range(36)]
improved_times = [timeit.timeit(lambda: func_memo(j), number=1) for j in range(36)]

plt.figure()
plt.plot(original_times, label='Original')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()
plt.savefig('ex1.6.1.jpg')


plt.figure()
plt.plot(improved_times, label='Improved')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()
plt.savefig('ex1.6.2.jpg')