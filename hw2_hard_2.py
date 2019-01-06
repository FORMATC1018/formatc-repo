#coding: utf-8
date = input("Введите дату через точку ")
date_list = date.split(".")
#print(date_list)
convert_date=int(date_list[0])
#print (convert_date)
convert_month=int(date_list[1])
#print(convert_month)
convert_year=int(date_list[2])
#print(convert_year)
long_month = [1, 3, 5, 7, 8, 10, 12]
if len(date_list[0]) != 2 or len(date_list[1]) != 2 or len(date_list[2]) != 4: 
	print("Не корректен формат даты")
elif convert_date > 31 or convert_date < 1:
	print("Не корректен формат даты")
elif convert_month>12 or convert_month<1:
	print("Не корректен формат даты")
elif convert_year>9999 or convert_year<1:
	print("Не корректен формат даты")
elif convert_month not in long_month and convert_date > 30:
	print("Не корректен формат даты")
else:
	print("Дата корректна")