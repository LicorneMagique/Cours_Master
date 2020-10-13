#include <iostream>
#include <cstdlib>
#include "SequenceCirculaire.h"

int main()
{
    std::cout << "Hello World" << std::endl;
    SequenceCirculaire<double> c(3, 5.5);
    c.affiche();
    c.insere(0, 0.0);
    c.insere(2, 3.0);
    SequenceCirculaire<double> c2(c);
    c.insere(4, 4.0);
    c.affiche();
    c2.affiche();
    std::cout << "test ad[2] = " << c[2] << std::endl;
    std::cout << "test ad[1] = " << c[1] << std::endl;

    SequenceCirculaire<double> cercle(10, 5.5); // sequence de période 10,
        // avec des éléments de valeur 5.5
    SequenceCirculaire<double> cercle2(cercle);
    cercle.affiche();
    // Affichage
    for (int i = 0; i < 30; i++)
        cercle.insere(i, i * 0.5);
    cercle.affiche();
    cercle = cercle2;
    //for (int i = 0; i < 30; i++)
    //  cercle[i] = i * 0.3;
    cercle.affiche();
    cercle = cercle2;
    double elem = rand() % 10 + 0.1; // #include<cstdlib>
    while (cercle.recherche(elem) != -1)
    {
        cercle.insere(0, elem);
        elem = rand() % 10 + 0;
        1;
    }
    return 0;
}
