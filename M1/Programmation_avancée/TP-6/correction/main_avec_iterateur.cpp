#include <iostream>
#include "tableau_avec_iterateur.h"

int main()
{
    Tableau<int,6> A(5);
    Tableau<int,4> B(8);
    std::cout << A.taille() << " " << B.taille() << std::endl;
    std::cout << A.capacite() << " " << B.capacite() << std::endl;
    std::cin >> A >> B;
    std::cout << A+B << std::endl;
    A.ajoute(6);
    std::cout << A.taille() << " " << B.taille() << std::endl;
    std::cout << A.capacite() << " " << B.capacite() << std::endl;
    std::cout << A << std::endl;
    Tableau<int,6> C(B);
    std::cout << C << std::endl;
    A=B;
    std::cout << A << std::endl;
    std::cout << Tableau<int,6>::nb_instances() << std::endl;
    Tableau<int,6>::iterator it=A.begin();
    Tableau<int,6>::iterator ite=A.end();

    //for(;operator!=<int,6>(it,ite);++it)
    for(;it!=ite;++it)
    {
        std::cout << *it << std::endl;
    }
    return 0;
}
