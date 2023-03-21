import requests
import importlib

# check if BeautifulSoup is installed
try:
    importlib.import_module('bs4')
except ImportError:
    # install BeautifulSoup using pip
    import subprocess
    subprocess.run(['pip', 'install', 'beautifulsoup4'])

from bs4 import BeautifulSoup

# prompt the user for the input source
input_source = input("Enter the path to the HTML file or a URL to fetch the HTML from: ")

# check if the input source is a URL
if input_source.startswith('http'):
    # fetch the HTML from the URL
    response = requests.get(input_source)
    html = response.text
else:
    # read in the HTML file
    with open(input_source, 'r') as f:
        html = f.read()

# parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# write out the indented code to a new file
output_path = input("Enter the path to the output file: ")
with open(output_path, 'w') as f:
    f.write(soup.prettify())
