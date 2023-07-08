#include "snake.h"

TM_USB_HIDHOST_Keyboard_t Keyboard;
int8_t Random[2], Snake_Food[2];
int8_t Snake_Head[2], Snake_Head_Last[2], Snake_Foot[2];
volatile uint8_t Snake_FirstTime = 1;
volatile uint8_t GameOver = 0, GameOverDisplay = 0;
char Buffer[50];
volatile TM_SNAKE_t Snake, Snake1;
volatile TM_SNAKE_Settings_t Settings, Settings1;

void TM_SNAKE_DrawPixel(uint8_t x, uint8_t y, uint16_t value);
void TM_SNAKE_PrepareDisplay(void);
void TM_SNAKE_DrawArea(void);
void TM_SNAKE_SetDefaultSnake(void);
void TM_SNAKE_SetFirstOptions(void);

void TM_SNAKE_DeleteFromArray(uint16_t index, int8_t *twobytesarray);
void TM_SNAKE_AddToArray(int8_t *twobytesarray);
void TM_SNAKE_ReplaceArray(uint16_t index, int8_t *twobytesarray);

void TM_SNAKE_SpeedUp(void);
void TM_SNAKE_SpeedDown(void);

void TM_SNAKE_Random(int8_t *twobytesarray);
void TM_SNAKE_GenerateTarget(void);

// sprawdzenie czy zadana pozycja X i Y jest równa kordynatom węża
uint8_t TM_SNAKE_MatchesSnakeLocations(int8_t *twobytesarray);

void TM_SNAKE_Start(void)
{
	// inicjalizacja delaya
	TM_DELAY_Init();

	// inicjalizaja leda
	TM_DISCO_LedInit();

	// wyłaczenie leda
	TM_DISCO_LedOff(LED_ALL);

	// inicjalizacja randoma
	TM_RNG_Init();

	// inicjalizacja LCD
	TM_ILI9341_Init();
	TM_ILI9341_Rotate(TM_ILI9341_Orientation_Portrait_2);

	// inicjalizacja hosta USB
	TM_USB_HIDHOST_Init();

	// ustawianie dafaultowych ustawień
	TM_SNAKE_SetFirstOptions();

	// ustawianie dafaultowych wartości
	TM_SNAKE_SetDefaultSnake();

	// przygotowanie wyświetlacza
	TM_SNAKE_PrepareDisplay();

	// ustawienie targetu generatoa random
	TM_SNAKE_GenerateTarget();

	// ustawienie czasu na 0
	TM_DELAY_SetTime(0);
	while (1)
	{
		// przetworzenie hosta usb
		TM_USB_HIDHOST_Process();

		// sprawdzenie czy snake ma się ruszyć
		if (TM_DELAY_Time() >= Settings.Micros && !Settings.Pause && !GameOver)
		{
			// resetowanie licznika
			TM_DELAY_SetTime(0);

			// pozyskanie nowej wartości kierunku
			Snake.Direction = Snake1.Direction;

			// pobranie ostatniej wartości X/Y z tablicy  = (głowy)
			Snake_Head[0] = Snake.Snake[Snake.LastIndex][0];
			Snake_Head[1] = Snake.Snake[Snake.LastIndex][1];

			// zapisanie ostatniej wartości położenie przed updatem
			Snake_Head_Last[0] = Snake_Head[0];
			Snake_Head_Last[1] = Snake_Head[1];

			if (!Snake_FirstTime)
			{
				// przemieszczenie snake'a
				switch (Snake.Direction)
				{
				case SNAKE_DIRECTION_LEFT:
					Snake_Head[0] -= 1;
					break;
				case SNAKE_DIRECTION_RIGHT:
					Snake_Head[0] += 1;
					break;
				case SNAKE_DIRECTION_UP:
					Snake_Head[1] -= 1;
					break;
				case SNAKE_DIRECTION_DOWN:
					Snake_Head[1] += 1;
					break;
				default:
					break;
				}
			}

			// overflow = tryb przechodzenia przez ścianę
			if (Settings.Overflow)
			{
				// sprawdzenie wartości X
				if (Snake_Head[0] == -1)
				{
					Snake_Head[0] = SNAKE_PIXELS - 1;
				}
				else if (Snake_Head[0] == SNAKE_PIXELS)
				{
					Snake_Head[0] = 0;
				}
				// sprawdzenie wartości Y
				if (Snake_Head[1] == -1)
				{
					Snake_Head[1] = SNAKE_PIXELS - 1;
				}
				else if (Snake_Head[1] == SNAKE_PIXELS)
				{
					Snake_Head[1] = 0;
				}
			}
			else
			{
				// sprawdzenie ścian kolizji
				if (
					Snake_Head[0] == -1 ||
					Snake_Head[0] == SNAKE_PIXELS ||
					Snake_Head[1] == -1 ||
					Snake_Head[1] == SNAKE_PIXELS)
				{
					// koniec gry w przypadku uderzenia
					GameOver = 1;
				}
			}

			if (!Snake_FirstTime)
			{
				// usuwanie 1 wartosći z tablicy pozycji(końca ogona)
				TM_SNAKE_DeleteFromArray(0, Snake_Foot);

				// sprawdzenie kolizji węża ze sobą
				if (TM_SNAKE_MatchesSnakeLocations(Snake_Head))
				{
					// koniec gry
					GameOver = 1;
				}
			}

			// sprawdzenie czy osiągnięto zadaną pozycję
			if (
				!GameOver &&
				Snake_Head[0] == Snake_Food[0] &&
				Snake_Head[1] == Snake_Food[1])
			{
				// dodanie nowego segmentu węża
				TM_SNAKE_AddToArray(Snake_Head);

				// inkrementacja wyniku
				Snake.Hits++;

				// generowanie nowego cukierka
				TM_SNAKE_GenerateTarget();
			}

			if (!GameOver)
			{
				if (!Snake_FirstTime)
				{
					// dodanie nowej val do tablicy = nowa głowa
					TM_SNAKE_AddToArray(Snake_Head);
				}

				// czyszczenie ostatniego piksela ogona
				TM_SNAKE_DrawPixel(Snake_Foot[0], Snake_Foot[1], 0);

				// rysowanie nowej głowy z zadanym kolorem
				TM_SNAKE_DrawPixel(Snake_Head[0], Snake_Head[1], 3);
				// rysowanie piksela po głowie usuwanie struktury głowy i zmiana koloru
				TM_SNAKE_DrawPixel(Snake_Head_Last[0], Snake_Head_Last[1], 1);
			}

			// czyszczenie flagi stanu początkowego
			if (Snake_FirstTime)
			{
				Snake_FirstTime = 0;
			}
		}

		if (GameOver)
		{
			// sprawdzanie czy flaga gameover jest postawiona
			if (!GameOverDisplay)
			{
				// ustawianie flagi
				GameOverDisplay = 1;

				// komunikat game over
				TM_ILI9341_Puts(88, 120, "Game\nOVER", &TM_Font_16x26, ILI9341_COLOR_WHITE, ILI9341_COLOR_BLACK);
				TM_ILI9341_Puts(28, 180, "Press 'r' to start again!!", &TM_Font_7x10, ILI9341_COLOR_WHITE, ILI9341_COLOR_BLACK);
			}
		}
		else
		{
			// czyszczenie glagi game over
			GameOverDisplay = 0;
		}

		// sprawdzanie czy użądzenie jest połączowe
		if (TM_USB_HIDHOST_Device() == TM_USB_HIDHOST_Result_KeyboardConnected)
		{
			// indykacja zielonym ledem
			TM_DISCO_LedOn(LED_GREEN);

			// odczyt z klawiatury
			TM_USB_HIDHOST_ReadKeyboard(&Keyboard);

			// jeśli jakiś przycisk jest wciśnięty
			if (Keyboard.ButtonStatus == TM_USB_HIDHOST_Button_Pressed)
			{
				// sprawdzenie wciśniętego przycisku i czy ma przypisaną akcję
				switch ((uint8_t)Keyboard.Button)
				{
				case SNAKE_KEY_LEFT:
					// zmiana kierunku jeśli jest możliwa
					if (
						Snake.Direction == SNAKE_DIRECTION_UP ||
						Snake.Direction == SNAKE_DIRECTION_DOWN ||
						Snake.Direction == SNAKE_DIRECTION_LEFT)
					{
						// pauza gry
						Settings.Pause = 0;
						// ustawienie kierunku
						Snake1.Direction = SNAKE_DIRECTION_LEFT;
					}
					break;
				case SNAKE_KEY_RIGHT:
					// zmiana kierunku jeśli jest możliwa
					if (
						Snake.Direction == SNAKE_DIRECTION_UP ||
						Snake.Direction == SNAKE_DIRECTION_DOWN ||
						Snake.Direction == SNAKE_DIRECTION_RIGHT)
					{
						// wyświetlenie pauzy
						Settings.Pause = 0;
						// ustawienie kierunku
						Snake1.Direction = SNAKE_DIRECTION_RIGHT;
					}
					break;
				case SNAKE_KEY_UP:
					// zmiana kierunku jeśli jest możliwa
					if (
						Snake.Direction == SNAKE_DIRECTION_LEFT ||
						Snake.Direction == SNAKE_DIRECTION_RIGHT ||
						Snake.Direction == SNAKE_DIRECTION_UP)
					{
						// wyłączenie trybu pauzy
						Settings.Pause = 0;
						// ustawienie kierunku
						Snake1.Direction = SNAKE_DIRECTION_UP;
					}
					break;
				case SNAKE_KEY_DOWN:
					// zmiana kierunku jeśli jest możliwa
					if (
						Snake.Direction == SNAKE_DIRECTION_LEFT ||
						Snake.Direction == SNAKE_DIRECTION_RIGHT ||
						Snake.Direction == SNAKE_DIRECTION_DOWN)
					{
						// wyłączenie trybu pauzy
						Settings.Pause = 0;
						// ustawienie kierunku
						Snake1.Direction = SNAKE_DIRECTION_DOWN;
					}
					break;
				case SNAKE_KEY_SPEED_UP:
					// zwiększenie prędkości jeśli jest to możliwe
					TM_SNAKE_SpeedUp();
					break;
				case SNAKE_KEY_SPEED_DOWN:
					// zmniejszenie prędkości jeśli jest to możliwe
					TM_SNAKE_SpeedDown();
					break;
				case SNAKE_KEY_PAUSE:
					// pauza
					if (Settings.Pause)
					{
						Settings.Pause = 0;
					}
					else
					{
						Settings.Pause = 1;
					}
					break;
				case SNAKE_KEY_RESET:
					// rysowanie węża
					TM_SNAKE_DrawArea();
					// ustawienie pozycji defaultowej
					TM_SNAKE_SetDefaultSnake();
					// generowanie cukierka
					TM_SNAKE_GenerateTarget();
					// reset flagi game over z poprzedniej rozgrywki
					GameOver = 0;
					// resetowanie flagi czasu
					Snake_FirstTime = 1;
					break;
				case SNAKE_KEY_OVERFLOW:
					// włączenie trybu przechodzenie przez ściany
					if (Settings.Overflow)
					{
						Settings.Overflow = 0;
					}
					else
					{
						Settings.Overflow = 1;
					}
					break;
				default:
					break;
				}
			}
		}
		else
		{
			// wyłączenie zielonego leda
			TM_DISCO_LedOff(LED_GREEN);
		}
		// update LCD z zmienionymi ustawieniami
		// sprawdzenmie trybu ściany
		if (Settings1.Overflow != Settings.Overflow || Settings1.Speed != Settings.Speed)
		{
			// zapisanie trybu
			Settings1.Overflow = Settings.Overflow;
			// zapisanie prędkości
			Settings1.Speed = Settings.Speed;
			// wyświetlenie //info o rozgrywce
			sprintf(Buffer, "Mode:%4d; Speed: %2d/%2d", Settings.Overflow, Settings.Speed, SNAKE_SPEED_MAX);
			TM_ILI9341_Puts(10, SNAKE_TEXT_LINE1, Buffer, &TM_Font_7x10, 0x0000, SNAKE_COLOR_MAIN_BCK);
		}
		// sprawdzenie wyniku
		if (Snake1.Hits != Snake.Hits)
		{
			// zapisanie wyniku
			Snake1.Hits = Snake.Hits;
			// wyświetlenie prędkości
			sprintf(Buffer, "Hits:%4d; Score: %5d", Snake.Hits, (2 - Settings.Overflow) * Snake.Hits * Settings.Speed);
			TM_ILI9341_Puts(10, SNAKE_TEXT_LINE2, Buffer, &TM_Font_7x10, 0x0000, SNAKE_COLOR_MAIN_BCK);
		}
	}
}

// rysowanie pikseli węża
void TM_SNAKE_DrawPixel(uint8_t x, uint8_t y, uint16_t value)
{
	uint16_t color;

	// pozyskanie koloru pixela
	if (value == 0)
	{
		color = SNAKE_COLOR_GAME_BCK; // wyczyszczenie piksela
	}
	else if (value == 1)
	{
		color = SNAKE_COLOR_PIXEL; // ustawienie piksela
	}
	else if (value == 2)
	{
		color = SNAKE_COLOR_TARGET; // ustawienie docelowego piksela
	}
	else if (value == 3)
	{
		color = SNAKE_COLOR_HEAD; // ustawienie głowy węża
	}

	// rysowanie wypełnionego prostokąta
	TM_ILI9341_DrawFilledRectangle(
		SNAKE_BACK_START_X + 2 + x * (SNAKE_PIXEL_SIZE + 1),
		SNAKE_BACK_START_Y + 2 + y * (SNAKE_PIXEL_SIZE + 1),
		SNAKE_BACK_START_X + 1 + x * (SNAKE_PIXEL_SIZE + 1) + SNAKE_PIXEL_SIZE,
		SNAKE_BACK_START_Y + 2 + y * (SNAKE_PIXEL_SIZE + 1) + SNAKE_PIXEL_SIZE,
		color);
}

void TM_SNAKE_PrepareDisplay(void)
{

	TM_ILI9341_Fill(SNAKE_COLOR_MAIN_BCK);
	// rysowanie węrza
	TM_SNAKE_DrawArea();
	// wyświetlenie tekstu
	TM_ILI9341_Puts(40, 5, SNAKE_GAME_TITLE, &TM_Font_7x10, 0x0000, SNAKE_COLOR_MAIN_BCK);
}

void TM_SNAKE_SetFirstOptions(void)
{
	Settings.Speed = SNAKE_SPEED_DEFAULT;
	Settings.Micros = 1000000 / Settings.Speed;
	Settings.Pause = 0;
	Settings.Overflow = 1;
}

void TM_SNAKE_SetDefaultSnake()
{
	uint16_t i;
	// ustawienie dafaultowych ustawień
	Snake.Direction = Snake1.Direction = SNAKE_DIRECTION_RIGHT;
	Snake.LastIndex = 0;
	Snake.Length = 0;
	Snake.Hits = 0;
	// ustawienie defaultowych ustawiń dla snake1
	Snake1.Hits = 255;
	// random pozycję X i Y
	TM_SNAKE_Random(Random);
	Random[0] = 3;
	Random[1] = 3;
	// dodanie pierwszej pozycji do tablicy
	TM_SNAKE_AddToArray(Random);
	// przechowanie wartości
	for (i = 0; i < SNAKE_DEFAULT_LENGTH - 1; i++)
	{
		if (i == (SNAKE_DEFAULT_LENGTH - 2))
		{
			Random[0]++;
		}
		TM_SNAKE_AddToArray(Random);
	}
}

void TM_SNAKE_DeleteFromArray(uint16_t index, int8_t *twobytesarray)
{
	if (index < Snake.Length)
	{
		// zapisanie wartości do usunięcia
		twobytesarray[0] = Snake.Snake[index][0];
		twobytesarray[1] = Snake.Snake[index][1];
		// usunięcie wartości z tablicy o danym indekse
		for (; index < Snake.LastIndex; index++)
		{
			Snake.Snake[index][0] = Snake.Snake[index + 1][0];
			Snake.Snake[index][1] = Snake.Snake[index + 1][1];
		}
		// ostatni indeks
		Snake.LastIndex--;
		Snake.Length--;
	}
}

void TM_SNAKE_AddToArray(int8_t *twobytesarray)
{

	// inkrementacja liczniak i dodanie nowej pos do tablicy
	if (Snake.Length == 0)
	{
		Snake.Length++;
	}
	else
	{
		Snake.LastIndex++;
		Snake.Length++;
	}
	// doanie wartości do tablicy
	Snake.Snake[Snake.LastIndex][0] = twobytesarray[0];
	Snake.Snake[Snake.LastIndex][1] = twobytesarray[1];
}

void TM_SNAKE_ReplaceArray(uint16_t index, int8_t *twobytesarray)
{
	// zamiana wartości tablicy
	Snake.Snake[index][0] = twobytesarray[0];
	Snake.Snake[index][1] = twobytesarray[1];
}

void TM_SNAKE_SpeedUp(void)
{
	// max prędkość 10Hz
	if (Settings.Speed < SNAKE_SPEED_MAX)
	{
		Settings.Speed++;
		Settings.Micros = 1000000 / Settings.Speed;
	}
}

void TM_SNAKE_SpeedDown(void)
{
	// min prędkość 1Hz
	if (Settings.Speed > SNAKE_SPEED_MIN)
	{
		Settings.Speed--;
		Settings.Micros = 1000000 / Settings.Speed;
	}
}

void TM_SNAKE_Random(int8_t *twobytesarray)
{
	float temp;
	// generowanie 1 losowej liczby
	temp = (float)TM_RNG_Get() / (float)0xFFFFFFFF * (SNAKE_PIXELS - 1);
	twobytesarray[0] = (int8_t)temp;
	// generowanie 2 losowej liczby
	temp = (float)TM_RNG_Get() / (float)0xFFFFFFFF * (SNAKE_PIXELS - 1);
	twobytesarray[1] = (int8_t)temp;
}

uint8_t TM_SNAKE_MatchesSnakeLocations(int8_t *twobytesarray)
{
	uint16_t i;
	for (i = 0; i < Snake.Length; i++)
	{
		if (
			Snake.Snake[i][0] == twobytesarray[0] &&
			Snake.Snake[i][1] == twobytesarray[1])
		{
			// wąż udeżył sam siebie
			return 1;
		}
	}
	// wąż nie miał kolizji
	return 0;
}

void TM_SNAKE_GenerateTarget(void)
{
	// losowanie 2 kordynakót nowego cukierka nie będąćych wężu
	do
	{
		// losowanie pozycji X i Y
		TM_SNAKE_Random(Snake_Food);
	} while (TM_SNAKE_MatchesSnakeLocations(Snake_Food));
	// wyświetlenie cukierka na LCD
	TM_SNAKE_DrawPixel(Snake_Food[0], Snake_Food[1], 2);
}

void TM_SNAKE_DrawArea(void)
{
	// wysowanie wypełnionego prostokąta
	TM_ILI9341_DrawFilledRectangle(
		SNAKE_BACK_START_X,
		SNAKE_BACK_START_Y,
		SNAKE_BACK_START_X + SNAKE_PIXELS * (SNAKE_PIXEL_SIZE + 1) + 2,
		SNAKE_BACK_START_Y + SNAKE_PIXELS * (SNAKE_PIXEL_SIZE + 1) + 2,
		SNAKE_COLOR_GAME_BCK);

	// rysowanie krawędzi
	TM_ILI9341_DrawRectangle(
		SNAKE_BACK_START_X,
		SNAKE_BACK_START_Y,
		SNAKE_BACK_START_X + SNAKE_PIXELS * (SNAKE_PIXEL_SIZE + 1) + 2,
		SNAKE_BACK_START_Y + SNAKE_PIXELS * (SNAKE_PIXEL_SIZE + 1) + 2,
		SNAKE_COLOR_BORDER);
}