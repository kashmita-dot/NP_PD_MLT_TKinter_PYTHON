
# A Pandas DataFrame is a two-dimensional, tabular 
#data structure that works like a spreadsheet with rows and columns.

import pandas as pd

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "age": [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
# print(df.loc["Employee 1"])
# print(df.iloc[1])

# ADD A NEW COL
df["Job"] = ["Cook", "N/A", "Cashier"]

# ADD A NEW ROWS
new_rows = pd.DataFrame([{"Name": "Sandy", "age": 28, "Job": "Engineer"},
                        {"Name": "Eugene", "age": 60, "Job": "Manager"}],
                        index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_rows])
print(df)