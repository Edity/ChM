import numpy as np


from LU import LUmethod, matrixreverse

f = open("data1.3.txt")
n = 0
data = []
for line in f:
    data += list(map(float, line.split()))
    n += 1
a = (np.array(data)).reshape(n, n + 1)
b = a.copy()[:, n:]
a = a[:, :n]
epsilon = 0.01

alpha1 = a.copy()
beta1 = b.copy()
for i in range(n):
    beta1[i] = b[i] / a[i, i]
    for j in range(n):
        if i == j:
            alpha1[i, j] = 0
        else:
            alpha1[i, j] = -a[i, j] / a[i, i]
xi = beta1.copy()
xs = beta1.copy()
alpha2 = alpha1.copy()
beta2 = beta1.copy()

kepsilon1 = 1
itcount1 = 0
while kepsilon1 > epsilon:
    x1 = (alpha1 @ xi) + beta1
    maxvalue = 0
    for i in (x1 - xi):
        digit = i[0]
        if digit < 0: digit *= -1
        if maxvalue < digit:
            maxvalue = digit   
    kepsilon1 = maxvalue
    xi = x1
    itcount1 += 1


kepsilon2 = 1
itcount2 = 0
while kepsilon2 > epsilon:
    bigb = alpha2.copy()
    for i in range(n):
        for j in range(i + 1, n):
            bigb[i, j] = 0
    bigc = alpha2 - bigb
    e = (np.eye(n) - bigb)
    temp = LUmethod(e, b, n)
    re = matrixreverse(temp[1], temp[2], n) @ temp[3].transpose()
    alpha2 = (re @ bigc)
    beta2 = re @ beta2
    x1 =  alpha2 @ xs + beta2

    maxvalue = 0
    for i in (x1 - xs):
        digit = i[0]
        if digit < 0: digit *= -1
        if maxvalue < digit:
            maxvalue = digit
    kepsilon2 = maxvalue
    xs = x1
    itcount2 += 1

print("Epsilon:")
print(epsilon, '\n')
print("Accurate X:")
print(LUmethod(a, b, n)[0].reshape(n, 1), '\n')
print("Simple iteration X:")
print(xi, '\n') 
print("Iteration count:")
print(itcount1, '\n')
print("Seidel method:")
print(xs, '\n') 
print("Iteration count:")
print(itcount2, '\n')

if itcount2 < itcount1:
    print("Seidel method faster")
elif itcount1 < itcount2:
    print("Simple iteration faster")
else:
    print("Both methods equal")

