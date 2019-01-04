while True:
	i=0
	number = input("Введите число - ")
	if number[0]=="-" or number.isdigit ():
		float(number)
		number=int(number)
		i+=1
	if i==1: break
	else: continue
if number<0:
	number = number * (-1)

while number != 0:
	digit = number % 10
	number = number // 10
	print ("Цифра числа - ", digit)