#include <iostream>

class LaClasse
{
public :
  //Construction, conversion, affectation et destruction
  LaClasse() try : l(0), ptr(new double)
    {
        *ptr=0.0;
        std::cout << "LaClasse::LaClasse() \n";
    }
    catch (const std::bad_alloc& e) {std::cout << "Pas de place dans le tas pour un double: " << e.what() << '\n';}
    
  LaClasse(const LaClasse & lc) try : l(lc.l), ptr(new double)
    {
      *ptr=*(lc.ptr);
      // Remarque : Cette fois on a fait un constructeur par copie qui respecte la vraie sŽmantique d'une copie et le comportement du programme sera donc similaire qu'on supprime le mŽcanisme de copy elision ou pas
      std::cout << "LaClasse::LaClasse(const LaClasse & ) \n";
    }
    catch (const std::bad_alloc& e) {std::cout << "Pas de place dans le tas pour un double: " << e.what() << '\n';}
        
   LaClasse(LaClasse && lc) : l(lc.l), ptr(lc.ptr)
    {
        lc.ptr = nullptr;
        std::cout << "LaClasse::LaClasse(LaClasse && ) \n";
    }
 
  LaClasse(int i) try : l(i), ptr(new double)
    {
      *ptr=i+0.5;
      std::cout << "LaClasse::LaClasse(int) \n";
    }
  catch (const std::bad_alloc& e) {std::cout << "Pas de place dans le tas pour un double: " << e.what() << '\n';}
        
  operator bool() const
  {std::cout << "LaClasse::operator bool() const \n"; return true;}
        
  ~LaClasse()
  {
      delete ptr;
      std::cout << "~LaClasse::LaClasse() \n";
  }
        
  LaClasse & operator=(const LaClasse & c)
  {
    if(this!= &c)
    {
        l=c.l;
        delete ptr;
        try {ptr = new double;}
        catch (const std::bad_alloc& e) {std::cout << "Pas de place dans le tas pour un double: " << e.what() << '\n';}
        *ptr=*(c.ptr);
        std::cout << "LaClasse::operator=(const LaClasse &) \n";
    }
    return *this;
  }

  LaClasse & operator=(LaClasse && c)
    {
        if(this!= &c)
        {
            l=c.l;
            delete ptr;
            ptr = c.ptr;
            c.ptr =nullptr;
            std::cout << "LaClasse::operator=(LaClasse &&) \n";
        }
        return *this;
    }
        
  //Autre fonction membre
  LaClasse F(LaClasse);
  // Declaration fonction exterieure amie
  friend std::ostream & operator << (std::ostream & os, const LaClasse & lc);
        
public :
  int l;
  double *ptr;
};
        
class LaClasseSpecialisee : public LaClasse
{
public :
    LaClasseSpecialisee() : LaClasse(1), m(10)
    { std::cout << "LaClasseSpecialisee::LaClasseSpecialisee() \n";}
    LaClasseSpecialisee(const LaClasseSpecialisee & cs) : LaClasse(cs), m(cs.m)
     { std::cout << "LaClasseSpecialisee::LaClasseSpecialisee(const LaClasseSpecialisee &) \n";}
    LaClasseSpecialisee(LaClasseSpecialisee && cs) : LaClasse(std::move(cs)), m(cs.m)
    { std::cout << "LaClasseSpecialisee::LaClasseSpecialisee(LaClasseSpecialisee &&) \n";}
    LaClasseSpecialisee & operator=(const LaClasseSpecialisee & cs)
    {
     if(this!= &cs)
        {
         const LaClasse * pup = &cs;
         LaClasse * thisup = this;
         *thisup=*pup;
         m=cs.m;
         std::cout << "LaClasseSpecialisee::operator=(const LaClasseSpecialisee &) \n";
        }
        return *this;
    }
    LaClasseSpecialisee & operator=(LaClasseSpecialisee && cs)
    {
        if(this!= &cs)
        {
            LaClasse * pup = &cs;
            LaClasse * thisup = this;
            *thisup=std::move(*pup);
            m=cs.m;
            std::cout << "LaClasseSpecialisee::operator=(LaClasseSpecialisee &&) \n";
        }
        return *this;
    }
    ~LaClasseSpecialisee(){std::cout << "LaClasseSpecialisee::~LaClasseSpecialisee() \n";}
private :
    int m;
};

LaClasse F(LaClasse vv)
{
  std::cout << " in F \n";
  return vv;
}

LaClasse LaClasse::F(LaClasse v)
{
  std::cout << " in LaClasse::F \n";
  return ::F(v);
}

LaClasseSpecialisee G(LaClasseSpecialisee vv)
{
    std::cout << " in G \n";
    return vv;
}
        
std::ostream & operator << (std::ostream & os, const LaClasse & lc)
{
  os << " in ostream << LaClasse "<< lc.l << std::endl;
  return os;
}

// Testez et analysez la séquence d'appels aux fonctions membres 
// de LaClasse dans le programme suivant :


int main()
{
  LaClasse c1;            // LaClasse::LaClasse()
  LaClasse c2=LaClasse(); // LaClasse::LaClasse()
  LaClasse cc1(c1);       //LaClasse::LaClasse(const LaClasse & )
  LaClasse cc2=c1;        //LaClasse::LaClasse(const LaClasse & )
  LaClasse cc3=LaClasse(c1);//LaClasse::LaClasse(const LaClasse & )
  LaClasse cv1(5);        //LaClasse::LaClasse(int)
  LaClasse cv2=6;         //LaClasse::LaClasse(int)
  LaClasse cv3=LaClasse(7);//LaClasse::LaClasse(int)
  LaClasse cv4=(LaClasse)8;//LaClasse::LaClasse(int)
  LaClasse cv5=F(c1);       //LaClasse::LaClasse(const LaClasse & )
                            //in F
                            //LaClasse::LaClasse(LaClasse && )
                            //~LaClasse::LaClasse()
  std::cout << std::endl;
  c1=cv1;                  //LaClasse::operator=(const LaClasse &)
  c1=F(cv1);              //LaClasse::LaClasse(const LaClasse & )
                          //in F
                          //LaClasse::LaClasse(LaClasse && )
                          //LaClasse::operator=(LaClasse &&)
                          //~LaClasse::LaClasse()
                          //~LaClasse::LaClasse()

  std::cout << std::endl;
  c2=9;
    // LaClasse::LaClasse(int)
    // LaClasse::operator=(const LaClasse &&)
    // ~LaClasse::LaClasse()
  std::cout << std::endl;
    
  if(cv1) //LaClasse::operator bool() const
    {
      cv1=F(10);
        //LaClasse::LaClasse(int)
        //in F
        //LaClasse::LaClasse(const LaClasse && )
        //LaClasse::operator=(const LaClasse &&)
        //~LaClasse::LaClasse()
        //~LaClasse::LaClasse()
      cv1=F(c1);
        //LaClasse::LaClasse(const LaClasse & )
        //in F
        //LaClasse::LaClasse(const LaClasse && )
        //LaClasse::operator=(const LaClasse &&)
        //~LaClasse::LaClasse()
        //~LaClasse::LaClasse()
      cv1=c1.F(c2);
        //LaClasse::LaClasse(const LaClasse & )
        //in LaClasse::F
        //LaClasse::LaClasse(const LaClasse & )
        //in F
        //LaClasse::LaClasse(const LaClasse && )
        //~LaClasse::LaClasse()
        //LaClasse::operator=(const LaClasse &&)
        //~LaClasse::LaClasse()
        //~LaClasse::LaClasse()
        // See Copy elision and return value optimization
        // https://en.wikipedia.org/wiki/Return_value_optimization
    }
    
  LaClasseSpecialisee cs1; //LaClasse::LaClasse(int)
                           //LaClasseSpecialisee::LaClasseSpecialisee()
  LaClasseSpecialisee cs2(cs1); //LaClasse::LaClasse(const LaClasse & )
                                //LaClasseSpecialisee::LaClasseSpecialisee(const LaClasseSpecialisee &)
  LaClasseSpecialisee cs3(G(cs1));
    //LaClasse::LaClasse(const LaClasse & )
    //LaClasseSpecialisee::LaClasseSpecialisee(const LaClasseSpecialisee &)
    //in G
    //LaClasse::LaClasse(LaClasse && )
    //LaClasseSpecialisee::LaClasseSpecialisee(LaClasseSpecialisee &&)
    //LaClasseSpecialisee::~LaClasseSpecialisee()
    //~LaClasse::LaClasse()
  cs1=cs3;
    //LaClasse::operator=(const LaClasse &)
    //LaClasseSpecialisee::operator=(const LaClasseSpecialisee &)
  cs2=G(cs3);
    //LaClasse::LaClasse(const LaClasse & )
    //LaClasseSpecialisee::LaClasseSpecialisee(const LaClasseSpecialisee &)
    //in G
    //LaClasse::LaClasse(LaClasse && )
    //LaClasseSpecialisee::LaClasseSpecialisee(LaClasseSpecialisee &&)
    //LaClasse::operator=(LaClasse &&)
    //LaClasseSpecialisee::operator=(LaClasseSpecialisee &&)
    //LaClasseSpecialisee::~LaClasseSpecialisee()
    //~LaClasse::LaClasse()
    //LaClasseSpecialisee::~LaClasseSpecialisee()
    //~LaClasse::LaClasse()
  std::cout << "Tableaux \n";
  LaClasse tab[3];
    //LaClasse::LaClasse()
    //LaClasse::LaClasse()
    //LaClasse::LaClasse()
  LaClasse *pc=new LaClasse(tab[0]);
    //LaClasse::LaClasse(const LaClasse & )
  delete pc;
    //~LaClasse::LaClasse()
  std::cout << "Avant de sortir ... \n";
    //~LaClasse::LaClasse()
    //~LaClasse::LaClasse()
    //~LaClasse::LaClasse()
    //LaClasseSpecialisee::~LaClasseSpecialisee()
    //~LaClasse::LaClasse()
    //LaClasseSpecialisee::~LaClasseSpecialisee()
    //~LaClasse::LaClasse()
    //LaClasseSpecialisee::~LaClasseSpecialisee()
    //~LaClasse::LaClasse()
    //~LaClasse::LaClasse()
    //~LaClasse::LaClasse()
    //~LaClasse::LaClasse()
    //~LaClasse::LaClasse()
    //~LaClasse::LaClasse()
    //~LaClasse::LaClasse()
    //~LaClasse::LaClasse()
    //~LaClasse::LaClasse()
    //~LaClasse::LaClasse()
    //~LaClasse::LaClasse()
  return 0; 
}
 
