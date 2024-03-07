import os
path = "..\dir\Strawhats.txt"
if os.access(path, os.F_OK): #existence
    print("exists")
    name = os.path.basename(path)
    print(name)
    current_directory = os.getcwd()
    print(current_directory)