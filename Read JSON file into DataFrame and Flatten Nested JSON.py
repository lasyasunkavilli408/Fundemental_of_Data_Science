# Program: Read JSON file and convert nested JSON to flat DataFrame

import pandas as pd

# Sample nested JSON data
data = {
    "students": [
        {
            "id": 1,
            "name": "Alice",
            "address": {"city": "New York", "zip": "10001"},
            "marks": 85
        },
        {
            "id": 2,
            "name": "Bob",
            "address": {"city": "Los Angeles", "zip": "90001"},
            "marks": 78
        }
    ]
}

# Convert nested JSON to flat table
df = pd.json_normalize(data["students"])

print("Flattened DataFrame:")
print(df)
