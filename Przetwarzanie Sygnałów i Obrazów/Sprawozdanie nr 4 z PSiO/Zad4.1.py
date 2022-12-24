import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp as chirp
from scipy.io import wavfile

def fun(x,a):
    d1 = len(x)
    F = (1-a)*x**2
    for i in range (1,d1):
        F[i] = a*F[i-1]+F[i]
    return F

def code(a,skala):

    plt.figure(figsize=(8,6),tight_layout=1)

    plt.subplot(4,2,1)
    plt.title('Szum gaussa')
    plt.xlabel('Czas[s]')
    plt.ylabel('Amplituda')
    plt.grid(True,which='both')
    plt.axhline(y=0,color='k')
    plt.axvline(x=0,color='k')
    plt.xlim(0,5000)
    plt.ylim(-5,5)
    plt.xticks([0,1000,2000,3000,4000,5000],[r'0',r'1',r'2',r'3',r'4',r'5'])
    plt.plot(x,y)

    plt.subplot(4,2,2)
    plt.title('Szum Gaussowski - Obwiednia mocy, a='+str(a))
    plt.xlabel('Czas[s]')
    plt.ylabel('Moc')
    plt.grid(True,which='both')
    plt.axhline(y=0,color='k')
    plt.axvline(x=0,color='k')
    plt.xlim(0,5000)
    plt.ylim(0,skala)
    plt.xticks([0,1000,2000,3000,4000,5000],[r'0',r'1',r'2',r'3',r'4',r'5'])
    plt.plot(x,fun(y,a))

    plt.subplot(4,2,3)
    plt.title('Sygnał sinusoidalny o stałej cześtotliwosci')
    plt.xlabel('Czas[s]')
    plt.ylabel('Amplituda')
    plt.grid(True,which='both')
    plt.axhline(y=0,color='k')
    plt.axvline(x=0,color='k')
    plt.plot(t,sin)

    plt.subplot(4,2,4)
    plt.title('Sygnał sinusoidalny - Obwiednia mocy, a='+str(a))
    plt.xlabel('Czas[s]')
    plt.ylabel('Moc')
    plt.grid(True,which='both')
    plt.axhline(y=0,color='k')
    plt.axvline(x=0,color='k')
    plt.ylim(0,1)
    plt.plot(t,fun(sin,a))

    plt.subplot(4,2,5)
    ch = chirp(t,0,c,f)
    plt.title('Sygnał o zmiennej częstotliwości')
    plt.xlabel('Czas[s]')
    plt.ylabel('Amplituda')
    plt.grid(True,which='both')
    plt.axhline(y=0,color='k')
    plt.axvline(x=0,color='k')
    plt.plot(t,ch)

    plt.subplot(4,2,6)
    plt.title('Sygnał o zmiennej częstotliwości - Obwiednia mocy, a='+str(a))
    plt.xlabel('Czas[s]')
    plt.ylabel('Moc')
    plt.grid(True,which='both')
    plt.axhline(y=0,color='k')
    plt.axvline(x=0,color='k')
    plt.ylim(0,1)
    plt.plot(t,fun(ch,a))

    plt.subplot(4,2,7)
    plt.title('Sygnał mowy')
    plt.xlabel('Czas[s]')
    plt.ylabel('Moc')
    plt.grid(True,which='both')
    plt.axhline(y=0,color='k')
    plt.axvline(x=0,color='k')
    plt.xticks([0,8000,16000,24000,32000,40000],[0,1,2,3,4,5])
    plt.xlim(0,40000)
    plt.plot(mowa)

    plt.subplot(4,2,8)
    plt.title('Sygnał mowy - Obwiednia mocy, a='+str(a))
    plt.xlabel('Czas[s]')
    plt.ylabel('Moc')
    plt.grid(True,which='both')
    plt.axhline(y=0,color='k')
    plt.axvline(x=0,color='k')
    plt.xticks([0,8000,16000,24000,32000,40000],[0,1,2,3,4,5])
    plt.xlim(0,40000)
    plt.plot(fun(mowa,a))

    plt.show()

c = 5
fs = 8000
f = 1000
t = np.linspace(0,c,fs)
sin= np.sin(2*np.pi*f*t)
x = np.arange(0,fs,1)
y = np.random.normal(0,1,fs)
rate,sound = wavfile.read('sound.wav')
mowa = sound/(rate*np.pi)

code(0.999,2)

code(0.99,2)

code(0.001,20)