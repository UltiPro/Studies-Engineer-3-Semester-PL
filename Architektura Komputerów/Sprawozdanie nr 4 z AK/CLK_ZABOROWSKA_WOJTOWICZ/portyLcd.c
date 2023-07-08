#include <msp430x14x.h>

void InitPortsLcd(void)
{
  
  P2SEL = 0;  //selekcja wszystkich pinów jako I/O
  P2OUT = 0;  //ustawienie wyjscia wszystkich pinow na wartosc zero
  P2DIR = ~BIT0;   //ustawienie trybu pinow jako output ( za wyjatkiem pinu 0 )
}