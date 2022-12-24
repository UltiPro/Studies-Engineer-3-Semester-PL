import numpy as np  # Biblioteka numpy jako np
import matplotlib.pyplot as plt # Biblioteka matplotlib od python plot jako plt
import soundfile as sf # Biblioteka soundfile jak sf
import wave as w # Biblioteka wave jak w

SNR = 3 # Współczynnik sygnał-szum z treści zadania

sound = w.open("Razdwatrzy.wav") # Otwarcie pliku audio w zmiennej
frames_frequency = sound.getframerate()*2 # Wyliczanie częstotliwości klatek
record = np.frombuffer(sound.readframes(-1),dtype="int16")/2000 # Wczytanie dźwięku do zmiennej z zmiennej z plikiem audio
x = np.arange(0, record.size/frames_frequency, 1/frames_frequency) # Stworzenie zakresu o długości <0;record.size/frames_frequency>
noise = np.random.normal(0,1,record.size) # Stworzenie randomowego szumu do połączenia z audio

plt.plot(x,noise) # Rysowanie w zakresie zmiennej x funkcji noise
plt.axhline(y=0,color = "k") # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0,color = "k") # Zaznacznie lini x=0 kolorem czarnym
plt.grid(True,which='both') # Włączenie siatki
plt.title('Szum') # Tytuł wykresu 
plt.xlabel("Czas [s]") # Podpis osi x
plt.ylabel("Amplituda") # Podpis osi y
plt.show() # Wywołanie wykresu

sf.write('Razdwatrzy - szum.wav',noise,frames_frequency) # Eksportowanie do pliku wav funkcji noise o próbkowaniu frames_frequency
record = record + noise/(5 * SNR)

plt.plot(x,record) # Rysowanie w zakresie zmiennej x funkcji record
plt.axhline(y=0,color = "k") # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0,color = "k") # Zaznacznie lini x=0 kolorem czarnym
plt.grid(True,which='both') # Włączenie siatki
plt.title('Nagranie "Razdwatrzy" + Szum') # Tytuł wykresu 
plt.xlabel("Czas [s]") # Podpis osi x
plt.ylabel("Amplituda") # Podpis osi y
plt.show() # Wywołanie wykresu

sf.write('Razdwatrzy - nagranie+szum.wav',record,frames_frequency) # Eksportowanie do pliku wav funkcji noise o próbkowaniu 
# frames_frequency