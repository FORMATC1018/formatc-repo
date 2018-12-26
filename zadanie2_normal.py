while True:
	i=0
	number_1 = input("Введите 1 число - ")
	number_2 = input("Введите 2 число - ")  
	if number_1[0]=="-" or number_1.isdigit ():
		float(number_1)
		number_1=int(number_1)
		i+=1
	
	if number_2[0]=="-" or number_2.isdigit ():
		float(number_2)
		number_2=int(number_2)
		i+=1
	
	if i==2: break
	else: continue

print("Number_1 = ", number_1)
print ("Number_2 = ", number_2)
number_1 = number_1 + number_2
number_2 = number_1 - number_2
number_1 = number_1 - number_2
print("Number_1 = ", number_1)
print ("Number_2 = ", number_2)

# Еще способ
# number_1, number_2 = number_2, number_1

# Еще способ
# bufer = number_1
# number_1 = number_2
# number_2 = bufer
