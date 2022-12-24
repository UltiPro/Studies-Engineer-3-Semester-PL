import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as siw
import scipy.signal as ss
import soundfile as sf
import utility as u

fs, a = siw.read('Universal Linear Accelerator.wav')
fs, h1 = siw.read('BathRoom.wav')
fs, h2 = siw.read('Living Room.wav')

plt.figure(figsize=(8,6),tight_layout=1)

plt.subplot(3,1,1)
plt.plot(a)
plt.title('Muzyka Techno w komorze bezechowej')
plt.ylabel('Amplituda')
plt.xlabel('Ilość Próbek')
plt.axhline(y=0,color = "k",)
plt.axvline(x=0,color = "k")
plt.grid(True,which='both')
plt.xlim(0,1400000)
plt.ylim(-25000,25000)

plt.subplot(3,1,2)
plt.plot(h1)
plt.title('Akustyczna odpowiedź impulsowa w łazience')
plt.ylabel('Amplituda')
plt.xlabel('Ilość Próbek')
plt.axhline(y=0,color = "k",)
plt.axvline(x=0,color = "k")
plt.grid(True,which='both')
plt.xlim(0,15000)
plt.ylim(-15000,15000)

plt.subplot(3,1,3)
plt.plot(h2)
plt.title('Akustyczna odpowiedź impulsowa w salonie')
plt.ylabel('Amplituda')
plt.xlabel('Ilość Próbek')
plt.axhline(y=0,color = "k",)
plt.axvline(x=0,color = "k")
plt.grid(True,which='both')
plt.xlim(0,15000)
plt.ylim(-15000,15000)

plt.show()

a = u.pcm2float(a,'float32')
h1 = u.pcm2float(h1,'float32')
h2 = u.pcm2float(h2,'float32')

y1 = ss.convolve(a,h1)
y2 = ss.convolve(a,h2)

plt.figure(figsize=(8,6),tight_layout=1)

plt.subplot(3,1,1)
plt.plot(a)
plt.title('Muzyka Techno w komorze bezechowej')
plt.ylabel('Amplituda')
plt.xlabel('Ilość Próbek')
plt.axhline(y=0,color = "k",)
plt.axvline(x=0,color = "k")
plt.grid(True,which='both')
plt.xlim(0,1400000)

plt.subplot(3,1,2)
plt.plot(y1)
plt.title('Muzyka Techno w komorze bezechowej + Akustyczna odpowiedź impulsowa w łazience')
plt.ylabel('Amplituda')
plt.xlabel('Ilość Próbek')
plt.axhline(y=0,color = "k",)
plt.axvline(x=0,color = "k")
plt.grid(True,which='both')
plt.xlim(0,1400000)

plt.subplot(3,1,3)
plt.plot(y2)
plt.title('Muzyka Techno w komorze bezechowej + Akustyczna odpowiedź impulsowa w salonie')
plt.ylabel('Amplituda')
plt.xlabel('Ilość Próbek')
plt.axhline(y=0,color = "k",)
plt.axvline(x=0,color = "k")
plt.grid(True,which='both')
plt.xlim(0,1400000)

plt.show()

sf.write("jeden.wav",y1,fs)
sf.write("dwa.wav",y2,fs)