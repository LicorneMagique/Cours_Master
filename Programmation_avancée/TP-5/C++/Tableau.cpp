#include "Tableau.h"

template <class T, int AGRANDISSEMENT>
T* Tableau<T, AGRANDISSEMENT>::getTab()
{
    return tab;
}

//template <class T, int AGRANDISSEMENT>
//void Tableau<T, AGRANDISSEMENT>::add(T elem)
//{
    // tab[size++] = elem;
    // if (size == capacite)
    // {
    //     capacite += AGRANDISSEMENT;
    //     T* newTab(capacite);
    //     for (int i = 0; i < size; i++)
    //     {
    //         newTab[i] = tab[i];
    //     }
    //     tab = newTab;
    // }
//}
