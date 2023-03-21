import importlib
import subprocess

def fix_python_code(file_path):
    # check if autopep8 is installed
    try:
        importlib.import_module('autopep8')
    except ImportError:
        # install autopep8 using pip
        subprocess.run(['pip', 'install', 'autopep8'])

    import autopep8

    # Opening file and learning content
    with open(file_path, 'r') as f:
        code = f.read()

    # fix the code using the autopep8 library
    fixed_code = autopep8.fix_code(code)

    # write the fixed code to a new file
    output_file_path = file_path.replace(".py", "_fix.py")
    with open(output_file_path, 'w') as f:
        f.write(fixed_code)

    print(f"Fixed code written to {output_file_path}")

    # prompt the user to choose whether to keep the libraries installed at the beginning
    keep_libraries = input("Do you want to keep the libraries installed? (y/n): ")
    if keep_libraries.lower() == 'n':
        # uninstall autopep8 using pip
        subprocess.run(['pip', 'uninstall', '-y', 'autopep8'], check=True)
