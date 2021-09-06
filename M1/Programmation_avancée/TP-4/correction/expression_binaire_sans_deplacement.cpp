#include <iostream>

class Expression
{
public:
    Expression()
    {
        std::cout << "Expression() " << std::endl;
    }
    virtual ~Expression()
    {
        std::cout << "~Expression() " << std::endl;
    }
    virtual int eval() const = 0;
    virtual Expression *clone() const = 0;

    Expression(const Expression &e) = delete;
    Expression &operator=(const Expression &e) = delete;
};

class Binaire : public Expression
{
public:
    Binaire()
    {
        std::cout << "Binaire() " << std::endl;
    }
    Binaire(const Expression &e1, const Expression &e2) : exp1(e1.clone()), exp2(e2.clone())
    {
        std::cout << "Binaire(const Expression &,const Expression &) " << std::endl;
    }
    ~Binaire()
    {
        std::cout << "~Binaire() " << std::endl;
        delete exp1;
        delete exp2;
    }

    Binaire(const Binaire &e) = delete;
    Binaire &operator=(const Binaire &e) = delete;

protected:
    Expression *exp1;
    Expression *exp2;
};

class Constante : public Expression
{
public:
    Constante(const int &i) : val(i)
    {
        std::cout << "Constante(const int &) " << i << std::endl;
    }
    ~Constante()
    {
        std::cout << "~Constante() " << std::endl;
    }
    int eval() const override { return val; }
    Constante *clone() const override
    {
        std::cout << "clone Constante " << std::endl;
        return new Constante(val);
    }

    Constante(const Constante &e) = delete;
    Constante &operator=(const Constante &e) = delete;

protected:
    int val;
};

class Plus : public Binaire
{
public:
    Plus()
    {
        std::cout << "Plus()" << std::endl;
    }
    Plus(const Expression &e1, const Expression &e2) : Binaire(e1, e2)
    {
        std::cout << "Plus(const Expression &, const Expression &)" << std::endl;
    }
    ~Plus()
    {
        std::cout << "~Plus()" << std::endl;
    }
    int eval() const override { return exp1->eval() + exp2->eval(); }
    Plus *clone() const override
    {
        std::cout << "clone Plus " << std::endl;
        return new Plus(*exp1, *exp2);
    }

    Plus(const Plus &e) = delete;
    Plus &operator=(const Plus &e) = delete;
};

class Moins : public Binaire
{
public:
    Moins()
    {
        std::cout << "Moins()" << std::endl;
    }
    Moins(const Expression &e1, const Expression &e2) : Binaire(e1, e2)
    {
        std::cout << "Moins(const Expression &, const Expression &)" << std::endl;
    }
    ~Moins()
    {
        std::cout << "~Moins()" << std::endl;
    }
    int eval() const override { return exp1->eval() - exp2->eval(); }
    Moins *clone() const override
    {
        std::cout << "clone Moins " << std::endl;
        return new Moins(*exp1, *exp2);
    }

    Moins(const Moins &e) = delete;
    Moins &operator=(const Moins &e) = delete;
};

class Mult : public Binaire
{
public:
    Mult()
    {
        std::cout << "Mult()" << std::endl;
    }
    Mult(const Expression &e1, const Expression &e2) : Binaire(e1, e2)
    {
        std::cout << "Mult(const Expression &, const Expression &)" << std::endl;
    }
    ~Mult()
    {
        std::cout << "~Mult()" << std::endl;
    }
    int eval() const override { return exp1->eval() * exp2->eval(); }
    Mult *clone() const override
    {
        std::cout << "clone Mult " << std::endl;
        return new Mult(*exp1, *exp2);
    }
    Mult(const Mult &e) = delete;
    Mult &operator=(const Mult &e) = delete;
};

int main()
{
    int a;
    std::cout << "Donnez une valeur a?" << std::endl;
    std::cin >> a;
    const Expression &e = Mult(Plus(Constante(a), Constante(2)), Constante(-2));
    std::cout << e.eval() << std::endl;
    return 0;
}
