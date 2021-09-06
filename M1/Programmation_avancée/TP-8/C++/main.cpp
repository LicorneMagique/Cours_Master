#include <iostream>
#include "Tableau.h"

/* Partie factorielle */
// template <int N>
// inline double Factorielle()
// {
//     return N * Factorielle<N - 1>();
// }
// template <>
// inline double Factorielle<0>()
// {
//     return 1.0;
// }
// constexpr double factorial(int n)
// {
//     return n <= 1 ? 1 : (n * factorial(n - 1));
// }
template <unsigned int N>
struct Factorielle
{
    enum
    {
        valeur = N * Factorielle<N - 1>::valeur
    };
};
template <>
struct Factorielle<0>
{
    enum
    {
        valeur = 1
    };
};
/* Partie factorielle */

template <typename TL>
struct Length;
template <typename T1, typename TL>
struct Length<TypeList<T1, TL>>
{
    enum
    {
        valeur = 1 + Length<TL>::valeur
    };
};
template <>
struct Length<NullType>
{
    enum
    {
        valeur = 0
    };
};

/*
- Length<typename TL>
- IndexOf<typename TL, typename T>
- TypeAt<typename TL, int N>
- Union<typename TL1, typename TL2>
*/

int main()
{

    std::cout << Factorielle<4>::valeur << std::endl;
    TypeList<int, TypeList<double, TypeList<short, NullType>>> test;
    std::cout << Length<test>::valeur << std::endl;

    return 0;
}
