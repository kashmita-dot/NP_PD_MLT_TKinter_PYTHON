# Random numbers in NumPy are useful for simulations,
# modeling, applying random transformations, and testing purposes.

import numpy as np
rng = np.random.default_rng() 
print(rng.integers(low=1, high=7, size=(3, 4))) # 3x4 array of Ints

# Floating Point Numbers
np.random.seed()
print(np.random.uniform(low=-1, high=1, size=(3, 2))) # floats between 2 values

# Shuffle
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

# Random Choice
fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])
print(rng.choice(fruits, size=(3, 3)))