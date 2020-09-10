#include <iostream>
#include <stdio.h>
#include <string.h>
#include "Expression.h"

using namespace std;

int main()
{
    cout << "Hello World" << endl;

    int a = 5;
    Constante c(a);
    // const Expression& test = Constante(4);
    // Plus p(c, c);
    // cout << c.eval() << endl;
    // cout << c.eval() << endl;
    // const Expression& e = Mult(
    //     Plus(
    //         Constante(a),
    //         Constante(-2)
    //     ),
    //     Plus(
    //         Constante(1),
    //         Constante(3)
    //     )
    // );
    // std::cout << e.eval() << std::endl;
    return 0;
}
