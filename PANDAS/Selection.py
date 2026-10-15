# Selection in Pandas means pulling out specific data from a Series or DataFrame.

import pandas as pd

df = pd.read_csv("PK_DATA.csv", index_col="Name")

# SELECTION BY COL
print(df["Name"]. to_string())
print(df["Height"]. to_string())
print(df["Weight"]. to_string())
print(df[["Name", "Height", "Weight"]]. to_string())

# SELECTION BY ROW
print(df.loc["Pikachu", ["Height", "Weight"]])
print(df.iloc[0:11])
print(df.iloc[0:11:2, 0:3])

# EXERCISE
df = pd.read_csv("PK_DATA.csv", index_col="Name")
pokemon = input("Enter a Pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")