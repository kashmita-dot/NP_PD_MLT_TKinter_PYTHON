# Slicing in NumPy allows you to extract portions of an array using
#                 a [start:stop:step] syntax. 
#                 It works similarly to Python lists but is 
#                 more powerful, especially for multi-dimensional arrays.

import numpy as np

array = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

# array[start:end:step]

# ROW SELECTION
print(array[::-1])   #reverse
print(array[0:4:4])

# COLUMN SELECTION
print(array[:,3])
print(array[:,-1])
print(array[:,::-2])  #reserve

# ROW AND COLUMN SELECTION
print(array[0:2, 0:2])  #1,2,5,6
print(array[0:2, 2:])     #3,4,7,8
print(array[2:, 0:2])   #9,10,13,14
print(array[2:, 2:])    #11,12,15,16
