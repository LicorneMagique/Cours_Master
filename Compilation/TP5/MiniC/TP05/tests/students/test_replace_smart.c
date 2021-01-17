#include "printlib.h"

int main()
{

    int a, b, c, d, e, f;
    a = 1;
    b = 2;
    c = 3;
    d = 4;
    e = 5;
    f = 6;
    a = (a + b + c + d + e + f);
    println_int(a);

    return 0;
}

// EXPECTED
// 21
