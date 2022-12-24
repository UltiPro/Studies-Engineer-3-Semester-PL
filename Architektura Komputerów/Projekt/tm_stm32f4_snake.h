
#ifndef TM_SNAKE_H
#define TM_SNAKE_H 110

/* C++ detection */
#ifdef __cplusplus
extern C {
#endif

/**
 * Includes
 */
#include "stm32f4xx.h"
#include "defines.h"
#include "tm_stm32f4_delay.h"
#include "tm_stm32f4_disco.h"
#include "tm_stm32f4_rng.h"
#include "tm_stm32f4_ili9341_ltdc.h"
#include "tm_stm32f4_usb_hid_host.h"

#define SNAKE_GAME_TITLE		"Snake Game"
	
/* kolor gry */
#define SNAKE_COLOR_BORDER		ILI9341_COLOR_BLACK
#define SNAKE_COLOR_MAIN_BCK	ILI9341_COLOR_BLUE2
#define SNAKE_COLOR_GAME_BCK	ILI9341_COLOR_GREEN2
#define SNAKE_COLOR_PIXEL		ILI9341_COLOR_BROWN
#define SNAKE_COLOR_TARGET		ILI9341_COLOR_BLACK
#define SNAKE_COLOR_HEAD		ILI9341_COLOR_RED

//rozmiar snake na LCD
#define SNAKE_PIXELS			39
#define SNAKE_PIXEL_SIZE		5	// rozmiar w pikselach jednej czści węża 
#define SNAKE_BACK_START_X		1	// kordynat X startu 
#define SNAKE_BACK_START_Y		20	// kordynat Y startu 

#define SNAKE_DEFAULT_LENGTH	8	// Default długość węża 

#define SNAKE_SPEED_MAX			15	// 15Hz max V 
#define SNAKE_SPEED_MIN			1	// 1Hz min V 
#define SNAKE_SPEED_DEFAULT		5	// Default speed w Hz 

//kordynaty węża
#define SNAKE_DIRECTION_LEFT	0
#define SNAKE_DIRECTION_RIGHT	1
#define SNAKE_DIRECTION_UP		2
#define SNAKE_DIRECTION_DOWN	3

// przyciski klawaitury
#define SNAKE_KEY_LEFT			((uint8_t) 'a')	// 'a' 
#define SNAKE_KEY_RIGHT			((uint8_t) 'd')	// 'd' 
#define SNAKE_KEY_UP			((uint8_t) 'w')	// 'w' 
#define SNAKE_KEY_DOWN			((uint8_t) 's')	// 's' 
#define SNAKE_KEY_SPEED_UP		((uint8_t) 'u')	// 'u' 
#define SNAKE_KEY_SPEED_DOWN	((uint8_t) 'i')	// 'i' 
#define SNAKE_KEY_PAUSE			((uint8_t) 'p')	// 'p' 
#define SNAKE_KEY_RESET			((uint8_t) 'r')	// 'r' 
#define SNAKE_KEY_OVERFLOW		((uint8_t) 'm')	// 'm' 

//lokalizacja tekstu
#define SNAKE_TEXT_LINE1		265		
#define SNAKE_TEXT_LINE2		285
#define SNAKE_TEXT_LINE3		305

typedef struct {
	int8_t Snake[SNAKE_PIXELS * SNAKE_PIXELS][2];
	uint16_t Length;
	uint16_t LastIndex;
	uint8_t Direction;
	uint16_t Hits;
} TM_SNAKE_t;

typedef struct {
	uint8_t Overflow;
	uint8_t Speed;
	uint32_t Micros;
	uint8_t Pause;
} TM_SNAKE_Settings_t;

void TM_SNAKE_Start(void);

/* C++ detection */
#ifdef __cplusplus
}
#endif

#endif
