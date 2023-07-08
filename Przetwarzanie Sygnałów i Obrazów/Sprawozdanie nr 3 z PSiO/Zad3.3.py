import numpy as np
import matplotlib.pyplot as plt

# zadanie 1

n = 32
x = np.arange(n)
y = np.sin(2*np.pi*x/n)
yfft = np.fft.fft(y)
yifft = np.fft.ifft(yfft)

plt.figure(figsize=(8, 6), tight_layout=1)

plt.subplot(3, 2, 1)
plt.title('Re(y)')
plt.xlabel('Numer próbki')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.real(y), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(3, 2, 2)
plt.title('Im(y)')
plt.xlabel('Numer próbki')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.ylim(-1, 0.1)
plt.stem(np.imag(y), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(3, 2, 3)
plt.title('abs(fft(y))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.abs(yfft), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(3, 2, 4)
plt.title('angle(fft(y))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Faza [pi x rad]')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.angle(yfft)/np.pi, use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(3, 2, 5)
plt.title('Re(ifft(y))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.ylim(-1.1, 1.1)
plt.stem(np.real(yifft), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(3, 2, 6)
plt.title('Im(ifft(y))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.ylim(-1, 1)
plt.stem(np.imag(yifft), use_line_collection=1)
plt.grid(True, which='both')

plt.show()

# zadanie 2

y1 = np.cos(2*np.pi*x/n+(np.pi/4))
y2 = 0.5*np.cos(4*np.pi*x/n)
y3 = 0.25*np.cos(8*np.pi*x/n+(np.pi/2))
y4 = y1+y2+y3

f4 = 2*np.fft.fft(y4)/n

if4 = 2*np.fft.ifft(f4)/n

plt.figure(figsize=(8, 6), tight_layout=1)

plt.subplot(3, 2, 1)
plt.title('Re(y4)')
plt.xlabel('Numer próbki')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.real(y4), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(3, 2, 2)
plt.title('Im(y4)')
plt.xlabel('Numer próbki')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.ylim(-1, 1)
plt.stem(np.imag(y4), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(3, 2, 3)
plt.title('Moduł Widma')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.abs(f4), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(3, 2, 4)
plt.title('Faza Widma')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Faza [pi x rad]')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.angle(f4)/np.pi, use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(3, 2, 5)
plt.title('Re(ifft(y4))')
plt.xlabel('Numer próbki')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.stem(np.real(if4), use_line_collection=1)
plt.grid(True, which='both')

plt.subplot(3, 2, 6)
plt.title('Im(ifft(y4))')
plt.xlabel('Numer próbki')
plt.ylabel('Amplituda')
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.ylim(-0.1, 1)
plt.stem(np.imag(if4), use_line_collection=1)
plt.grid(True, which='both')

plt.show()
