import numpy as np

f = open('data1.2.1.txt')
n = 0
adata = [0]
bdata = []
for line in f:
    temp = list(map(float, line.split()))
    last = temp[-1]
    bdata.append(last)
    if n == 0:
        temp = temp[n : n + 2]
    else:
        temp = temp[n - 1: n + 2]
    adata += temp
    n += 1
adata[-1] = 0
a = np.array(adata)
b = np.array(bdata)
a = a.reshape(n, 3)
b = b.reshape(n, 1)

p = []
q = []
for i in range(n):
    ai = a[i, 0]
    bi = a[i , 1]
    ci = a[i , 2]
    di = b[i , 0]
    if i == 0:
        pi = -ci / bi
        qi = di/ bi
    else:
        pi = -ci / (bi + ai * p[i - 1])
        qi = (di - ai * q[i - 1])/ (bi + ai * p[i - 1])
    p.append(pi)
    q.append(qi)

x = np.zeros(n)
x[n - 1] = q[n - 1]
for i in range(n - 2, -1, -1):
    x[i] = p[i] * x[i + 1] + q[i]
x = x.reshape(n, 1)

print("")
print("All P:")
for i in range(n):
    print(f"P{i}:", round(p[i], 3))
print("")
print("All Q:")
for i in range(n):
    print(f"Q{i}:", round(q[i], 3))
print("")
print("X")
print(x)

