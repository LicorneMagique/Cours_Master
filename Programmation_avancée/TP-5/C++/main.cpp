#include <iostream>
#include <cstring>
#include "Tableau.h"

using namespace std;

template<typename T>
void mySwap(T& a, T& b)
{
    T temp = a;
    a = b;
    b = temp;
}

template<typename T>
const T myMin(T const & a, T const & b)
{
    if (a < b) return a;
    return b;
}

template<>
char* const myMin(char* const & a, char* const & b)
{
    if (strcmp(a, b) <= 0) return a;
        return b;
}

int main()
{
    cout << "Hello World" << endl;

    cout << "min entre a et b : " << myMin<char>('a', 'b') << endl;

    cout << "min entre 5 et 6 : " << myMin<int>(5, 6) << endl;
    cout << "min entre 6 et 5 : " << myMin<int>(6, 5) << endl;
    cout << "min entre lili et lala : " << myMin<char*>((char*) "lili", (char*) "lala") << endl;
    cout << "min entre li et lala : " << myMin<char*>((char*) "li", (char*) "lala") << endl; // 2 arguments de types différents
    const char* cc = "mumu";
    const char* dd = "ma";
    cout << "min entre cc=mumu et dd=ma : " << myMin<const char*>(cc, dd) << endl;
    char ee[5] = "toto";
    char ff[5] = "ta"; // tableau de même taille que le précédent
    cout << "min entre ee=toto et ff=ta : " << myMin<char*>(ee, ff) << endl;
    cout << "min entre zut et ff=ta : " << myMin<char*>((char*) "zut", ff) << endl;

    Tableau<int, 2> lalalala = Tableau<int, 2>(4);
    cout << "size : " << lalalala.getSize() << endl;
    cout << "capacité : " << lalalala.getCapacite() << endl;
    for (int i = 0; i < 7; i++)
    {
        lalalala.add(i);
    }
    cout << "size : " << lalalala.getSize() << endl;
    cout << "size : " << lalalala.getCapacite() << endl;
    for (int i = 0; i < 7; i++)
    {
        cout << "val : " << lalalala.get(i) << endl;
    }

    return 0;
}
