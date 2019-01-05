#coding: utf-8
#import random
#lst = [random.randint(-10, 10) for i in range(10)]
new_lst = []
new_lst_2 = []
lst = [1 , 2, 4, 5, 6, 2, 5, 2]
print(lst)
new_lst = list(set(lst))
print (new_lst)
for item in lst:
	count = lst.count(item)
	if count==1:
		new_lst_2.append(item)
print(new_lst_2)