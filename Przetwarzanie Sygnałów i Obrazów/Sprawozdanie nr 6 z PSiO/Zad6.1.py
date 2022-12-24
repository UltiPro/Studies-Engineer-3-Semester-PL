from matplotlib import pyplot as plt
import numpy as np
from scipy import signal

def filter(x, a, b):
    y = []
    for i in range(0, len(x)):
        if(i == 0):
            val = b[0]*x[i]
            y.append(val)
        elif(i == 1):
            val = b[0]*x[i]+b[1]*x[i-1]-a[1]*y[i-1]
            y.append(val)
        else:
            val = b[0]*x[i]+b[1]*x[i-1]*b[2]*x[i-2]-a[1]*y[i-1]-a[2]*y[i-2]
            y.append(val)
    return y

a = [0.9, 0.25, 0.9]
b = [0.5, 0.9, 0.3]
x = np.zeros(20)
x[1] = 1
y = filter(x, a, b)

plt.figure(figsize=(10,4),tight_layout=1)

plt.subplot(1,2,1)
plt.stem(y)
plt.title("Własna implementacja filtru")
plt.xlabel('Numer próbki')
plt.ylabel('Amplituda')
plt.grid(True,which='both')
plt.axvline(x=0,color='k')
plt.axhline(y=0,color='k')

y = signal.lfilter(b,a,x)

plt.subplot(1,2,2)
plt.stem(y)
plt.title("Funkcja scipy.signal.lfilter")
plt.xlabel('Numer próbki')
plt.ylabel('Amplituda')
plt.grid(True,which='both')
plt.axvline(x=0,color='k')
plt.axhline(y=0,color='k')

plt.show()
