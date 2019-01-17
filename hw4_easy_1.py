import random
#Заполняем список случайными числами
N = int(input("Введите количество элементов в списке - "))
lst = [random.randint(-10, 10) for i in range(N)]
#Выводим исходный список
print("Исходный список - ", lst)
#Генерируем новый список и выводим его
res_lst = [x**2 for x in lst]
print("Новый список - ", res_lst)