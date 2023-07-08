import numpy as np  # Biblioteka numpy jako np
import matplotlib.pyplot as plt  # Biblioteka matplotlib od python plot jako plt

A = 1  # Amplituda
F = 1000  # Częstotliwość
Fs = 8000  # Częstotliwość próbkowania
Ts = 1/Fs  # Częstotliwość próbkowania w sekundach
O = 2*np.pi*F  # Omega
Phi = 0  # Przesunięcie fazowe
# Określenie dziedziny <0,0.0051>, Ts pomiarów w tym zakresie
x = np.arange(0, 0.0051, Ts)
y = A * np.sin(O*x + Phi)  # Wzór funkcji y

plt.plot(x, y)  # Rysowanie w zakresie zmiennej x funkcji y
plt.axhline(y=0, color="k")  # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0, color="k")  # Zaznacznie lini x=0 kolorem czarnym
# Zaznaczeni lini x=0.005 kolorem szarym linią przerywaną
plt.axvline(x=0.005, color="grey", linestyle="--")
plt.grid(True, which='both')  # Włączenie siatki
# Włączenie lini punktów wykresu
plt.stem(x, y, '-', use_line_collection="true")
plt.title('Fs = 8000 Hz | F = 1000 Hz')  # Tytuł wykresu
plt.xlabel("Czas [s]")  # Podpis osi x
plt.ylabel("Amplituda")  # Podpis osi y
plt.show()  # Wywołanie wykresu
