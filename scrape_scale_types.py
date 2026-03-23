import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import os

# Fetch the webpage
url = "https://pulse.berklee.edu/scales/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract scale types
scale_types = []

# Find all h2 and h3 headers to get scale categories and types
for h2 in soup.find_all('h2'):
    category = h2.get_text(strip=True)
    # Skip the generic "All Scales" header
    if category != "All Scales":
        scale_types.append({
            'category': None,
            'type': category
        })

for h3 in soup.find_all('h3'):
    scale_type = h3.get_text(strip=True)
    scale_types.append({
        'category': None,
        'type': scale_type
    })

# Create dataframe
df = pd.DataFrame(scale_types)

# Remove duplicates (the structure repeats)
df = df.drop_duplicates(subset=['type']).reset_index(drop=True)

print(f"Found {len(df)} unique scale types:")
print(df)

# Connect to SQLite database
db_path = os.path.expanduser('~/ai_music.db')
conn = sqlite3.connect(db_path)

# Write dataframe to SQLite database, replace if table exists
df.to_sql('scale_types', conn, if_exists='replace', index=False)

print(f"\nSuccessfully inserted {len(df)} scale types into the 'scale_types' table in {db_path}")

# Close connection
conn.close()

# Save to CSV in root folder
csv_path = os.path.expanduser('~/scale_types.csv')
df.to_csv(csv_path, index=False)
print(f"Successfully saved {len(df)} scale types to {csv_path}")
