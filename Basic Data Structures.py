# Program: Basic Data Structures in Python

import numpy as np
import pandas as pd

# ------------------------
# List Example
# ------------------------

numbers = [10, 20, 30, 40]

print("List:")
print(numbers)

numbers.append(50)

print("Updated List:")
print(numbers)


# ------------------------
# NumPy Array
# ------------------------

array = np.array([1, 2, 3, 4, 5])

print("\nNumPy Array:")
print(array)

print("Array multiplied by 2:")
print(array * 2)


# ------------------------
# Matrix Example
# ------------------------

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("\nMatrix:")
print(matrix)

print("\nTranspose of Matrix:")
print(matrix.T)


# ------------------------
# DataFrame Example
# ------------------------

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 22, 20],
    "Marks": [85, 78, 90]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nMarks Column:")
print(df["Marks"])

print("\nStatistics:")
print(df.describe())
