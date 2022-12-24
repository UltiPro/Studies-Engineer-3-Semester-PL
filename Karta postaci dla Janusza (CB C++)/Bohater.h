#include "Postac.h"
#include <string>

using namespace std;

class Bohater : public Postac
{
    string rasa;
    string klasa;
    string imie;
    string plec;

    public:
        Bohater();
        Bohater(int,int,int,string);
        Bohater(string,string,string,string,int,int,int,int,int);
        ~Bohater() override;
        static Bohater Dodaj();
        string To_String();
        void Awansuj(int);
        friend void Zmien_Imie();
};
