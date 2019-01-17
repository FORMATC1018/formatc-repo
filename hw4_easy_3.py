import random
#Заполняем список случайными числами
N = int(input("Введите количество элементов в списке - "))
lst = [random.randint(-100, 100) for i in range(N)]
#Выводим исходный список
print("Исходный список - ", lst)
#Генерируем новый список и выводим его
res_lst = [x for x in lst if x>0 and x%3==0 and x%4!=0]
print("Новый список - ", res_lst)