import random
n=8
x = [random.randint(0,8) for _ in range(n)]
y = [random.randint(0,8) for _ in range(n)]
print (x)
print (y)
correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
if correct:
	print("NO")
else:
	print("YES")