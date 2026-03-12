# Program: Handling Missing Values and Outliers

import pandas as pd
import numpy as np

# Sample dataset with missing values and outliers
data = {
    "Marks": [85, 78, np.nan, 88, 150, 75, 90, np.nan]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# --------------------------------
# Handling Missing Values
# --------------------------------

# Fill missing values with mean
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

print("\nAfter Handling Missing Values (Imputation using Mean):")
print(df)

# --------------------------------
# Detecting and Removing Outliers
# --------------------------------

# Calculate Q1 and Q3
Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)

# Interquartile Range
IQR = Q3 - Q1

# Define limits
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter dataset to remove outliers
filtered_df = df[(df["Marks"] >= lower_bound) & (df["Marks"] <= upper_bound)]

print("\nDataset After Removing Outliers:")
print(filtered_df)
