import os

#print(os.listdir()) # вывод всех файлов
#os.mkdir("") # создать папку dir
dirs_list = os.listdir()
for dir in dirs_list:
    print(dir) # вывод названия файла
    print(os.path.isfile(dir)) # проверка на файл
    print(os.path.isdir(dir)) # проверка на папку
    print("______")
path_to_folder = "/"
print(os.listdir(path_to_folder))

#file = open("Strawhats.txt","r")
#r - reading w - writing a - appending x - create a file

file = open("Strawhats.txt","r")
print(file.readline())
file.close()
file = open("Strawhats.txt","r")
print(file.readlines())
file.close()
file = open("Strawhats.txt","r")
print(file.read())
file.close()

with open("Strawhats.txt", "r") as file:
    print(file.read())

#os.remove(file)
#os.rmdir(folder)

#Проверка доступа
#os.access(filename, os.F_OK) existence
#os.access(filename, os.R_OK) readable
#os.access(filename, os.W_OK) writable
#os.access(filename, os.X_OK) executable
#current_dir = os.getcwd() в какой директории мы / путь
# os.mkdir(current_dir + "\dir2" / создание папки dir2
