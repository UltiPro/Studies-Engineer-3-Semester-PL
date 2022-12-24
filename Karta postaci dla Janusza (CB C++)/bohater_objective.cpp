#include <iostream>
#include <conio.h>
#include <string>
#include <unistd.h>
#include "Bohater.h"

using namespace std;

Bohater::Bohater() : Postac()
{
    this->rasa = "Czlowiek";
    this->klasa = "Krasnolud";
    this->imie = "Janusz";
    this->plec = "Male";
}

Bohater::Bohater(int rasa, int klasa, int plec, string imie) : Postac()
{
    switch(rasa)
    {
        case 49: this->rasa = "Czlowiek"; break;
        case 50: this->rasa = "Krasnolud"; break;
        case 51: this->rasa = "Ork"; break;
        case 52: this->rasa = "Elf"; break;
    }
    switch(klasa)
    {
        case 49: this->klasa = "Wojownik"; break;
        case 50: this->klasa = "Mag"; break;
        case 51: this->klasa = "Lowca"; break;
        case 52: this->klasa = "Norbert"; break;
    }
    switch(plec)
    {
        case 49: this->plec = "Male"; break;
        case 50: this->plec = "Female"; break;
    }
    this->imie = imie;
}

Bohater::Bohater(string imie, string rasa, string klasa, string plec, int poziom, int hp,int sila, int inteligencja, int zrecznosc) : Postac(poziom,hp,sila,inteligencja,zrecznosc)
{
    this->imie = imie;
    this->rasa = rasa;
    this->klasa = klasa;
    this->plec = plec;
}

Bohater::~Bohater()
{
    //cout<<"Usuwanie Obiektu\n";
}

Bohater Bohater::Dodaj()
{
    rasa_goto:

    system("cls");

    cout<<"Wybierz Rase:"<<endl;
    cout<<"1. Czlowiek"<<endl;
    cout<<"2. Krasnolud"<<endl;
    cout<<"3. Ork"<<endl;
    cout<<"4. Elf"<<endl;

    int rasa = getch();
    if(rasa!=49&&rasa!=50&&rasa!=51&&rasa!=52)
    {
        for(int i=3;i>0;i--)
        {
            system("cls");
            cout<<"Nie ma takiej opcji rasy! Program odswiezy sie za "<<i<<" sekund"<<endl;
            sleep(1);
        }
        goto rasa_goto;
    }

    klasa_goto:

    system("cls");

    cout<<"Wybierz Klase:"<<endl;
    cout<<"1. Wojownik"<<endl;
    cout<<"2. Mag"<<endl;
    cout<<"3. Lowca"<<endl;
    cout<<"4. Norbert"<<endl;

    int klasa = getch();
    if(klasa!=49&&klasa!=50&&klasa!=51&&klasa!=52)
    {
        for(int i=3;i>0;i--)
        {
            system("cls");
            cout<<"Nie ma takiej opcji klasy! Program odswiezy sie za "<<i<<" sekund"<<endl;
            sleep(1);
        }
        goto klasa_goto;
    }

    plec_goto:

    system("cls");

    cout<<"Wybierz Plec:"<<endl;
    cout<<"1. Male"<<endl;
    cout<<"2. Female"<<endl;

    int plec = getch();
    if(plec!=49&&plec!=50)
    {
        for(int i=3;i>0;i--)
        {
            system("cls");
            cout<<"Nie ma takiej opcji plci! Program odswiezy sie za "<<i<<" sekund"<<endl;
            sleep(1);
        }
        goto plec_goto;
    }

    system("cls");

    // obsluga bledu postaci zROBIC

    cout<<"Podaj imie postaci: ";
    string imie;
    cin>>imie;

    return Bohater(rasa,klasa,plec,imie);
}

string Bohater::To_String()
{
    string _rasa(rasa);
    string _klasa(klasa);
    string _plec(plec);
    string s=imie+" "+_rasa+" "+_klasa+" "+_plec+" "+Postac::To_String();
    return s;
}

void Bohater::Awansuj(int _poziom)
{
    Postac::Awansuj(_poziom,klasa);
}
