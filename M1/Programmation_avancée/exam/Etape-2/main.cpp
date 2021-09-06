#include <iostream>
#include <cstdlib>
#include "SequenceCirculaire.h"

int main()
{
    std::cout << "Hello World" << std::endl;
    SequenceCirculaire<double> cercle(10,5.5);
    cercle.affiche();
    for (int i = 0; i < 10; i++)
        cercle.insere(i, i * 0.1);
    cercle.affiche();
    Circulateur<double> circ(cercle, 5); //circ initialisé sur l’emplacement 5 de cercle
    Circulateur<double> circend(cercle, 4);
    for(; circ != circend; circ++)
            circ.affiche();
    cercle.affiche();
    // circ = cercle.makeCirculateur(0);
    // for (int i = 0; i < 20; i++)
    // {
    //     *circ = i + 0.2;
    //     ++circ;
    // }
    // std::cout << cercle << std::endl;
    return 0;
}
