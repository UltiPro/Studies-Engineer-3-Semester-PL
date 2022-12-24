import numpy as np  # Biblioteka numpy jako np
import matplotlib.pyplot as plt # Biblioteka matplotlib od python plot jako plt
from scipy import signal as si # Biblioteka scipy importowanie signala jako si

x = np.linspace(0,5*2*np.pi,200) # Określenie dziedziny <0,10π>, 200 pomiarów w tym zakresie 
y = np.random.normal(0,np.sqrt(0.5),size = (200)) # Wzór funkcji y

plt.plot(x,y) # Rysowanie w zakresie zmiennej x funkcji y
plt.axhline(y=0,color = "k") # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0,color = "k") # Zaznacznie lini x=0 kolorem czarnym
plt.grid(True,which='both') # Włączenie siatki
plt.title('Szum Gaussowski') # Tytuł wykresu 
plt.xlabel("Numer próbki") # Podpis osi x
plt.ylabel("Wartość próbki") # Podpis osi y
plt.show() # Wywołanie wykresu