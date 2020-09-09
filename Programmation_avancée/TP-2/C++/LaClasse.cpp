#include <iostream>
#include <stdio.h>
#include <string.h>

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
                // std::cout << x << " " << y << " " << z << std::endl;
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
            i = new Image(2, 3);
        }

        LaClasse(const LaClasse& lc): l(lc.l) // Constructeur par copie
        {
            std::cout << "copie\n";
            i = new Image(2, 3);
        }

        LaClasse(int i): l(i) // Constructeur avec paramètre int
        {
            std::cout << "int\n";
            this->i = new Image(2, 3);
        }

        const LaClasse& operator=(const LaClasse& c) // Constructeur par affectation
        {
            l = c.l;
            std::cout << "constructeur par affectation\n";
            return *this;
        }

        operator bool() const // `if (lc)` atteindra le bloc `then` avec lc: LaClasse
        {
            std::cout << "bool\n";
            return true;
        }

        ~LaClasse() // Destructeur
        {
            std::cout << "destructeur\n";
            delete i;
        }

        const LaClasse& operator=(LaClasse &&x) // Affectation par déplacement
        {
            std::cout << "affectation par déplacement\n";
            if (this != &x)
            {
                delete i;
                i = x.i;
                x.i = nullptr;
            }
            return *this;
        }

        LaClasse(LaClasse&& lc): l(lc.l) // Constructeur par déplacement
        {
            std::cout << "constructeur par déplacement" << std::endl;
            i = lc.i;
            lc.i = nullptr;
        }

        //Autre fonction membre
        LaClasse F(LaClasse);

        // Déclaration fonction extérieure amie
        friend std::ostream & operator << (std::ostream & os, const LaClasse & lc);

    private :
        int l;
        Image* i;
};

class LaClasseSpecialisee: LaClasse
{
    public:
        LaClasseSpecialisee() // Constructeur par défaut
        {
            std::cout << "Constructeur défaut LaClasseSpecialisee\n";
        }

        LaClasseSpecialisee(const LaClasseSpecialisee& lc) // Constructeur par copie
        {
            std::cout << "Constructeur copie LaClasseSpecialisee\n";
        }

        const LaClasseSpecialisee& operator=(const LaClasseSpecialisee& c) // Constructeur par affectation
        {
            std::cout << "Constructeur affectation LaClasseSpecialisee\n";
            return *this;
        }

        ~LaClasseSpecialisee() // Destructeur
        {
            std::cout << "Destructeur LaClasseSpecialisee\n";
        }
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

class String
{
    public:
        String() // Constructeur par défaut
        {
            std::cout << "Constructeur par défaut" << std::endl;
            string = new char[0];
        }

        String(char* chars)
        {
            std::cout << "Constructeur par valeur" << std::endl;
            string = new char[strlen(chars)];
            for (int i = 0; i < strlen(chars); i++) {
                string[i] = chars[i];
            }
        }

        String(char c)
        {
            string = new char[1];
            string[0] = c;
        }

        String(const String& s)
        {
            string = new char[strlen(s.string)];
            for (int i = 0; i < strlen(s.string); i++)
            {
                string[i] = s.string[i];
            }
        }

        String operator+(const String& s)
        {
            std::cout << "je dois renvoyer : '" << string << s.string << "'" << std::endl;
            int size = strlen(string) + strlen(s.string);
            char* newString = new char[size];
            for (int i = 0; i < size; i++)
            {
                if (i < strlen(string))
                {
                    newString[i] = string[i];
                }
                else
                {
                    newString[i] = s.string[i - strlen(string)];
                }
            }
            return newString;
        }

        const bool operator==(const String& s)
        {
            return strcmp(string, s.string) == 0;
        }

        const bool operator!=(const String& s)
        {
            return strcmp(string, s.string) != 0;
        }

        const bool operator<(const String& s)
        {
            return strcmp(string, s.string) < 0;
        }

        const bool operator>(const String& s)
        {
            return strcmp(string, s.string) > 0;
        }

        const bool operator<=(const String& s)
        {
            return strcmp(string, s.string) <= 0;
        }

        const bool operator>=(const String& s)
        {
            return strcmp(string, s.string) >= 0;
        }

        ~String()
        {
            std::cout << "Destructeur" << std::endl;
            delete string;
        }

        char* getValue()
        {
            return string;
        }
    private:
        char* string;
};

// Testez et analysez la séquence d'appels aux fonctions membres
// de LaClasse dans le programme suivant :

int main()
{
    // LaClasse c1; // défaut
    // LaClasse c2 = LaClasse(); // défaut indiqué explicitement
    // LaClasse cc1(c1); // copie
    // LaClasse cc2 = c1; // copie indiqué explicitement
    // LaClasse cc3 = LaClasse(c1); // défaut puis affectation
    // LaClasse cc4 = F(c1);
    // cc4 = F(c2); // test affectation par déplacement
    // LaClasse cc5(std::move(c1)); // test constructeur par affectation
    // LaClasse cv1(5); // int
    // LaClasse cv2 = 5; // défaut puis int
    // LaClasse cv3 = LaClasse(5); // défaut puis int
    // LaClasse cv4 = (LaClasse)5; // défaut puis int
    // std::cout << std::endl;
    // c1 = cc1;
    // std::cout << std::endl;
    // c2 = 8;
    // std::cout << std::endl;
    // if (cv1)
    // {
    //     cv1 = F(10);
    //     cv1 = F(c1);
    //     cv1 = c1.F(c2);
    // }
    // std::cout << "Tableaux \n";
    // LaClasse tab[3];
    // LaClasse* pc = new LaClasse(tab[0]);
    // delete pc;
    // std::cout << "Avant de sortir ... \n";
    // LaClasseSpecialisee lcs;
    // LaClasseSpecialisee lcs3(std::move(lcs));
    // LaClasseSpecialisee lcs2 = LaClasseSpecialisee();
    char* test = "ceci est un test";
    char test2 = 'a';
    String s;
    String s2 = test;
    String s3 = test2;
    String s4 = s2 + s3;
    String s5 = s2;
    String a = 'a';
    String b = 'b';

    std::cout << "s : " << s.getValue() << std::endl;
    std::cout << "s2 : " << s2.getValue() << std::endl;
    std::cout << "s3 : " << s3.getValue() << std::endl;
    std::cout << "s4 : " << s4.getValue() << std::endl;
    std::cout << "s5 : " << s5.getValue() << std::endl;
    std::cout << std::endl;

    std::cout << "a == b : " << (a == b) << std::endl;
    std::cout << "a == a : " << (a == a) << std::endl;
    std::cout << "a != b : " << (a != b) << std::endl;
    std::cout << "a != a : " << (a != a) << std::endl;
    std::cout << std::endl;

    std::cout << "a < b : " << (a < b) << std::endl;
    std::cout << "b < a : " << (b < a) << std::endl;
    std::cout << "a > b : " << (a > b) << std::endl;
    std::cout << "b > a : " << (b > a) << std::endl;
    std::cout << std::endl;

    std::cout << "a <= a : " << (a <= a) << std::endl;
    std::cout << "a <= b : " << (a <= b) << std::endl;
    std::cout << "b <= a : " << (b <= a) << std::endl;
    std::cout << std::endl;

    std::cout << "a >= a : " << (a >= a) << std::endl;
    std::cout << "a >= b : " << (a >= b) << std::endl;
    std::cout << "b >= a : " << (b >= a) << std::endl;
    return 0;
}
