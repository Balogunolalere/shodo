import os
import requests
from bs4 import BeautifulSoup

# Define the Wikipedia page URL
url = 'https://en.wikipedia.org/wiki/Algorithmic_efficiency'

# Send a GET request to the URL and get the response object
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the page title and clean it up for use in file names
page_title = soup.find('h1', class_='firstHeading').text.strip().replace(' ', '_')

# Extract the main text content of the page and clean it up for saving to a file
main_content = soup.find('div', class_='mw-parser-output').get_text().strip()

# Define the directory where the text files will be saved
output_dir = 'wikipedia_pages'

# Create the output directory if it doesn't already exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the file name format and write the content to files
lines_per_file = 10
for i, line in enumerate(main_content.split('\n\n')):
    file_num = i // lines_per_file
    file_name = f"ECO_{file_num}.txt"
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'a', encoding='utf-8') as f:
        if i % lines_per_file == 0:
            f.write(f"--- Start of file {file_num} ---\n")
        f.write(line + '\n')
        if i % lines_per_file == lines_per_file - 1:
            f.write(f"--- End of file {file_num} ---\n")
