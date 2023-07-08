#include <msp430x14x.h>
#include "uart.h"
#include "lcd.h"
#include "portyUart.h"
#include "portyLcd.h"
#define KL1 BIT4 &P4IN
#define KL2 BIT5 &P4IN
#define KL3 BIT6 &P4IN
#define KL4 BIT7 &P4IN
// transmisja szeregowa z p�ytki do kompa, z kompa do p�ytki
char Bufor[32]; // bufor odczytywanych danych
int low = 0;    // znacznik pocz�teku danych w buforze
int high = 0;   // zmacznik ko�ca danych w buforze

void main(void)
{
   WDTCTL = WDTPW + WDTHOLD; // wy��czenie WDT

   InitPortsLcd();   // inicjalizacja port�w LCD
   InitLCD();        // inicjalizacja LCD
   clearDisplay();   // czyszczenie wy�wietlacza
   initPortyUart();  // inicjalizacja portow UART
   initUart(115200); // inicjalizacja UARTa pr�dko�� transmisji 2400 Budo�w

   _EINT(); // w��czenie przerwa�
   int i = 0;
   while (1) // niesko�czona p�tla
   {

      if ((KL1) == 0)
      {
         UartCharTransmit('P'); // wys�anie napisu Tekst do ternimala
         for (long int i = 0; i < 300000; i++)
            ;
      }
      else if ((KL2) == 0)
      {
         UartCharTransmit('U'); // wys�anie napisu Tekst do ternimala
         for (long int i = 0; i < 300000; i++)
            ;
      }
      else if ((KL3) == 0)
      {
         UartCharTransmit('T'); // wys�anie napisu Tekst do ternimala
         for (long int i = 0; i < 300000; i++)
            ;
      }
      else if ((KL4) == 0)
      {
         UartCharTransmit('Y'); // wys�anie napisu Tekst do ternimala
         for (long int i = 0; i < 300000; i++)
            ;
      }

      while (high != low) // gdy odebrano dane
      {
         putc(Bufor[low]); // wypisanie danych na wy�wietlaczu
         if (low % 33 == 0)
         {
            SEND_CMD(DD_RAM_ADDR2);
         }
         else if (low % 17 == 0)
         {
            SEND_CMD(DD_RAM_ADDR2);
            clearDisplay();
         }
         low = (++low) % 33;
      }
   }
}

#pragma vector = UART0RX_VECTOR // procedura obs�ugi przerwania UART
__interrupt void usart0_rx(void)
{
   Bufor[high] = RXBUF0; // wpisanie odebranych danych do bufora
   high = (++high) % 33; // inkrementowanie znacznika ko�ca danych
}