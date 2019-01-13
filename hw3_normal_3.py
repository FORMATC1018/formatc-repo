def filter_func(function, iterable):
    return (item for item in iterable if function(item))
 
import random
N = int(input("Введите количество элементов в списке - "))
lst = [random.randint(-100, 100) for i in range(N)]
print ("Исходный список " , lst)
print("Отфильтрованный список (четные положительные числа - )", list(filter_func(lambda x: True if x % 2 == 0 and x>0 else False,
                  lst)))