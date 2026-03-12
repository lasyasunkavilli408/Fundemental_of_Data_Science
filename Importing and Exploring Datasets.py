# Program: Importing and Exploring Dataset

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset (instead of loading a file)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [21, 22, 20, 23, 21],
    "Marks": [85, 78, 90, 88, 92]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Show first rows
print("\nFirst 5 rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Statistical summary
print("\nStatistics:")
print(df.describe())

# Column names
print("\nColumns:")
print(df.columns)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Plot marks
df["Marks"].plot(kind="bar", title="Student Marks")
plt.show()
