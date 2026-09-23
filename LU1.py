import numpy as np


# a = np.array([[1, 2, -2, 6, 24], [-3, -5, 14, 13, 41], [1, 2, -2, -2, 0], [-2, -4, 5, 10, 20]])
# a = np.array([[2, 7., -8., 6., -39.], [4. , 4., 0., -7., 41.], [-1., -3., 6., 3., 4.], [9., -7., -2., -8., 113.]])
# a = np.array([[9, -5., -6., 3., -8.], [1. , -7., 1., 0., 38.], [3., -4., 9., 0., 47.], [6., -1., 9., 8., -8.]])
# a = np.array([[-1, -7., -3., -2., -12.], [-8. , 1., -9., 0., -60.], [8., 2., -5., -3., -91.], [-5., 3., 5., -9., -43.]])
a = np.array([[10, 1, 1], [2, 10, 1], [2, 2, 10]])

a1 = a.copy()
n = a.shape[0]
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
# print(np.dot())