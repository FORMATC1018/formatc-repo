def fibonacci(n, m):
    a, b = 1, 1
    f_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        f_list.append(a)

    return f_list[n - 1:m]





n = int(input("Введите n - "))
m = int(input("Введите m - "))
print('fibonacci(n, m): ', fibonacci(n, m))