#include <iostream>
#include <stdio.h>
#include <string.h>
#include "Expression.h"

using namespace std;

int Constante::eval() const
{
    return nombre;
}

Expression* Constante::clone() const
{
    return new Constante(nombre);
}

int Plus::eval() const
{
    return e1->eval() + e2->eval();
}

Expression* Plus::clone() const
{
    return new Plus(*e1->clone(), *e2->clone());
}

int Moins::eval() const
{
    return e1->eval() - e2->eval();
}

Expression* Moins::clone() const
{
    return new Moins(*e1->clone(), *e2->clone());
}

int Mult::eval() const
{
    return e1->eval() * e2->eval();
}

Expression* Mult::clone() const
{
    return new Mult(*e1->clone(), *e2->clone());
}
