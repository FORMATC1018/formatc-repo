#coding: utf-8
date = input("Введите дату через точку ")
date_list=date.split(".")
dict_months = {
'01': 'января',
'02': 'февраля',
'03': 'марта',
'04': 'апреля',
'05': 'мая',
'06': 'июня',
'07': 'июля',
'08': 'августа',
'09': 'сентября',
'10': 'октября',
'11': 'ноября',
'12': 'декабря',
}
dict_days = {
'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое',
'06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
'11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое',
'16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
'21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвёртое',
'25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
'29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое',
}

for key in dict_days:
	if date_list[0] == key:
		date_list[0] = dict_days[key]

for key in dict_months:
	if date_list[1] == key:
		date_list[1] = dict_months[key]

answer_date = date_list[0] + ' ' + date_list[1] + ' ' + date_list[2] + ' ' "года"
print(answer_date)