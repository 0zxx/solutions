import autopep8
import subprocess

# prompt the user for the script file path
script_path = input("Enter the path to the Python script: ")

# install necessary packages
subprocess.run(['pip', 'install', 'autopep8', 'flake8'])

# use autopep8 to format the script
fixed_script = autopep8.fix_file(script_path)

# write the fixed script to a new file
with open('fixed_script.py', 'w') as f:
    f.write(fixed_script)

# use flake8 to identify issues in the fixed script
output = subprocess.run(['flake8', 'fixed_script.py'], capture_output=True, text=True)

# print the output of flake8
print(output.stdout)

# ask the user whether to keep or remove the installed packages
response = input("Do you want to keep or remove the installed packages? (keep/remove): ")
if response == "remove":
    subprocess.run(['pip', 'uninstall', '-y', 'autopep8', 'flake8'])
