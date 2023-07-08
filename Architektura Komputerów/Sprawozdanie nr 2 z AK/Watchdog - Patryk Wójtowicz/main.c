// Program demonstruje działanie układu watchdog timer w trybie pracy watchdog
// Podczas pracy po resecie zasilania dioda Status jest zapalona
// W przypadku naciśnięcia klawisza następuje zawieszenie programu
// Układ watchdog restartuje program a użytkownikowi jest to oznajmiane po przez
// Zapalenie diód sygnalizujących P.1.5 oraz P.1.6

#include <msp430x14x.h>
#define KL1 BIT4 &P4IN // Klawisz - P4.4
#define D1 BIT5 &P1OUT // Dioda - P1.5
#define D2 BIT6 &P1OUT // Dioda - P1.6

void main(void)
{
  WDTCTL = WDTPW + WDTHOLD;       // Wyłączenie układu WDT
  P1DIR |= BIT5 + BIT6;           // Ustawienie bitu P.1.5 i P.1.6 jako wyjście
  P1OUT &= ~BIT5;                 // Zgaszenie diody P1.5
  P1OUT &= ~BIT6;                 // Zgaszenie diody P1.6
  P2DIR |= BIT1;                  // Ustawienie bitu P.2.1 jako wyjście
  P2OUT &= ~BIT1;                 // Zapalenie diody P.2.1 (Status)
  BCSCTL1 |= XTS + DIVA1 + DIVA0; // (ACLK = LFXT1 = HF XTAL)/8

  do
  {
    IFG1 &= ~OFIFG;         // Czyszczenie flgi OSCFault
  } while ((IFG1 & OFIFG)); // Dopóki OSCFault jest ciągle ustawiona

  WDTCTL = WDTPW + WDTCNTCL + WDTSSEL; // Tryb pracy watchdog ACLK

  if (WDTIFG & IFG1) // Demonsrcja po przez zgaszenie diody P.2.1 (STATUS)
                     // oraz zapalenie diody P.1.5, P.1.6 że WDT przechwycił przerwanie
  {
    IFG1 &= ~WDTIFG; // Czyszczenie Flagi WDTIFG
    P2OUT |= BIT1;
    P1OUT |= BIT5;
    P1OUT |= BIT6;
  }

  while (1)
  {
    if ((KL1) == 0) // Sprawdzenie czy klawiesz jest wciśnięty
    {
      while (1)
        ; // Pętla nieskończona, zawieszenie progrmu
    }
    else
    {
      WDTCTL = WDTPW + WDTCNTCL; // Zerowanie WDT
    }
  }
}