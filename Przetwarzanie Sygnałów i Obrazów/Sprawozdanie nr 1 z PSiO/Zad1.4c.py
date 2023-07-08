import numpy as np  # Biblioteka numpy jako np
import matplotlib.pyplot as plt  # Biblioteka matplotlib od python plot jako plt
from scipy import signal as si  # Biblioteka scipy importowanie signala jako si

# Określenie dziedziny <0,2π>, 1000 pomiarów w tym zakresie
x = np.linspace(0, 0.005, 1000)
# Wzór funkcji z określeniem sygnały piłokształtnego na trójkątny
y = 2 * si.sawtooth(2*np.pi*1000*x, 0.5)

# Rysowanie w zakresie zmiennej x funkcji y, 'c' oznacza linie ciągłą koloru cyjankowego
plt.plot(x, y, 'c')
plt.axhline(y=0, color="k")  # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0, color="k")  # Zaznacznie lini x=0 kolorem czarnym
# Zaznaczeni lini x=0.005 kolorem szarym linią przerywaną
plt.axvline(x=0.005, color="grey", linestyle="--")
plt.grid(True, which='both')  # Włączenie siatki
# Tytuł wykresu
plt.title("Wykres sygnału trójkątnego o amplitudzie 2V i częstotliwości 1kHz")
plt.xlabel("Czas [s]")  # Podpis osi x
plt.ylabel("Napięcie [V]")  # Podpis osi y
plt.show()  # Wywołanie wykresu
