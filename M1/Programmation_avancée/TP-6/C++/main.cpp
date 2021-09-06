#include <iostream>
#include "Tableau.h"

int main()
{
    Tableau<int, 6> a(5);
    std::cout << a.get(2);
    // TableauIt<int, 6> it = a.begin();
    // TableauIt<int, 6> ite = a.end();
    // for (; it != ite; ++it)
    //     std::cout << *it << std::endl;
    return 0;
}
