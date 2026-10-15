# Matplotlib is a Python library used for data visualization. 
# It provides a MATLAB-like interface for quick plotting. 
# After finishing this series, I would recommend learning linear algebra, 
# Scikit-learn, or more advanced Matplotlib topics.

import matplotlib.pyplot as plt
import numpy as np
# print(matplotlib.__version__)

x = np.array([2023, 2024, 2025, 2026])
y = np.array([15, 25, 30, 20])

plt.plot(x, y)

plt.show()