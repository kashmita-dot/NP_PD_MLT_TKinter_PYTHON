import numpy as np

# Aggregate functions = summarize data and typically 
#                       return a single value

array = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])

print(np.sum(array)) # Sum of all elements
print(np.mean(array)) # Average of all elements
print(np.std(array)) # Measure of spread
print(np.var(array)) # Square of standard deviation
print(np.min(array)) # Smallest value
print(np.max(array)) # Largest value
print(np.argmin(array)) # Position (flattened) of smallest
print(np.argmax(array)) # Position (flattened) of largest
print(np.sum(array, axis=0)) # sum column-wise (vertically)
print(np.sum(array, axis=1)) # sum row-wise (horizontally)