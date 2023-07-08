import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp as chirp
from scipy.signal import spectrogram as spectrogram
from scipy.io import wavfile

f = 1000
fs = 24000
c = 5
t = np.linspace(0, c, fs)
sin = 2*np.sin(2*np.pi*f*t)
f, t, Sxx = spectrogram(sin, fs, 'hamming', 256)
Sxx = 20*np.log10(Sxx)
rate, sound = wavfile.read('sound.wav')

plt.figure(figsize=(8, 6), tight_layout=1)

plt.subplot(2, 2, 1)
plt.title('Sygnał sinusoidalny o stałej częstotliwości')
plt.ylabel('Częstotliwość [kHz]')
plt.xlabel('Czas [s]')
plt.pcolormesh(t, f/3000, Sxx)
bar = plt.colorbar()
plt.xticks([0.2, 0.4, 0.6, 0.8], [1, 2, 3, 4])
bar.ax.set_ylabel('Moc/Częstotliwosć [dB/Hz]')

plt.subplot(2, 2, 2)

y = np.random.normal(0, 1.2, fs)
x = np.arange(0, fs, 1)
f, t, Sxx = spectrogram(y, fs, 'hamming', 256)
Sxx = 20*np.log10(Sxx)

plt.title('Sygnał szumu')
plt.ylabel('Częstotliwość [kHz]')
plt.xlabel('Czas [s]')
plt.pcolormesh(t, f/3000, Sxx)
bar = plt.colorbar()
plt.xticks([0.2, 0.4, 0.6, 0.8], [1, 2, 3, 4])
bar.ax.set_ylabel('Moc/Częstotliwosć [dB/Hz]')

plt.subplot(2, 2, 3)

f = 1000
t = np.linspace(0, c, fs)
ch = chirp(t, 0, c, f)
f, t, Sxx = spectrogram(ch, fs, 'hamming', 256)
Sxx = 20*np.log10(Sxx)

plt.title('Sygnał o zmiennej częstotliwości')
plt.ylabel('Częstotliwość [kHz]')
plt.xlabel('Czas [s]')
plt.pcolormesh(t, f/3000, Sxx)
bar = plt.colorbar()
plt.xticks([0.2, 0.4, 0.6, 0.8], [1, 2, 3, 4])
bar.ax.set_ylabel('Moc/Częstotliwosć [dB/Hz]')

plt.subplot(2, 2, 4)

f = 1000
t = np.linspace(0, c, fs)
f, t, Sxx = spectrogram(sound/(rate*np.pi), fs, 'hamming', 256)
Sxx = 20*np.log10(Sxx)

plt.title('Sygnał mowy')
plt.ylabel('Częstotliwość [kHz]')
plt.xlabel('Czas [s]')
plt.pcolormesh(t, f/3000, Sxx)
bar = plt.colorbar()
plt.xticks([0.2, 0.4, 0.6, 0.8], [1, 2, 3, 4])
bar.ax.set_ylabel('Moc/Częstotliwosć [dB/Hz]')

plt.show()
