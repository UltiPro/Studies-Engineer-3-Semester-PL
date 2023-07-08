#include <msp430x14x.h>
#include "uart.h"

void initUart(int Speed)
{
  int i;
  BCSCTL1 |= XTS; // ACLK = LFXT1 = HF XTAL 8MHz
  do
  {
    IFG1 &= ~OFIFG; // Czyszczenie flgi OSCFault
    for (i = 0xFF; i > 0; i--)
      ;                     // odczekanie
  } while ((IFG1 & OFIFG)); // dop�ki OSCFault jest ci�gle ustawiona
  BCSCTL2 |= SELM1 + SELM0; // MCLK =LFXT1
  BCSCTL1 |= SELS;

  switch (Speed)
  {
  case 1200:
  {
    ME1 |= UTXE0 + URXE0; // W��czenie USART0 TXD/RXD
    UCTL0 |= CHAR;        // 8-bit�w
    UTCTL0 |= SSEL0;      // UCLK = ACLK
    UBR00 = 0x0A;         // 8MHz/Speed in Bauds
    UBR10 = 0x1A;         //
    UMCTL0 = 0x5B;        // Modulation
    UCTL0 &= ~SWRST;      // Inicjalizacja UARTA
    IE1 |= URXIE0;        // W��czenie przerwa� od RX
    break;
  }
  case 2400:
  {
    ME1 |= UTXE0 + URXE0; // W��czenie USART0 TXD/RXD
    UCTL0 |= CHAR;        // 8-bit�w
    UTCTL0 |= SSEL0;      // UCLK = ACLK
    UBR00 = 0x05;         // 8MHz/Speed in Bauds
    UBR10 = 0x0D;         //
    UMCTL0 = 0x5B;        // Modulation
    UCTL0 &= ~SWRST;      // Inicjalizacja UARTA
    IE1 |= URXIE0;        // W��czenie przerwa� od RX
    break;
  }
  case 9600:
  {
    ME1 |= UTXE0 + URXE0; // W��czenie USART0 TXD/RXD
    UCTL0 |= CHAR;        // 8-bit�w
    UTCTL0 |= SSEL0;      // UCLK = ACLK
    UBR00 = 0x41;         // 8MHz/Speed in Bauds
    UBR10 = 0x03;         //
    UMCTL0 = 0x5B;        // Modulation
    UCTL0 &= ~SWRST;      // Inicjalizacja UARTA
    IE1 |= URXIE0;        // W��czenie przerwa� od RX
    break;
  }
  case 115200:
  {
    ME1 |= UTXE0 + URXE0; // W��czenie USART0 TXD/RXD
    UCTL0 |= CHAR;        // 8-bit�w
    UTCTL0 |= SSEL0;      // UCLK = ACLK
    UBR00 = 0x45;         // 8MHz/Speed in Bauds
    UBR10 = 0x00;         //
    UMCTL0 = 0x5B;        // Modulation
    UCTL0 &= ~SWRST;      // Inicjalizacja UARTA
    IE1 |= URXIE0;        // W��czenie przerwa� od RX
    break;
  }
  }
}

//---------------- wysy�anie znaku ---------
void UartCharTransmit(unsigned char znak)
{
  while ((IFG1 & UTXIFG0) == 0)
    ;            // gdy uk��d nie jest zaj�ty
  TXBUF0 = znak; // wysy�amy znak
}

//---------------- wysy�anie napisu ----------
void UartStringTransmit(char *napis)
{
  while (*napis)
    UartCharTransmit(*napis++);
}