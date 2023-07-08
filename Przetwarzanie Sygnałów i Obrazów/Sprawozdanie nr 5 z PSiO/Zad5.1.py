import numpy as np
import matplotlib.pyplot as plt


def show(x1):
    plt.figure(figsize=(8, 6), tight_layout=1)

    plt.subplot(2, 2, 1)
    plt.plot(x, y1)
    plt.title('x1[n]')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.axvline(x=0.97, color="grey", linestyle='--')
    plt.grid(True, which='both')
    plt.yticks(np.arange(-1, 5, 1))
    plt.xticks([0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75,
               0.875, 1.0], [0, 4, 8, 12, 16, 20, 24, 28, 32])

    plt.subplot(2, 2, 2)
    plt.plot(x, y2)
    plt.title('x2[n]')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.axvline(x=0.97, color="grey", linestyle='--')
    plt.grid(True, which='both')
    plt.yticks(np.arange(-1, 5, 1))
    plt.xticks([0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75,
               0.875, 1.0], [0, 4, 8, 12, 16, 20, 24, 28, 32])

    plt.subplot(2, 2, 3)
    plt.plot(x1, S1+S2)
    plt.title('S{x1[n]}+S{x2[n]}')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.axvline(x=0.97, color="grey", linestyle='--')
    plt.grid(True, which='both')
    if i != 2:
        plt.yticks(np.arange(0, 5, 1))
    plt.xticks([0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75,
               0.875, 1.0], [0, 4, 8, 12, 16, 20, 24, 28, 32])

    plt.subplot(2, 2, 4)
    if i == 0:
        plt.plot(x1, fun_a(y1+y2))
    if i == 1:
        plt.plot(x1, fun_b(y1+y2))
    if i == 2:
        plt.plot(x1, fun_c(y1+y2))
    plt.title('S{x1[n]}+S{x2[n]}')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.axvline(x=0.97, color="grey", linestyle='--')
    plt.grid(True, which='both')
    if i != 2:
        plt.yticks(np.arange(0, 5, 1))
    plt.xticks([0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75,
               0.875, 1.0], [0, 4, 8, 12, 16, 20, 24, 28, 32])

    plt.show()


def fun_a(f):
    f = [f[i]*2
         for i in range(len(f))]
    return np.array(f)


def fun_b(f):
    f = [f[i]+1
         for i in range(len(f))]
    return np.array(f)


def fun_c(f):
    f = [f[i+1]-f[i]
         for i in range(len(f)-1)]
    return np.array(f)


N = 32
x = np.arange(N)/N
y1 = np.sin(2*np.pi*x)
y2 = np.ones(32)

i = 0

# Podpunkt A

S1 = fun_a(y1)
S2 = fun_a(y2)

show(x)

i += 1

# Podpunkt B

S1 = fun_b(y1)
S2 = fun_b(y2)

show(x)

i += 1

# Podpunkt C

x1 = np.arange(31)/31
S1 = fun_c(y1)
S2 = fun_c(y2)

show(x1)
