import importlib
import subprocess

# check if autopep8 is installed
try:
    importlib.import_module('autopep8')
except ImportError:
    # install autopep8 using pip
    subprocess.run(['pip', 'install', 'autopep8'])

import autopep8

# Path of File
nome_arquivo = input("Insira o nome do arquivo ou caminho completo do arquivo: ")

# Opening file and learning content
with open(nome_arquivo, 'r') as arquivo:
    codigo = arquivo.read()

# fix the code using the autopep8 library
codigo_corrigido = autopep8.fix_code(codigo)

# rewrite the code with the fixed code
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(codigo_corrigido)

print(f"O arquivo {nome_arquivo} foi corrigido com sucesso.")

# prompt the user to choose whether to keep the libraries installed at the beginning
keep_libraries = input("Deseja manter as bibliotecas instaladas no início? (s/n): ")
if keep_libraries.lower() == 'n':
    # uninstall autopep8 using pip
    subprocess.run(['pip', 'uninstall', '-y', 'autopep8'])
