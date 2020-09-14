#ifndef TABLEAU_INCLUDED
#define TABLEAU_INCLUDED

template <typename T, int AGRANDISSEMENT>
class Tableau
{
    private:
        T* tab;
        int size;
        int capacite;
    public:
        Tableau(int size): tab(new T[(size/AGRANDISSEMENT + 1)*AGRANDISSEMENT]),
                            size(0),
                            capacite((size/AGRANDISSEMENT + 1)*AGRANDISSEMENT){}
        ~Tableau(){ delete tab; }
        T* getTab();
        int getSize(){ return size; }
        int getCapacite(){ return capacite; }
        void add(T elem)
        {
            tab[size++] = elem;
            if (size == capacite)
            {
                capacite += AGRANDISSEMENT;
                T* newTab = new T[capacite];
                for (int i = 0; i < size; i++)
                {
                    newTab[i] = tab[i];
                }
                tab = newTab;
            }
        }
        T get(int i)
        {
            return tab[i];;
        }
};

#endif // TABLEAU_INCLUDED
