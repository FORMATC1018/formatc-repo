#coding: utf-8
import random
import math
lst = [random.randint(-100, 100) for i in range(20)]
new_lst = []
print(lst)
for i in range (20):
	if lst[i]>0 and math.sqrt(lst[i])%1==0:
		new_lst.append(math.sqrt(lst[i]))
print(new_lst)