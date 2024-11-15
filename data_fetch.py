import requests
from bs4 import BeautifulSoup
import os

# URL of the page containing JSON links
url = "https://www.sec.gov/edgar/sec-api-documentation"

# Make a request to the webpage
response = requests.get(url)
response.raise_for_status()  # Check for errors

# Parse the page content
soup = BeautifulSoup(response.text, "html.parser")

# Create a directory to store JSON files
os.makedirs("json_files", exist_ok=True)

# Find all links ending with .json
json_links = []
for link in soup.find_all("a", href=True):
    if link['href'].endswith('.json'):
        json_links.append(link['href'])

# Download each JSON file
for json_link in json_links:
    # Complete the URL if it is relative
    json_url = json_link if json_link.startswith("http") else f"https://www.sec.gov{json_link}"
    
    # Get the file name
    file_name = os.path.join("json_files", json_url.split("/")[-1])

    # Download the JSON file
    print(f"Downloading {file_name}...")
    json_response = requests.get(json_url)
    json_response.raise_for_status()

    # Save the file
    with open(file_name, "wb") as file:
        file.write(json_response.content)
        
print("All JSON files have been downloaded!")
