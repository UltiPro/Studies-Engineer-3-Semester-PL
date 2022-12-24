import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

n = 32
x = np.arange(n)
y = np.sin(((5*np.pi)+0.5)*x/n)

plt.title('Funkcja y')
plt.xlabel('Numer próbki')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(y,use_line_collection=1)
plt.grid(True,which='both')

plt.show()

plt.xlabel('Numer próbki')
plt.ylabel('Waga')
plt.plot(np.bartlett(n))
plt.plot(np.blackman(n))
plt.plot(np.hamming(n))
plt.plot(sig.hann(n))
plt.plot(np.kaiser(n,1))
plt.plot(np.kaiser(n,0))
plt.legend(["bartlett","blackman","hamming","hann","kaiser","rectwin"],loc="upper right")
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.grid(True,which='both')

plt.show()

plt.figure(figsize=(8,6),tight_layout=1)

z = np.fft.fft(y)
plt.subplot(2,2,1)
plt.title('Moduł FFT - Brak wykresu')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(abs(z),use_line_collection=1)

z1 = np.bartlett(n)*y
z12 = 2*np.fft.fft(z1)/n
plt.subplot(2,2,2)
plt.title('Moduł FFT - Bartlett')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(abs(z12),use_line_collection=1)

z2 = sig.hann(n)*y
z22 = 2*np.fft.fft(z2)/n
plt.subplot(2,2,3)
plt.title('Moduł FFT - Hann')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(abs(z22),use_line_collection=1)

z3 = np.hamming(n)*y
z32 = 2*np.fft.fft(z3)/n
plt.subplot(2,2,4)
plt.title('Moduł FFT - Hamming')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(abs(z32),use_line_collection=1)

plt.show()

plt.figure(figsize=(8,6),tight_layout=1)

z4 = np.kaiser(n,1)*y
z42 = 2*np.fft.fft(z4)/n
plt.subplot(2,2,1)
plt.title('Moduł FFT - Kaiser')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(abs(z42),use_line_collection=1)

z5 = np.kaiser(n,0)*y
z52 = 2*np.fft.fft(z5)/n
plt.subplot(2,2,2)
plt.title('Moduł FFT - Rectwin')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(abs(z52),use_line_collection=1)

z6 = np.blackman(n)*y
z62 = 2*np.fft.fft(z6)/n
plt.subplot(2,2,3)
plt.title('Moduł FFT - Rectwin')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(abs(z62),use_line_collection=1)

plt.show()