import os
path = "..\dir\Strawhats.txt"
if os.access(path, os.F_OK): #existence
    print("exists")
if os.access(path, os.R_OK): #readable
    print("readable")
if os.access(path, os.W_OK): #writable
    print("writable")
if os.access(path, os.X_OK): #executable
    print("executable")