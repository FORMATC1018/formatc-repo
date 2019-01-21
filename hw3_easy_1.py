def my_round(number, ndigits): 
	number = number*(10**ndigits)+0.41 
	number = number//1 
	return number/(10**ndigits) 
print(my_round(0.6, 0)) 