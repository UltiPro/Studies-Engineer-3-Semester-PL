#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <conio.h>
#include <windows.h>
#include <unistd.h>
#include <list>
#include <fstream>
#include "Bohater.h"

using namespace std;

list<Bohater> lista_bohaterow;

bool sprawdz_czy_puste()
{
    if (lista_bohaterow.empty())
    {
        cout << "Brak bohaterow, wczytaj bohaterow lub dodaj nowych z zakladki menu glowne!" << endl;
        system("pause");
        return true;
    }
    return false;
}

void Wypisz_liste_bohaterow()
{
    system("cls");
    int i = 1;
    for (Bohater b : lista_bohaterow)
    {
        cout << "Postac Nr " << i << " ";
        cout << b.To_String() << endl;
        i++;
    }
}

int wybierz_bohatera()
{
wybierz_poprawnie:
    cout << "Wybierz bohatera:" << endl;
    Wypisz_liste_bohaterow();
    int wybor;
    cout << "Twoj wybor: ";
    wybor = getch();
    if (wybor < 49 || wybor > (48 + lista_bohaterow.size()))
    {
        system("cls");
        cout << "Nie ma takiego Bohatera! Wybierz innego!" << endl;
        system("pause");
        goto wybierz_poprawnie;
    }
    return wybor;
}

void Zapisz()
{
    fstream plik;
    plik.open("bohaterzy.txt", ios::in | ios::out | ios::trunc);

    if (plik.good() == 0)
    {
        throw runtime_error("Blad otwarcia pliku!");
    }

    for (Bohater b : lista_bohaterow)
    {
        plik << b.To_String() << endl;
    }

    plik.close();
}

void Wczytaj()
{
    fstream plik;
    plik.open("bohaterzy.txt", ios::in | ios::out | ios::app);

    if (plik.good() == 0)
    {
        throw runtime_error("Blad otwarcia pliku!");
    }

    while (!plik.eof())
    {
        string imie, rasa, klasa, plec;
        int poziom, hp, sila, inteligencja, zrecznosc;

        plik >> imie;
        plik >> rasa;
        plik >> klasa;
        plik >> plec;
        plik >> poziom;
        plik >> hp;
        plik >> sila;
        plik >> inteligencja;
        plik >> zrecznosc;

        if (imie != "")
            lista_bohaterow.push_back(Bohater(imie, rasa, klasa, plec, poziom, hp, sila, inteligencja, zrecznosc));
    }
}

void Awansuj_Bohatera()
{
    system("cls");
    if (sprawdz_czy_puste())
        return;
    int wybor = wybierz_bohatera();
    system("cls");
    int ile_poziomow;
    cout << "Ile poziomow ma awansowac postac: ";
    cin >> ile_poziomow;
    auto element = lista_bohaterow.begin();
    advance(element, wybor - 49);
    Bohater b = *element;
    b.Awansuj(ile_poziomow);
    *element = b;
}

void Zmien_Imie()
{
    system("cls");
    if (sprawdz_czy_puste())
        return;
    int wybor = wybierz_bohatera();
    system("cls");
    string new_imie;
    cout << "Nowe imie dla Bohatera: ";
    cin >> new_imie;
    auto element = lista_bohaterow.begin();
    advance(element, wybor - 49);
    Bohater b = *element;
    b.imie = new_imie;
    *element = b;
}

void Edycja_Swiata()
{
    int wybor;
    bool in_action = true;

    while (in_action)
    {
        system("cls");

        cout << "MENU EDYCJI SWIATA" << endl;
        cout << "--------------------" << endl;
        cout << "1. Awansuj Bohatera" << endl;
        cout << "2. Zmien Imie Bohatera" << endl;
        cout << "9. Wyjdz do menu glownego" << endl;

        wybor = getch();

        switch (wybor)
        {
        case 49:
            Awansuj_Bohatera();
            break;
        case 50:
            Zmien_Imie();
            break;
        case 57:
            in_action = false;
            break;
        default:
        {
            for (int i = 3; i > 0; i--)
            {
                system("cls");
                cout << "Nie ma takiej opcji edycji swiata! Program odswiezy sie za " << i << " sekund" << endl;
                sleep(1);
            }
            break;
        }
        }
    }
}

int main()
{
    bool in_action = true;
    bool allow_to_read = true;

    int wybor;

    while (in_action)
    {
        system("cls");

        cout << "MENU GLOWNE" << endl;
        cout << "--------------------" << endl;
        cout << "1. Dodaj bohatera" << endl;
        cout << "2. Wypisz liste bohaterow" << endl;
        cout << "3. Zapisz postacie" << endl;
        cout << "4. Wczytaj postacie" << endl;
        cout << "5. Edytor swiata" << endl;
        cout << "9. Wyjdz z programu" << endl;

        wybor = getch();

        switch (wybor)
        {
        case 49:
            lista_bohaterow.push_back(Bohater::Dodaj());
            break;
        case 50:
            Wypisz_liste_bohaterow();
            system("pause");
            break;
        case 51:
            Zapisz();
            break;
        case 52:
            if (allow_to_read)
            {
                Wczytaj();
                allow_to_read = false;
            }
            else
            {
                system("cls");
                cout << "Nie mozna wczytac dwukrotnie danych!" << endl;
                system("pause");
            }
            break;
        case 53:
            Edycja_Swiata();
            break;
        case 57:
            in_action = false;
            break;
        default:
        {
            for (int i = 3; i > 0; i--)
            {
                system("cls");
                cout << "Nie ma takiej opcji w menu! Program odswiezy sie za " << i << " sekund" << endl;
                sleep(1);
            }
            break;
        }
        }
    }

    return 0;
}