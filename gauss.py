import numpy as np
#оставил по приколу, че зря писал что-ли

#     /\/\/\/\/\
#    \/\/\/\/\/\/\ 
# <\/\/\/\/\/\/\/\/\>
#   ( |<U>   ___| )        < - Гаусс
#     \     >   /
#      \   V   /
#       ﹋|﹋|﹋ 

# a = np.array([[1, 2, -2, 6, 24], [-3, -5, 14, 13, 41], [1, 2, -2, -2, 0], [-2, -4, 5, 10, 20]])
# a = np.array([[2, 7., -8., 6., -39.], [4. , 4., 0., -7., 41.], [-1., -3., 6., 3., 4.], [9., -7., -2., -8., 113.]])
# a = np.array([[9, -5., -6., 3., -8.], [1. , -7., 1., 0., 38.], [3., -4., 9., 0., 47.], [6., -1., 9., 8., -8.]])


a = np.array([[-1, -7., -3., -2., -12.], [-8. , 1., -9., 0., -60.], [8., 2., -5., -3., -91.], [-5., 3., 5., -9., -43.]])
n = 4
print(a)
print(" ")
for i in range(n):
    # выбор опорного элемента
    if a[i, i] == 0:
        for j in range(i + 1, n):
            if a[j, i] != 0:
                m1 = np.array(a[:j - 1])
                m2 = np.array(a[j - 1:j])
                m3 = np.array(a[j:])
                a = np.concatenate((m1, m3, m2))
                break
    anew = np.array(a[:i + 1])
    # прямой ход
    mainrow = a[i:i + 1]
    for j in range (i + 1, n):
        victimrow = a[j:j + 1] + (-(a[j, i]/a[i,i]) * mainrow)
        anew = np.concatenate((anew, victimrow))
    a = anew
print(" ")
print(a)
# обратный ход
ans = np.zeros(n)
for i in range(n - 1, -1, -1):
    d = 1.
    for j in range(n + 1):
        if j == i:
            d = a[i, j]
        elif j != n:
            ans[i] -= (a[i, j] * ans[j])
        else:
            ans[i] += a[i,j]
    ans[i] /= d
print(" ")
print(ans)
