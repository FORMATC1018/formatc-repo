while True:
	number = input("Введите число - ")
	if number.isdigit ():
		number=int(number)
		break
	else:
		continue

while number != 0:
	digit = number % 10
	number = number // 10
	print ("Цифра числа - ", digit)