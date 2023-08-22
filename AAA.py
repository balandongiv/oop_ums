import numpy as np
import sys

my_arr = np.arange(100000000)
my_list = list(range(100000000))

# Check memory usage of NumPy array
numpy_memory_usage = sys.getsizeof(my_arr)
print(f"Memory usage of NumPy array: {numpy_memory_usage} bytes")

# Check memory usage of Python list
list_memory_usage = sys.getsizeof(my_list)
print(f"Memory usage of Python list: {list_memory_usage} bytes")


import numpy as np

# Create a 2D Python list
data_2d = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

# Convert the 2D Python list to a NumPy array
arr_2d = np.array(data_2d)

# Display the 2D NumPy array
print("2D NumPy Array:")
print(arr_2d)
