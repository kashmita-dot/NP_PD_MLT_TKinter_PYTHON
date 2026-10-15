import numpy as np

array = np.array('A')   # 0 dim
array = np.array(['A', 'B', 'C'])   # 1 dim

array = np.array([['A', 'B', 'C'],
                ['D', 'E', 'F'],
                ['G', 'H', 'I']])  # 2 dim 

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'],['G', 'H', 'I']],
                [['J', 'K', 'L'], ['M', 'N', 'O'],['P', 'Q', 'R']],
                [['S', 'T', 'U'], ['V', 'W', 'X'],['Y', 'Z', ' ']]])  # 3 dim
print(array.ndim)
print(array.shape)

# INDEXING
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'],['G', 'H', 'I']],
                [['J', 'K', 'L'], ['M', 'N', 'O'],['P', 'Q', 'R']],
                [['S', 'T', 'U'], ['V', 'W', 'X'],['Y', 'Z', ' ']]])
print(array[0][0][0])
print(array[0,0,0])  #A
print(array[0,0,1])  #B
print(array[0,0,2])  #C
print(array[0,1,0])  #D
print(array[0,1,1])  #E
print(array[1,1,1])  #N

# EXERCISE 1

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'],['G', 'H', 'I']],
                [['J', 'K', 'L'], ['M', 'N', 'O'],['P', 'Q', 'R']],
                [['S', 'T', 'U'], ['V', 'W', 'X'],['Y', 'Z', ' ']]])

word = array[0,0,0] + array[2,0,0] + array[2,0,0] + array[0,2,1] + array[1,1,2] + array[1,0,2] +array[0,1,1]

print(word)