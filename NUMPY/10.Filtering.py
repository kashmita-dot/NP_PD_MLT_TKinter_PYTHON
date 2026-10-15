
# Filtering = Refers to the process of selecting 
#             elements from an array that match a given condition

import numpy as np
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                [39, 22, 15, 99, 19, 18, 20, 21]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 ==0]
odds = ages[ages % 2 !=0]
print(odds)

# SHAPES
adults = np.where(ages >= 18, ages, 0)
print(adults)