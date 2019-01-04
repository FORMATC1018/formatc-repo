while True:
	i=0
	number = input("Введите число - ")
	if number[0]=="-" or number.isdigit ():
		float(number)
		number=int(number)
		i+=1
	if i==1: break
	else: continue
max_digit = 0
if number<0:
	number = number * (-1)
while number != 0:
	digit = number % 10
	number //= 10
	if digit>max_digit:
		max_digit = digit
print ("Максимальная цифра числа - ", max_digit)