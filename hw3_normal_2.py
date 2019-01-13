def bubbleSort(lst):
	for j in range (len(lst) -1):
		for i in range (len(lst)-1):
			if lst[i]>lst[i+1]:
				lst[i], lst[i+1] = lst[i+1], lst[i]
	return lst





import random
N = int(input("Введите количество элементов в списке - "))
lst = [random.randint(-100, 100) for i in range(N)]
print ("Исходный список " , lst)

print ("Отсортированный список " , bubbleSort(lst))