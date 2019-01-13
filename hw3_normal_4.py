def is_parallelogram(a1, a2, a3, a4):
    if abs(int(a3[0]) - int(a2[0])) == abs(int(a4[0]) - int(a1[0])) and \
       abs(int(a2[1]) - int(a1[1])) == abs(int(a3[1]) - int(a4[1])):
        return True
    return False

a1 = input("Введите координаты точки A1 через ; - ")
a1 = a1.split(";")
a2 = input("Введите координаты точки A2 через ; - ")
a2 = a2.split(";")
a3 = input("Введите координаты точки A3 через ; - ")
a3 = a3.split(";")
a4 = input("Введите координаты точки A4 через ; - ")
a4 = a4.split(";")

answer = is_parallelogram(a1, a2, a3, a4)

if answer:
	print("Точки являются вершинами параллелограмма")
else:
	print("Точки не являются вершинами параллелограмма")