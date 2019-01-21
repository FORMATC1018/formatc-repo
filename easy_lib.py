import os
import shutil
import sys

def gotoDir ():
	user_ans = input("Введите имя директории ")
	full_name = os.path.join(os.getcwd(), user_ans)
	try:
		os.chdir(full_name)
		print("Успешный переход ")
	except:
		print (user_ans, " - такой директории нет")

def listDir():
	main_path = os.getcwd()
	for i in os.listdir(main_path):
		print(i)

def remFile():
    user_ans = input("Введите имя директории ")
    full_name = os.path.join(os.getcwd(), user_ans)
    try:
        os.rmdir(full_name)
        print("Успешное удаление ")
    except:
        print(user_ans + ' - такой директории нет')

def makeDir():
    user_ans = input("Введите имя директории ")
    full_name = os.path.join(os.getcwd(), user_ans)
    try:
    	os.mkdir(full_name)
    	print("Успешное создание ")
    except:
        print(dir_path + ' - такая директория уже есть')