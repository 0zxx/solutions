import requests
from bs4 import BeautifulSoup
import urllib.parse
import os

# Define a tag que o usuário quer buscar
tag = "alchemy"

# Define a URL de pesquisa do Google Imagens
url = "https://www.google.com/search?q=" + tag + "&tbm=isch"

# Define um cabeçalho HTTP para se passar por um navegador
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

# Faz a requisição HTTP para a URL de pesquisa
response = requests.get(url, headers=headers)

# Extrai todas as miniaturas de imagem da página HTML
soup = BeautifulSoup(response.text, "html.parser")
img_tags = soup.find_all("img", class_="rg_i")

# Define a pasta onde as imagens serão salvas
folder_name = "imagens_" + tag
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Percorre as miniaturas e baixa as imagens em tamanho completo
for img_tag in img_tags:
    try:
        img_url = img_tag["data-src"]
        if img_url is not None:
            img_url = urllib.parse.unquote(img_url)
            img_url = img_url.split("&")[0]
            response = requests.get(img_url, headers=headers)
            with open(os.path.join(folder_name, os.path.basename(img_url)), "wb") as f:
                f.write(response.content)
            print("Imagem salva: " + img_url)
    except:
        pass
