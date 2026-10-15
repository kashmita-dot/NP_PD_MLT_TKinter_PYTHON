import matplotlib.pyplot as plt
import numpy as np

# Bar chart = compare categories of data by representing each category with a bar

categories = np.array(["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets" ])
values = np.array([4, 3, 2, 5, 3, 1])

plt.bar(categories, values, color="skyblue")
# plt.barh(categories, values, color="skyblue")      #Horozontal bar chart

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")
plt.show()