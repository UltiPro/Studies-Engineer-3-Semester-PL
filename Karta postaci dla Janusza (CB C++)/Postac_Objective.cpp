#include <iostream>
#include <conio.h>
#include <string>
#include <unistd.h>
#include "Postac.h"

Postac::Postac()
{
    poziom = 1;
    hp = 100;
    sila = 10;
    inteligencja = 10;
    zrecznosc = 10;
}

Postac::Postac(int poziom, int hp, int sila, int inteligencja, int zrecznosc)
{
    this->poziom = poziom;
    this->hp = hp;
    this->sila = sila;
    this->inteligencja = inteligencja;
    this->zrecznosc = zrecznosc;
}

Postac::~Postac() {}

string Postac::To_String()
{
    string s = to_string(poziom) + " " + to_string(hp) + " " + to_string(sila) + " " + to_string(inteligencja) + " " + to_string(zrecznosc);
    return s;
}

void Postac::Awansuj(int _poziom, string _klasa)
{
    poziom += _poziom;
    if (_klasa == "Wojownik")
    {
        hp = (1 + (_poziom * 0, 25)) * hp;
        sila += (_poziom * 3);
        inteligencja += (_poziom * 1);
        zrecznosc += (_poziom * 2);
    }
    else if (_klasa == "Mag")
    {
        hp = (1 + (_poziom * 0, 10)) * hp;
        sila += (_poziom * 1);
        inteligencja += (_poziom * 3);
        zrecznosc += (_poziom * 1);
    }
    else if (_klasa == "Lowca")
    {
        hp = (1 + (_poziom * 0, 15)) * hp;
        sila += (_poziom * 2);
        inteligencja += (_poziom * 1);
        zrecznosc += (_poziom * 3);
    }
    else if (_klasa == "Norbert")
    {
        hp = (1 + (_poziom * 0, 7)) * hp;
        sila += (_poziom * 5);
        inteligencja += (_poziom * 0, 5);
        zrecznosc += (_poziom * 3);
    }
    else
    {
        hp += 1;
        sila += 1;
        inteligencja += 1;
        zrecznosc += 1;
    }
}