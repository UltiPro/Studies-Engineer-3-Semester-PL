from matplotlib import pyplot as plt
import numpy as np


def filter(x, a, b):
    y = []
    for i in range(0, len(x)):
        if (i == 0):
            val = b[0]*x[i]
            y.append(val)
        elif (i == 1):
            val = b[0]*x[i]+b[1]*x[i-1]-a[1]*y[i-1]
            y.append(val)
        else:
            val = b[0]*x[i]+b[1]*x[i-1]*b[2]*x[i-2]-a[1]*y[i-1]-a[2]*y[i-2]
            y.append(val)
    return y


a = [1, 0.25, 0.9]
b = [0.5, 0.9, 0.3]
x = np.random.normal(0, 1, 512)
gauss = np.log10(np.abs(np.fft.rfft(x)))
fil = np.log10(np.abs(np.fft.rfft(filter(x, a, b))))

plt.figure(figsize=(10, 4), tight_layout=1)

plt.subplot(2, 1, 1)
plt.plot(gauss)
plt.title("Gauss")
plt.xlabel("Numer próbki")
plt.ylabel("Amplituda")
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axvline(x=256, color='grey', linestyle='--')
plt.axhline(y=0, color='k')


plt.subplot(2, 1, 2)
plt.plot(fil)
plt.title("Przefiltrowany")
plt.xlabel("Numer próbki")
plt.ylabel("Amplituda")
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axvline(x=256, color='grey', linestyle='--')
plt.axhline(y=0, color='k')

plt.show()
