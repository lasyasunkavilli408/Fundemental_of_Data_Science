# Program: Web scraping HTML table and converting to DataFrame

import requests
import pandas as pd
from bs4 import BeautifulSoup

# Example website containing tables
url = "https://www.w3schools.com/html/html_tables.asp"

# Send request to webpage
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the table
table = soup.find("table")

# Extract table headers
headers = []
for th in table.find_all("th"):
    headers.append(th.text)

# Extract table rows
rows = []
for tr in table.find_all("tr")[1:]:
    cols = tr.find_all("td")
    rows.append([col.text for col in cols])

# Convert to DataFrame
df = pd.DataFrame(rows, columns=headers)

print("Extracted Table Data:")
print(df)
