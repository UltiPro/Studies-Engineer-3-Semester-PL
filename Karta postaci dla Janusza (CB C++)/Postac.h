#include <string>

using namespace std;

class Postac
{
    int poziom;
    int hp;
    int sila;
    int inteligencja;
    int zrecznosc;

    public:
        Postac();
        Postac(int,int,int,int,int);
        virtual ~Postac() = 0;
        string To_String();
        void Awansuj(int,string);
};
