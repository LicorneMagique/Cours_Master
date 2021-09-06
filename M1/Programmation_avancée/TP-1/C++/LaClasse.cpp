#include <iostream>

class Pixel
{
    public:
        Pixel(): x(0), y(0), z(0){}
        int getX()
        {
            return x;
        }
        int getY()
        {
            return y;
        }
        int getZ()
        {
            return z;
        }
        void setX(int newX)
        {
            x = newX;
        }
        void setY(int newY)
        {
            y = newY;
        }
        void setZ(int newZ)
        {
            z = newZ;
        }

    private:
        int x;
        int y;
        int z;
};

class Image
{
    public:
        Image(int _w, int _h): w(_w), h(_h)
        {
            pixels = new Pixel[h*w];
            setPixels(0, 0, 0);
        }
        Pixel getPixel(int _w, int _y)
        {
            return pixels[_y*h + _w];
        }
        void setPixels(int x, int y, int z)
        {
            for (int i = 0; i < w*h; i++)
            {
                pixels[i].setX(x);
                pixels[i].setY(y);
                pixels[i].setZ(z);
                std::cout << x << " " << y << " " << z << std::endl;
            }
        }
    private:
        int w;
        int h;
        Pixel* pixels;
};

class LaClasse
{
    public :
        // Construction, conversion, affectation et destruction
        LaClasse(): l(0) // Constructeur par défaut
        {
            std::cout << "défaut\n";
        }

        LaClasse(const LaClasse& lc): l(lc.l) // Constructeur par copie
        {
            std::cout << "copie\n";
        }

        LaClasse(int i): l(i) // Constructeur avec paramètre int
        {
            std::cout << "int\n";
        }

        operator bool() const // `if (lc)` atteindra le bloc `then` avec lc: LaClasse
        {
            std::cout << "bool\n";
            return true;
        }

        ~LaClasse() // Destructeur
        {
            std::cout << "destructeur\n";
        }

        const LaClasse& operator=(const LaClasse& c) // Constructeur par affectation
        {
            l = c.l;
            std::cout << "affectation\n";
            return *this;
        }

        // Autre fonction membre
        LaClasse F(LaClasse);

        // Déclaration fonction extérieure amie
        friend std::ostream & operator << (std::ostream & os, const LaClasse & lc);

    private :
        int l;
};

LaClasse F(LaClasse vv)
{
    std::cout << " in F \n";
    return 8;
}

LaClasse LaClasse::F(LaClasse v)
{
    std::cout << " in LaClasse::F \n";
    return ::F(v);
}

std::ostream & operator << (std::ostream & os, const LaClasse & lc)
{
    os << " in ostream << LaClasse "<< lc.l << std::endl;
    return os;
}

// Testez et analysez la s�quence d'appels aux fonctions membres
// de LaClasse dans le programme suivant :

int main()
{
    LaClasse c1; // défaut
    LaClasse c2 = LaClasse(); // défaut indiqué explicitement
    LaClasse cc1(c1); // copie
    LaClasse cc2 = c1; // copie indiqué explicitement
    LaClasse cc3 = LaClasse(c1); // défaut puis affectation
    LaClasse cv1(5); // int
    LaClasse cv2 = 5; // défaut puis int
    LaClasse cv3 = LaClasse(5); // défaut puis int
    LaClasse cv4 = (LaClasse)5; // défaut puis int
    std::cout << std::endl;
    c1 = cc1;
    std::cout << std::endl;
    c2 = 8;
    std::cout << std::endl;
    if (cv1)
    {
        cv1 = F(10);
        cv1 = F(c1);
        cv1 = c1.F(c2);
    }
    std::cout << "Tableaux \n";
    LaClasse tab[3];
    LaClasse *pc = new LaClasse(tab[0]);
    delete pc;
    std::cout << "Avant de sortir ... \n";
    Pixel p;
    std::cout << "test " << p.getX() << " " << p.getY() << " " << p.getZ() << std::endl;
    Image img = Image(2, 3);
    return 0;
}
