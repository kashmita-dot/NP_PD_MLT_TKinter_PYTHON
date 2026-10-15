# Data cleaning is the process of fixing or removing: incomplete, incorrect, or irrelevant data. ~75% of work done with Pandas is data cleaning.

import pandas as pd
df = pd.read_csv("PK_DATA.csv")

#1. Drop irrelevant columns
df = df.drop(columns=["Legendary", "No"])

# 2. Handle missing data
df = df.dropna(subset=["Type2"])
df = df.fillna({"Type2": "None" })

#3. Fix inconsistent value
df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
                                    "Fire": "FIRE",
                                    "Water": "WATER"})

# 4. Standardize text
df["Name"] = df["Name"].str.lower()

# 5. Fix data types
df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicate values
df = df.drop_duplicates()
print(df.to_string())