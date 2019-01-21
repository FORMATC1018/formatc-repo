import easy_lib

do ='a'
while do != '0':
    print("")
    print("Что сделать в текущей директории?")
    print("Перейти в папку - выбрать 1")
    print("Просмотреть содержимое текущей папки - выбрать 2")
    print("Удалить папку - выбрать 3")
    print("Создать папку - выбрать 4")
    print("Для выхода - выбрать 0")
    print("")
    do = input('Выбрать: ' )
    print("")
    

    if do=="1":
	    easy_lib.gotoDir ()
    elif do=="2":
	    easy_lib.listDir ()
    elif do=="3":
	    easy_lib.remFile ()
    elif do=="4":
	    easy_lib.makeDir ()
    elif do=="0":
	    pass
    else:
    	print("Такого пункта меню нет")