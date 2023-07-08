import numpy as np  # Biblioteka numpy jako np
import matplotlib.pyplot as plt  # Biblioteka matplotlib od python plot jako plt
from scipy import signal as si  # Biblioteka scipy importowanie signala jako si

# Określenie dziedziny <0,10π>, 200 pomiarów w tym zakresie
x = np.linspace(0, 5*2*np.pi, 200)
y1 = np.sin(x)  # Wzór funkcji y1 (sinusoidalny)
y2 = si.sawtooth(x)  # Wzór funkcji y2 (piłokształtny)
y3 = si.square(x)  # Wzór funkcji y3 (prostokątny)

plt.plot(x, y1)  # Rysowanie w zakresie zmiennej x funkcji y1
plt.plot(x, y2)  # Rysowanie w zakresie zmiennej x funkcji y2
plt.plot(x, y3)  # Rysowanie w zakresie zmiennej x funkcji y3
plt.legend(['sin(x)', 'sawtooth(x)', 'square(x)'],
           bbox_to_anchor=(1, 0.87), loc="center right")
# Stworzenie legendy i ustalenie jej lokalizacji na wykresie
plt.axhline(y=0, color="k")  # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0, color="k")  # Zaznacznie lini x=0 kolorem czarnym
plt.grid(True, which='both')  # Włączenie siatki
# Tytuł wykresu
plt.title('Przebiegi periodyczne sinusoidalny, piłokształtny oraz prostokątny')
plt.xlabel("Kąt[rad]")  # Podpis osi x
plt.ylabel("Amplituda")  # Podpis osi y
plt.show()  # Wywołanie wykresu
