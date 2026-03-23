import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

# Fetch the webpage
url = "https://pulse.berklee.edu/scales/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the Blues Scales section
blues_scales = []

# Find the h2 header with "Blues Scales"
h2_tag = soup.find('h2', string="Blues Scales")

if h2_tag:
    # Get all links starting from the h2
    all_links = h2_tag.find_all_next('a')
    
    for link in all_links:
        # Stop if we encounter another h2 (next major section)
        next_h2 = link.find_previous('h2')
        if next_h2 and next_h2 != h2_tag:
            break
        
        scale_name = link.get_text(strip=True)
        scale_url = link.get('href')
        
        # Initialize notes and signature
        notes = ""
        signature = ""
        
        try:
            # Fetch the individual scale page
            scale_response = requests.get(scale_url, timeout=5)
            scale_soup = BeautifulSoup(scale_response.content, 'html.parser')
            
            # Find the scales-description div
            scales_desc = scale_soup.find('div', class_='scales-description')
            
            if scales_desc:
                # Get all strong tags
                strong_tags = scales_desc.find_all('strong')
                
                # First strong tag contains notes
                if len(strong_tags) > 0:
                    notes = strong_tags[0].get_text(strip=True)
                
                # Second strong tag contains signature
                if len(strong_tags) > 1:
                    signature = strong_tags[1].get_text(strip=True)
            
            # Add a small delay to be respectful to the server
            time.sleep(0.3)
            
        except Exception as e:
            print(f"Error fetching {scale_url}: {e}")
        
        blues_scales.append({
            'scale_name': scale_name,
            'url': scale_url,
            'notes': notes,
            'signature': signature
        })

# Create dataframe
df = pd.DataFrame(blues_scales)

print(f"Found {len(df)} Blues Scales:")
print(df)

# Save to CSV in root folder
csv_path = os.path.expanduser('~/blues_scales.csv')
df.to_csv(csv_path, index=False)
print(f"\nSuccessfully saved {len(df)} blues scales to {csv_path}")
