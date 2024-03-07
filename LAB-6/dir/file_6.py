import os
path = './dirx/'
for i in range(ord('A'),ord('Z')+1):
    with open(path + f"{chr(i)}.txt",'w') as file:
        file.write("ggs")