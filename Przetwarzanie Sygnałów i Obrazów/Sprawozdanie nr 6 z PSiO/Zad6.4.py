import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fo = 2000
fp = 8000
fn = fp/2
rzad = 3
fal = 1
b, a = signal.cheby1(rzad, fal, fo/fn, btype='lowpass', analog=False)
w, h = signal.freqz(b, a)
f = fn*np.arange(len(w))/len(w)

plt.figure(figsize=(10, 4), tight_layout=1)

plt.subplot(1, 2, 1)
plt.plot(f, 20 * np.log10(abs(h)))
plt.title('Chebyshev (Typ 1) - Charakterystyka Amplitudowa')
plt.xlabel('Częstotliwośc [Hz]')
plt.ylabel('Amplituda')
plt.margins(0, 0.1)
plt.axvline(fo, color='r', linewidth=0.75)
plt.grid(True, which='both')
plt.axvline(x=0, color='k')


plt.subplot(1, 2, 2)
plt.plot(f, np.degrees(np.angle(h)))
plt.title('Chebyshev (Typ 1) - Charakterystyka Fazowa')
plt.xlabel('Częstotliwośc [Hz]')
plt.ylabel('Faza')
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axvline(x=4000, color='grey', linestyle='--')
plt.axhline(y=0, color='k')

plt.show()
