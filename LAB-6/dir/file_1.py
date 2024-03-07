import os
path = "/..dir/"
dirs_list = os.listdir()
for path in dirs_list:
    if os.path.isfile(path):
        print(os.path.basename(path))
    if os.path.isdir(path):
        print(os.path.dirname(path))

