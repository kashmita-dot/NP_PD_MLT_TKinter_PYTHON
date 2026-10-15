import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 =np.array([13, 15, 20, 30])

line_style = dict(marker=".",
                markersize=20,                    
                markerfacecolor="black",            
                markeredgecolor="black",
                linestyle="solid",
                linewidth=3)

plt.plot(x, y1, color="red", **line_style)           
plt.plot(x, y2, color="blue", **line_style)
plt.plot(x, y3, color="green", **line_style)
plt.show()