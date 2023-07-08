import numpy as np  # Biblioteka numpy jako np
import matplotlib.pyplot as plt  # Biblioteka matplotlib od python plot jako plt
import soundfile as sf  # Biblioteka soundfile jak sf
import wave as w  # Biblioteka wave jak w

sound = w.open("Razdwatrzy.wav")  # Otwarcie pliku audio w zmiennej
frames_frequency = sound.getframerate()*2  # Wyliczanie częstotliwości klatek
# Wczytanie dźwięku do zmiennej z zmiennej z plikiem audio
record = np.frombuffer(sound.readframes(-1), dtype="int16")/2000
# Stworzenie zakresu o długości <0;record.size/frames_frequency>
x = np.arange(0, record.size/frames_frequency, 1/frames_frequency)
# z badaniem próbek 1/frames_frequency

plt.plot(x, record)  # Rysowanie w zakresie zmiennej x funkcji record
plt.axhline(y=0, color="k")  # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0, color="k")  # Zaznacznie lini x=0 kolorem czarnym
plt.grid(True, which='both')  # Włączenie siatki
plt.title('Raz Dwa Trzy -> Mówione')  # Tytuł wykresu
plt.xlabel("Czas [s]")  # Podpis osi x
plt.ylabel("Amplituda")  # Podpis osi y
plt.show()  # Wywołanie wykresu

sf.write('Razdwatrzy.wav', record, frames_frequency)
# Eksportowanie do pliku wav funkcji record o próbkowaniu frames_frequency
