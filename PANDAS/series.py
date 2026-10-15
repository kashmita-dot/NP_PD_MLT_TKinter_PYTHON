# A Series is a one-dimensional labeled array that can hold data of any type. 
# Think of it like a single column in a spreadsheet.
# Each value in a Series has an associated index label 
# (like row numbers, but can be customized).

import pandas as pd

data = [100, 102, 104]
series = pd.Series(data, index=["a", "b", "c"])
series.loc["c"] = 200
print(series)
print(series.iloc[0])
print(series[series < 200])

# DICt
calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)
series.loc["Day 3"] += 500
print(series.loc["Day 3"])
print(series[series >= 2000])
print(series[series < 2000])
print(series)
