#include <iostream>
#include <stdio.h>
#include <string.h>

class Generateur
{
    public:
        Generateur(int n): nombre(n), occ(1)
        {
        }

        int getNext()
        {
            return occ++ * nombre;
        }

    private:
        int nombre;
        int occ;
};

int main()
{
    Generateur g(3);
    for (int i = 0; i < 10; i++)
    {
        std::cout << g.getNext() << std::endl;
    }
    return 0;
}
