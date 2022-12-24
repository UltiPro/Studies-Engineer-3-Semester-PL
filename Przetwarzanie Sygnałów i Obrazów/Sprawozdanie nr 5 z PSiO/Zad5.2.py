import numpy as np
import matplotlib.pyplot as plt

def show():
    plt.figure(figsize=(8,6),tight_layout=1)

    plt.subplot(3,3,1)
    plt.plot(x,y1)
    plt.title('y1')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=63,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-1,1.1,0.5))
    plt.xlim(0,80)

    plt.subplot(3,3,2)
    plt.plot(np.convolve(y1,h))
    plt.title('Splot Liniowy y1*h')
    plt.yticks(np.arange(-1,1.1,0.5))
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=126,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.xlim(0,150)

    plt.subplot(3,3,3)
    plt.plot(np.convolve(h,y1))
    plt.title('Splot Liniowy h*y1')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=126,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-1,1.1,0.5))
    plt.xlim(0,150)

    plt.subplot(3,3,4)
    plt.plot(x,y2)
    plt.title('y2')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=63,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-1,1.1,0.5))
    plt.xlim(0,80)

    plt.subplot(3,3,5)
    plt.plot(np.convolve(y2,h))
    plt.title('Splot Liniowy y2*h')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=126,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-1,1.1,0.5))
    plt.xlim(0,150)

    plt.subplot(3,3,6)
    plt.plot(np.convolve(h,y2))
    plt.title('Splot Liniowy h*y2')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=126,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-1,1.1,0.5))
    plt.xlim(0,150)

    plt.subplot(3,3,7)
    plt.stem(h,use_line_collection='true')
    plt.title('h')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=63,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-1,1.1,0.5))
    plt.xlim(-1,80)

    plt.subplot(3,3,8)
    plt.plot(np.convolve(y1,y2))
    plt.title('Splot Liniowy y1*y2')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=126,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-10,10.1,5))
    plt.xlim(0,150)

    plt.subplot(3,3,9)
    plt.plot(np.convolve(y2,y1))
    plt.title('Splot Liniowy y2*y1')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=126,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-10,10.1,5))
    plt.xlim(0,150)

    plt.show()

def show2():
    plt.figure(figsize=(8,6),tight_layout=1)

    plt.subplot(3,2,1)
    plt.plot(x,y1)
    plt.title('y1')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=63,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-1,1.1,0.5))
    plt.xlim(0,80)

    plt.subplot(3,2,2)
    plt.plot(np.convolve(y1+y2,h))
    plt.title('Splot sumy (y1+y2)*h')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=126,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-2,2.1,1))
    plt.xlim(0,150)

    plt.subplot(3,2,3)
    plt.plot(x,y2)
    plt.title('x2')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=63,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-1,1.1,0.5))
    plt.xlim(0,80)

    plt.subplot(3,2,4)
    plt.plot(np.convolve(y1,h)+np.convolve(y2,h))
    plt.title('Splot sumy x1*h + x2*h')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=126,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-2,2.1,1))
    plt.xlim(0,150)

    plt.subplot(3,2,5)
    plt.stem(h,use_line_collection='true')
    plt.title('h')
    plt.xlabel('Numer próbki')
    plt.ylabel('Amplituda')
    plt.axhline(y=0,color = "grey",linestyle='--')
    plt.axvline(x=0,color = "grey",linestyle='--')
    plt.axvline(x=63,color = "grey",linestyle='--')
    plt.grid(True,which='both')
    plt.yticks(np.arange(-1,1.1,0.5))
    plt.xlim(0,80)

    plt.show()

N = 64
k = 0
x = np.arange(N)
y1 = np.sin(2*np.pi*x/N)
y2 = np.sin(4*np.pi*x/N)
h = np.zeros(N)/N
h[k] = 1

show()

show2()

h[k] = 0
k=16
h[k] = 1

show()

show2()

h[k] = 0
k=32
h[k] = 1

show()

show2()
