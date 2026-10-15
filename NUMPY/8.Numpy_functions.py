
import numpy as np

# Creates an array with zeros
array = np.zeros((2, 3, 10))
print(array)

# # Creates an array with ones
array = np.ones((2, 3, 10))
print(array)

# # Creates an array with a given value
array = np.full((2, 3, 10), 9)
print(array)

# # Creates an array w/o initializing entries
array = np.empty((2, 3))
print(array)

# # Creates an identity matrix with 0s and 1s
array = np.eye(5)
print(array)

# # Creates an array with evenly spaced values up to a given range
array = np.arange(0, 100, 0.1) # (start, stop, step)
print(array)

# # Creates an array with a set number of values that are evenly spaced
array = np.linspace(0, 10, 5) # (start, stop, num)
print(array)