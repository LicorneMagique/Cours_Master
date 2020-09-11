#ifndef TABLEAU_INCLUDED
#define TABLEAU_INCLUDED

// class Tableau
// {
//     private:
//     public:
//         Tableau(){}
//         virtual int eval() const = 0;
//         virtual Tableau* clone() const = 0;
//         Tableau(const Tableau& e) = delete; // empêche la construction par copie
//         const Tableau& operator=(const Tableau&) = delete; // pareil pour l'affectation
// };

// class Constante: public Tableau
// {
//     private:
//         int nombre;
//     public:
//         Constante(int n): Tableau(), nombre(n) {}
//         int eval() const;
//         Tableau* clone() const;
// };

// class Plus: public Tableau
// {
//     private:
//         Tableau* e1;
//         Tableau* e2;
//     public:
//         Plus(const Tableau& a, const Tableau& b): Tableau(), e1(a.clone()), e2(b.clone()) {}
//         int eval() const;
//         Tableau* clone() const;
// };

// class Moins: public Tableau
// {
//     private:
//         Tableau* e1;
//         Tableau* e2;
//     public:
//         Moins(const Tableau& _e1, const Tableau& _e2): Tableau(), e1(_e1.clone()), e2(_e2.clone()){}
//         int eval() const;
//         Tableau* clone() const;
// };

// class Mult: public Tableau
// {
//     private:
//         Tableau* e1;
//         Tableau* e2;
//     public:
//     Mult(const Tableau& _e1, const Tableau& _e2): Tableau(), e1(_e1.clone()), e2(_e2.clone()){}
//         int eval() const;
//         Tableau* clone() const;
// };

#endif // TABLEAU_INCLUDED
