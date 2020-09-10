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
