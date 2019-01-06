#coding: utf-8
equation = 'y = -12x + 11111140.2121'
print ("F(x) - ", equation)
list =equation.split(" ")
list_kx=list[2]
k=float(list_kx[:-1])
x = float(input("Введите значение х - "))
y=k*x+float(list[-1])
print("y = ", y)