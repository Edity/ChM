import numpy as np
import matplotlib.pyplot as plt


def f(x):
    x1, x2 = x
    return np.array([
        3 * x1 - np.cos(x2),
        3 * x2 - np.exp(x1)
    ])


def J(x):
    x1, x2 = x
    return np.array([
        [3, np.sin(x2)],
        [-np.exp(x1), 3]
    ])


def phi(x):
    x1, x2 = x
    return np.array([
        np.cos(x2) / 3,
        np.exp(x1) / 3
    ])

def dphi(x):
    x1, x2 = x
    return np.array([
        [0, -np.sin(x2) / 3],
        [np.exp(x1) / 3, 0]
    ])


a = np.array([0, 0])
b = np.array([1 / 3, 1])

q = max(np.sum(abs(dphi(a)), axis=1).max(),
        np.sum(abs(dphi(b)), axis=1).max())

eps = float(input("Enter accuracy: "))

x0 = np.array([0.30, 0.45])


x = x0.copy()
xdata1 = []
edata1 = []

for i in range(10000):
    xnew = phi(x)

    e = max(abs(xnew[0] - x[0]),
            abs(xnew[1] - x[1]))

    values = f(xnew)
    residual = max(abs(values[0]), abs(values[1]))

    xdata1.append(xnew.copy())
    edata1.append(e)

    x = xnew

    error = q / (1 - q) * e
    if error < eps:
        break

print("\nSimple iteration method")

for i in range(len(xdata1)):
    print(f"Iteration {i + 1}: x1 = {xdata1[i][0]:.10f}, "
          f"x2 = {xdata1[i][1]:.10f}")

print("Root:", x)
print("Iterations:", len(xdata1))
print("Residual:", max(abs(f(x)[0]), abs(f(x)[1])))



x = x0.copy()
xdata2 = []
edata2 = []

for i in range(10000):
    values = f(x)
    matrix = J(x)

    delta = np.linalg.solve(matrix, -values)
    xnew = x + delta

    e = max(abs(xnew[0] - x[0]),
            abs(xnew[1] - x[1]))

    values_new = f(xnew)

    xdata2.append(xnew.copy())
    edata2.append(e)

    x = xnew

    if e < eps:
        break

print("\nNewton method")

for i in range(len(xdata2)):
    print(f"Iteration {i + 1}: x1 = {xdata2[i][0]:.10f}, "
          f"x2 = {xdata2[i][1]:.10f}")

print("Root:", x)
print("Iterations:", len(xdata2))
print("Residual:", max(abs(f(x)[0]), abs(f(x)[1])))



x1graph = np.linspace(0, 1 / 3, 500)

y1graph = np.arccos(3 * x1graph)
y2graph = np.exp(x1graph) / 3

plt.plot(x1graph, y1graph, label="x2 = arccos(3*x1)")
plt.plot(x1graph, y2graph, label="x2 = exp(x1)/3")

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Graphical solution of the system")
plt.grid()
plt.legend()
plt.show()



plt.semilogy(range(1, len(edata1) + 1),
             edata1, marker="o", label="Simple iteration")

plt.semilogy(range(1, len(edata2) + 1),
             edata2, marker="s", label="Newton method")

plt.xlabel("Iterations")
plt.ylabel("Difference between approximations")
plt.title("Error depending on iteration count")
plt.legend()
plt.grid()
plt.show()
