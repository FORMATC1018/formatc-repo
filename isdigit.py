
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
print (a, type(a))
print (b, type(b))
print (c, type(c))