import numpy as np  # Biblioteka numpy jako np
import matplotlib.pyplot as plt # Biblioteka matplotlib od python plot jako plt
import soundfile as sf # Biblioteka soundfile jak sf

A = 1 # Amplituda
F = 10000 # Częstotliwość
Fs = 44100 # Częstotliwość próbkowania
Ts = 1/Fs # Częstotliwość próbkowania w sekundach
O = 2*np.pi*F # Omega
Phi = 0 # Przesunięcie fazowe
x = np.arange(0,0.001,Ts) # Określenie dziedziny <0,0.001>, Ts pomiarów w tym zakresie 
y = A * np.sin(O*x + Phi) # Wzór funkcji y

plt.plot(x,y) # Rysowanie w zakresie zmiennej x funkcji y
plt.axhline(y=0,color = "k") # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0,color = "k") # Zaznacznie lini x=0 kolorem czarnym
plt.grid(True,which='both') # Włączenie siatki
plt.title('Amplituda = 0') # Tytuł wykresu 
plt.xlabel("Czas [s]") # Podpis osi x
plt.ylabel("Amplituda") # Podpis osi y
sf.write('wynik.wav',y,Fs) # Eksportowanie do pliku wav funkcji y o próbkowaniu Fs
plt.show() # Wywołanie wykresu