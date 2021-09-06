#include <iostream>

template <typename T>
const T & min(const T & a,const T & b)
{
  std::cout<<"template min"<<std::endl;
  return (a<b?a:b);
}

// Pour les chaines de caractères, on peut proposer une surcharge spécifique de min
// const char *  min(const char * a,const char * b)
// Elle convient tout à fait mais ce n'est pas une spécialisation du template ci-dessus
// qui prend des références

template <>
const char * const & min<char const *>(const char * const & a,const char * const & b)
{   
  std::cout<<"specialisation pour const char *"<<std::endl;
  int i=0;
  while(a[i]==b[i])
    {
      if(a[i]=='\0')
	return a;
      else i++;
    }
  return (a[i]<b[i]?a:b);
}

template <>
char * const & min<char *>(char * const & a,char * const & b)
{   
  std::cout<<"Specialisation pour char *"<<std::endl;
  int i=0;
  while(a[i]==b[i])
    {
      if(a[i]=='\0')
	return a;
      else i++;
    }
  return (a[i]<b[i]?a:b);
}

//--------------------------------------------------------------------
// Un autre template pour les tableaux statiques de tailles différentes
// Il ne s'agit pas d'une spécialisation mais d'une surcharge du premier
// template général

template <int I, int J>
const char * min(const char (&a)[I],const char (&b)[J])
{
    std::cout<<"Un autre template pour const char [I] et const char [J]"<<std::endl;
    int i=0;
    while(a[i]==b[i])
    {
        if(a[i]=='\0')
            return a;
        else i++;
    }
    return (a[i]<b[i]?a:b);
}

// Un autre template pour les tableaux statiques de même taille
// La spécialisation du template précédent ne passe pas.
template <int I>
const char * min(const char (&a)[I],const char (&b)[I])
{
    std::cout<<"Un autre template pour const char [I]"<<std::endl;
    int i=0;
    while(a[i]==b[i])
    {
        if(a[i]=='\0')
            return a;
        else i++;
    }
    return (a[i]<b[i]?a:b);
}

int main()
{
  std::cout << min<>(5,6) <<std::endl;
  std::cout << min(6,5) <<std::endl;
  std::cout << min("lili","lala") <<std::endl;
  std::cout << min("li","lala") <<std::endl; // 2 arguments de types différents
  const char * cc="mumu";
  const char * dd="ma";
  std::cout << min(cc,dd) <<std::endl;
  char ee[5]="toto";
  char ff[5]="ta"; //tableau de même taille que le précédent
  std::cout << min(ee,ff) <<std::endl;
  std::cout << min("zut",ff) <<std::endl;
  return 0;
}

/*
 template min
 5
 template min
 5
 Un autre template pour const char [I]
 lala
 Un autre template pour const char [I] et const char [J]
 lala
 specialisation pour const char *
 ma
 Un autre template pour const char [I]
 ta
 Un autre template pour const char [I] et const char [J]
 ta
*/





