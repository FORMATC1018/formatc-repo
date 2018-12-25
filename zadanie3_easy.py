while True:
	age = input("Введите пожалуйста Ваш возраст - ")
	if age.isdigit ():
		age=int(age)
		if age>=18:
			print ("Доступ разрешен")
		else:
			print("Извините, пользование данным ресурсом только с 18 лет")
		break
	else:
		print ("Вы ввели не число")
		continue