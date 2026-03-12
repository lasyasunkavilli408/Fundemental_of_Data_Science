# Program: Histogram and Box Plot to understand distribution

import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Marks": [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -------------------------
# Histogram
# -------------------------

plt.figure(figsize=(6,4))
plt.hist(df["Marks"], bins=5, color="skyblue", edgecolor="black")

plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

# -------------------------
# Box Plot
# -------------------------

plt.figure(figsize=(6,4))
plt.boxplot(df["Marks"])

plt.title("Box Plot of Marks")
plt.ylabel("Marks")

plt.show()
