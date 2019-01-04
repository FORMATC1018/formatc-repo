import math

print("Решаем квадратное уравнение ax^2 + bx + c = 0")
print("Введите коэффициенты a, b, c")
while True:
	i=0
	a = input("Введите коэффициент a - ")
	b = input("Введите коэффициент b - ")
	c = input("Введите коэффициент c - ")  
	if a[0]=="-" or a.isdigit ():
		float(a)
		a=int(a)
		i+=1
	
	if b[0]=="-" or b.isdigit ():
		float(b)
		b=int(b)
		i+=1
	if c[0]=="-" or c.isdigit ():
		float(c)
		c=int(c)
		i+=1
	
	if i==3: break
	else: continue	
D = b**2 - 4*a*c
if D>0:
	x1 = (-b + math.sqrt(D))/(2*a)
	x2 = (-b - math.sqrt(D))/(2*a)
	print ("x1 = ", x1)
	print ("x2 = ", x2)
elif D==0:
	print("2 совпадающих корня")
	x = (-b)/(2*a)
	print ("x1 = x2 = ", x)
else:
	print ("Уравнение не имеет корней")