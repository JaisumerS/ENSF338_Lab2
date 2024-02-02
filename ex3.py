# 1. A profiler is a tool that measures various aspects of a program execution. It can provide
# information about the time and space complexity of a program.

# 2. Profiling measures the time and space complexity of a program while benchmarking measures the performance of a 
# program.


import cProfile

# Start the profiler
profiler = cProfile.Profile()
profiler.enable()


# Stop the profiler
profiler.disable()

# Print the profiling results
profiler.print_stats()