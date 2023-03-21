import requests
import importlib

# define a list of required packages
required_packages = ['bs4', 'autopep8']

# check if the required packages are installed
for package in required_packages:
    try:
        importlib.import_module(package)
    except ImportError:
        # install the missing package using pip
        import subprocess
        subprocess.run(['pip', 'install', package])

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

# prompt the user if they want to keep the installed packages
answer = input("Do you want to keep the installed packages? (y/n) ")
if answer.lower() == 'n':
    # remove the installed packages using pip
    for package in required_packages:
        subprocess.run(['pip', 'uninstall', '-y', package])
