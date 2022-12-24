import numpy as np
import matplotlib.pyplot as plt

n = 32
x = np.arange(n)
y1 = np.cos(2*np.pi*x/n+(np.pi/4))
y2 = 0.5*np.cos(4*np.pi*x/n)
y3 = 0.25*np.cos(8*np.pi*x/n+(np.pi/2))

plt.figure(figsize=(8,6))

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3,'y')
plt.grid(True,which='both')
plt.title('Wykres trzech sygnałów cosinusoidalnych')
plt.xlabel('Numer próbki')
plt.ylabel('Wartość')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.axvline(x=n-1,color = "grey",linestyle = "--")
plt.legend(['y1(n) = cos(2π/n + π/4)','y2(n) = 0.5*cos(2π/n + π/4)','y3(n) = 0.25*cos(8π/n + π/4'])

plt.show()

# Podpunkt 2 , obliczenia powtórz dla sygnału y4 = y1 + y2 +y3
y4 = y1 + y2 + y3

plt.figure(figsize=(8,6))
plt.grid(True,which='both')
plt.title('Wykres połączonych sygnałów cosinusoidalnych')
plt.xlabel('Numer próbki')
plt.ylabel('Wartość')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")
plt.axvline(x=n-1,color = "grey",linestyle = "--")
plt.plot(x,y4)
plt.show()

# Podpunkt 1, obliczenia tranformatory Fouriera dla poszczególnych funkcji 
f1 = 2*np.fft.fft(y1)/n
f2 = 2*np.fft.fft(y2)/n
f3 = 2*np.fft.fft(y3)/n
f4 = 2*np.fft.fft(y4)/n

#Część rzeczywista

plt.figure(figsize=(8,6),tight_layout=1)

plt.subplot(2,2,1)
plt.grid(True,which='both')
plt.stem(np.real(f1),use_line_collection=1)
plt.ylim(0,1)
plt.title('Re(fft(y1))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.subplot(2,2,2)
plt.grid(True,which='both')
plt.stem(np.real(f2),use_line_collection=1)
plt.ylim(0,1)
plt.title('Re(fft(y2))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.subplot(2,2,3)
plt.grid(True,which='both')
plt.stem(np.real(f3),use_line_collection=1)
plt.ylim(0,1)
plt.title('Re(fft(y3))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.subplot(2,2,4)
plt.grid(True,which='both')
plt.stem(np.real(f4),use_line_collection=1)
plt.ylim(0,1)
plt.title('Re(fft(y4))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.show()

#Część urojona

plt.figure(figsize=(8,6),tight_layout=1)

plt.subplot(2,2,1)
plt.grid(True,which='both')
plt.stem(np.imag(f1),use_line_collection=1)
plt.title('Im(fft(y1))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.subplot(2,2,2)
plt.grid(True,which='both')
plt.stem(np.imag(f2),use_line_collection=1)
plt.title('Im(fft(y2))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.subplot(2,2,3)
plt.grid(True,which='both')
plt.stem(np.imag(f3),use_line_collection=1)
plt.title('Im(fft(y3))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.subplot(2,2,4)
plt.grid(True,which='both')
plt.stem(np.imag(f4),use_line_collection=1)
plt.title('Im(fft(y4))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Amplituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.show()

# Moduł

plt.figure(figsize=(8,6),tight_layout=1)

plt.subplot(2,2,1)
plt.grid(True,which='both')
plt.stem(np.absolute(f1),use_line_collection=1)
plt.ylim(0,1.5)
plt.title('abs(fft(y1))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.subplot(2,2,2)
plt.grid(True,which='both')
plt.stem(np.absolute(f2),use_line_collection=1)
plt.ylim(0,1.5)
plt.title('abs(fft(y2))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.subplot(2,2,3)
plt.grid(True,which='both')
plt.stem(np.absolute(f3),use_line_collection=1)
plt.ylim(0,1.5)
plt.title('abs(fft(y3))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.subplot(2,2,4)
plt.grid(True,which='both')
plt.stem(np.absolute(f4),use_line_collection=1)
plt.ylim(0,1.5)
plt.title('abs(fft(y4))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Magnituda')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.show()

# Kąt

plt.figure(figsize=(8,6),tight_layout=1)

plt.subplot(2,2,1)
plt.grid(True,which='both')
plt.stem(np.angle(f1)/np.pi,use_line_collection=1)
plt.ylim(-1,1)
plt.title('angle(fft(y1))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Faza [pi x rad]')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.subplot(2,2,2)
plt.grid(True,which='both')
plt.stem(np.angle(f2)/np.pi,use_line_collection=1)
plt.ylim(-1,1)
plt.title('angle(fft(y2))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Faza [pi x rad]')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.subplot(2,2,3)
plt.grid(True,which='both')
plt.stem(np.angle(f3)/np.pi,use_line_collection=1)
plt.ylim(-1,1)
plt.title('angle(fft(y3))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Faza [pi x rad]')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.subplot(2,2,4)
plt.grid(True,which='both')
plt.stem(np.angle(f4)/np.pi,use_line_collection=1)
plt.ylim(-1,1)
plt.title('angle(fft(y4))')
plt.xlabel('Numer pasma częstotliwości')
plt.ylabel('Faza [pi x rad]')
plt.axhline(y=0,color = "k")
plt.axvline(x=0,color = "k")

plt.show()