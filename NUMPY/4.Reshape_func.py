# reshape() = Changes the shape of an array
#             w/o altering its underlying data
#             array.reshape(layers, rows, columns)

import numpy as np

array = np.array([1, 2, 3, 4, 5 ,6, 7, 8, 9, 10, 11, 12])

array = array.reshape(6,2)
array = array.reshape(3,2,2) # dim
array = array.reshape(-1,1)
print(array)