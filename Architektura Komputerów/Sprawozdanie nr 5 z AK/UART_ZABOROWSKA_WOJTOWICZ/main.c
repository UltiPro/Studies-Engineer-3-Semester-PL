#include<msp430x14x.h>
#include "uart.h"
#include "lcd.h"
#include "portyUart.h" 
#include "portyLcd.h" 
#define KL1 BIT4 &P4IN
#define KL2 BIT5 &P4IN
#define KL3 BIT6 &P4IN
#define KL4 BIT7 &P4IN
//transmisja szeregowa z p³ytki do kompa, z kompa do p³ytki
char Bufor[32];                         // bufor odczytywanych danych
int low=0;                              // znacznik pocz¹teku danych w buforze  
int high=0;                             // zmacznik koñca danych w buforze

void main(void)
{
 WDTCTL=WDTPW + WDTHOLD;                // wy³¹czenie WDT
  
 InitPortsLcd();                        // inicjalizacja portów LCD
 InitLCD();                             // inicjalizacja LCD
 clearDisplay();                        // czyszczenie wyœwietlacza
 initPortyUart();                       // inicjalizacja portow UART  
 initUart(115200);                        // inicjalizacja UARTa prêdkoœæ transmisji 2400 Budoów  

 _EINT();                               // w³¹czenie przerwañ 
int i=0;
while(1)                                // nieskoñczona pêtla
 {
   
   if( (KL1) ==0)
   {
	 UartCharTransmit('P');        // wys³anie napisu Tekst do ternimala 
	for(long int i=0;i<300000;i++);
   }
   else if( (KL2) ==0)
   {
	 UartCharTransmit('U');        // wys³anie napisu Tekst do ternimala
	 for(long  int i=0;i<300000;i++);
   }
   else if( (KL3) ==0)
   {
	 UartCharTransmit('T');        // wys³anie napisu Tekst do ternimala
	 for(long int i=0;i<300000;i++);
   }
   else if( (KL4) ==0)
   {
	 UartCharTransmit('Y');        // wys³anie napisu Tekst do ternimala 
	 for(long int i=0;i<300000;i++);
   }

   while(high != low)                  // gdy odebrano dane 
    {
     putc(Bufor[low]);                 // wypisanie danych na wyœwietlaczu    
     if(low%33 ==0)
	 {
	    SEND_CMD(DD_RAM_ADDR2);
	 }
	 else if(low%17 ==0)
	 {
	   SEND_CMD(DD_RAM_ADDR2);
	   clearDisplay();
	 }
	 low = (++low)%33;
    }

 }



}


#pragma vector=UART0RX_VECTOR           // procedura obs³ugi przerwania UART
__interrupt void usart0_rx (void)
{ 
Bufor[high]=RXBUF0;                     // wpisanie odebranych danych do bufora
high=(++high)%33;                       // inkrementowanie znacznika koñca danych
}