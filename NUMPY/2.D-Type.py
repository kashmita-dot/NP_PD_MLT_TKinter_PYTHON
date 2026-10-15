# dtype = Keyword argument that tells NumPy what kind of values are stored in an array
#        Otherwise NumPy guesses the best data type based on your data
#        Manually setting dtype improves performance
#        & is more memory efficient (especially when working with large data sets)

# integer (int8, int16, int32, int64)
# float (float16, float32, float64)
# boolean (bool_)
# string (str_)
# object (object_)

import numpy as np

# INTERGER

array = np.array([1, 2, 3, 4, 5], dtype=np.int64)    # 1 Bytes = 8 Bytes, Min= -9.22e18 Max= 9.22e18
array = np.array([1, 2, 3, 4, 5], dtype=np.int32)    # 1 Bytes = 4 Bytes, Min= -2,147,483,648 Max= 2,147,483,647
array = np.array([1, 2, 3, 4, 5], dtype=np.int16)    # 1 Bytes = 2 Bytes, Min= -32,768 Max= 32,767
array = np.array([1, 2, 3, 4, 5], dtype=np.int8)       # 1 Bytes = 1 Bytes, Min= -128 Max= 127
array = np.array([126, 127, 128], dtype=np.int8)       #OverflowError: Python integer 128 out of bounds for int8
print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")

# FLOAT 

array = np.array([1, 2, 3, 4, 5], dtype=np.float64)
array = np.array([1, 2, 3, 4, 5], dtype=np.float32)
array = np.array([1, 2, 3, 4, 5], dtype=np.float16)
print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")

# BOOLEAN

array = np.array([1, 2, 3, 4, 5], dtype=np.bool_)   #Not equal to zero is not bool
print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")

# STRINGS

array = np.array([1, 2, 3, 4, 5], dtype=np.str_)  #<U1
array = np.array([10, 20, 30, 40, 50], dtype=np.str_)  #<U2
array = np.array(["apple", "banana", "orange", "kiwi"], dtype=np.str_)  #<U6
array = np.array(["apple", "banana", "orange", "kiwi"], dtype="<U4")
print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")

# OBJECTS

array = np.array([1, 2.1, "apple", 4, True], dtype=np.object_)
print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")

# CONVERTING DATA TYPE

array = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
array = array.astype(np.float16)
array = array.astype(np.int16)
print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")