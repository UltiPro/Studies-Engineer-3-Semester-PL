#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool comparator (int i,int j) { return (i<j); }
bool comparator2 (int i,int j) { return (i>j); }
bool comparator3 (int i,int liczba1) { return (i>liczba1); }
bool comparator4 (int i,int liczba1) { return (i>liczba1); }

int main()
{
    int n=7;
    int liczby[] = {32,71,12,45,26,80,53,32};

    sort(liczby,liczby+8,comparator);

    for(int i=0;i<n;i++)
    {
        cout<<liczby[i]<<" ";
    }

    cout<<"\n";

    sort(liczby,liczby+8,comparator2);

    for(int i=0;i<n;i++)
    {
        cout<<liczby[i]<<" ";
    }

    cout<<"\n";

    int liczba1 = 46;
    int liczba2 = 45;

    sort(liczby,liczby+8,comparator);

    if(binary_search(liczby,liczby+8,liczba1)) cout<<"Jest liczba "<<liczba1; 
    else cout<<"Nie ma liczby "<<liczba1;

    cout<<"\n";

    if(binary_search(liczby,liczby+8,liczba2)) cout<<"Jest liczba "<<liczba2; 
    else cout<<"Nie ma liczby "<<liczba2;

    cout<<"\n";
    int liczba3=20,liczba4=50;

    auto count = std::count_if(liczby, liczby+8,
    [liczba3, liczba4](int32_t n){
        if(liczba3 <= n && liczba4 >= n)
            return true;
        else
            return false;
    });

    cout<<count;

    cout<<"\n";

    //zad 2

    int liczby1[]={12,26,32,32,45,53,71,80};
    int liczby2[]={13,18,44,53,55,75,88,99};
    vector<int> wspolne(8);
    vector<int> wynik(16);
 
    sort(liczby1, liczby1+8);
    sort(liczby2, liczby2+8);
 
    merge(liczby1, liczby1+8, liczby2, liczby2+8, wynik.begin());
 
    set_intersection(liczby1, liczby1+8, liczby2, liczby2+8, wspolne.begin());
 
    for(int i=0;i<16;i++)
    {
        cout<<wynik[i]<<" ";
    }

    cout<<"\n";
 
    for(int i=0;i<wspolne.capacity();i++)
    {
        cout<<wspolne[i]<<" ";
    }

    return 0;
}