import numpy as np  # Biblioteka numpy jako np
import matplotlib.pyplot as plt # Biblioteka matplotlib od python plot jako plt

x=np.linspace(-10,10,1000) # Określenie dziedziny <-10,10>, 1.000 pomiarów w tym zakresie
y=pow(x,2)+5 # wzór funkcji

plt.plot(x,y,'c') # Rysowanie w zakresie zmiennej x funkcji y, 'c' oznacza linie ciągłą koloru cyjankowego
plt.axhline(y=0,color = "k") # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0,color = "k") # Zaznacznie lini x=0 kolorem czarnym
plt.grid(True,which='both') # Włączenie siatki
plt.title("Wykres funkcji y = x^2 + 5") # Tytuł wykresu
plt.xlabel("x") # Podpis osi x
plt.ylabel("y") # Podpis osi y
plt.show() # Wywołanie wykresu
