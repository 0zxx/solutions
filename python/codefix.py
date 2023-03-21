import importlib
import subprocess

def fix_code(file_name):
    # check if autopep8 is installed
    try:
        importlib.import_module('autopep8')
    except ImportError:
        # install autopep8 using pip
        subprocess.run(['pip', 'install', 'autopep8'])

    import autopep8

    # Opening file and learning content
    with open(file_name, 'r') as file:
        code = file.read()

    # fix the code using the autopep8 library
    fixed_code = autopep8.fix_code(code)

    # rewrite the code with the fixed code
    with open(f"{file_name.split('.')[0]}_fix.py", 'w') as file:
        file.write(fixed_code)

    print(f"O arquivo {file_name} foi corrigido com sucesso e salvo como {file_name.split('.')[0]}_fix.py")

    # prompt the user to choose whether to keep the libraries installed at the beginning
    keep_libraries = input("Deseja manter as bibliotecas instaladas no início? (s/n): ")
    if keep_libraries.lower() == 'n':
        # uninstall autopep8 using pip
        subprocess.run(['pip', 'uninstall', '-y', 'autopep8'])
