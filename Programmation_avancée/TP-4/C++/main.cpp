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
    const Expression& test = Constante(4);
    Plus p(c, c);
    cout << c.eval() << endl;
    cout << p.eval() << endl;
    const Expression& e = Mult( // 12
        Plus( // 3
            Constante(a), // 5
            Constante(-2) // -2
        ),
        Plus( // 4
            Constante(1), // 1
            Constante(3) // 3
        )
    );
    std::cout << e.eval() << std::endl;
    return 0;
}
