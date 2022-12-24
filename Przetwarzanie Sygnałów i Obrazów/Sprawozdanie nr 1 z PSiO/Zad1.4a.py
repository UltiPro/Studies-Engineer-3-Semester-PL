import numpy as np  # Biblioteka numpy jako np
import matplotlib.pyplot as plt # Biblioteka matplotlib od python plot jako plt

x = np.linspace(0, 0.005, 1000) # Określenie dziedziny <0,2π>, 1000 pomiarów w tym zakresie 
y = 2 * np.cos(2*np.pi*1000*x) # Wzór funkcji

plt.plot(x,y,'c') # Rysowanie w zakresie zmiennej x funkcji y, 'c' oznacza linie ciągłą koloru cyjankowego
plt.axhline(y=0,color = "k") # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0,color = "k") # Zaznacznie lini x=0 kolorem czarnym
plt.axvline(x=0.005,color = "grey",linestyle = "--") # Zaznaczeni lini x=0.005 kolorem szarym linią przerywaną
plt.grid(True,which='both') # Włączenie siatki
plt.title("Wykres sygnału cosinusoidalnego o amplitudzie 2V i częstotliwości 1kHz") # Tytuł wykresu 
plt.xlabel("Czas [s]") # Podpis osi x
plt.ylabel("Napięcie [V]") # Podpis osi y
plt.show() # Wywołanie wykresu
