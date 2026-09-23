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
print(a, b)