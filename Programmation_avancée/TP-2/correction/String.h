//====================================================================
// classe String : specification
//==================================================================== 

#ifndef _String_H_
#define _String_H_

#include <iostream>

class String 
{
public:
  // Construction et conversions
  String(const char * ="");
  String(char);
  String(const String &); // INDISPENSABLE car l'objet "logique"
                          // ne se reduit ici pas a l'objet "technique":
                          // Il faut effectuer des "copies profondes"
  operator const char *() const; // Conversion String -> const char  *

  // Affectation
  const String & operator=(const String &); //INDISPENSABLE cf plus haut

  // Destruction
  ~String(); //INDISPENSABLE

  // Operations d'acces
  char & operator[](size_t);//Acces "read/write" a une lettre de la String
  char operator[](size_t) const ;//Acces "read only" pour une const String

  // Operations de concatenations
  friend String operator+(const String &,const String &); 
  const String & operator+=(const String &);    

  // Operateurs relationnels
  friend bool operator== (const String &,const String &);
  friend bool operator!= (const String &,const String &);
  friend bool operator< (const String &,const String &);
  friend bool operator> (const String &,const String &);

  // Operateurs d'entree-sortie
  friend std::ostream& operator<< (std::ostream&, const String &);
  friend std::istream& operator>> (std::istream&, String &);

private:
  size_t longueur;
  char * chaine;

  String(size_t l); //Constructeur utilise en interne

  // declaration de membre static 
  static unsigned int compteur; // Attention, cette variable reste a definir!
};

#endif //_String_H_
