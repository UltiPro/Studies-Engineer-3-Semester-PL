void InitLCD(void);
void putc(char c);
void clearDisplay();
void printDecDigit(int Number);
void printDecimal(int Number);
void printHex(unsigned int Number);
void printString(char *String);
void gotoSecondLine();
void SEND_CHAR(unsigned char c);
void SEND_CMD(unsigned char e);
void MAKE_DEFINED_CHAR(unsigned char c);
void Delayx100us(unsigned char b);