#include <msp430x14x.h>
#include "lcd.h"
#include "portyLcd.h"

#define KL1 BIT4 &P4IN // Zdefiniowanie Klawisza pierwszego jako KL1
#define KL2 BIT5 &P4IN // Zdefiniowanie Klawisza drugiego jako KL2

unsigned char znak1, znak2, znak3; // Zdefiniowanie zmiennej znakowej znak1 , znak2 oraz znak3

// Przesuni�cie o jedn� pozycje w prawo lub lewo po klikni�ciu klawisza
// minimum 4 znaki, w tym jeden polski, wz�r -> <=�=>
// Dodatkowo obiekt znajduje si� na obu wierszach

void polski_znaczek() // Funkcja wys�ania znaku do pami�ci
{
  SEND_CMD(CG_RAM_ADDR);                       // Inicjonowanie wysy�ania do pami�ci
  int znaczek[8] = {4, 0, 31, 2, 4, 8, 31, 0}; // Definicja znaku w systemie dziesi�tkowym ale indexy pikseli
                                               // od prawej liczone w systemie pot�g dw�jki (1,2,4,8,16)
  for (int i = 0; i < 8; i++)
    SEND_CHAR(znaczek[i]); // Wysy�anie z tablicy znaku do pami�ci
}

void main(void)
{
  znak1 = '<';              // Znak ko�ca lewego
  znak2 = '=';              // Znak �rodka
  znak3 = '>';              // Znak ko�ca prawego
  WDTCTL = WDTPW + WDTHOLD; // Zatrzymanie WDT

  InitPortsLcd(); // Inicjalizacja port�w
  InitLCD();      // Inicjalizacja LCD
  clearDisplay(); // Czyszczenie LCD

  polski_znaczek(); // Wywo�anie funkcji inicjuj�cej znaczek

  SEND_CMD(DD_RAM_ADDR); // Ustawienie pisania na wiersz pierwszy

  SEND_CHAR(znak1); // Wys�anie pierwszego znaku (pocz�tek)
  SEND_CHAR(znak2); // Wys�anie drugiego znaku (�rodek)
  SEND_CHAR(8);     // Wys�anie polskiego znaku (�rodek), 8 index jest indexem
                    // w kt�rym przechowywuje si� nasz znak (pierwszy wolny, dla uzytkownika)
  SEND_CHAR(znak2); // Wys�anie drugiego znaku (�rodek)
  SEND_CHAR(znak3); // Wys�anie trzeciego znaku (koniec)

  SEND_CMD(DD_RAM_ADDR2); // Ustawienie pisania na wiersz drugi

  SEND_CHAR(znak1); // Wys�anie pierwszego znaku (pocz�tek)
  SEND_CHAR(znak2); // Wys�anie drugiego znaku (�rodek)
  SEND_CHAR(8);     // Wys�anie polskiego znaku (�rodek), 8 index jest indexem
                    // w kt�rym przechowywuje si� nasz znak (pierwszy wolny, dla uzytkownika)
  SEND_CHAR(znak2); // Wys�anie drugiego znaku (�rodek)
  SEND_CHAR(znak3); // Wys�anie trzeciego znaku (koniec)

  while (1) // Niesko�czona p�tla
  {
    if ((KL1) == 0)
      SEND_CMD(DATA_ROL_LEFT); // Przesuwanie napisu w lewo w momencie klikni�cia przycisku pierwszego
    else if ((KL2) == 0)
      SEND_CMD(DATA_ROL_RIGHT); // Przesuwanie napisu w prawo w momencie klikni�cia przycisku drugiego
    Delayx100us(100);           // Ustawienie op�nienia na 100ms w celu przesuwania znak�w o jedno pole
  }                             // oraz umo�liwienie szybkiego klikania przycisku (p�ynno�� przechodzenia)
}