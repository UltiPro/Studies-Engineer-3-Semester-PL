from music21 import note, stream # Z biblioteki music21 importujemy note oraz stream

#Tworzenie nut do "wlazł kotek na płotek"
n1 = note.Note('G', quarterLength=1)
n2 = note.Note('E', quarterLength=1)
n3 = note.Note('E', quarterLength=1)
n4 = note.Note('F', quarterLength=1)
n5 = note.Note('D', quarterLength=1)
n6 = note.Note('D', quarterLength=1.1)

n7 = note.Note('C', quarterLength=1)
n8 = note.Note('E', quarterLength=1)
n9 = note.Note('G', quarterLength=1.1)

n10 = note.Note('C', quarterLength=1)
n11 = note.Note('E', quarterLength=1)
n12 = note.Note('G', quarterLength=1.25)

n13 = note.Note('G', quarterLength=1)
n14 = note.Note('E', quarterLength=1)
n15 = note.Note('E', quarterLength=1)
n16 = note.Note('F', quarterLength=1)
n17 = note.Note('D', quarterLength=1)
n18 = note.Note('D', quarterLength=1.1)

n19 = note.Note('C', quarterLength=1)
n20 = note.Note('E', quarterLength=1)
n21 = note.Note('C', quarterLength=1.1)

n22 = note.Note('C', quarterLength=1)
n23 = note.Note('E', quarterLength=1)
n24 = note.Note('C', quarterLength=1.25)

s = stream.Stream() # Rozpoczęcie sklejania nut
s.append([n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24]) 
# Ciąg nut razem sklejony

s.write('midi',fp='kotek') # Zapis do pliku midi

from midi2audio import FluidSynth # Z biblioteki midi2audio improtuje FluidSynth

fs = FluidSynth() # Rozpoczęcie konwertera
fs.midi_to_audio('kotek.midi','my_melody.wav') # Konwertowanie z MIDI do WAV

import numpy as np  # Biblioteka numpy jako np
import matplotlib.pyplot as plt # Biblioteka matplotlib od python plot jako plt
import soundfile as sf # Biblioteka soundfile jak sf
import wave as w # Biblioteka wave jak w

sound = w.open("kotek.wav") # Otwarcie pliku audio w zmiennej
frames_frequency = sound.getframerate()*2 # Wyliczanie częstotliwości klatek
record = np.frombuffer(sound.readframes(-1),dtype="int16")/2000 # Wczytanie dźwięku do zmiennej z zmiennej z plikiem audio
x = np.arange(0, record.size/frames_frequency, 1/frames_frequency) # Stworzenie zakresu o długości <0;record.size/frames_frequency>

plt.plot(x,record) # Rysowanie w zakresie zmiennej x funkcji record
plt.axhline(y=0,color = "k") # Zaznacznie lini y=0 kolorem czarnym
plt.axvline(x=0,color = "k") # Zaznacznie lini x=0 kolorem czarnym
plt.grid(True,which='both') # Włączenie siatki
plt.title('Wlazł Kotek na Płotek') # Tytuł wykresu 
plt.xlabel("Czas [s]") # Podpis osi x
plt.ylabel("Amplituda") # Podpis osi y
plt.show() # Wywołanie wykresu