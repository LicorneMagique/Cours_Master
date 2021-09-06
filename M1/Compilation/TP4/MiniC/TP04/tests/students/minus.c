#include "printlib.h"

int main() {

    int a;
    a = -(4);
    println_int(a);
    a = -(-(-5)*2);
    println_int(a);

    return 0;
}

// EXPECTED
// -4
// -10
