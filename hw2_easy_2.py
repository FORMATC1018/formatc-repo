#coding: utf-8
lst = [1,2,3,4,5,6,7,8,9]
lst_2 = [2,3,4]

for i in lst_2:
	if i in lst:
		lst.remove(i)
print(lst)