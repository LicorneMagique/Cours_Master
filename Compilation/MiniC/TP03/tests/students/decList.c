#include "printlib.h"

int main() {
    int x,y,z;
    x = 1;
    y = 2;
    z = 3;
    println_int(x);
    println_int(y);
    println_int(z);
    return 0;
}

// EXPECTED
// 1
// 2
// 3
