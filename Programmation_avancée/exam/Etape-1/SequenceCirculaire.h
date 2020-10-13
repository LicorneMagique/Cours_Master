#include <iostream>

template <typename T>
class SequenceCirculaire
{
private:
    T *ad;
    int p;
    int capacite;

public:
    SequenceCirculaire(int cap, T v) : ad(new T[cap]), p(0), capacite(cap)
    {
        for (int i = 0; i < cap; i++)
        {
            ad[i] = v;
        }
    }
    SequenceCirculaire(const SequenceCirculaire<T> &s) : ad(new T[s.capacite]), p(s.p), capacite(s.capacite)
    {
        for (int i = 0; i < capacite; i++)
        {
            ad[i] = s.ad[i];
        }
    }
    SequenceCirculaire operator=(const SequenceCirculaire<T> &s)
    {
        return SequenceCirculaire(s);
    }
    ~SequenceCirculaire()
    {
        delete ad;
    }
    void affiche()
    {
        std::cout << "p = " << p << ", capacité = " << capacite << ", liste = ";
        for (int i = 0; i < capacite; i++)
        {
            std::cout << ad[i] << " ";
        }
        std::cout << std::endl;
    }
    void insere(int index, T elem)
    {
        if (index >= capacite) // Si l'index est plus grand que la séquence on
        {                      // augmente la taille
            capacite *= 2;
            T *newTab = new T[capacite];
            for (int i = 0; i < p; i++)
            {
                newTab[i] = ad[i];
                // mettre valeur ?
            }
            delete ad;
            ad = newTab;
        }
        ad[index] = elem;
        p++;
    }
    T operator[](signed int index)
    {
        return ad[index];
    }
    int recherche(const T elem)
    {
        for (int i = 0; i < capacite; i++)
        {
            if (elem == ad[i])
            {
                return i;
            }
        }
        return -1;
    }
};
