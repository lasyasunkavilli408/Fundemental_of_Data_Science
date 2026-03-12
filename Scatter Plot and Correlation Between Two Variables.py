# Program: Scatter plot and correlation coefficient

import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Study_Hours": [1,2,3,4,5,6,7,8],
    "Marks": [50,55,60,65,70,75,80,85]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -------------------------
# Scatter Plot
# -------------------------

plt.scatter(df["Study_Hours"], df["Marks"], color="blue")

plt.title("Scatter Plot: Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()

# -------------------------
# Correlation Coefficient
# -------------------------

correlation = df["Study_Hours"].corr(df["Marks"])

print("\nCorrelation Coefficient:", correlation)
