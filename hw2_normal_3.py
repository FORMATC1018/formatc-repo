#coding: utf-8
import random
N = int(input("Введите количество элементов в списке - "))
lst = [random.randint(-100, 100) for i in range(N)]
print(lst)