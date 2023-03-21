from bs4 import BeautifulSoup
import requests

# prompt the user to input the URL or HTML file
input_type = input("Enter 'url' or 'file' to specify the input type: ")
if input_type == "url":
    url = input("Enter the URL to fix: ")
    response = requests.get(url)
    html = response.content
elif input_type == "file":
    file_path = input("Enter the path to the HTML file to fix: ")
    with open(file_path, "r") as f:
        html = f.read()
else:
    print("Invalid input type")
    exit()

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# fix the HTML issues
# remove any <meta> tags that have a content attribute but no name attribute
for tag in soup.find_all("meta"):
    if "content" in tag.attrs and "name" not in tag.attrs:
        tag.decompose()

# add a charset meta tag if one is not present
if not soup.find("meta", charset=True):
    soup.head.append(soup.new_tag("meta", charset="utf-8"))

# remove any <link> tags that have a type attribute but no rel attribute
for tag in soup.find_all("link"):
    if "type" in tag.attrs and "rel" not in tag.attrs:
        tag.decompose()

# print the fixed HTML content
print(soup.prettify())
