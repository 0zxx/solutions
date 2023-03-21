import solc
import os
import shutil

# define a list of required packages
required_packages = ['solc','autopep8']

# check if the required packages are installed
for package in required_packages:
    try:
        importlib.import_module(package)
    except ImportError:
        # install the missing package using pip
        import subprocess
        subprocess.run(['pip', 'install', package])

def get_path_to_file():
    # Ask the user for the file name or path
    input_str = input("Enter the name or path of the Solidity file: ")
    
    # Check if the input string is a path or a file name
    if os.path.exists(input_str):
        # If the input string is a path, use it as is
        path_to_file = input_str
    else:
        # If the input string is a file name, assume it's in the current directory
        path_to_file = os.path.join(os.getcwd(), input_str)
    
    # Check if the file exists
    if not os.path.exists(path_to_file):
        raise ValueError(f"File not found: {path_to_file}")
    
    # Return the path to the file
    return path_to_file

# Set the Solidity versions to use
solidity_versions = ["0.4.0", "0.5.0", "0.6.0", "0.7.0", "0.8.0", "0.8.1", "0.8.2", "0.8.3", "0.8.4"]

# Compile the Solidity code for each version of Solidity
for version in solidity_versions:
    # Set the Solidity compiler options
    compiler_options = {
        "language": "Solidity",
        "sources": {
            path_to_file: {
                "content": open(path_to_file, "r").read()
            }
        },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["*"]
                }
            },
            "optimizer": {
                "enabled": True,
                "runs": 200
            },
            "evmVersion": "istanbul"
        },
        "version": version
    }
    
    # Compile the Solidity code
    compiled_code = solc.compile(compiler_options)
    
    # Format the Solidity code
    formatted_code = compiled_code["contracts"][path_to_file]["Example"]["evm"]["bytecode"]["object"]
    
    # Save the compiled and formatted code to a file
    output_path = f"compiled_{version}.bin"
    with open(output_path, "w") as f:
        f.write(formatted_code)

# prompt the user if they want to keep the installed packages
answer = input("Do you want to keep the installed packages? (y/n) ")
if answer.lower() == 'n':
    # remove the installed packages using pip
    for package in required_packages:
        subprocess.run(['pip', 'uninstall', '-y', package])
