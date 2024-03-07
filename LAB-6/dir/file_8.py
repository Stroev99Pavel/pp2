import os
print(os.getcwd())
#C:\Users\Ba99er\PycharmProjects\pythonProject1\LAB-6\dir
path = "..\dir\pain.txt"
if os.access("pain.txt", os.F_OK):
    print("exists")
    os.remove(path)
