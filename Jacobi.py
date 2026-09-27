import numpy as np

f = open("data1.4.txt")
n = 0
data = []
for line in f:
    data += list(map(float, line.split()))
    n += 1
a = (np.array(data)).reshape(n, n)
la = a.copy()
epsilon = 0.01

t = 1
u = np.eye(n)

count = 0
while t > epsilon and count < 5:
    maxvalue = [0, 0 ,0]
    for i in range(n):
        for j in range(n):
            if i > j:
                digit = la[i, j]
                if digit < 0 : digit *= -1
                if maxvalue[0] < digit:
                    maxvalue[0] = digit
                    maxvalue[1] = i
                    maxvalue[2] = j
    ui = np.eye(n)
    i1 = maxvalue[1]
    j1 = maxvalue[2]
    if la[i1, i1] == la[j1, j1]:
        fi = np.pi / 4
    else:
        temp = (2 * la[i1, j1]) / (la[i1, i1] - la[j1, j1])
        fi = 0.5 * np.arctan(temp)
    ui[i1, j1] = -np.sin(fi)
    ui[j1, i1] = np.sin(fi)
    ui[i1, i1] = ui[j1, j1] = np.cos(fi)
    la = (ui.transpose() @ la) @ ui
    sum = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                sum += la[i, j] ** 2
    u = u @ ui
    t = sum ** 0.5
    count += 1

print("Epsilon:")
print(epsilon, '\n')
print("Eigenvalues:")
for i in range(n):
    print(f"λ{i + 1} :", la[i,i], '\n')
print("Eigenvectors:")
for i in range(n):
    print(f"h{i + 1} :")
    print(u[0:n, i])
print('\n')
print("U matrix:")
print(u, '\n')
print("A * U:")
print(a @ u, '\n')
print("U * L:")
print(u @ la, '\n')