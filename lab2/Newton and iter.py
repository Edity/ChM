import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 4 ** x - 5 * x - 2

def df(x):
    return np.log(4) * 4 ** x - 5

def phi(x):
    return np.log(5 * x + 2) / np.log(4)

def dphi(x):
    return 5 / (np.log(4) * (5 * x + 2))


eps = float(input("Enter accuracy: "))
x0 = 2.0
a = 1.5
b = 2.0

q = max(abs(dphi(a)), abs(dphi(b)))
print("q:", q)
print("q / (1 - q):", q / (1 - q))
x = x0
xdata1 = []
edata1 = []
fdata1 = []

for i in range(10000):
    xnew = phi(x)
    e = abs(xnew - x)
    error = q / (1 - q) * e

    xdata1.append(xnew)
    edata1.append(error)
    fdata1.append(abs(f(xnew)))

    x = xnew

    if error < eps:
        break

print("")
print("Simple iteration method")
for i in range(len(xdata1)):
    print(f"X{i + 1}:", xdata1[i])
print("Root:", x)
print("Iterations:", len(xdata1))
print("Error:", abs(f(x)))


x = x0
xdata2 = []
edata2 = []
fdata2 = []

for i in range(10000):
    xnew = x - f(x) / df(x)
    e = abs(xnew - x)
    xdata2.append(xnew)
    edata2.append(e)
    fdata2.append(abs(f(xnew)))
    x = xnew
    if e < eps:
        break

print("")
print("Newton method")
for i in range(len(xdata2)):
    print(f"X{i + 1}:", xdata2[i])
print("Root:", x)
print("Iterations:", len(xdata2))
print("Error:", abs(f(x)))


xgraph = np.linspace(0, 3, 300)
ygraph = f(xgraph)
plt.plot(xgraph, ygraph)
plt.axhline(0, color="black")
plt.axvline(x0, color="gray", linestyle="--")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("4^x - 5x - 2 = 0")
plt.grid()
plt.show()


plt.semilogy(range(1, len(edata1) + 1), edata1, label="Simple iteration")
plt.semilogy(range(1, len(edata2) + 1), edata2, label="Newton method")
plt.xlabel("Iterations")
plt.ylabel("Difference between approximations")
plt.title("Error depending on iteration count")
plt.legend()
plt.grid()
plt.show()
