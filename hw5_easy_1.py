import os
import shutil
import sys

path_dir = [('dir_' + str(i + 1)) for i in range(9)]


def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' - такая директория уже есть')

def rem_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.rmdir(dir_path)
    except:
        print(dir_path + ' - такой директории нет')


user_answer=input("Что сделать с директориями Dir1 - Dir9 (1 - создать/0 - удалить ) ")
if user_answer == "1":
    for i in path_dir:
        make_dir(i)
else:
    for i in path_dir:
        rem_dir(i)