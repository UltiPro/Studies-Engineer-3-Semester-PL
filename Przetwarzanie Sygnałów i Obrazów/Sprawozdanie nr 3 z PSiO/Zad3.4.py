import numpy as np
import matplotlib.pyplot as plt

n = 32
x = np.arange(n)
y = np.exp(1j*(2*np.pi*1/n*x+np.pi/2))
z = 2*np.fft.fft(y)/n 

plt.figure(figsize=(8,6),tight_layout=1)

plt.subplot(3,2,1)
plt.title('Re(y)')
plt.xlabel('Numer próbki')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(np.real(y),use_line_collection=1)
plt.grid(True,which='both')

plt.subplot(3,2,2)
plt.title('Im(y)')
plt.xlabel('Numer próbki')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(np.imag(y),use_line_collection=1)
plt.grid(True,which='both')

plt.subplot(3,2,3)
plt.title('Re(fft(y))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.ylim(-1,1)
plt.stem(np.real(z),use_line_collection=1)
plt.grid(True,which='both')

plt.subplot(3,2,4)
plt.title('Im(fft(y))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(np.imag(z),use_line_collection=1)
plt.grid(True,which='both')

plt.subplot(3,2,5)
plt.title('Moduł(fft(y))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(np.abs(z),use_line_collection=1)
plt.grid(True,which='both')

plt.subplot(3,2,6)
plt.title('Phase(fft(y))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Faza [pi x rad]')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.stem(np.angle(z)/np.pi,use_line_collection=1)
plt.grid(True,which='both')

plt.show()