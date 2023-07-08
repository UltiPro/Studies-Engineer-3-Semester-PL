import numpy as np  # Biblioteka numpy jako np
import matplotlib.pyplot as plt  # Biblioteka matplotlib od python plot jako plt
from scipy import signal as si  # Biblioteka scipy importowanie signala jako si

# Tworzy tablice o 40 wartościach z domyślnie wpisanymi zerami
x = np.zeros(40)
x[0] = 1  # Dla pierwzej wartości w tablicy przypisanie jedynki
x[39] = 1  # Dla ostatniej wartośći w tablicy przypisanie jedynki

# Rysuje linie pod punktami (w tym przypadku widoczne dla ostatniej wartości)
plt.stem(x)
plt.axhline(y=0, color="k")  # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0, color="k")  # Zaznacznie lini x=0 kolorem czarnym
plt.grid(True, which='both')  # Włączenie siatki
# Tytuł wykresu
plt.title('Impuls jednostkowy oraz impuls przesunięty (40 próbek)')
plt.xlabel("Numer próbki")  # Podpis osi x
plt.ylabel("Wartość próbki")  # Podpis osi y
plt.show()  # Wywołanie wykresu
