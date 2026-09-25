import numpy as np

f = open('data1.1.txt')
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
epsilon = 3

a1 = a.copy()
b1 = b.copy()
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
        pmatrix = wmatrix @ pmatrix
        a = wmatrix @ a
        flag = False

    mmatrix = np.eye(n)
    rmatrix = np.eye(n)
    for j in range (i + 1, n):
        m = a[j, i]/a[i,i]
        mmatrix[j, i] = -m
        rmatrix[j, i] = m
    if flag:
        lmatrix = lmatrix @ rmatrix
    else:
        lmatrix = (wmatrix @ lmatrix) @ (wmatrix @ rmatrix)
    a = mmatrix @ a
umatrix = a

deta = 1
for i in range(n):
    deta *= umatrix[i, i] * lmatrix[i, i]

b = pmatrix @ b
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

ematrix = np.eye(n)
y = [0] * n
for io in range(n):
    e = ematrix[io,0:n].reshape(n, 1)
    y1 = np.zeros(n)
    y1[0] = e[0, 0]
    for i in range(1, n):
        sigma = 0
        for j in range(0, i):
            sigma += lmatrix[i, j] * y1[j]
        y1[i] = e[i, 0] - sigma
    y[io] = y1
rx = [0] * n

for io in range(n):
    y2 = y[io]
    x1 = np.zeros(n)
    x1[n - 1] = y2[n - 1] / umatrix[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sigma = 0
        for j in range(i + 1, n):
            sigma += umatrix[i, j] * x1[j]
        x1[i] = (y2[i] - sigma) / umatrix[i, i]   
    rx[io] = x1
    
areverse = np.vstack(rx).transpose()
    


print("L matrix:")
print(np.round(lmatrix, epsilon), '\n')
print("U matrix:")
print(np.round(umatrix, epsilon), '\n')
print("LU matrix:")
print(np.round(lmatrix @ umatrix, epsilon), '\n')
print("X:")
print(np.round(x.reshape(n, 1), epsilon), '\n')
print("reverse A:")
print(np.round(areverse, epsilon), '\n')
print("det A:")
print(deta, '\n')
print("A * reverse A:")
print(np.round((pmatrix @ a1 @ areverse), epsilon), '\n')
print("LU matrix:")
print(np.round(lmatrix @ umatrix, epsilon), '\n')
print("PA matrix:")
print(np.round(pmatrix @ a1, epsilon), '\n')
