#include <msp430x14x.h>

void main( void )
{
    WDTCTL = WDTPW + WDTHOLD; // Wyłączenie układu WDT oraz inicjalizacja zegara
  
    //   |=   Suma OR
    //   &=   Iloczyn AND
    //   ~    Negacja NOT
    //   ^=   Altrernatywa Rozłączna XOR
    
    P1DIR |= BIT5 + BIT6; // Ustawienie P1 Bitu 5 oraz 6 na wyjście
    P4DIR &= ~BIT4; // Ustawienie P4 Bitu 4 na wejście
    
    unsigned int i,j; // Deklaracja zmiennych typu integer i oraz j 
    
    while(1) // nieskończona pętla inna reprezentacja -> for(;;)
    {
      if((P4IN & BIT4) == 0) // Jeżeli guzik 1 jest wcisniśty zapal obie diody (P4IN <- wejście), ! Zero reprezentuje wciśnięcie !
      {
          P1OUT ^= BIT5 + BIT6; //Stan wysoki , przypisuje wartość 0 gdyż brak jest ~ na początku bitów
      }
      else if((P4IN & BIT5) == 0) // Jeżeli guzik 2 jest wcisniśty zapal diody w trybie "konika"
      {
          for(i=0;i<40000;i++); // Czas między wykonywanymi poleceniami inaczej interwał
          P1OUT ^= BIT5; 
          for(i=0;i<40000;i++);
          P1OUT ^= BIT6;
      }
      else if((P4IN & BIT6) == 0) // Jeżeli guzik 3 jest wcisnięty zapal każdą lapkę po 3 razy (jak kierunkowskaz)
      {
        for(j=0;j<6;j++) // Można zauważyć że mimo puszczenia guzika w trakcie wykonania schemat się dokończy
        {
          if(j==0||j==1||j==2)
          {
            for(i=0;i<45000;i++) P1OUT ^= BIT5;
            for(i=0;i<45000;i++) P1OUT &= ~BIT5;
          }
          else
          {
            for(i=0;i<45000;i++) P1OUT ^= BIT6;
            for(i=0;i<45000;i++) P1OUT &= ~BIT6;
          }
        }
      }
      else // Jeżeli guzik nie jest wciśnięty zgaś lampki
      {
        P1OUT &= ~BIT5 + ~BIT6; // Stan niski &= przypisuje wartość 1 gdyż jest ~ na początku bitów
      }
    }
}
