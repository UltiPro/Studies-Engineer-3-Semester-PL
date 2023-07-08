#include <msp430x14x.h>
#include "LCD.h"
#include "portyLcd.h"
// #include "lcd1.c"
// #include "portyLcd1.h"
#define INTERVAL 50000 // okres licznika 0,5s
#define _5s 10         // okres pomiar�w

void znaczek_stopni()
{
  LCD_cmd(CG_RAM_ADDR);
  int znaczek[8] = {1, 0, 0, 0, 0, 0, 0, 0};
  for (int i = 0; i < 8; i++)
    LCD_char(znaczek[i]);
}
long long int temp;
unsigned int cntr;
void show(void);
main(void)
{
  // znaczek_stopni();
  unsigned int k;
  WDTCTL = WDTPW + WDTHOLD;
  ini_display();                         // inicjalizacja LCD
  ADC12CTL0 = ADC12ON | REFON | SHT0_15; // w3. rdzenia, w3.gen. nap. odniesienia, wyb�r nap. odniesienia
  ADC12CTL1 = SHP | CSTARTADD_0;         // pr�bkowanie impulsowe, wynik sk3adany w ADC12MEM0
  ADC12MCTL0 = INCH_10 | SREF_1;         // kana3 10, Yr�d3o nap. odniesienia - wew. generator (1,5V)
  for (k = 0; k < 0x3600; k++)
    ; // czas na ustabilizowanie generatora nap. odniesienia

  CCR0 = INTERVAL;                // ustala nowy okres licznika
  TACTL = TASSEL_2 | ID_3 | MC_1; // Yr�d3o taktowania SMCLK, dzielone przez 8,tryb UP
  CCTL0 = CCIE;                   // uaktywnienie przerwania od TACCR0 CCIFG
  _BIS_SR(GIE);                   // w3aczenie przerwan

  ADC12CTL0 |= ENC; // uaktywnienie konwersji
  while (1)
  {
    P2OUT ^= BIT1;
    ADC12CTL0 |= ADC12SC; // start konwersji
    while ((ADC12CTL1 & ADC12BUSY) == 1)
      ;                                    // czekanie na koniec konwersji
    temp = ADC12MEM0 * 1.0318 - 2777.4647; // wartooa temperatury z dok. 1-miejsce po przecinku
    show();                                // wyowietla na LCD
    _BIS_SR(LPM0_bits);                    // wejocie w tryb oszczedny
  }
}

void show(void)
{
  long long int cyfra, waga = 10, cyfrafar, wagafar = 10, far = ((2 * temp) + 284), cyfrakel, wagakel = 10, kel = temp + 2730;
  LCD_cmd(CLR_LCD);
  wait(_2ms);
  // stopnie celcjusza
  if (temp < 0)
  {
    LCD_char('-');
    temp *= -1;
  }
  if (temp < 10)
    LCD_char('0');

  if (temp >= 1000)
  {
    LCD_char('?');
    return;
  }
  while (waga <= temp)
  {
    waga *= 10;
  }
  while ((waga /= 10) > 1)
  {
    cyfra = temp / waga;
    LCD_char((int)('0' + cyfra));
    temp -= cyfra * waga;
  }
  LCD_char('.');
  LCD_char((int)('0' + temp));
  LCD_char(' ');
  LCD_char('C');
  LCD_char(' ');
  // farenhighty
  if (far < 0)
  {
    LCD_char('-');
    far *= -1;
  }
  if (far < 10)
    LCD_char('0');
  while (wagafar <= far)
  {
    wagafar *= 10;
  }
  while ((wagafar /= 10) > 1)
  {
    cyfrafar = far / wagafar;
    LCD_char((int)('0' + cyfrafar));
    far -= cyfrafar * wagafar;
  }
  LCD_char('.');
  LCD_char((int)('0' + far));
  LCD_char(' ');
  LCD_char('F');
  LCD_char(' ');
  // kelwiny
  LCD_cmd(DD_RAM_ADDR2);
  if (kel < 0)
  {
    LCD_char('-');
    kel *= -1;
  }
  if (kel < 10)
  {
    LCD_char('0');
  }
  while (wagakel <= kel)
  {
    wagakel *= 10;
  }
  while ((wagakel /= 10) > 1)
  {
    cyfrakel = kel / wagakel;
    LCD_char((int)('0' + cyfrakel));
    kel -= cyfrakel * wagakel;
  }
  LCD_char('.');
  LCD_char((int)('0' + kel));
  LCD_char(' ');
  LCD_char('K');
  LCD_char(' ');
}

#pragma vector = TIMERA0_VECTOR
__interrupt void Timer_A(void)
{
  if (++cntr == _5s)
  {
    _BIC_SR_IRQ(LPM0_bits); // wyjocie z trybu oszczednego
    cntr = 0;
  }
}