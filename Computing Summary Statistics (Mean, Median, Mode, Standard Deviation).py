# Program: Computing Summary Statistics for a dataset

import pandas as pd

# Sample dataset
data = {
    "Marks": [85, 78, 90, 88, 92, 75, 85]
}

# Convert to DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -----------------------------
# Summary Statistics
# -----------------------------

# Mean
mean_value = df["Marks"].mean()

# Median
median_value = df["Marks"].median()

# Mode
mode_value = df["Marks"].mode()[0]

# Standard Deviation
std_dev = df["Marks"].std()

print("\nSummary Statistics:")
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Standard Deviation:", std_dev)
