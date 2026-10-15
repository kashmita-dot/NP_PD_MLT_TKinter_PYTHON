import pandas as pd

# CSV
df = pd.read_csv("PK_DATA.csv")
print(df.to_string())
print(df)

# JSON
df = pd.read_json("PK_DATA.json")
print(df)
