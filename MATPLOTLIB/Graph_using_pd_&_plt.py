import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("PK_DATA.csv")
type_count = df["Type1"].value_counts(ascending=True)
plt.barh(type_count.index, type_count.values, color="orange",
                                                    edgecolor="black")

plt.title("# of Pokemon by primary Type")
plt.xlabel("count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()