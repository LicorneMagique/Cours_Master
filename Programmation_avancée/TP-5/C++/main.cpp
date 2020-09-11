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
    if (T == char)
    {
        if (strcmp(a, b) <= 0) return a;
        return b;
    }

    if (a < b) return a;
    return b;
}

template<>
const myMin(char* const & a, char* const & b)
{
    if (strcmp(a, b) <= 0) return a;
        return b;
}

int main()
{
    cout << "Hello World" << endl;

    int a = 5;
    int b = 6;
    cout << a << " " << b << endl;
    mySwap<int>(a, b);
    cout << a << " " << b << endl;
    cout << "Swap validé" << endl << endl;

    cout << "min entre " << a << " et " << b << " : " << myMin<int>(a, b) << endl;
    cout << "min entre a et b : " << myMin<char>('a', 'b') << endl;
    cout << "myMin validé" << endl << endl;

    // std::cout << min(5, 6) << std::endl;
    // std::cout << min(6, 5) << std::endl;
    // std::cout << min("lili", "lala") <<std::endl;
    // std::cout << min("li","lala") << std::endl; // 2 arguments de types différents
    // const char* cc = "mumu";
    // const char* dd = "ma";
    // std::cout << min(cc, dd) << std::endl;
    // char ee[5] = "toto";
    // char ff[5] = "ta"; // tableau de même taille que le précédent
    // std::cout << min(ee,ff) << std::endl;
    // std::cout << min("zut",ff) << std::endl;

    return 0;
}
