import autopep8

# Path of File
nome_arquivo = input("Insira o nome do arquivo ou caminho completo do arquivo: ")

# Opening file and learning content
with open(nome_arquivo, 'r') as arquivo:
    codigo = arquivo.read()

# fix the code opening the lib of autopep8
codigo_corrigido = autopep8.fix_code(codigo)

# rewrite the code with the fixed code
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(codigo_corrigido)

print(f"O arquivo {nome_arquivo} foi corrigido com sucesso.")
