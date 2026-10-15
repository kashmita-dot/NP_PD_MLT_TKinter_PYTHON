
import numpy as np

# --------------------------------------------
# Save a NumPy array
# --------------------------------------------
array = np.array([[1, 2, 3], [4, 5, 6]])
np.save("data", array)
print("File saved!")

# --------------------------------------------
# Load a single NumPy array
# --------------------------------------------
array = np.load("data.npy")
print(array)
# ------------------------------------------
# Save multiple NumPy arrays
# --------------------------------------------
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([2022, 2023, 2024, 2025])
array3 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])

np.savez("data", array1, array2, array3)  #where Z is ZIP

print("NumPy data was saved!")

# --------------------------------------------
# Load multiple NumPy arrays
# --------------------------------------------
arrays = np.load("data.npz")

print(arrays["arr_0"])
print(arrays["arr_1"])
print(arrays["arr_2"])