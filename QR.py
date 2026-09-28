import numpy as np

def QR(a, n):
    q = np.eye(n)
    for i in range(n - 1):
        v = np.zeros(n)
        for j in range(n):
            if i < j:
               v[j] = a[j, i]
            elif j == i:
                asum = 0
                for k in range(i, n):
                    asum += (a[k, i]) ** 2
                v[j] = a[j, i] + np.sign(a[j, i]) * (asum ** 0.5)
        v = v.reshape(n, 1)
        hi = np.eye(n) - 2 * ((v @ v.transpose()) / (v.transpose() @ v))
        a = hi @ a
        q = q @ hi
    return q, a


def main():
    f = open("data1.5.txt")
    n = 0
    data = []
    for line in f:
        data += list(map(float, line.split()))
        n += 1
    epsilon = 0.01
    a0 = (np.array(data)).reshape(n, n)
    q0, r0 = QR(a0, n)
    a = a0.copy()
    d = 1
    cmplxh = [0] * n
    while epsilon < d:
        q, r = QR(a, n)
        a = r @ q


        asum = 0
        for m in range(n):
            for l in range(m + 1, n):
                asum += (a[l, m]) ** 2
        d = (asum) ** 0.5
        for i in range(n - 1):
            temp = a[i:i + 2, i:i + 2]
            coeff = [1, -(temp[0, 0] + temp[1, 1]), temp[0, 0] * temp[1, 1] - temp[0, 1] * temp[1, 0]]
            h1, h2 = np.roots(coeff)
            if h1 == np.conj(h2):
                d1 = np.abs(h1 - cmplxh[i])
                if epsilon > d1: d = d1
                cmplxh[i] = h1
  
    cmplxh = [0] * n
    for i in range(n - 1):
        temp = a[i:i + 2, i:i + 2]
        coeff = [1, -(temp[0, 0] + temp[1, 1]), temp[0, 0] * temp[1, 1] - temp[0, 1] * temp[1, 0]]
        h1, h2 = np.roots(coeff)
        if h1 == np.conj(h2):
            cmplxh[i] = h1
            cmplxh[i + 1] = h2

    for i in range(n):
        if cmplxh[i] == 0:
            cmplxh[i] = a[i, i]
        
    print("A matrix:")
    print(a0, '\n')
    print("Q matrix:")
    print(q0, '\n')
    print("R matrix:")
    print(r0, '\n')
    print("Q * R:")
    print(q0 @ r0, '\n')
    print("Eigenvalues:")
    for i in range(n):
        print(f"λ{i + 1} :", cmplxh[i], '\n')

if __name__ == "__main__":
    main()