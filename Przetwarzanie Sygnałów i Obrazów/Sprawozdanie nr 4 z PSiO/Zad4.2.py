import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sig
from scipy.signal import chirp as chirp
from scipy.signal import welch as welch
from scipy.signal import spectrogram as spectrogram
from scipy.io import wavfile

N = 1024
fs = 8000
noise = np.random.normal(0, 1, N)
x = np.linspace(0, fs, N)
sinone = 0.5*np.sin(2*np.pi*x*500/fs)
sintwo = np.sin(2*np.pi*x*1200/fs)
sinthree = sinone - sintwo
y = sinthree + noise*0.1
f1, p1 = sig.periodogram(noise, fs)
f2, p2 = sig.periodogram(sinthree, fs)
f3, p3 = sig.periodogram(y, fs)

# a

plt.figure(figsize=(8, 6), tight_layout=1)

plt.subplot(3, 1, 1)
plt.title('Periodiagram - oszacowanie widmowej sęstości mocy')
plt.xlabel('Częstotliwość (x π rad/numer próbki)')
plt.ylabel('Moc/Częstotliowść')
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axvline(x=1.245, color='grey', linestyle='--')
plt.yticks(np.arange(-80, 1, 20))
plt.plot(f1/N/np.pi, np.log(p1/N))

plt.subplot(3, 1, 2)
plt.title('Periodiagram - oszacowanie widmowej sęstości mocy')
plt.xlabel('Częstotliwość (x π rad/numer próbki)')
plt.ylabel('Moc/Częstotliowść')
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axvline(x=1.245, color='grey', linestyle='--')
plt.yticks(np.arange(-80, 1, 20))
plt.plot(f2/N/np.pi, np.log(p2/N))

plt.subplot(3, 1, 3)
plt.title('Periodiagram - oszacowanie widmowej sęstości mocy')
plt.xlabel('Częstotliwość (x π rad/numer próbki)')
plt.ylabel('Moc/Częstotliowść')
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axvline(x=1.245, color='grey', linestyle='--')
plt.yticks(np.arange(-80, 1, 20))
plt.plot(f3/N/np.pi, np.log(p3/N))

plt.show()

# b

plt.figure(figsize=(8, 6), tight_layout=1)

fhann1, phann1 = sig.periodogram(noise, fs, window='hann')
fhann2, phann2 = sig.periodogram(sinthree, fs, window='hann')
fhann3, phann3 = sig.periodogram(y, fs, window='hann')

plt.subplot(3, 1, 1)
plt.title('Periodiagram - oszacowanie widmowej sęstości mocy')
plt.xlabel('Częstotliwość (x π rad/numer próbki)')
plt.ylabel('Moc/Częstotliowść')
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axvline(x=1.245, color='grey', linestyle='--')
plt.yticks(np.arange(-30, -9, 5))
plt.plot(fhann1/N/np.pi, np.log(phann1/N))

plt.subplot(3, 1, 2)
plt.title('Periodiagram - oszacowanie widmowej sęstości mocy')
plt.xlabel('Częstotliwość (x π rad/numer próbki)')
plt.ylabel('Moc/Częstotliowść')
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axvline(x=1.245, color='grey', linestyle='--')
plt.yticks(np.arange(-50, -5, 10))
plt.plot(fhann2/N/np.pi, np.log(phann2/N))

plt.subplot(3, 1, 3)
plt.title('Periodiagram - oszacowanie widmowej sęstości mocy')
plt.xlabel('Częstotliwość (x π rad/numer próbki)')
plt.ylabel('Moc/Częstotliowść')
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axvline(x=1.245, color='grey', linestyle='--')
plt.yticks(np.arange(-35, -5, 5))
plt.plot(fhann3/N/np.pi, np.log(phann3/N))

plt.show()

# c

plt.figure(figsize=(8, 6), tight_layout=1)

welchf1, welchp1 = welch(noise, fs, window='hanning',
                         nperseg=256, noverlap=128)
welchf2, welchp2 = welch(noise, fs, window='hanning', nperseg=128, noverlap=64)
welchf3, welchp3 = welch(noise, fs, window='hanning', nperseg=64, noverlap=32)

plt.subplot(3, 1, 1)
plt.title('Szum gaussowski - Periodiagram Welscha')
plt.xlabel('Częstotliwość')
plt.ylabel('PSD (db/Hz)')
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axvline(x=4000, color='grey', linestyle='--')
plt.plot(welchf1, np.log(welchp1/N), label='NFFT=256')
plt.plot(welchf2, np.log(welchp2/N), label='NFFT=128')
plt.plot(welchf3, np.log(welchp3/N), label='NFFT=64')
plt.legend(loc='upper right')

welchfsin1, welchpsin1 = welch(
    sinthree, fs, window='hanning', nperseg=256, noverlap=128)
welchfsin2, welchpsin2 = welch(
    sinthree, fs, window='hanning', nperseg=128, noverlap=64)
welchfsin3, welchpsin3 = welch(
    sinthree, fs, window='hanning', nperseg=64, noverlap=32)

plt.subplot(3, 1, 2)
plt.title('Szum sinusoidalny - Periodiagram Welscha')
plt.xlabel('Częstotliwość')
plt.ylabel('PSD (db/Hz)')
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axvline(x=4000, color='grey', linestyle='--')
plt.yticks(np.arange(-40, -5, 5))
plt.plot(welchfsin1, np.log(welchpsin1/N), label='NFFT=256')
plt.plot(welchfsin2, np.log(welchpsin2/N), label='NFFT=128')
plt.plot(welchfsin3, np.log(welchpsin3/N), label='NFFT=64')
plt.legend(loc='upper right')

welchfy1, welchpy1 = welch(y, fs, window='hanning', nperseg=256, noverlap=128)
welchfy2, welchpy2 = welch(y, fs, window='hanning', nperseg=128, noverlap=64)
welchfy3, welchpy3 = welch(y, fs, window='hanning', nperseg=64, noverlap=32)

plt.subplot(3, 1, 3)
plt.title('Sygnał w szumie - Periodiagram Welscha')
plt.xlabel('Częstotliwość')
plt.ylabel('PSD (db/Hz)')
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axvline(x=4000, color='grey', linestyle='--')
plt.yticks(np.arange(-25, -5, 2))
plt.plot(welchfy1, np.log(welchpy1/N), label='NFFT=256')
plt.plot(welchfy2, np.log(welchpy2/N), label='NFFT=128')
plt.plot(welchfy3, np.log(welchpy3/N), label='NFFT=64')
plt.legend(loc='upper right')

plt.show()
