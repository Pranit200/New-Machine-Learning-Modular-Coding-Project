import os ,sys
from pathlib import Path
import logging

while True:
    project_name = input("Enter your project name: ")
    if project_name != "":
        break

list_of_files =[
     f"{project_name}/__init__.py",
     f"{project_name}/components/__init__.py",
     f"{project_name}/config/__init__.py",
     f"{project_name}/constants/__init__.py",
     f"{project_name}/entity/__init__.py",
     f"{project_name}/exception/__init__.py",
     f"{project_name}/logger/__init__.py",
     f"{project_name}/pipeline/__init__.py",
     f"{project_name}/utils/__init__.py",
     f"config/config.yaml",
     "schema.yaml",
     "app.py",
     "main.py",
     "logs.py",
     "exception.py",
     "setup.py"
]

for filepth in list_of_files:
    filepath = Path(filepth)
    filedir, filename = os.path.split(filepath)
# we define multiple files in list_of_files variable,now we want to split each file independently 
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
# check dir in above code we create file dir and skip it if file dir exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        logging.info("file is already present at : {filepath}")
# in above code we check if filepath not exists or filepath is not available then we open folder an generate list of the files