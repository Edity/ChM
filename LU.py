import numpy as np

f = open('data.txt')
n = 0
data = []
for line in f:
    data += list(map(float, line.split()))
    n += 1
a = np.array(data)
a = a.reshape(n, n + 1)
b = a.copy()
a = a[:, :n]
b = b[:, n:]

a1 = a.copy()
umatrix = np.eye(n)
lmatrix = np.eye(n)
pmatrix = np.eye(n)
for i in range(n):
    flag = True
    maxa = [a[i,i], i]
    for j in range(i + 1, n):
        if a[j, i] > maxa[0]: 
            maxa = [float(a[j, i]), j]
    if i != maxa[1]:
        wmatrix = np.eye(n)
        wmatrix[maxa[1], i] = wmatrix[i, maxa[1]] = 1
        wmatrix[maxa[1], maxa[1]] = wmatrix[i, i] = 0
        pmatrix = np.dot(wmatrix, pmatrix)
        a = np.dot(wmatrix, a)
        flag = False

    mmatrix = np.eye(n)
    rmatrix = np.eye(n)
    for j in range (i + 1, n):
        m = a[j, i]/a[i,i]
        mmatrix[j, i] = -m
        rmatrix[j, i] = m
    if flag:
        lmatrix = np.dot(lmatrix, rmatrix)
    else:
        lmatrix = np.dot(np.dot(wmatrix, lmatrix), np.dot(wmatrix, rmatrix))
    a = np.dot(mmatrix, a)
umatrix = a

deta = 1
for i in range(n):
    deta *= umatrix[i, i] * lmatrix[i, i]

z = np.zeros(n)
z[0] = b[0, 0]
for i in range(1, n):
    sigma = 0
    for j in range(0, i):
        sigma += lmatrix[i, j] * z[j]
    z[i] = b[i, 0] - sigma 

x = np.zeros(n)
x[n - 1] = z[n - 1] / umatrix[n - 1, n - 1]
for i in range(n - 2, -1, -1):
    sigma = 0
    for j in range(i + 1, n):
        sigma += umatrix[i, j] * x[j]
    x[i] = (z[i] - sigma) / umatrix[i, i]



print("L matrix:")
print(lmatrix, '\n')
print("U matrix:")
print(umatrix, '\n')
print("LU matrix:")
print(np.dot(lmatrix, umatrix), '\n')
print("det A:")
print(deta, '\n')
print("PA matrix:")
print(np.dot(pmatrix, a1), '\n')
print("X:")
print(x, '\n')
