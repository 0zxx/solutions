1) Instalar o Selenium:  
```  
# Instalar o Python e o pip (caso ainda não estejam instalados)  
sudo apt update  
sudo apt install python3 python3-pip -y  
  
# Instalar o Selenium  
pip3 install selenium  
```  
2) Criar um script de exemplo:  
Crie um arquivo com o nome exemplo_selenium.py (ou qualquer outro nome que você preferir) e adicione o seguinte código:  
```  
from selenium import webdriver

# Configurações do navegador
options = webdriver.FirefoxOptions()
options.headless = True  # Rodar o navegador sem exibir a interface gráfica

# Inicializar o navegador
driver = webdriver.Firefox(options=options)

# Acessar uma página
driver.get('https://www.google.com')

# Encontrar um elemento e interagir com ele
search_box = driver.find_element_by_name('q')
search_box.send_keys('Selenium')
search_box.submit()

# Fechar o navegador
driver.quit()
```  
Este script acessa o Google, busca por "Selenium" e fecha o navegador. Você pode modificar este código para realizar outras ações de acordo com suas necessidades.  
Lembre-se de instalar o driver do navegador que deseja usar (por exemplo, o geckodriver para o Firefox). Para instalar o geckodriver, basta executar o seguinte comando:  
```  
sudo apt install firefox-geckodriver -y
```  
