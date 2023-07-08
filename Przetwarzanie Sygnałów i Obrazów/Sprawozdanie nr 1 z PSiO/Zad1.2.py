import numpy as np  # Biblioteka numpy jako np
import matplotlib.pyplot as plt  # Biblioteka matplotlib od python plot jako plt

# Określenie dziedziny <0,2π>, 10.000 pomiarów w tym zakresie
x = np.linspace(0, 2 * np.pi, 10000)
y1 = np.sin(x)  # Wzór funkcji y1
y2 = np.cos(x)  # Wzór funkcji y2

# Rysowanie w zakresie zmiennej x funkcji y1, 'c' oznacza linie ciągłą koloru cyjankowego
plt.plot(x, y1, 'c')
# Rysowanie w zakresie zmiennej x funkcji y2, 'b' oznacza linie ciągłą koloru niebieskiego
plt.plot(x, y2, 'b')
# Stworzenie legendy i ustalenie jej lokalizacji na wykresie
plt.legend(['sin(x)', 'cos(x)'], bbox_to_anchor=(0.5, 1))
plt.axhline(y=0, color="k")  # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0, color="k")  # Zaznacznie lini x=0 kolorem czarnym
plt.grid(True, which='both')  # Włączenie siatki
# Tytuł wykresu
plt.title("Wykres funkcji sin(x) oraz cos(x), w dziedzinie od 0 do 2π.")
plt.xlabel("x")  # Podpis osi x
plt.ylabel("y")  # Podpis osi y
plt.show()  # Wywołanie wykresu
