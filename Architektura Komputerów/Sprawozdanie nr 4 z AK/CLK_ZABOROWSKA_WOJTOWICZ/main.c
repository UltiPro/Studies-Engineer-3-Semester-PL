#include <msp430x14x.h>
#include "lcd.h"
#include "portyLcd.h"

//piny P4.4 - P4.7 jako wejścia
#define KL1 BIT4 &P4IN 
#define KL2 BIT5 &P4IN 
#define KL3 BIT6 &P4IN
#define KL4 BIT7 &P4IN
//---------------- zmienne globalne -------------
unsigned int i = 0;
unsigned int licznik = 0;
unsigned char znaki[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}; // tablica znaków możliwych do wyświetlenia
unsigned int ilem_j = 0, ilem_d = 0, ile_s = 0, ile_d = 0, 
minuty_j = 0, minuty_d = 0, godz_j = 0, godz_d = 0; 						//licznik jedności i dziesiątek w godzinie, minucie sekundzie i milisekundzie
unsigned int ster = 0;

void Clock(void);	// deklaracja funkcji Clock()
void start_s();		// deklaracja funkcji start_s()

//----------------- main program -------------------
void main(void)
{
	P2DIR |= BIT1; // STATUS LED

	WDTCTL = WDTPW + WDTHOLD; // Wyłączenie WDT

	InitPortsLcd(); // inicjalizacja portów LCD
	InitLCD();		// inicjalizacja LCD
	clearDisplay(); // czyszczenie wyświetlacza

	// Basic Clock Module ustawiamy na ACLK(zegar 8 MHz ) i dzielimy częstotliwość przez 2 (4 MHz)
	BCSCTL1 |= XTS; // ACLK = LFXT1 = HF XTAL 8MHz

	do
	{
		IFG1 &= ~OFIFG; 				// Czyszczenie flgi OSCFault
		for (i = 0xFF; i > 0; i--);		// odczekanie
	} while ((IFG1 & OFIFG) == OFIFG); 	// dopóki OSCFault jest ciągle ustawiona

	BCSCTL1 |= DIVA_1;		  // ACLK=8 MHz/2=4 MHz
	BCSCTL2 |= SELM0 | SELM1; // MCLK= LFTX1 =ACLK

	// Timer_A  ustawiamy na 500 kHz
	// a przerwanie generujemy co 100 ms
	TACTL = TASSEL_1 + MC_1 + ID_3; // Wybieram ACLK, ACLK/8=500kHz,tryb Up
	CCTL0 = CCIE;					// włączenie przerwan od CCR0
	CCR0 = 5000;					// podzielnik 50000: przerwanie generowane co 100 ms

	_EINT(); 	// włączenie przerwań
	start_s();	// wywołanie funkcji wyświetlającej poczatkowy zegar
	for (;;)
	{
		_BIS_SR(LPM3_bits); // przejscie do trybu LPM3
		Clock();			// wywołanie zegara
	}
}

void Clock(void) // funkcja zegara
{
	if ((KL1) == 0) 	// jeżeli klawisz pierwszy jest wciśnięty
	{					// zmienną sterującą ustawiamy na 1
		ster = 1;		// by można było rozpocząć liczenie stopera
	}
	else if ((KL2) == 0)	// jeżeli klawisz drugi jest wciśnięty
	{						// zmienną sterująca ustawiamy na 0					
		ster = 0;			// by można było zatrzymać liczenie 
	}
	else if ((KL3) == 0 && ster == 0) 	// jeżeli klawisz trzeci jest wciśnięty
	{									// oraz zmienna sterująca jest ustawiona na 0,
		ile_s = 0;						// czyli stoper jest zatrzymany wtedy następuje
		ile_d = 0;						// wyzerowanie stopera, czyli przwyrócenie go w stan początkowy
		minuty_j = 0;						// oraz wyświetlenie ponowne samych zer funkca start_s()
		minuty_d = 0;
		godz_j = 0;
		godz_d = 0;
		ster = 0;
		start_s();
	}
	else if ((KL4) == 0 && ster == 1) 		// jeśli wciśnięto klaiwsz czwarty oraz stoper nie jest zatrzymany
	{								  		// to w górnej liny wyświetla zapisuje się międzyczas
		SEND_CMD(DD_RAM_ADDR);	// wyświetlanie w pierwszej lini wyświetlacza	  		
		SEND_CHAR(znaki[godz_d % 10]);		// godziny
		SEND_CHAR(znaki[godz_j % 6]);
		SEND_CHAR(':');
		SEND_CHAR(znaki[minuty_d % 10]);	// minuty
		SEND_CHAR(znaki[minuty_j % 6]);
		SEND_CHAR(':');
		SEND_CHAR(znaki[ile_d % 10]);		// sekundy
		SEND_CHAR(znaki[ile_s % 10]);
		SEND_CHAR(':');
		SEND_CHAR(znaki[ilem_d % 10]);		// milisekundy
		SEND_CHAR(znaki[ilem_j % 10]);
	}
	if (licznik % 10 == 0 && ster == 1) // gdy mineła sekunda (10 * 100 milisekund) i nie zatrzymano timera
	{
		licznik = 0;
		for (int k = 0; k < 10; k++) // dla każdych 10 ms wyświetla odświerzony czas.
		{
			SEND_CMD(DD_RAM_ADDR2); 			// wyświetlanie w drugiej lini wyświetlacza
			SEND_CHAR(znaki[godz_d % 10]); 		// godziny
			SEND_CHAR(znaki[godz_j % 6]);
			SEND_CHAR(':');
			SEND_CHAR(znaki[minuty_d % 10]); 	// minuty
			SEND_CHAR(znaki[minuty_j % 6]);
			SEND_CHAR(':');
			SEND_CHAR(znaki[ile_d % 10]); 		// sekundy
			SEND_CHAR(znaki[ile_s % 10]);
			SEND_CHAR(':');
			SEND_CHAR(znaki[ilem_d % 10]); 		// milisekundy
			SEND_CHAR(znaki[ilem_j % 10]);
			P2OUT ^= BIT1; 						//zapal diodę
			ilem_j++; 							// zwiększamy jedności milisekund o 1
		}
		if (godz_j >= 10)	// jeżeli godziny w jednościach są większe równe 10 zwiększamy
		{					// godziny w dziesiątkach i zerujemy godziny w jednościach
			godz_d++;
			godz_j = 0;
		}
		if (minuty_d >= 6)	// jeżeli minuty w dziesiątkach są większe równe 6 zwiększamy
		{					// godziny w jednościach i zerujemy minuty w dziesiątkach
			godz_j++;		
			minuty_d = 0;
		}
		if (minuty_j >= 10)	// jeżeli minuty w jednościach są większe równe 10 zwiększamy
		{					// minuty w dziesiątek i zerujemy minuty w jednościach
			minuty_d++;					
			minuty_j = 0;
		}
		if (ile_d >= 6)		// jeżeli sekundy w dziesiątkach są większe równe 6 zwiększamy
		{					// minuty w jednościach i zerujemy sekundy w dziesiątkach
			minuty_j++;
			ile_d = 0;
		}
		if (ile_s >= 10)	// jeżeli sekundy w jednościach są większe równe 10 zwiększamy
		{					// sekundy w dziesiątkach i zerujemy sekundy w jednościach
			ile_d++;
			ile_s = 0;
		}
		if (ilem_d >= 10)	// jeżeli milisekundy w dziesiątkach są większe równe 10 zwiększamy
		{					// sekundy w jednościach i zerujemy milisekundy w dziesiątkach
			ile_s++;
			ilem_d = 0;
		}
		if (ilem_j >= 10) 	// jeżeli milisekundy w jednościach są większe równe 10 zwiększamy 
		{					// milisekundy w dziesiątkach i zerujemy milisekundy w jednościach
			ilem_d++;
			ilem_j = 0;
		}
		SEND_CMD(CUR_SHIFT_LEFT); // powrót kursorem na początek
	}
}

// procedura obsługi przerwania od TimerA
#pragma vector = TIMERA0_VECTOR
__interrupt void Timer_A(void)
{
	licznik += 1;			//do zliczania milisekund *100
	_BIC_SR_IRQ(LPM3_bits); // wyjście z trybu LPM3
}

void start_s() //funkcja wyświetlająca stan początkowy czyli 00:00:00:00
{
	clearDisplay();
	SEND_CMD(DD_RAM_ADDR2); // zapis w drugiej lini wyświetlacza
	SEND_CHAR('0');
	SEND_CHAR('0');
	SEND_CHAR(':');
	SEND_CHAR('0');
	SEND_CHAR('0');
	SEND_CHAR(':');
	SEND_CHAR('0');
	SEND_CHAR('0');
	SEND_CHAR(':');
	SEND_CHAR('0');
	SEND_CHAR('0');
	SEND_CMD(CUR_SHIFT_LEFT); // powrót kursorem na początek
}