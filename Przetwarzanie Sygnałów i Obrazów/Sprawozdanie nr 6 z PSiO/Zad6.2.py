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

N = 64
#a = [0.5, 0.9, 0.1]
a = [1,1,1]
b = [0.1, 0.2, 0.3]
x = np.zeros(20)
x[1] = 1
y = filter(x,a,b)
w, h = signal.freqz(y,1)

plt.figure(figsize=(10,4),tight_layout=1)

plt.subplot(1,2,1)
plt.plot(w,abs(h))
plt.title("Charakterystyka amplitudowa filtru")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.grid(True,which='both')
plt.axvline(x=0,color='k')
plt.axvline(x=3.15,color='grey',linestyle='--')
plt.axhline(y=0,color='k')

f = (w*N)

plt.subplot(1,2,2)
plt.plot(f, np.degrees(np.unwrap(np.angle(h))))
plt.title("Charakterystyka fazowa filtru")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Faza")
plt.grid(True,which='both')
plt.axvline(x=0,color='k')
plt.axvline(x=201,color='grey',linestyle='--')
plt.axhline(y=0,color='k')

plt.show()

z, p, k = signal.tf2zpk(b, a)
s = np.linspace(0, 2*np.pi, 64)

plt.plot(np.cos(s), np.sin(s))
plt.scatter(np.real(z), np.imag(z), marker="x")
plt.scatter(np.real(p), np.imag(p), marker="o")
plt.title("Okrąg jednostkowy")
plt.xlabel('Część rzeczywista')
plt.ylabel('Część urojona')
plt.grid(True,which='both')
plt.axvline(x=0,color='k')
plt.axhline(y=0,color='k')

plt.show()