import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import dft as dft


def DFT(y, n):
    m = dft(n)
    return y@m


def IDFT(f, n):
    m = dft(n)
    odw = np.conj(m)/n
    return f@odw

# Porównanie własnej funkcji z funkcją z zadania 3.1


n = 32
x = np.arange(n)
y = np.sin(2*np.pi*x/n)
z = 2*np.fft.fft(y)/n
ydft = 2*DFT(y, n)/n

plt.figure(figsize=(8, 6), tight_layout=1)

plt.title('Re(y)')
plt.xlabel('Numer próbki')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.real(y), use_line_collection=1)
plt.grid(True, which='both')

plt.show()

plt.figure(figsize=(8, 6), tight_layout=1)

plt.subplot(4, 2, 1)
plt.title('Re(z)')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.real(z), use_line_collection=1)
plt.ylim(-1, 1)
plt.grid(True, which='both')

plt.subplot(4, 2, 2)
plt.title('Re(ydft) - funkcja własna')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.ylim(-1, 1)
plt.stem(np.real(ydft), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(4, 2, 3)
plt.title('Im(z)')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.imag(z), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(4, 2, 4)
plt.title('Im(ydft) - funkcja własna')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.imag(ydft), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(4, 2, 5)
plt.title('abs(z)')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.abs(z), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(4, 2, 6)
plt.title('abs(ydft) - funkcja własna')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.abs(ydft)/np.pi, use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(4, 2, 7)
plt.title('angle(z)')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Faza [pi x rad]')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.angle(z)/np.pi, use_line_collection=1)

plt.subplot(4, 2, 8)
plt.title('angle(ydft) - funkcja własna')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Faza [pi x rad]')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.angle(ydft)/np.pi, use_line_collection=1)

plt.show()

# Porównanie własnej funkcji z funkcją z zadania 3.2

y1 = np.cos(2*np.pi*x/n+(np.pi/4))
y2 = 0.5*np.cos(4*np.pi*x/n)
y3 = 0.25*np.cos(8*np.pi*x/n+(np.pi/2))
y4 = y1 + y2 + y3
f4 = 2*np.fft.fft(y4)/n
ydft = 2*DFT(y4, n)/n

plt.figure(figsize=(8, 6), tight_layout=1)

plt.title('y4 = y1+y2+y3')
plt.xlabel('Numer próbki')
plt.ylabel('Wartość')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(y4, use_line_collection=1)
plt.grid(True, which='both')

plt.show()

plt.figure(figsize=(8, 6), tight_layout=1)

plt.subplot(4, 2, 1)
plt.title('Re(f4)')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.real(f4), use_line_collection=1)
plt.ylim(-1, 1)
plt.grid(True, which='both')

plt.subplot(4, 2, 2)
plt.title('Re(ydft) - funkcja własna')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.ylim(-1, 1)
plt.stem(np.real(ydft), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(4, 2, 3)
plt.title('Im(f4)')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.imag(f4), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(4, 2, 4)
plt.title('Im(ydft) - funkcja własna')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.imag(ydft), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(4, 2, 5)
plt.title('abs(f4)')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.abs(f4), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(4, 2, 6)
plt.title('abs(ydft) - funkcja własna')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.abs(ydft)/np.pi, use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(4, 2, 7)
plt.title('angle(z)')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Faza [pi x rad]')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.angle(f4)/np.pi, use_line_collection=1)

plt.subplot(4, 2, 8)
plt.title('angle(ydft) - funkcja własna')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Faza [pi x rad]')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.angle(ydft)/np.pi, use_line_collection=1)

plt.show()
