#include <msp430x14x.h>
#include <stdlib.h>
#include "portyLcd.h"
#include "lcd.h"
#define B1 BIT4&P4IN
#define DALLAS BIT7
#define WE 0
#define PORT_1Wire DALLAS
#define SET_1Wire P1DIR |= DALLAS;P1OUT |= DALLAS
#define CLEAR_1Wire P1DIR |= DALLAS;P1OUT &= ~DALLAS
unsigned int cntr;
int wait_flag=0;

int zerowy = 1, wcisniety = 0;

int bit_is_clear(int a, int b){
    P1DIR &= ~DALLAS;
    return !(P1IN & DALLAS);
}

int bit_is_set(int a, int b){
    P1DIR &= ~DALLAS;
    __delay_cycles(80);
    return P1IN & DALLAS;
}

int bit_is_set2(int a, int b){
    P1DIR &= ~DALLAS;
    return P1IN & DALLAS;
}

unsigned char RESET_PULSE(void)
{
    unsigned char PRESENCE;
    CLEAR_1Wire;    //ustawiamy magistrale w poziom niski
    __delay_cycles(4000); // >480us
    SET_1Wire;     //ustawiamy magistrale w poziom wysoki
    __delay_cycles(240); //oczekiwanie na ustawienie linii w stan niski przez DS 15-60us

    //sprawdzamy poziom linii (czy w stanie niskim)
    if(bit_is_clear(PORT_1Wire, WE)) PRESENCE=1;
    else PRESENCE=0;

    //1-odebrano bit PRESENCE, 0- stan nieaktywnooci
    __delay_cycles(3840); //odczekanie rzez mastera 480us i spr. czy DALLAS podciagnal magistrale
    
    //sprawdzamy posiom linii (czy ustawiona)
    if(bit_is_set(PORT_1Wire, WE)) PRESENCE=1;
    else PRESENCE=0;
    
    return PRESENCE; //zwracamy wartosc do funkcji
}

void send(char bit)
{
    CLEAR_1Wire; //ustawienie w stan niski magistralii
    __delay_cycles(40);
    if(bit==1) SET_1Wire; // zwolnienie magistralii - wyslanie jedynki    
    __delay_cycles(640); // przetrzymanie - wyslanie zera
    SET_1Wire;
}

unsigned char read(void)
{
    unsigned char PRESENCE=0;
    CLEAR_1Wire; //ustawienie w stan niski DQ
    __delay_cycles(16); //odczekanie 2us
    SET_1Wire; //zwolnienie magistrali
    __delay_cycles(120); //delay 15us
    if(bit_is_set2(PORT_1Wire, WE))  PRESENCE=1;
    else PRESENCE=0;         //odbior jedynki lub zera
    
    return(PRESENCE);
}

void send_byte(char wartosc)
{
    unsigned char i; //zmienna licznikowa
    unsigned char pom; //zmienna pomocnicza

    for(i=0; i<8; i++)    
    {
        pom=wartosc>>i;//przesuniecie bitowe w prawo
        pom &=0x01; //skopiowanie bitu do zmiennej pomocniczej
        send(pom); //wyslanie bitu na magistrale
    }

    __delay_cycles(800); //odczekanie 100us
}

char read_byte(void)
{
    unsigned char i; // zmienna licznikowa
    unsigned char wartosc =0; //zczytywana wartosc

    for(i=0; i<8; i++) //petla wykonywana 8 razy    
    {
        if (read()) wartosc|=0x01<<i;
        __delay_cycles(120); //odczekanie 15us
    }
    return(wartosc); //zwrot wartosci do funkcji
}

int celsiusToFarenheit(int t)
{
    int u = t % 100;
    float f = 32 + 9*((t - u)/100.f + u/100.f)/5.f;	// obliczanie temp
    float x = (f - (int)f)*100;
    if(x - (int)x >= 0.5) f += 0.01f;

    return (int)(f * 100);
}

void show(long int t)
{
    int cyfra, waga=10;
    Delayx100us(2);
    if(t < 0) 					// wypisanie �-� przed wartosci1 ujemna
    {
        SEND_CHAR('-');
        t *= -1;
    }
    if(t < 10) SEND_CHAR('0');
    if(t >= 10000) 				// wypisanie �?� jezeli temperatura przekroczy dopuszczalny poziom
    {
        SEND_CHAR('?');
        return;
    }
    while(waga <= t) waga *= 10;
    while((waga /= 10) > 10)
    {
        cyfra = t / waga;			// liczba kt�ra zostanie wyowietlona jako temperatura
        SEND_CHAR((int)('0' + cyfra));
        t -= cyfra * waga;
    }
    SEND_CHAR('.');
    cyfra = t / waga;				// pierwsza cyfra po przecinku
    SEND_CHAR((int)('0' + cyfra));
    t -= cyfra * waga;			// druga cyfra po przecinku
    SEND_CHAR((int)('0' + t));
}

int main(void)
{
    unsigned char sprawdz;
    char temp1=0,temp2=0;
    int temp;
    unsigned int k;
    WDTCTL=WDTPW + WDTHOLD;
    InitPortsLcd();                   // inicjalizacja port�w LCD
    InitLCD();                        // inicjalizacja LCD
    clearDisplay();                   // czyszczenie wyowietlacza
    //Mierzenie temperatury wewn�trznej
    ADC12CTL0 = ADC12ON | REFON | SHT0_15;	// wlaczenie rdzenia i generatora napiecia odniesienia oraz wyb�r napiecia odniesienia
    ADC12CTL1 = SHP | CSTARTADD_0;   	// pr�bkowanie impulsowe, wynik skladany w ADC12MEM0
    ADC12MCTL0 = INCH_10 | SREF_1;   	// kanal 10, zr�dlo napiecia odniesienia � wewnetrzny generator 1,5 V
    for(k = 0; k < 0x3600; k++);    	// czas na ustabilizowanie generatora napiecia odniesienia
    clearDisplay();                   // czyszczenie wyowietlacza
    clearDisplay();                   // czyszczenie wyowietlacza
    CCR0 = 50000;                  	// ustala nowy okres licznika
    TACTL = TASSEL_2 | ID_3 | MC_1;   	// zr�dlo taktowania SMCLK dzielone przez 8, tryb UP
    CCTL0 = CCIE;      			// uaktywnienie przerwania od TACCR0
    _BIS_SR(GIE);      			// wlaczenie przerwan
    ADC12CTL0 |= ENC;  			// uaktywnienie konwersji
    int i;

    P2DIR |= BIT1 ;

    BCSCTL1 |= XTS;                       // ACLK = LFXT1 = HF XTAL 8MHz
    do
    {
        IFG1 &= ~OFIFG;                     // Czyszczenie flgi OSCFault
        for (i = 0xFF; i > 0; i--);         // odczekanie
    }
    while ((IFG1 & OFIFG) == OFIFG);    // dop�ki OSCFault jest ci1gle ustawiona

    BCSCTL1 |= DIVA_0;                    // ACLK=8 MHz
    BCSCTL2 |= SELM0 | SELM1;             // MCLK= LFTX1 =ACLK

    for(;;)    
    {
        if(0==0)        
        {
            wcisniety = 1;
            zerowy = 0;
            sprawdz=RESET_PULSE(); //impuls resetu
            if(sprawdz==1)            
            {
                send_byte(0xCC); //SKIP ROM
                send_byte(0x44); //CONVERT T
                for(k=0; k<9; k++)__delay_cycles(600000); //odczekaj 750ms - czas konwersji
                sprawdz=RESET_PULSE(); //wyslanie impulsu reset
                send_byte(0xCC); //SKIP ROM
                send_byte(0xBE); //READ SCRATCHPAD
                temp1=read_byte(); //odczytanie LSB
                temp2=read_byte(); //odczytanie MSB
                sprawdz=RESET_PULSE(); //zwolnienie magistrali
                float temp=0; //zmienna do obliczen
                temp=(float)(temp1+(temp2*256))/16; //obl. temp
                SEND_CMD(DD_RAM_ADDR+0x00);
                if(temp < 0) 					// wypisanie �-� przed wartosci1 ujemna
                {
                    SEND_CHAR('-');
                    temp *= -1;
                }
                if(((int)(temp/10) != 0) &&(((int)(temp)%10)!=0)&&(((int)(temp*10)%10)!=0))
                {
                    clearDisplay();
                    SEND_CHAR((int)(temp/10)+0x30);
                    SEND_CHAR((int)(temp)%10+0x30);
                    SEND_CHAR('.');
                    SEND_CHAR((int)(temp*10)%10+0x30);
                    SEND_CHAR('C');
                    __delay_cycles(16000);
                }
                else //jezli nie wykryto PRESENCE_PULSE
                {
                    if(((int)(temp/10) == 0) &&(((int)(temp)%10)==0)&&(((int)(temp*10)%10)==0))
                    {
                        SEND_CMD(DD_RAM_ADDR+0x00);

                        SEND_CHAR(' ');
                        SEND_CHAR('B');
                        SEND_CHAR('R');
                        SEND_CHAR('A');
                        SEND_CHAR('K');
                        SEND_CHAR(' ');
                        SEND_CHAR('C');
                        SEND_CHAR('Z');
                        SEND_CHAR('U');
                        SEND_CHAR('J');
                        SEND_CHAR('N');
                        SEND_CHAR('I');
                        SEND_CHAR('K');
                        SEND_CHAR('A');
                        SEND_CHAR(' ');
                    }
                }
            }
            else //jezli nie wykryto PRESENCE_PULSE
            {
                SEND_CMD(DD_RAM_ADDR+0x00);
                SEND_CHAR(' ');
                SEND_CHAR('Z');
                SEND_CHAR('L');
                SEND_CHAR('E');
                SEND_CHAR(' ');
                SEND_CHAR('W');
                SEND_CHAR('P');
                SEND_CHAR('I');
                SEND_CHAR('E');
                SEND_CHAR('T');
                SEND_CHAR('Y');
                SEND_CHAR(' ');
                SEND_CHAR(' ');
                SEND_CHAR(' ');
                SEND_CHAR(' ');
                SEND_CHAR(' ');
            }
        } 
        else wcisniety = 0;
        
        ADC12CTL0 |= ADC12SC;       	// start konwersji
        while((ADC12CTL1 & ADC12BUSY) == ADC12BUSY);	// czekanie na koniec konwersji
        temp=(int)(ADC12MEM0*1.0318-2777.4647)*10;
        if(wait_flag==0 && zerowy==0)
        {
            SEND_CHAR(' ');
            SEND_CHAR(' ');
            SEND_CHAR('T');
            SEND_CHAR('E');
            SEND_CHAR('M');
            SEND_CHAR('P');
            SEND_CHAR('.');
            SEND_CHAR('O');
            SEND_CHAR('U');
            SEND_CHAR('T');
            wait_flag=1;
        } 
        else if(zerowy==1)
        {
            SEND_CHAR(' ');
            SEND_CHAR('B');
            SEND_CHAR('R');
            SEND_CHAR('A');
            SEND_CHAR('K');
            SEND_CHAR(' ');
            SEND_CHAR(' ');
            SEND_CHAR('T');
            SEND_CHAR('E');
            SEND_CHAR('M');
            SEND_CHAR('P');
            SEND_CHAR('.');
            SEND_CHAR('O');
            SEND_CHAR('U');
            SEND_CHAR('T');
            SEND_CHAR(' ');       
        } 
        if(!wcisniety || zerowy==1) 
        {
            SEND_CMD(DD_RAM_ADDR2);
            show(temp);                 	// wyswietla na wyswietlaczu
            SEND_CHAR('C');
            SEND_CHAR(' ');
            SEND_CHAR('T');
            SEND_CHAR('E');
            SEND_CHAR('M');
            SEND_CHAR('P');
            SEND_CHAR('.');
            SEND_CHAR('I');
            SEND_CHAR('N');
            SEND_CHAR('P');
            SEND_CHAR(' ');
            SEND_CHAR(' ');
        }
        for(int i=0; i < 10000; i++){}
    }
}

#pragma vector = TIMERA0_VECTOR
__interrupt void Timer_A(){
    if(++cntr == 10) {
        _BIC_SR_IRQ(LPM0_bits);
cntr = 0;
    }
}