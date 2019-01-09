#coding: utf-8
import random
lst = [random.randint(-10, 10) for i in range(10)]
new_lst = []
print(lst)
for i in range (10):
	if lst[i] % 2 ==0:
		new_lst.append(lst[i]/float(4))
	else:
		new_lst.append(lst[i]*float(2))
print (new_lst)