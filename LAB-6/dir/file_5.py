import os
g = 5
i = 0
with open("5.txt",'w') as file:
    while i < g:
        ins = input()
        file.write(ins + '\n')
        i = i + 1
