#ifndef EXPRESSION_INCLUDED
#define EXPRESSION_INCLUDED

class Expression
{
    private:
    public:
        Expression(){}
        virtual int eval() const = 0;
        virtual Expression* clone() const = 0;
        Expression(const Expression& e) = delete; // empêche la construction par copie
        const Expression& operator=(const Expression&) = delete; // pareil pour l'affectation
};

class Constante: public Expression
{
    private:
        int nombre;
    public:
        Constante(int n): Expression(), nombre(n) {}
        int eval() const;
        Expression* clone() const;
};

class Plus: public Expression
{
    private:
        Expression* e1;
        Expression* e2;
    public:
        Plus(const Expression& a, const Expression& b): Expression(), e1(a.clone()), e2(b.clone()) {}
        int eval() const;
        Expression* clone() const;
};

class Moins: public Expression
{
    private:
        Expression* e1;
        Expression* e2;
    public:
        Moins(const Expression& _e1, const Expression& _e2): Expression(), e1(_e1.clone()), e2(_e2.clone()){}
        int eval() const;
        Expression* clone() const;
};

class Mult: public Expression
{
    private:
        Expression* e1;
        Expression* e2;
    public:
    Mult(const Expression& _e1, const Expression& _e2): Expression(), e1(_e1.clone()), e2(_e2.clone()){}
        int eval() const;
        Expression* clone() const;
};

#endif // EXPRESSION_INCLUDED
