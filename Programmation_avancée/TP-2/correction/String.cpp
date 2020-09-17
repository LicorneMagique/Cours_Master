//====================================================================
// classe String : implantation
//====================================================================

#include <iostream>
#include <cstring>
#include "String.h"

//Definition des variables de classe
unsigned int String::compteur = 0;

//Constructions et conversions
String::String(const char *ch)
try : longueur(std::strlen(ch)), chaine(new char[longueur + 1])
{
    compteur++;
    std::strcpy(chaine, ch);
}
catch (const std::bad_alloc &e)
{
    std::cout << "Pas de place pour construire une String: " << e.what() << '\n';
}

String::String(char c) : longueur(1), chaine(new char[2])
{
    compteur++;
    chaine[0] = c;
    chaine[1] = '\0';
}

String::String(const String &s)
try : longueur(std::strlen(s.chaine)),
            chaine(new char[longueur + 1])
{
    compteur++;
    std::strcpy(chaine, s.chaine);
}
catch (const std::bad_alloc &e)
{
    std::cout << "Pas de place pour construire une String: " << e.what() << '\n';
}

String::operator const char *() const
{
    return chaine; //Ici, on ne renvoie pas un clone de la "sequence
                                 //de caracteres" pointee, mais un acces READ ONLY
                                 //a l'original.
                                 //Le renvoi d'un clone necessiterait de
                                 //l'allocation memoire dans le tas. Qui
                                 //s'occuperait ensuite de sa desallocation?
                                 //(surtout lorsque cette conversion est utilisee
                                 // pour creer un objet temporaire)
}

//Construction private
String::String(size_t l)
try : longueur(l),
            chaine(new char[longueur + 1])
{
    compteur++;
}
catch (const std::bad_alloc &e)
{
    std::cout << "Pas de place pour construire une String: " << e.what() << '\n';
}

// Affectation
const String &String::operator=(const String &s)
{
    if (this != &s) //Eviter l'auto-affectation!
    {
        delete[] chaine;
        longueur = s.longueur;
        try
        {
            chaine = new char[longueur + 1];
        }
        catch (const std::bad_alloc &e)
        {
            std::cout << "Pas de place pour allonger une String: " << e.what() << '\n';
        }
        std::strcpy(chaine, s.chaine);
    }
    return *this;
}

// Destruction
String::~String()
{
    compteur--;
    delete[] chaine;
}

// Operations d'acces
char &String::operator[](size_t i)
{
    if (i > longueur - 1)
        i = longueur - 1;
    return chaine[i];
}
char String::operator[](size_t i) const
{
    if (i > longueur - 1)
        i = longueur - 1;
    return chaine[i];
}

// Operations de concatenations
String operator+(const String &s1, const String &s2)
{
    String res(s1.longueur + s2.longueur);
    std::strcpy(res.chaine, s1);
    std::strcat(res.chaine, s2);
    return res;
}
const String &String::operator+=(const String &s)
{
    char *res;
    try
    {
        res = new char[longueur + s.longueur + 1];
    }
    catch (const std::bad_alloc &e)
    {
        std::cout << "Pas de place pour allonger une String: " << e.what() << '\n';
    }
    std::strcpy(res, chaine);
    std::strcat(res, s.chaine);
    delete[] chaine;
    longueur = longueur + s.longueur + 1;
    chaine = res;
    return *this;
}

// Operateurs relationnels
bool operator==(const String &s1, const String &s2)
{
    return (std::strcmp(s1.chaine, s2.chaine) == 0);
}
bool operator!=(const String &s1, const String &s2)
{
    return (std::strcmp(s1.chaine, s2.chaine) != 0);
}
bool operator<(const String &s1, const String &s2)
{
    return (std::strcmp(s1.chaine, s2.chaine) < 0);
}
bool operator>(const String &s1, const String &s2)
{
    return (std::strcmp(s1.chaine, s2.chaine) > 0);
}

// Operateurs d'entree-sortie
std::ostream &operator<<(std::ostream &os, const String &s)
{
    os << s.chaine;
    return os;
}
std::istream &operator>>(std::istream &is, String &s)
{
    char temp[100];
    is.getline(temp, 99, '\n'); //istream& istream::getline (char* s, streamsize n, char delim );
    s = temp;
    return is;
}
