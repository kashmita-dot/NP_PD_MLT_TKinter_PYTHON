import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 250, 275, 225])
colors = ["pink", "lightgrey", "beige", "skyblue"]

plt.pie(values, labels=categories,
                autopct="%1.1f%%",
                colors=colors,
                explode=[0,0,0,0.2],
                shadow=True,
                startangle=90)

plt.title("cody college")
plt.show()