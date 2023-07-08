#include<msp430x14x.h>
#include "lcd.h"
#include "portyLcd.h"

#define KL1 BIT4&P4IN                         		// Zdefiniowanie Klawisza pierwszego jako KL1
#define KL2 BIT5&P4IN                         		// Zdefiniowanie Klawisza drugiego jako KL2
	
unsigned char znak1 ,znak2, znak3;  				// Zdefiniowanie zmiennej znakowej znak1 , znak2 oraz znak3

// Przesuniêcie o jedn¹ pozycje w prawo lub lewo po klikniêciu klawisza
// minimum 4 znaki, w tym jeden polski, wzór -> <=¿=>
// Dodatkowo obiekt znajduje siê na obu wierszach

void polski_znaczek()								// Funkcja wys³ania znaku do pamiêci
{													 
  	SEND_CMD(CG_RAM_ADDR);							// Inicjonowanie wysy³ania do pamiêci
  	int znaczek[8] = {4,0,31,2,4,8,31,0};			// Definicja znaku w systemie dziesi¹tkowym ale indexy pikseli 
													// od prawej liczone w systemie potêg dwójki (1,2,4,8,16)
	for(int i=0;i<8;i++) SEND_CHAR(znaczek[i]);		// Wysy³anie z tablicy znaku do pamiêci
}

void main( void )
{
  znak1='<';										// Znak koñca lewego
  znak2='=';										// Znak œrodka
  znak3='>';										// Znak koñca prawego
  WDTCTL=WDTPW+WDTHOLD;                       		// Zatrzymanie WDT
  
  InitPortsLcd();                               	// Inicjalizacja portów  
  InitLCD();                                    	// Inicjalizacja LCD
  clearDisplay();                               	// Czyszczenie LCD  
  
  polski_znaczek();									// Wywo³anie funkcji inicjuj¹cej znaczek
  
  SEND_CMD(DD_RAM_ADDR);							// Ustawienie pisania na wiersz pierwszy
  
  SEND_CHAR(znak1);									// Wys³anie pierwszego znaku (pocz¹tek)
  SEND_CHAR(znak2);									// Wys³anie drugiego znaku (œrodek)
  SEND_CHAR(8); 									// Wys³anie polskiego znaku (œrodek), 8 index jest indexem 
  													// w którym przechowywuje siê nasz znak (pierwszy wolny, dla uzytkownika)
  SEND_CHAR(znak2);									// Wys³anie drugiego znaku (œrodek)
  SEND_CHAR(znak3);									// Wys³anie trzeciego znaku (koniec)
  
  SEND_CMD(DD_RAM_ADDR2);							// Ustawienie pisania na wiersz drugi
  
  SEND_CHAR(znak1);									// Wys³anie pierwszego znaku (pocz¹tek)
  SEND_CHAR(znak2);									// Wys³anie drugiego znaku (œrodek)
  SEND_CHAR(8); 									// Wys³anie polskiego znaku (œrodek), 8 index jest indexem 
  													// w którym przechowywuje siê nasz znak (pierwszy wolny, dla uzytkownika)
  SEND_CHAR(znak2);									// Wys³anie drugiego znaku (œrodek)
  SEND_CHAR(znak3);									// Wys³anie trzeciego znaku (koniec)
  
  	while (1)                                       // Nieskoñczona pêtla 
  	{
      if((KL1)==0) SEND_CMD(DATA_ROL_LEFT);       	// Przesuwanie napisu w lewo w momencie klikniêcia przycisku pierwszego 
      else if((KL2)==0) SEND_CMD(DATA_ROL_RIGHT); 	// Przesuwanie napisu w prawo w momencie klikniêcia przycisku drugiego
      Delayx100us(100);								// Ustawienie opóŸnienia na 100ms w celu przesuwania znaków o jedno pole 
	}												// oraz umo¿liwienie szybkiego klikania przycisku (p³ynnoœæ przechodzenia)
}