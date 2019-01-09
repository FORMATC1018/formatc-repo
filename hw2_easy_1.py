#coding: utf-8
lst = ["яблоко", "киви", "груша", "банан"]
for i in range (len(lst)):
	print(str(i+1) + "." + "{:>10}".format(lst[i]))